from packages.email_core.gmail_provider import build_gmail_service


def fetch_threads(max_results: int = 10):

    service = build_gmail_service()

    threads = []
    page_token = None

    while True:

        response = service.users().threads().list(
            userId="me",
            maxResults=max_results,
            pageToken=page_token
        ).execute()

        threads.extend(response.get("threads", []))

        page_token = response.get("nextPageToken")

        if not page_token:
            break

    return threads
