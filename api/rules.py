import hashlib


def get_rule_mapping():
    return {
        '1': execute_rule_1,
        '2': execute_rule_2
    }


def execute_rule_1(message):
    return message[::-1]


def execute_rule_2(message):
    return hashlib.md5(message.encode()).hexdigest()
