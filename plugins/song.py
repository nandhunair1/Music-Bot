#                     ----------------------------- @Peterparker6 ---------------------------


import os
import time
import ffmpeg
import logging
import requests
import youtube_dl
from pyrogram import filters, Client, idle
from youtube_search import YoutubeSearch
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

## Extra Fns -------
# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


## Commands --------
@Client.on_message(filters.command(['start']))
async def start(client, message):
       await message.reply("👋 𝗛𝗲𝗹𝗹𝗼 𝗕𝗿𝗼\n\n𝐈 𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫[🎶](https://telegra.ph/file/92a1f08c6ca91e0e8c163.mp4)\n\n𝑺𝒆𝒏𝒕 𝒕𝒉𝒆 𝑵𝒂𝒎𝒆 𝒐𝒇 𝒕𝒉𝒆 𝐒𝐨𝐧𝐠 𝒀𝒐𝒖 𝑾𝒂𝒏𝒕... 😍🥰🤗\n<b>Also I Support Inline YouTube Search 😉</b>\n\n𝗝𝘂𝘀𝘁 𝗧𝘆𝗽𝗲 𝗮 𝗦𝗼𝗻𝗴 𝗡𝗮𝗺𝗲\n\n𝐄𝐠. `Believer`",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('😌 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿', url='https://t.me/MrC_VENOM'),
                    InlineKeyboardButton('Group 😎', url='https://t.me/tvseriezzz')
                ],
                [
                    InlineKeyboardButton('Search Inline', switch_inline_query_current_chat='')
                ]
            ]
        )
    )

@Client.on_message(filters.command(['help']))
async def help(client, message):
       await message.reply("<b>Simplest Way😂</b>\n\n<i>How many times have I said that just giving the name of a song is enough.🙄\nDo not expect any other help from me😠</i>\n\n<b>Eg</b> `Vaathi Coming`",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('😎 Group', url='https://t.me/tvseriezzz')
                ]
            ]
        )
    )

@Client.on_message(filters.command(['about']))
async def about(client, message):
       await message.reply("➪<b>Name</b> : ✫<i>Music Downloader</i>\n➪<b>Developer</b> : ✫[MrC《》VENOM](https://t.me/MrC_VENOM)\n➪<b>Language</b> : ✫<i>Python3</i>\n➪<b>Server</b> : ✫[𝘏𝘦𝘳𝘰𝘬𝘶](https://heroku.com/)",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Search Inline', switch_inline_query_current_chat='')
                ]
            ]
        )
    )

@Client.on_message(filters.text)
def a(client, message):
    query=message.text
    print(query)
    m = message.reply('🔎 𝗦𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴 𝘁𝗵𝗲 𝗦𝗼𝗻𝗴...')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 7000:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            performer = f"[Alan Walker]"
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('𝐅𝐨𝐮𝐧𝐝 𝐍𝐨𝐭𝐡𝐢𝐧𝐠. 𝐓𝐫𝐲 𝐂𝐡𝐚𝐧𝐠𝐢𝐧𝐠 𝐓𝐡𝐞 𝐒𝐩𝐞𝐥𝐥𝐢𝐧𝐠 𝐀 𝐋𝐢𝐭𝐭𝐥𝐞 😐')
            return
    except Exception as e:
        m.edit( "Eg.`/s Believer`")
        print(str(e))
        return
    m.edit("Please Wait for Some Seconds.")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep =  f'🎧 𝗧𝗶𝘁𝘁𝗹𝗲 : {title}\n\n📮 𝗕𝘆: {message.from_user.mention()}\n<b>📤 𝗕𝘆 :- <a href= "https://t.me/tvseriezzz">♠️ 𝑨𝒍𝒍 𝑰𝒏 𝑶𝒏𝒆 𝑮𝒓𝒐𝒖𝒑 🎬</a> </b>'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='HTML',quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name)
        m.delete()
    except Exception as e:
        m.edit('𝙁𝙖𝙞𝙡𝙚𝙙\n\n`Plesase Try Again Later`')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
