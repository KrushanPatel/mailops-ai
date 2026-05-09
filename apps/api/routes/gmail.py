from fastapi import APIRouter

from packages.email_core.gmail_provider import build_gmail_service

router = APIRouter()


@router.get("/gmail/profile")
async def gmail_profile():

    service = build_gmail_service()

    profile = service.users().getProfile(
        userId="me"
    ).execute()

    return profile
