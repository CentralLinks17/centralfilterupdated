# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


class script(object):
    START_TXT = """<b> Hello... {} 👋
    
✯ My name is <a href=https://telegram.dog/{}>{}</a>
✯ I am the latest and most advanced auto filter bot.
✯ I Can Provide MOVIES,SERIES And Lot More
✯ Don't waste your time looking to add me to your group; I'm only for @CentralRequest.
If you need this bot, it's paid for. If required, DM @CentralLinks_ContactBot.
✯ TEAM - @Central_Links</b>"""

    HELP_TXT = """<b>Hey {}
Here Is The Help For My Channel</b>"""

    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://telegram.dog/central_links>Team CENTRAL LINKS</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹.12
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: V4.2.7 [ 𝙱𝙴𝚃𝙰 ]"""

    SUBSCRIPTION_TXT = """
<b>Refer your link to your friends, family, channel, and group to get a free premium for {}.

Referral Link: https://telegram.me/{}?start=CL-{}

If {} unique user starts the bot with your referral link, then you will be automatically added to the premium list.

Buy a paid plan by /plan</b>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>
- CENTRAL FILTER is the feature were users can get automated replies for a particular keyword and Central Filter will respond whenever a keyword is found the message
<b>NOTE:</b>
1. CENTRAL FILTER should have admin privilege.
2. only ADMINS can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>
- CENTRAL FILTER Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. CENTRAL FILTER supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://telegram.dog/Central_links)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
These are the extra features of the Central Filter
 <b>✯ Maintained by : <a href=https://t.me/Thiyaku_Suriya>☢Thiyaku Suriya☢</a></b>
  
 <b>✯ Join here : <a href=https://t.me/Central_Links>☢My updates and invite link.☢</a></b> 
