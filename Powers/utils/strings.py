start_msg = """
• 𝗛𝗲𝗹𝗹𝗼!! 𝗖𝗼𝗺𝗽𝗮𝗱𝗿𝗲 ꈍ◡ꈍ

<b><i>» I'm Anime Stream - I Can Share Streaming And Download Links of Any Anime With You.
» Just Type Name of Any Anime, And Get Surprised By The Results.
» You Must Join My Channel @Sonic_Otakus To Use Me.
» [Guide For Using Me](https://t.me/Anime_Stream_LLC/50) - [Click Here](https://t.me/Anime_Stream_LLC/50)
» For Any Assistance - Do /help
» Enjoy Your Anime Watching Experience.</i></b>"""

# [Sonic Otakus](https://t.me/Sonic_Otakus)! I can give streamable link as well as download link of all anime and do much more see help to know what I can do.

help_msg = """
<i><b>» Just Send Me The Name of Any Anime, And I Will Give You The Results.

**» <u>Available Commands</u>**

• <u>For Anime</u>: Just Type A Name, And Send It.</i></b>

• /top: Top 10 All Time Popular Anime.
• /character [character name]: Search For The Given Character.

» <u>NOTE:</u> Ongoing Anime Are ❌ Not Included In The Search List.
» Only Completed Anime Are Available ✅ In This Bot.</i></b>

» 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐜𝐞 - [𝐀𝐝𝐦𝐢𝐧 𝐒𝐮𝐩𝐩𝐨𝐫𝐭](https://t.me/Illusion_Don)
"""

dev_msg = """
**OWNER COMMANDS**
• /addsudo [reply to user]: Will add sudoer
• /rmsudo [id of the user]: Will remove the sudoer

**SUDO COMMANDS**
• /addfsub [channel id] [type] [btn_name]: Add channel in force subscribe. Default to auto
• /ufname [channel id] [new btn_name]: Update the button name of the channel id.
• /rmfsub [channel id]: Remove channels from force subscribe
• /changetype [channel id] [newtype]: Replace the type of join 
• /addlink [link] [btn name]: Add a link to the force sub kb.
• /ulname [link] [new btn name]: Update the name of the button for the given link.
• /getlinks : Give all the current links
• /rmlink [link]: Remove the link from database
• /getfsubs: Return all the fsubs channel with their types
• /currorder: Return the current order of keyboard
• /rmorder: Remove the order of keyboard
• /setorder: Bot will ask for the order you want to set
• /logs: Return logs
• /stats: Current stats of the bot
• /gcast [tag] [reply to message]: Will broadcast replied message according to given tag
    Available tags:
        -u : Broadcast messages to all users.
        -c : Broadcast messages in all the chats
        -all : Broadcast messages to all chats and users
    In case you don't give tag or you give wrong the tag -all will be considered as default
"""

ani_info_string = """
<b>[🇺🇲]</b> <i><b>{english}</b></i>
<b>[{flag}]</b> <i><b>{local}</b></i>

<b><i>» <u>Score</u> ~ {score}
» <u>Source</u> ~ {source}
» <u>Type</u> ~ {mtype}
» <u>Episodes</u> ~ {episodes}
» <u>Duration</u> ~ {duration} minutes
» <u>Status</u> ~ {status}
» <u>Format</u> ~ {format}
» <u>Genre</u> ~ {genre}
» <u>Tags</u> ~ {tags}
» <u>Adult Rated</u> ~ {isAdult}
» <u>Studio</u> ~ {studio}
» <u>Trailer</u> ~ {trailer}
» <u>Website</u> ~ {siteurl}</i></b>
"""

ani_info_def_string = """
<b>{name}</b>

<b><i>» <u>Type</u> ~ {mtype}
» <u>Episodes</u> ~ {episodes}
» <u>Status</u> ~ {status}
» <u>Genre</u> ~ {genre}
» <u>First Aired</u> ~ {aired} 
» <u>Other Name</u> ~ {oname}</i></b>
"""


char_info_string = """
<b><i>{name}

» <u>Gender</u> ~ {gender}
» <u>Date of Birth</u> ~ {date_of_birth}
» <u>Age</u> ~ {age}
» <u>Blood Type</u> ~ {blood_type}
» <u>favourites</u> ~ {favorites}
» <u>Website</u> ~ {siteurl}{role_in}</i></b>
"""

anime_res_txt = "<b><i>» Found Results For: {q}\n\n» Page: {p}/{tp}</i></b>"

ep_txt = "<b><i>» Choose The Episode You Want To Stream / Download From Below.\n\n» Total Episodes - {ep}\n\n» Page - {p}</i></b>"


SHARE_TEXT = """
Hey currently I am watching an Anime and I think you may find it interesting
Click on the link above to directly get it
"""
#If don't want this text then set the variable as SHARE_TEXT = None

DEFAULT_TEXT = """
Hey currently I am watching an Anime
Click on the link above to start watcing.
"""
