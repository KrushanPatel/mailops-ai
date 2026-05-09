from packages.email_core.gmail_provider import build_gmail_service


def fetch_threads(max_results: int = 10):

    service = build_gmail_service()

    response = service.users().threads().list(
        userId="me",
        maxResults=max_results
    ).execute()

    return response.get("threads", [])
