import os
from flask import Flask, request, abort, jsonify
import json

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['jFQmEA2tmScAjVLQWbMfUAuhDgK+kei4yE4vRGhv9va+2zuOemi0enicuPpwfugMu2ekYfz6PgEPFbSExOkQQyinN7ai5M9MSvLj6xPZPYYjKtlKxIrKgExYf6xcvLhyB9RNbIP4gvQHMeu2G4q89AdB04t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['43241adb34ce8b3c4bb8f29dc8750bfd'])

@app.route("/")
def index():
    return "Hello World"

@app.route("/callback", methods=['POST'])
def callback():
#    return "ok"
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
#        TextSendMessage(text=event.message.text)
        TextSendMessage(text="Academia sinica")
    )


if __name__ == "__main__":
    app.run()
