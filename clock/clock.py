"""
Clock for Telegram profile
Python v3.9
                                                                                        Turdibek Jumabaev: https://github.com/turdibekjumabaev/
"""

from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from PIL import Image, ImageDraw, ImageFont
import time
client = TelegramClient(session='SESSION_NAME',
                        api_id="", api_hash="")
client.start()
time1 = ''
time2 = ''


def tick():
    global time1
    global time2
    time2 = time.strftime('%H:%M')
    if time2 != time1:
        time1 = time2
    else:
        return "NO"
    img = Image.new('RGB', (640, 640), color=(40, 40, 40))
    d = ImageDraw.Draw(img)
    d.text(((640-(len(time2)*22))/2, 640/2-30), time2, size=1000, font=ImageFont.truetype('clock/mc_font.woff', 130),
           fill=(238, 238, 238))
    img.save('profile.jpg')


while True:
    t = tick()
    if t != "NO":
        client(DeletePhotosRequest(client.get_profile_photos('me')))

        result = client(UploadProfilePhotoRequest(
            file=client.upload_file('profile.jpg')
        ))