<b>Commands and Usage:</b>  
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /song - Download any song [<code>example /song vaa vaathi song</code>] 
• /telegraph - <code>Telegraph generator sen under 5MB video or photo I give telegraph link</code> 
• /tts - <code>This command usage text to voice converter</code> 
• /video - This command usage any YouTube video download hd [<code>example /video https://youtu.be/Aiue8PMuD-k</code>]
• /font - This command usage stylish and cool font generator [<code>example /font hi</code>]
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""


    ADMIN_TXT = """help: Admin Mods <b> note: </b>
This module only works for my admin commands and usage:
• /logs: <code>to get the recent errors</code>
• /stats: <code> to get the status of the file in the database. This command can be used by anyone. </code>
• /delete: <code>to delete a specific from the database. </code>
• /users: <code>to get a list of my users and their IDs. </code>
• /chats: <code>to get a list of my chats and their IDs.  </code>
• /leave: <code>to leave from a chat. </code>
• /disable: <code>to disable a chat. </code>
• /ban: <code>to ban a user. </code>
• /unban: <code>to unban a user. </code>
• /channel: <code>to get liꜱt of total connected channelꜱ</code>
• /broadcast: <code>to broadcast a message to all users</code>
• /grp_broadcast: <code> To broadcast a message to all connected groups.</code>
• /gfilter: <code>to add global filters</code>
• /gfilters: <code>to view a list of all global filters</code>
• /delg: <code> to delete a specific global filter</code>
• /request: <code> To send a movie or series request to bot admins. Only works in the support group. [This command can be used by anyone.] </code>
• /delallg: <code> To delete all Gfilters from the bot's database.</code>
• /deletefiles: <code> To delete CamRip and PreDVD files from the bot's database. </code>"""
    STATUS_TXT = """<b>       
   <u>Bot Statistics</u>
    
★ Total Files: <code>{}</code>
★ Total Users: <code>{}</code>
★ Total Users: <code>{}</code>
★ Used Storage: <code>{} MB</code>
★ Free Storage: <code>{} MB</code>

   <u>Server Statistics</u>
★ CPU Usage: {}
★ Disk Usage: {}
★ Bot Uptime: {}</b>"""


    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ALRT_TXT = """Hello {},
This is not your movie request,
Request your's..."""

    OLD_ALRT_TXT = """Hey {},
You're using one of my old messages, 
Please send your request again."""

    CUDNT_FND = """<b>
I Couldn't find anything related to the search {} 

Please check your spelling in <u>[google.com](https://google.com)</u> before requesting.
</b>"""

    I_CUDNT = """<b>Sorry, no files were found for your request. {} 😕

Check your spelling on Google and try again. 😃

Movie Request Format👇

Example: Uncharted, Uncharted 2022, or Uncharted En

Series Request Format 👇

Example: Loki S01 or Loki S01 EP04 or Lucifer S03 E24 or Loki S01E01

🚯 dont uꜱe ➠ ':(!,./)</b>"""

    I_CUD_NT = """I couldn't find any movie related to {}.
Please check the spelling on Google or Imdb."""

    MVE_NT_FND = """Movie not found in database. Admin will soon add it !"""

    TOP_ALRT_MSG = """Checking for query in the database"""

    MELCOW_ENG = """<b>Hello {} 😍, and welcome to our {} group ❤️
    ╾───────────────╼
More than 500,000+ Movies / Series uploaded in our <a href-"https://t.me/centralfilter3bot">BOT</a> .. !!

‣ Search in <a href="https://www.google.com/">GOOGLE.COM</a> To Find The Correct Spelling of Movie and Year of Release, then Type the copied Movie/Series name in @CentralRequest to get the Files.

NOTE : Search Only The Movie Name And Touch The Result That Comes With Movie Name Alone (Not The Movie Name That Comes With Year)
 
‣ If You Do Not Know How To Search, <a href = "https://graph.org/How-To-Request-In-Our-Group-06-23">CLICK HERE</a> 👈

‣ If it Appears JOIN UPDATES CHANNEL ... <a href-"https://t.me/central_links">CLICK HERE</a> ... Join in this Channel and then try again !!

PS : Access to movies can only be obtained by joining [@Central_Links] on our main channel.
</b>"""


    SHORTLINK_INFO = """

🫵 Select Your Language And Earn Money 💰"""

    REQINFO = """
⚠ Infomation ⚠

After 10 minutes, this message will be automatically deleted.

If you do not see the requested movie or series file, look at the next page. """

    SELECT = """Select your preferred language, quality, season, and episode."""

    SINFO = """
🫣 For Movie Join First Then Click On Try Again Button 😅"""

    NORSLTS = """ 
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    CAPTION = """
<b>📂 {file_caption}</b>

<b>Size ⚙️: {file_size}

<b>JOIN : @Central_Links × @CentralRequest</b>"""

    IMDB_TEMPLATE_TXT = """
<b>Query: {query}
IMDb Data:

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10</b>
⏰ Result Shown in: {remaining_seconds} <i>seconds</i> 🔥

Requested by : {message.from_user.mention}

@Central_Links</b>"""
    
    ALL_FILTERS = """
<b>Hey {}, These are my three types of filters.</b>"""
    
    GFILTER_TXT = """
<b> Welcome to Global Filters. Global filters are the filters set by bot admins that will work on all groups. </b>
    
Available commands:
• /gfilter: <code>To create a global filter.</code>
• /gfilters: <code>To view all global filters.</code>
• /delg: <code>To delete a particular global filter.</code>
• /delallg: <code>To delete all global filters.</code>"""
    
    FILE_STORE_TXT = """ <b>File store is the feature that will create a shareable link for a single or multiple files. </b>

Available commands:

• /batch: <code>To create a batch link of multiple files.</code>

• /link: <code>To create a single file store link. </code>

• /pbatch: <code>Just like /batch, the files will be sent with forward restrictions. </code>

• /plink: <code>Just like /link, the file will be sent with a forward restriction. </code>"""

    SONG_TXT ="""<b>Song Download Module

Song download module for those who love music. You can use this feature to download any song at super-fast speeds. It works on bots and groups only...

Commands: 𝄟⃝.  <code>/song song name</code></b>"""
  
    YTDL_TXT = """<b>Help you download videos from YouTube.

Usage: you can download any video from YouTube.

How to use the type: /video or /mp4

Example: <code>/mp4 https://youtu.be/example...</code></b>""" 
  
    TTS_TXT = """<b>TTS🎤 module: translate text to speech

Command: /tts</b>""" 
  
    GTRANS_TXT = """<b>Help: Google Translater

This command tells you to translate a text to any language you want. This command works on both PM and Group.

command and usage: /tr to translate text to a specific language.

Note: While using /tr, you should read the language code.

Examᴩle: /tr ml 
• en = English 
• ml = Malayalam 
• hi = Hindi</b>""" 
  
    TELE_TXT = """<b>Help: telegraph do as you wish with telegra.ph module!

Usage: /telegraph - Send me a picture or video under 5 MB.

Note: 
 This command is available in groups and PMs. 
 This command can be used by everyone.</b>""" 
  
    CORONA_TXT = """<b>Help: COVID
    
This command helps you get daily information about COVID.

Commands and usage:
/covid - Use this command with your country name to get COVID information.

Example: <code>/covid India</code>

⚠️ THIS SERVICE HAS BEEN STOPPED. ⚠️  
  
 </b>""" 

    PROGRESS_BAR = """\n
╭━━━━❰ Tech CL Renaming... ❱━➣
┣⪼ 🗂️ : {1} | {2}
┣⪼ ⏳️ : {0}%
┣⪼ 🚀 : {3}/s
┣⪼ ⏱️ : {4}
╰━━━━━━━━━━━━━━━➣ """
  
    ABOOK_TXT = """<b>Help: Audiobook

You can convert a PDF file to an audio file with this command.
✯ Commands and usage:
/audiobook: reply to this command to any pdf to generate the audio.
</b>""" 
  
 
    PINGS_TXT = """<b>Ping testing helps you know your ping🪄
Commandꜱ: 
• /alive: to check if you are alive.
• /help: to get help.
• /ping: to get your ping.
Usage :
These commands can be used in PMs and groups.
These commands can be used by everyone in the groups and bots.
Share with us for more features. 
  </b>""" 
  
    STICKER_TXT = """<b>You can use this module to find any sticker ID. 
⭕ How do I use it?
        Send <code>/stickerid</code> to find its sticker id.
 </b>""" 
  
    FONT_TXT= """<b>Usage 
  
You can use this module to change your font style.  
Command: /font Your text (Optional) 
Example: /font Hello 
 </b>""" 
  
    PURGE_TXT = """<b>Purge  
      Delete all of message from the group.
Access only for Admins
◉ /purge :- Delete all messages from the replied-to message to the current message.</b>""" 
  
    WHOIS_TXT = """<b>ᴡʜᴏɪꜱ ᴍᴏᴅᴜʟᴇ 
  
 ɴᴏᴛᴇ:- ɢɪᴠᴇ ᴀ ᴜꜱᴇʀ ᴅᴇᴛᴀɪʟꜱ 
 /whois :- ɢɪᴠᴇ ᴀ ᴜꜱᴇʀ ꜰᴜʟʟ ᴅᴇᴛᴀɪʟꜱ 📑 
 </b>""" 
  
    JSON_TXT = """<b> 
 ᴊsᴏɴ:  
 ʙᴏᴛ ʀᴇᴛᴜʀɴs ᴊsᴏɴ ꜰᴏʀ ᴀʟʟ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇs ᴡɪᴛʜ /json 
  
 ꜰᴇᴀᴛᴜʀᴇs: 
  
 ᴍᴇssᴀɢᴇ ᴇᴅɪᴛᴛɪɴɢ ᴊsᴏɴ 
 ᴘᴍ sᴜᴘᴘᴏʀᴛ 
 ɢʀᴏᴜᴘ sᴜᴘᴘᴏʀᴛ 
  
 ɴᴏᴛᴇ: 
  
 ᴇᴠᴇʀʏᴏɴᴇ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ , ɪꜰ sᴘᴀᴍɪɴɢ ʜᴀᴘᴘᴇɴs ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʙᴀɴ ʏᴏᴜ ꜰʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ.</b>""" 
  
    URLSHORT_TXT = """<b>Help: URL Shortener 
<i><b> This command helps you shorten the URL. </i></b> 
Commands and usage: 
   ﻿/short: <b>Use this command with your link to get short links.</b>

Example:<code>/short https://youtu.be/example...</code>
</b>""" 
  
    CARB_TXT = """<b>Help for carbon 
Carbon is a feature to make the image as shown at the top with your texts. 
To use the module, just send the text and replay it with the /carbon command. The bot will reply with the carbon image.
</b>""" 
    GEN_PASS = """<b>Help: Password generator 
  
There is nothing more to know. Send me the limit of your password. 
- I will give the password for that limit. 
 Command and Usage: 
 • /genpassword or /genpw 20 
  
 NOTE: 
 • Only digits are allowed.
 • Maximum allowed digits: 84.
 (I can't generate passwords above the length of 84.) 
 • IMDb should have admin privileges. 
 • The command works on both PM and group. 
 • The command can be used by any group member. </b>""" 
  
    SHARE_TXT = """<b>Get your text share url. 
  
 - Example :- /share
  
 </b>""" 
  
    PIN_TXT = """<b>ᴩIn module 
 Pin a message... 
 
All the pin-related commands can be found here: 

📌commandꜱ and uꜱage📌 
  
 /pin: to pin the message on your chats.
 /unpin: to unpin the current pinned message.</b>"""

 
    RESTART_TXT = """
<b> Bot Restarted !

📅 Date : <code>{}</code>
⏰ Time : <code>{}</code>
🌐 TimeZone : <code>Asia/Kolkata</code>
🛠️ Build Status: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    LOGO = """


█▀▄▀█ ▄▀█ █▀▄ █▀▀   █▄▄ █▄█   █▀▀ █▀▀ █▄░█ ▀█▀ █▀█ ▄▀█ █░░   █░░ █ █▄░█ █▄▀ █▀
█░▀░█ █▀█ █▄▀ ██▄   █▄█ ░█░   █▄▄ ██▄ █░▀█ ░█░ █▀▄ █▀█ █▄▄   █▄▄ █ █░▀█ █░█ ▄█


"""
 
    TAMIL_INFO = """
ஏய் <a href='tg://settings'>My Friend</a> 

 இப்போது டெலிகிராமிலும் பணம் சம்பாதிக்கலாம்.

 தந்தி மூலம் பணம் சம்பாதிக்க உங்களிடம் 1 குழு இருக்க வேண்டும்.
 உங்களிடம் குழு இருந்தால், எங்கள் bot ஐ உங்கள் குழுவில் சேர்ப்பதன் மூலம் நீங்கள் பணம் சம்பாதிக்கலாம்.

 உங்கள் குழுவில் அதிக உறுப்பினர்கள் இருந்தால், உங்கள் வருமானம் அதிகரிக்கும்.

 எப்படி மற்றும் என்ன செய்ய வேண்டும்

 படி 1: இந்த CentralFilterbot போட் உங்கள் குழுவை நிர்வாகியாக்குங்கள்

 படி 2: உங்கள் இணையதளம் மற்றும் API ஐச் சேர்க்கவும்

 Exp: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

 வீடியோவைச் சேர்க்கவும்

 👇 எப்படி சேர்ப்பது 👇

 Example: /set_tutorial video link

மேலும் உங்கள் குழுவில் பயிற்சி வீடியோ தொகுப்பு ஆகிடும்..."""

    ENGLISH_INFO = """
Hey <a href='tg://settings'My Friend</a>

 Now you can earn money on Telegram too.

 You must have 1 group to earn money by telegram.
 If you have a group, you can earn money by adding our bot to your group.

 The more members you have in your group, the higher your income will be.

 How and what to do

 Step 1: Administer this CentralFilterbot bot to your group

 Step 2: Add your website and API

 Exp: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

 Add a video

 👇 How to add 👇

 Exp: /set_tutorial video link

Also your tutorial will be Added Your Group..."""

    TELUGU_INFO = """
హే <a href='tg://settings'>My Friend</a> 


 ఇప్పుడు మీరు టెలిగ్రామ్‌లో కూడా డబ్బు సంపాదించవచ్చు.

 టెలిగ్రామ్ ద్వారా డబ్బు సంపాదించడానికి మీరు తప్పనిసరిగా 1 గ్రూప్‌ని కలిగి ఉండాలి.
 మీకు గ్రూప్ ఉన్నట్లయితే, మా బాట్‌ను మీ గ్రూప్‌కి జోడించడం ద్వారా మీరు డబ్బు సంపాదించవచ్చు.

 మీ గ్రూప్‌లో ఎంత ఎక్కువ మంది సభ్యులు ఉంటే మీ ఆదాయం అంత ఎక్కువగా ఉంటుంది.

 ఎలా మరియు ఏమి చేయాలి

 దశ 1: ఈ CentralFilterbot బాట్‌ని మీ సమూహానికి నిర్వహించండి

 దశ 2: మీ వెబ్‌సైట్ మరియు APIని జోడించండి

 గడువు: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

 వీడియోను జోడించండి

 👇 ఎలా జోడించాలి 👇

 గడువు: /set_tutorial వీడియో లింక్

అలాగే మీ బృందం వీడియో సేకరణకు శిక్షణ ఇస్తుంది..."""

    HINDI_INFO = """
अरे <a href='tg://settings'>My Friend</a> 

 अब आप टेलीग्राम पर भी पैसे कमा सकते हैं।

 टेलीग्राम से पैसे कमाने के लिए आपके पास 1 ग्रुप होना चाहिए।
 यदि आपके पास एक समूह है, तो आप हमारे बॉट को अपने समूह में जोड़कर पैसा कमा सकते हैं।

 आपके समूह में जितने अधिक सदस्य होंगे, आपकी आय उतनी ही अधिक होगी।

 कैसे और क्या करना है

 चरण 1: इस CentralFilterbot बॉट को अपने समूह में प्रशासित करें

 चरण 2: अपनी वेबसाइट और एपीआई जोड़ें

 एक्सप: /शॉर्टलिंक earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

 एक वीडियो जोड़ें

 👇कैसे जोड़ें 👇

 ऍक्स्प: /set_tutorial वीडियो लिंक

साथ ही आपकी टीम वीडियो संग्रह का प्रशिक्षण भी देगी..."""

    MALAYALAM_INFO = """
ഹേയ് <a href='tg://settings'>My Friend</a> 


 ഇപ്പോൾ നിങ്ങൾക്ക് ടെലിഗ്രാമിലും പണം സമ്പാദിക്കാം.

 ടെലിഗ്രാം വഴി പണം സമ്പാദിക്കാൻ നിങ്ങൾക്ക് ഒരു ഗ്രൂപ്പ് ഉണ്ടായിരിക്കണം.
 നിങ്ങൾക്ക് ഒരു ഗ്രൂപ്പ് ഉണ്ടെങ്കിൽ, നിങ്ങളുടെ ഗ്രൂപ്പിലേക്ക് ഞങ്ങളുടെ ബോട്ട് ചേർത്തുകൊണ്ട് നിങ്ങൾക്ക് പണം സമ്പാദിക്കാം.

 നിങ്ങളുടെ ഗ്രൂപ്പിൽ കൂടുതൽ അംഗങ്ങൾ ഉണ്ടെങ്കിൽ, നിങ്ങളുടെ വരുമാനം ഉയർന്നതായിരിക്കും.

 എങ്ങനെ, എന്ത് ചെയ്യണം

 ഘട്ടം 1: ഈ CentralFilterbot ബോട്ട് നിങ്ങളുടെ ഗ്രൂപ്പിലേക്ക് നൽകുക

 ഘട്ടം 2: നിങ്ങളുടെ വെബ്‌സൈറ്റും API-യും ചേർക്കുക

 കാലഹരണപ്പെടൽ: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

 ഒരു വീഡിയോ ചേർക്കുക

 👇 എങ്ങനെ ചേർക്കാം 👇

 കാലഹരണപ്പെടൽ: /set_tutorial വീഡിയോ ലിങ്ക്

നിങ്ങളുടെ ടീം വീഡിയോ ശേഖരണവും പരിശീലിപ്പിക്കും..."""

    URTU_INFO = """
 <a href='tg://settings'>My Friend</a> 


 اب آپ ٹیلی گرام پر بھی پیسے کما سکتے ہیں۔

 ٹیلی گرام کے ذریعے پیسے کمانے کے لیے آپ کے پاس 1 گروپ ہونا ضروری ہے۔
 اگر آپ کا کوئی گروپ ہے، تو آپ ہمارے بوٹ کو اپنے گروپ میں شامل کر کے پیسے کما سکتے ہیں۔

 آپ کے گروپ میں جتنے زیادہ ممبر ہوں گے آپ کی آمدنی اتنی ہی زیادہ ہوگی۔

 کیسے اور کیا کرنا ہے۔

 مرحلہ 1: اپنے گروپ میں اس CentralFilterbot بوٹ کا انتظام کریں۔

 مرحلہ 2: اپنی ویب سائٹ اور API شامل کریں۔

 Exp: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

 ایک ویڈیو شامل کریں۔

 👇 کیسے شامل کریں 👇

 Exp: /set_tutorial ویڈیو لنک

نیز آپ کی ٹیم ویڈیو جمع کرنے کی تربیت دے گی..."""

    GUJARATI_INFO = """
અરે <a href='tg://settings'>My Friend</a> 


 હવે તમે ટેલિગ્રામ પર પણ પૈસા કમાઈ શકો છો.

 ટેલિગ્રામ દ્વારા પૈસા કમાવવા માટે તમારી પાસે 1 જૂથ હોવું આવશ્યક છે.
 જો તમારી પાસે જૂથ છે, તો તમે અમારા બોટને તમારા જૂથમાં ઉમેરીને પૈસા કમાઈ શકો છો.

 તમારા જૂથમાં તમારા જેટલા વધુ સભ્યો હશે તેટલી તમારી આવક વધુ હશે.

 કેવી રીતે અને શું કરવું

 પગલું 1: તમારા જૂથમાં આ CentralFilterbot બોટનું સંચાલન કરો

 પગલું 2: તમારી વેબસાઇટ અને API ઉમેરો

 સમાપ્તિ: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

 વિડિઓ ઉમેરો

 👇 કેવી રીતે ઉમેરવું 👇

 સમાપ્તિ: /set_tutorial વિડિઓ લિંક

તેમજ તમારી ટીમ વિડિયો કલેક્શનની તાલીમ આપશે..."""

    KANNADA_INFO = """
ಹೇ {message.from_user.mention}

 ಈಗ ನೀವು ಟೆಲಿಗ್ರಾಮ್‌ನಲ್ಲಿಯೂ ಹಣ ಗಳಿಸಬಹುದು.

 ಟೆಲಿಗ್ರಾಮ್ ಮೂಲಕ ಹಣ ಗಳಿಸಲು ನೀವು 1 ಗುಂಪನ್ನು ಹೊಂದಿರಬೇಕು.
 ನೀವು ಗುಂಪನ್ನು ಹೊಂದಿದ್ದರೆ, ನಮ್ಮ ಬೋಟ್ ಅನ್ನು ನಿಮ್ಮ ಗುಂಪಿಗೆ ಸೇರಿಸುವ ಮೂಲಕ ನೀವು ಹಣವನ್ನು ಗಳಿಸಬಹುದು.

 ನಿಮ್ಮ ಗುಂಪಿನಲ್ಲಿ ನೀವು ಹೆಚ್ಚು ಸದಸ್ಯರನ್ನು ಹೊಂದಿದ್ದರೆ, ನಿಮ್ಮ ಆದಾಯವು ಹೆಚ್ಚಾಗುತ್ತದೆ.

 ಹೇಗೆ ಮತ್ತು ಏನು ಮಾಡಬೇಕು

 ಹಂತ 1: ಈ CentralFilterbot ಬೋಟ್ ಅನ್ನು ನಿಮ್ಮ ಗುಂಪಿಗೆ ನಿರ್ವಹಿಸಿ

 ಹಂತ 2: ನಿಮ್ಮ ವೆಬ್‌ಸೈಟ್ ಮತ್ತು API ಸೇರಿಸಿ

 ಅವಧಿ: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

 ವೀಡಿಯೊ ಸೇರಿಸಿ

 👇 ಸೇರಿಸುವುದು ಹೇಗೆ 👇

 ಅವಧಿ: /set_tutorial ವೀಡಿಯೊ ಲಿಂಕ್

ನಿಮ್ಮ ತಂಡವು ವೀಡಿಯೋ ಸಂಗ್ರಹಣೆಗೆ ತರಬೇತಿ ನೀಡಲಿದೆ..."""

    BANGLADESH_INFO = """
আরে <a href='tg://settings'>My Friend</a> 

 এখন আপনি টেলিগ্রামেও অর্থ উপার্জন করতে পারেন।

 টেলিগ্রামের মাধ্যমে অর্থ উপার্জন করতে আপনার অবশ্যই 1টি গ্রুপ থাকতে হবে।
 আপনার যদি একটি গ্রুপ থাকে, আপনি আপনার গ্রুপে আমাদের বট যোগ করে অর্থ উপার্জন করতে পারেন।

 আপনার গ্রুপে যত বেশি সদস্য থাকবেন আপনার আয় তত বেশি হবে।

 কিভাবে এবং কি করতে হবে

 ধাপ 1: আপনার গ্রুপে এই CentralFilterbot বট পরিচালনা করুন

 ধাপ 2: আপনার ওয়েবসাইট এবং API যোগ করুন

 মেয়াদ: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

 একটি ভিডিও যোগ করুন

 👇 কিভাবে যোগ করবেন 👇

 মেয়াদ: /set_tutorial ভিডিও লিঙ্ক

এছাড়াও আপনার দল ভিডিও সংগ্রহের প্রশিক্ষণ দেবে..."""


    DEVELOPER_TXT = """
Special Thanks To ❤️ Developers -> @Central_Links
"""

    RENAME_TXT = """
🌌 <b><u>HOW TO SET THUMBNAIL</u></b>
  
•> /set_thumb - send any picture to automatically set thumbnail.
•> /del_thumb use this command and delete your old thumbnail.
•> /view_thumb use this command view your current thumbnail.

📑 <b><u>HOW TO SET CUSTOM CAPTION</u></b>

•> /set_caption - set a custom caption
•> /see_caption - see your custom caption
•> /del_caption - delete custom caption

Example:- /set_caption 📕 File Name: {filename}
💾 Size: {filesize}
⏰ Duration: {duration}

✏️ <b><u>HOW TO RENAME A FILE</u></b>

•> /rename - send any file and click rename option and type new file name and then select [document, video, audio]👈 choice this.
"""

    STREAM_TXT = """<b><u>HOW TO GET STREAM AND DOWNLOAD LINK :</u>

/stream - Get a streamable and downloadable link to any file.</b>"""
