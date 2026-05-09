import base64

from bs4 import BeautifulSoup


def extract_email_body(payload):

    body_data = ""

    if "parts" in payload:

        for part in payload["parts"]:

            mime_type = part.get("mimeType")

            if mime_type == "text/plain":

                data = part["body"].get("data")

                if data:
                    body_data = data
                    break

            elif mime_type == "text/html":

                data = part["body"].get("data")

                if data:
                    body_data = data

    else:

        body_data = payload["body"].get("data", "")

    if not body_data:
        return ""

    decoded_bytes = base64.urlsafe_b64decode(
        body_data.encode("UTF-8")
    )

    decoded_body = decoded_bytes.decode(
        "utf-8",
        errors="ignore"
    )

    clean_body = clean_html(decoded_body)

    return clean_body


def clean_html(html_content):

    soup = BeautifulSoup(
        html_content,
        "html.parser"
    )

    return soup.get_text(separator=" ", strip=True)
