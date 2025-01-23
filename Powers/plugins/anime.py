import os

from pyrogram import filters
from pyrogram.types import Message

from Powers.config import NO_RES_PIC, SEARCH_PIC, TRENDING
from Powers.functions import *
from Powers.streamer import DENDENMUSHI
from Powers.utils import *

from .start import u_pref


@DENDENMUSHI.on_message(filters.command("character"))
@is_joined
async def retrieve_char_info(_, m: Message):
    if len(m.command) <= 1:
        await m.reply_text("<b>»</b> 𝗘𝘅𝗮𝗺𝗽𝗹𝗲 - `/character Horikita`")
        return

    to_del = await m.reply_text("<b>»</b> 𝚂𝚎𝚊𝚛𝚌𝚑𝚒𝚗𝚐 𝙵𝚘𝚛 𝚃𝚑𝚎 𝙲𝚑𝚊𝚛𝚊𝚌𝚝𝚎𝚛 - 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 . . .")
    character = m.text.split(None, 1)[1]
    txt, picture = get_character_info(character)
    if not txt:
        await to_del.delete()
        await m.reply_photo(NO_RES_PIC, caption=f"<b>»</b> ❌ 𝙽𝚘 𝙲𝚑𝚊𝚛𝚊𝚌𝚝𝚎𝚛 𝙵𝚘𝚞𝚗𝚍 𝚆𝚒𝚝𝚑 𝙽𝚊𝚖𝚎 - <b>{character}</b>")
        return

    kb = await char_description_back(character)
    await to_del.delete()
    await m.reply_photo(picture, caption=txt, reply_markup=kb)
    os.remove(picture)
    return


@DENDENMUSHI.on_message(filters.command("anime") & filters.private)
@is_joined
async def retrieve_anime(_, m: Message):
    if len(m.command) <= 1:
        await m.reply_text("<b>»</b> 𝗘𝘅𝗮𝗺𝗽𝗹𝗲: `One Piece`")
        return
    global u_pref
    u_pref[m.from_user.id] = "ask"
    to_del = await m.reply_text("<b>»</b> 𝗝𝘂𝘀𝘁 𝗦𝗲𝗻𝗱 𝗡𝗮𝗺𝗲 𝗼𝗳 𝗧𝗵𝗲 𝗔𝗻𝗶𝗺𝗲.")
    query = m.text.split(None, 1)[1]
    results = get_anime_results(query)

    if not results:
        await to_del.delete()
        await m.reply_photo(NO_RES_PIC, caption=f"<b>»</b> ❌ 𝙽𝚘 𝙰𝚗𝚒𝚖𝚎 𝙵𝚘𝚞𝚗𝚍 𝚆𝚒𝚝𝚑 𝙽𝚊𝚖𝚎 - <b>{query}</b> \n\n<b>»</b> 𝚃𝚛𝚢 𝚄𝚜𝚒𝚗𝚐 𝙰 𝚂𝚒𝚖𝚙𝚕𝚎 𝙽𝚊𝚖𝚎. \n\n<b>»</b>𝗘𝘅𝗮𝗺𝗽𝗹𝗲 - \n\n  𝙰𝚝𝚝𝚊𝚌𝚔 𝙾𝚗 𝚃𝚒𝚝𝚊𝚗 𝙵𝚞𝚕𝚕 𝙴𝚙𝚒𝚜𝚘𝚍𝚎 ❌ \n  𝙰𝚝𝚝𝚊𝚌𝚔 𝙾𝚗 𝚃𝚒𝚝𝚊𝚗 𝚂𝟷 𝚂𝟸 𝚂𝟹 𝙲𝚑𝚛𝚘𝚗𝚒𝚌𝚊𝚕 ❌ \n  𝙱𝚕𝚞𝚎 𝙴𝚡𝚘𝚛𝚡𝚒𝚜𝚝 𝙺𝚢𝚘𝚝𝚘 𝚂𝚊𝚐𝚊 ❌ \n\n  𝙰𝚝𝚝𝚊𝚌𝚔 𝙾𝚗 𝚃𝚒𝚝𝚊𝚗 ✅ \n  𝙱𝚕𝚞𝚎 𝙴𝚡𝚘𝚛𝚌𝚒𝚜𝚝 ✅ \n  𝙾𝚜𝚑𝚒 𝙽𝚘 𝙺𝚘 ✅ \n\n<b>»</b> 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐜𝐞 - /help")
        return

    total_pages = results[1]["totalPage"]

    txt = anime_res_txt(q=query, p=1, tp=total_pages)
    kb = await get_search_res_kb(results)
    await to_del.delete()
    await m.reply_photo(SEARCH_PIC, caption=txt, reply_markup=kb)
    return

