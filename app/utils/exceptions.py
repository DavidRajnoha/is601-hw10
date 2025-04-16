from typing import List


class UserCreationError(Exception):
    """Base class for user creation-related errors."""
    pass


class EmailAlreadyExists(UserCreationError):
    """Raised when trying to create a user with an email that already exists."""
    pass


class NicknameAlreadyExists(UserCreationError):
    """Raised when trying to create a user with a nickname that already exists."""
    pass


class UserValidationFailed(UserCreationError):
    """Raised when user input fails schema validation."""

    def __init__(self, validation_errors: List[dict]):
        self.validation_errors = validation_errors
        super().__init__("User validation failed")
