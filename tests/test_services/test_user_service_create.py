from app.services.user_service import UserService


async def test_provided_nickname_is_preserved(db_session, email_service):
    original_nickname = "custom_nickname_123"
    user_data = {
        "email": "john.unique@example.com",
        "password": "ValidPass123!",
        "nickname": original_nickname,
    }

    user = await UserService.create(db_session, user_data, email_service)

    assert user is not None, "User creation failed unexpectedly"
    assert user.nickname == original_nickname, f"Expected nickname '{original_nickname}', got '{user.nickname}'"