@DENDENMUSHI.on_message(filters.command(["ongoing", "top"]) & filters.private)
@is_joined
async def retrieve_totire_anime(_, m: Message):
    if m.command[0] == "ongoing":
        results = get_trending_anime()
        txt = "<b>»</b> 𝗧𝗼𝗽 𝟭𝟬+ 𝗢𝗻𝗴𝗼𝗶𝗻𝗴 𝗔𝗻𝗶𝗺𝗲 ─"
    else:
        txt = "<b>»</b> 𝗧𝗼𝗽 𝟭𝟬+ 𝗔𝗻𝗶𝗺𝗲 𝗼𝗳 𝗔𝗹𝗹 𝗧𝗶𝗺𝗲 ─"
        results = get_alltime_popular()

    if not results:
        await m.reply_text("Failed to get top animes")
        return
    kb = await genrate_top_anime_kb(results)

    global u_pref
    u_pref[m.from_user.id] = "ask"

    await m.reply_photo(TRENDING, caption=txt, reply_markup=kb)
    return

@DENDENMUSHI.on_message(filters.text & filters.private & no_cmd & ~filters.outgoing, group = 100)
@is_joined
async def search_anime_for_me(_, m: Message):
    query = m.text
    to_del = await m.reply_text(f"<b>»</b> 𝚂𝚎𝚊𝚛𝚌𝚑𝚒𝚗𝚐 𝙵𝚘𝚛 𝙰𝚗𝚒𝚖𝚎 - <b>{query}</b> | 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 . . .")
    try:
        results = get_anime_results(query)
    except Exception as e:
        LOGGER.error(e)
        LOGGER.error(format_exc())
        results = False

    if not results:
        await to_del.delete()
        await m.reply_photo(NO_RES_PIC, caption=f"<b>»</b> ❌ 𝙽𝚘 𝙰𝚗𝚒𝚖𝚎 𝙵𝚘𝚞𝚗𝚍 𝚆𝚒𝚝𝚑 𝙽𝚊𝚖𝚎 - <b>{query}</b>")
        return
    elif results == 429:
        await to_del.edit_text("» 𝚃𝚘𝚘 𝙼𝚊𝚗𝚢 𝚄𝚜𝚎𝚛𝚜 𝙰𝚛𝚎 𝚄𝚜𝚒𝚗𝚐 𝙼𝚎, 𝙿𝚕𝚎𝚊𝚜𝚎 𝚃𝚛𝚢 𝙰𝚐𝚊𝚒𝚗 𝙸𝚗 𝟻 𝙼𝚒𝚗𝚞𝚝𝚎𝚜.\n\n» 𝙲𝚔𝚎𝚌𝚔 𝙾𝚞𝚝 𝙼𝚢 𝙼𝚒𝚛𝚛𝚘𝚛𝚜 - [𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗿𝗲](https://t.me/Anime_Stream_LLC/39)")
        return
    
    global u_pref
    u_pref[m.from_user.id] = "ask"
        
    total_pages = results[1]["totalPage"]

    txt = anime_res_txt.format(q=query, p=1, tp=total_pages)
    to_del = await to_del.edit_text("<b>»</b> 𝙵𝚘𝚞𝚗𝚍 𝚂𝚘𝚖𝚎 𝚁𝚎𝚜𝚞𝚕𝚝𝚜 - 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 . . .")
    kb = await get_search_res_kb(results)
    
    await to_del.delete()
    await m.reply_photo(SEARCH_PIC, caption=txt, reply_markup=kb)
