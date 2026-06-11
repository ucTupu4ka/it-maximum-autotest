# Чувствительные данные лучше хранить, например, в vault
# и использовать в тестах через переменные среды
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    password: str



VALID_USER = User(
    username="tomsmith",
    password="SuperSecretPassword!"
)

INVALID_USER = User(
    username="test",
    password="test"
)
