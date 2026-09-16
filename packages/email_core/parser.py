import base64

from bs4 import BeautifulSoup


def extract_email_body(payload):

    body_data = _find_part_data(payload, "text/plain") or _find_part_data(
        payload, "text/html"
    )

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


def _find_part_data(payload, mime_type):

    if payload.get("mimeType") == mime_type:
        return payload.get("body", {}).get("data")

    for part in payload.get("parts", []):

        data = _find_part_data(part, mime_type)

        if data:
            return data

    return None


def clean_html(html_content):

    soup = BeautifulSoup(
        html_content,
        "html.parser"
    )

    return soup.get_text(separator=" ", strip=True)
