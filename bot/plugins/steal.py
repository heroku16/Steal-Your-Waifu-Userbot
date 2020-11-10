from pyrogram import filters
from bot import bot
import os
from bs4 import BeautifulSoup
import requests

screen_shot = "nana/downloads/"

@bot.on_message(filters.user([792028928, 1334822377, 1232515770]) & filters.photo)
async def harem_steal(client, message):
    dis_loc = ''
    if message.photo:
        dis = await client.download_media(
            message=message.photo,
            file_name=screen_shot
        )
        dis_loc = os.path.join(screen_shot, os.path.basename(dis))
        if dis_loc:
            base_url = "http://www.google.com"
            search_url = "{}/searchbyimage/upload".format(base_url)
            multipart = {
                "encoded_image": (dis_loc, open(dis_loc, "rb")),
                "image_content": ""
            }
            google_rs_response = requests.post(search_url, files=multipart, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
            os.remove(dis_loc)
        else:
            await message.delete()
            return
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
        }
        response = requests.get(the_location, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
        prs_anchor_element = prs_div.find("a")
        prs_text = prs_anchor_element.text
        out_str = f"/protecc {prs_text}"
    await message.reply(out_str, parse_mode="markdown")