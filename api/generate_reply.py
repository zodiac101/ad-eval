from api.rules import get_rule_mapping


def generate_reply(message):
    if '-' not in message:
        return 'Input format not proper', 400

    rule, text = message.split('-', 1)

    if rule == '':
        return 'Rule is empty', 400

    if text == '':
        return 'Message is empty', 400

    if not all(char.isalnum() for char in text):
        return 'Message contains special characters', 400

    if any(char.isupper() for char in text):
        return 'Message contains uppercase characters', 400

    rule_mapping = get_rule_mapping()

    for char in rule:
        if char not in rule_mapping:
            return 'Rule not supported', 400
        text = rule_mapping[char](text)

    return {
        'data': text
    }
