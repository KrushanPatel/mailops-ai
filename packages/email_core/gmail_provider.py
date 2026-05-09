from googleapiclient.discovery import build

from packages.email_core.gmail_auth import get_gmail_credentials


def build_gmail_service():

    creds = get_gmail_credentials()

    service = build(
        "gmail",
        "v1",
        credentials=creds
    )

    return service
