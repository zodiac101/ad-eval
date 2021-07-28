import hashlib


def generate_reply(message):
    if '-' not in message:
        return 'Input format not proper', 400

    rule, text = message.split('-', 1)

    if rule == '':
        return 'Rule is empty', 400

    if text == '':
        return 'Message is empty', 400

    if rule not in {'11', '12', '21', '22'}:
        return 'Rule not in correct format', 400

    if not all(char.isalnum() for char in text):
        return 'Message contains special characters', 400

    if any(char.isupper() for char in text):
        return 'Message contains uppercase characters', 400

    if rule[0] == '1':
        text = text[::-1]
    else:
        text = hashlib.md5(text.encode()).hexdigest()

    if rule[1] == '1':
        text = text[::-1]
    else:
        text = hashlib.md5(text.encode()).hexdigest()

    return {
        'data': text
    }
