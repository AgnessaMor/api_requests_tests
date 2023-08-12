from common.deco import logging as log
from fixtures.register.model import RegisterUserRequest, RegisterUserResponse
from fixtures.validator import Validator


class RegisterController(Validator):
    def __init__(self, app):
        self.app = app

    POST_REGISTER = "/register"

    @log("Register new user")
    def register_new_user(
        self, data: RegisterUserRequest, type_response=RegisterUserResponse
    ):
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_REGISTER}",
            json=data.to_dict(),
        )
        return self.structure(response, type_response=type_response)
