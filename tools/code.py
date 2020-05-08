import uuid
import random
import hashlib
import datetime
import logging
import jwt

from flask import current_app


def generate_uuid():
    return str(uuid.uuid4()).replace("-", "")


def generate_verification_code():
    code_list = []
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91):  # A-Z
        code_list.append(chr(i))
    for i in range(97, 123):  # a-z
        code_list.append(chr(i))

    verification_code = ''.join(random.sample(code_list, 6))
    return verification_code


def generate_digital_code():
    code = "".join([str(random.randint(0, 9)) for i in range(6)])
    return code


def generate_md5(orl):
    return hashlib.md5(orl.encode()).hexdigest()


def sha256(orl):
    return hashlib.sha256(orl.encode()).hexdigest()


def double_sha256(orl):
    return sha256(sha256(orl))


def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :return: string
    """
    secret_key = current_app.config.get("SECRET_KEY")
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30),
            "iat": datetime.datetime.utcnow() - datetime.timedelta(seconds=60),
            "sub": str(user_id)
        }
        return jwt.encode(
            payload,
            secret_key,
            algorithm="HS256"
        ).decode()
    except Exception as e:
        logging.info(e)
        return e


def decode_auth_token(auth_token):
    """
    Validates the gos_api token
    :param auth_token:
    :return: integer|string
    """
    secret_key = current_app.config.get("SECRET_KEY")
    try:
        payload = jwt.decode(auth_token, secret_key)
        user_id = payload["sub"]
        jwt.encode(
            payload,
            secret_key,
            algorithm="HS256"
        )
        return user_id
    except jwt.ExpiredSignatureError:
        logging.info("Signature expired. Please log in again.")
        return None
    except jwt.InvalidTokenError:
        logging.info("Invalid token. Please log in again.")
        return None


if __name__ == '__main__':
    print(generate_uuid())
    print(generate_verification_code())
    print(generate_digital_code())
    print(generate_md5("111"))
    print(sha256("131313131"))
    print(double_sha256("131313131"))
