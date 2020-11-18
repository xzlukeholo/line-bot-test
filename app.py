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

    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='11537',
            sticker_id='52002745'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)

        return

    if msg in ['你現在心情如何？', '你現在心情如何', '今天心情好嗎', '過得怎樣']:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        
        return

    if '心情如何' in msg:
        sticker_message = StickerSendMessage(
            package_id='11538',
            sticker_id='51626521'
        )
        
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        
        return

    if msg == '吃飯了嗎':
        random_num = random.randint(1, 2)
        if random_num == 1:
            r = '還沒耶owo，有罐罐嗎?'
        elif random_num == 2:
            r = '還沒吃~餓餓 (•͈⌔•͈⑅)'
    elif msg in ['hi', 'HI', 'Hi']:
        random_num = random.randint(1, 4)
        if random_num == 1:
            r = 'hi'
        elif random_num == 2:
            r = '喵囉哈~'
        elif random_num == 3:
            r = 'hello!'
        elif random_num == 4:
            r = '喵~owo'
    elif msg == 'こんにちは':
        r = 'こんにちはにゃ~'
    elif msg == 'おはよう':
        r = 'おはようにゃ~'
    elif msg == 'ただいま':
        r = 'おかえり(≧▽≦)'
    elif msg == '略略略':
        r = '略略略~٩(●˙▿˙●)۶…⋆ฺ'
    elif msg == '開心嗎？':
        r = '敲開心（ΦωΦ）!'
    elif msg == '開心嗎':
        r = '敲開心（ΦωΦ）!'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= r))


if __name__ == "__main__":
    app.run()