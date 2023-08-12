import pytest

from fixtures.constants import ResponseCode
from fixtures.register.model import RegisterUserRequest


@pytest.mark.api
class TestRegisterNewUser:
    def test_register_new_user_with_valid_data(self, app):
        """
        1. Try to register user with valid data
        2. Check the status code is Created (201)
        """
        data = RegisterUserRequest.random()
        res = app.register.register_new_user(data=data)
        assert res.status_code == ResponseCode.Created
