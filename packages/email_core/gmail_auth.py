from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]

TOKEN_PATH = "token.json"
CREDS_PATH = "credentials.json"


def get_gmail_credentials():

    creds = None

    if Path(TOKEN_PATH).exists():
        creds = Credentials.from_authorized_user_file(
            TOKEN_PATH,
            SCOPES
        )

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDS_PATH,
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())

    return creds
