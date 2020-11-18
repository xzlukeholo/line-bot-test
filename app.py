import random
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('hScclT7cFNSIwIvgHtzHuHfnbMGvbBFf19mgyonJdMVPpVL2n6J7seVnxs6dGsExSLpODERqHywZG0ATO1o879ieZVEMpd+3fK11Tyh/TxoWCSikthyumeTPra0ODtgbZfbGI7P9v5abvuP5oP6cxwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('cf46c25def64be5157542fce72c340d8')


@app.route("/callback", methods=['POST'])
def callback():
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
    msg = event.message.text

    if msg == '吃飯了嗎':
        r = '還沒耶owo，有罐罐嗎?'
    elif msg in ['hi', 'HI', 'Hi']:
        random_num = random.randint(1, 3)
        if random_num == 1:
            r = 'hi'
        elif random_num == 2:
            r = '喵囉哈~'
        elif random_num == 3:
            r = '嗨嗨嗨~'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= r))


if __name__ == "__main__":
    app.run()