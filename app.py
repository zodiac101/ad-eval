from flask import Flask

from api.generate_reply import generate_reply

app = Flask(__name__)


@app.route('/v2/reply/<string:message>')
def reply_message(message):
    return generate_reply(message)


@app.route('/v2/reply')
def reply_empty_message():
    return 'Message is empty', 404


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)