import json
from typing import Union
from flask import request
import jwt

from instance.config import BaseConfig


def read_json(filename: str, encoding: str = "utf-8") -> Union[list, dict]:
    with open(filename, encoding=encoding) as f:
        return json.load(f)

def email_required() -> str:
    """
    Получение email из headers
    :return: email
    """
    data = request.headers['Authorization']
    token = data.split('Bearer ')[-1]

    user = jwt.decode(token, BaseConfig.PWD_HASH_SALT, algorithms=[BaseConfig.JWT_ALGO])

    email = user['email']

    return email
