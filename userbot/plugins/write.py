import os
from PIL import Image, ImageDraw, ImageFont
import urllib
from userbot import catub
from . import *
from ..helpers.utils import edit_delete

plugin_category = "extra"
    
@catub.cat_cmd(
    pattern="write(?:\s|$)([\s\S]*)",
    command=("write", plugin_category),
    info={
        "header": "To write given text or replied message on paper.",
        "usage": "{tr}write <message/reply>",
        "examples": "{tr}write Hello World",
    },
)

async def writer(e):
    if e.reply_to:
        reply = await e.get_reply_message()
        text = reply.message
    elif e.pattern_match.group(1):
        text = e.text.split(maxsplit=1)[1]
    else:
        return await edit_delete(e, "`Give Some Text`")
    template = "downloads/template.png"
    if os.path.exists("downloads/template.png"):
        os.remove(template)
    urllib.request.urlretrieve("https://raw.githubusercontent.com/Jisan09/Files/main/template/template.jpg",template)
    im1 =  Image.open(template)
    k = await edit_delete(e, "`Processing ...`")
    fonts = "downloads/assfont.ttf"
    if os.path.exists("downloads/assfont.ttf"):
        os.remove(fonts)
    urllib.request.urlretrieve("https://github.com/Jisan09/Files/blob/main/fonts/assfont.ttf?raw=true",fonts)
    im1 =  Image.open(template)
    img = Image.open(template)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(fonts, 30)
    x, y = 150, 140
    lines = (text)
    line_height = font.getsize("hg")[1]
    draw.text((x, y), text, fill=(1, 22, 55), font=font)
    y = y + line_height - 5
    file = "pic.jpg"
    img.save(file)
    await e.reply(file=file)
    os.remove(file)