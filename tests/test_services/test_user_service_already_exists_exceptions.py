import pytest

from app.services.user_service import UserService
from app.utils.exceptions import EmailAlreadyExists, NicknameAlreadyExists, UserValidationFailed


async def test_create_user_email_already_exists(db_session, email_service, user):
    user_data = {
        "email": user.email,  # existing email
        "password": "AnotherPass123!"
    }

    with pytest.raises(EmailAlreadyExists):
        await UserService.create(db_session, user_data, email_service)


async def test_create_user_nickname_already_exists(db_session, email_service, user):
    user_data = {
        "email": "newuser@example.com",
        "password": "SecurePass123!",
        "nickname": user.nickname  # existing nickname
    }

    with pytest.raises(NicknameAlreadyExists):
        await UserService.create(db_session, user_data, email_service)


async def test_create_user_validation_fails(db_session, email_service):
    user_data = {
        "email": "not-an-email",
        "password": "short"
    }

    with pytest.raises(UserValidationFailed):
        await UserService.create(db_session, user_data, email_service)