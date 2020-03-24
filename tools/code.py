import uuid
import random


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


if __name__ == '__main__':
    print(generate_uuid())
    print(generate_verification_code())
    print(generate_digital_code())
