class Script(object):
    START_TXT = """<b><blockquote>Hello {}, My name is <a href=https://t.me/{}>{}</a></blockquote>
    
✯ I am the latest advanced and powerful auto filter bot with awesome filter, file store bot, manual filter, customized shortener support and best UI performance
✯ Don't waste your time looking to add me to your group; I'm only for @CentralRequest.
✯ If you need this bot, it's paid for. If required, DM @CentralLinks_ContactBot.
✯ TEAM - @Central_Links</b>"""

    HELP_TXT = """<b>Hey {}
Here is the help for my commands.</b>"""

    ABOUT_TXT = """<b><blockquote>⍟───[ My Details ]───⍟</blockquote>
    
‣ My name: <a href=https://t.me/{}>{}</a>
‣ My best friend: <a href='tg://settings'>This person</a> 
‣ Developer: <a href='https://t.me/Thiyaku_Suriya'>Thiyaku Suriya</a> 
‣ Library: <a href='https://docs.pyrogram.org/'>Pyrogram</a> 
‣ Language: <a href='https://www.python.org/download/releases/3.0/'>Python 3</a> 
‣ Database: <a href='https://www.mongodb.com/'>Mongo DB</a> 
‣ Bot Server: <a href='https://heroku.com'>Heroku</a> 
‣ Build Status: v2.7.1 [BETA]</b>"""

    SUBSCRIPTION_TXT = """
<b>Refer your link to your friends, family, channel, and group to get free premium for {}

Referral link - https://telegram.me/{}?start=CL-{}

If {} unique user starts the bot with your referral link then you will automatically be added to the premium list.

Buy paid plan by - /plan</b>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is a feature where users can set automated replies for a particular keyword and I will respond whenever a keyword is found in the message
<b>Note:</b>
1. This bot should have admin privilege.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.
Commands and Usage:
• /filter - <code>add a filter in a chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in a chat</code>
• /delall - <code>delete all filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>
- This bot supports both URL and alert inline buttons.
<b>Note:</b>
1. Telegram will not allow you to send buttons without any content, so content is mandatory.
2. This bot supports buttons with any Telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Central Links](buttonurl:https://t.me/central_links)</code>
<b>Alert buttons:</b>
<code>[Alert](buttonalert:this is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>Note: File Index</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contain camrips, porn, and fake files.
3. Forward the last message to me with quotes. I'll add all the files in that channel to my DB.

<b>Note: AutoFilter</b>
1. Add the bot as admin in your group.
2. Use /connect and connect your group to the bot.
3. Use /settings on bot's PM and turn on AutoFilter on the settings menu."""

    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.
<b>Note:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to your PM
Commands and Usage:
• /connect - <code>connect a particular chat to your PM</code>
• /disconnect - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: Extra Modules
<b>Note:</b>
My features stay here new features coming soon...  
 <b>✯ Maintained by: <a href=https://t.me/Thiyaku_Suriya>☢Thiyaku Suriya☢</a></b>
  
 <b>✯ Join here: <a href=https://t.me/central_links>☢Join my updates channel☢</a></b> 
  
 ./id - <code>get ID of a specified user.</code> 
  
 ./info - <code>get information about a user.</code> 
  
 ./song - Download any song [<code>example /song vaa vaathi song</code>] 
  
 ./telegraph - <code>Telegraph generator send under 5MB video or photo I give telegraph link</code> 
  
 ./tts - <code>This command usage text to voice converter</code> 
  
 ./video - This command usage any YouTube video download HD [<code>example /video https://youtu.be/Aiue8PMuD-k</code>]

 ./font - This command usage stylish and cool font generator [<code>example /font hi</code>]"""

    ADMIN_TXT = """Help: Admin Mods
<b>Note:</b>
This module only works for my admins
Commands and Usage:
• /logs - <code>to get the recent errors</code>
• /stats - <code>to get the status of files in DB. [This command can be used by anyone]</code>
• /delete - <code>to delete a specific file from DB.</code>
• /users - <code>to get the list of my users and IDs.</code>
• /chats - <code>to get the list of my chats and IDs</code>
• /leave - <code>to leave from a chat.</code>
• /disable - <code>to disable a chat.</code>
• /ban - <code>to ban a user.</code>
• /unban - <code>to unban a user.</code>
• /channel - <code>to get the list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
• /grp_broadcast - <code>to broadcast a message to all connected groups</code>
• /gfilter - to add global filters
• /gfilters - to view list of all global filters
• /delg - to delete a specific global filter
• /request - to send a movie/series request to bot admins. Only works on support group. [This command can be used by anyone]
• /delallg - to delete all gfilters from the bot's database.
• /deletefiles - to delete CamRip and PreDVD files from the bot's database."""

    STATUS_TXT = """<b>★ Total Files: <code>{}</code>
★ Total Users: <code>{}</code>
★ Total Chats: <code>{}</code>
★ Used Storage: <code>{}</code>
★ Free Storage: <code>{}</code></b>"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ALRT_TXT = """Hello {},
This is not your movie request,
request yours..."""

    OLD_ALRT_TXT = """Hey {},
You are using one of my old messages,
please send the request again."""

    CUDNT_FND = """I couldn't find anything related to {}
Did you mean any one of these?"""

    I_CUDNT = """<b>Sorry no files were found for your request {} 😕

Check your spelling in Google and try again 😃

Movie request format 👇

Example: Uncharted or Uncharted 2022 or Uncharted En

Series request format 👇

Example: Loki S01 or Loki S01E04 or Lucifer S01 EP24

🚯 Don't use ➠ ':(!,./)</b>"""

    I_CUD_NT = """I couldn't find any movie related to {}.
Please check the spelling on Google or IMDb..."""

    MVE_NT_FND = """Movie not found in database..."""

    TOP_ALRT_MSG = """Checking for movie in database..."""

    MELCOW_ENG = """<b>Hello {} 😍, and welcome to {} group ❤️</b>"""

    SHORTLINK_INFO = """
🫵 Select your language and earn money 💰"""

    REQINFO = """
⚠ Information ⚠

After 5 minutes this message will be automatically deleted

If you do not see the requested movie/series file, look at the next page"""

    SELECT = """Select your preferred language, quality, season and episode"""

    SINFO = """
🫣 For movie join first then click on try again button 😅"""

    NORSLTS = """
★ #NoResults ★

ID <b>: {}</b>

Name <b>: {}</b>

Message <b>: {}</b>"""

    CAPTION = """<b>📂Filename: {file_caption}</b>
<b> Size ⚙️: {file_size}

@Central_Links X @CentralRequest</b>"""

    IMDB_TEMPLATE_TXT = """
<b>Query: {query}

IMDb Data:

<b>🏷 Title</b>: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)
☀️ Languages : <code>{languages}</code>
📀 RunTime: {runtime} Minutes
📆 Release Info : {release_date}
🎛 Countries : <code>{countries}</code>


⏰Result shown in: {remaining_seconds} <i>seconds</i> 🔥

Requested by: {message.from_user.mention}</b>

@Central_Links X @CentralRequest"""
    
    ALL_FILTERS = """
<b>Hey {}, these are my three types of filters.</b>"""
    
    GFILTER_TXT = """
<b>Welcome to Global Filters. Global Filters are the filters set by bot admins which will work on all groups.</b>
    
Available commands:
• /gfilter - <code>To create a global filter.</code>
• /gfilters - <code>To view all global filters.</code>
• /delg - <code>To delete a particular global filter.</code>
• /delallg - <code>To delete all global filters.</code>"""
    
    FILE_STORE_TXT = """
<b>File store is the feature which will create a shareable link of a single or multiple files.</b>

Available commands:
• /batch - <code>To create a batch link of multiple files.</code>
• /link - <code>To create a single file store link.</code>
• /pbatch - <code>Just like /batch, but the files will be sent with forward restrictions.</code>
• /plink - <code>Just like /link, but the file will be sent with forward restrictions.</code>"""

    SONG_TXT = """<b>Song download module</b> 
      
 <b>Song download module, for those who love music. You can use this feature to download any song with super fast speed. Works both on bot and groups only...</b> 
  
 <b>Commands</b>: <b> 𝄟⃝.  /song song name</b>""" 
  
    YTDL_TXT = """<b>Help you to download video from YouTube. 
  
 Usage: You can download any video from YouTube 
  
 How to use: type - /video or /mp4 
  
 Example: <code>/mp4 https://youtu.be/example...</code></b>""" 
  
    TTS_TXT = """<b>TTS 🎤 module: Translate text to speech 
  
 Commands and usage: /tts</b>""" 
  
    GTRANS_TXT = """<b>Help: Google Translator 
  
 This command helps you to translate a text to any languages you want. This command works on both PM and group.
  
 Commands and usage: /tr - to translate text to a specific language 
  
 Note: While using /tr you should specify the language code.
  
 Example: /tr ml 
 • en = English 
 • ml = Malayalam 
 • hi = Hindi</b>""" 
  
    TELE_TXT = """<b>Help: Telegraph do as you wish with telegraph module! 
  
 Usage: /telegraph - send me picture or video under (5MB) 
  
 Note: 
 This command is available in groups and PMs 
 This command can be used by everyone</b>""" 
  
    CORONA_TXT = """<b>Help: COVID 
  
 This command helps you to know daily information about COVID.
  
 Commands and usage: 
  
 /covid - use this command with your country name to get COVID information.
 Example: <code>/covid India</code> 
  
 ⚠️ This service has been stopped 
  
 </b>""" 

    PROGRESS_BAR = """\n
╭━━━━❰ Central Links Renaming... ❱━➣
┣⪼ 🗂️ : {1} | {2}
┣⪼ ⏳️ : {0}%
┣⪼ 🚀 : {3}/s
┣⪼ ⏱️ : {4}
╰━━━━━━━━━━━━━━━➣ """
  
    ABOOK_TXT = """<b>Help : Audiobook 
  
 You can convert a PDF file to an audio file with this command ✯ 
  
 Commands and usage: 
 /audiobook: reply this command to any pdf to generate the audio..."""

    PINGS_TXT = """<b>Ping Testing: Helps you to know your ping 🪄
  
Commands:
• /alive - To check you are alive.
• /help - To get help.
• /ping - <b>To get your ping.
  
Usage:
• These commands can be used in PM and groups.
• These commands can be used by everyone in the groups and bot's PM.
• Share us for more features.
</b>"""

    STICKER_TXT = """<b>You can use this module to find any stickers ID.
  
Usage: To get sticker
  
⭕ How to use
/stickerid
</b>"""

    FONT_TXT = """<b>Usage
  
You can use this module to change font style   
  
Command: /font YOUR TEXT (Optional)
Eg: /font Hello
  
</b>"""

    PURGE_TXT = """<b>Purge
      
Delete a lot of messages from groups!  
      
Admin  
  
◉ /purge: Delete all messages from the replied to message, to the current message</b>"""

    WHOIS_TXT = """<b>Whois Module
  
Note: Give a user details
/whois: Give a user full details 📑
</b>"""

    JSON_TXT = """<b>JSON:  
Bot returns JSON for all replied messages with /json
  
Features:
• Message editing JSON
• PM support
• Group support
  
Note:
• Everyone can use this command, if spamming happens bot will automatically ban you from the group.</b>"""

    URLSHORT_TXT = """<b>Help: URL Shortener
  
<i><b>This command helps you to short to URL </i></b>
  
Commands and Usage:
/short: <b>Use this command with your link to get short links</b>
Example: <code>/short https://youtu.be/example...</code>
</b>"""

    CARB_TXT = """<b>Help for Carbon
  
Carbon is a feature to make the image as shown in the top with your texts.
For using the module just send the text and reply to it with /carbon command the bot will reply with the carbon image
</b>"""

    GEN_PASS = """<b>Help: Password Generator
  
There is nothing to know more. Send me the limit of your password.
- I will give the password of that limit.
  
Commands and Usage:
• /genpassword or /genpw 20
  
Note:
• Only digits are allowed
• Maximum allowed digits till 84  
(I can't generate passwords above the length 84)
• IMDB should have admin privilege.
• These commands works on both PM and group.
• These commands can be used by any group member.</b>"""

    SHARE_TXT = """<b>Get your text share URL.
  
- Ex: /share
  
</b>"""

    PIN_TXT = """<b>Pin Module
Pin a message...
  
All the pin-related commands can be found here:
  
📌Commands and Usage📌
  
/pin: To pin the message on your chats
/unpin: To unpin the current pinned message</b>"""

    RESTART_TXT = """
<b>Bot Restarted!

📅 Date: <code>{}</code>
⏰ Time: <code>{}</code>
🌐 Timezone: <code>Asia/Kolkata</code>
🛠️ Build Status: <code>v2.7.1 [ Stable ]</code></b>"""


    LOGO = """
𝘔𝘢𝘥𝘦 𝘣𝘺 𝘊𝘦𝘯𝘵𝘳𝘢𝘭 𝘓𝘪𝘯𝘬𝘴....

𝘉𝘰𝘵 𝘞𝘰𝘳𝘬𝘪𝘯𝘨 𝘗𝘳𝘰𝘱𝘦𝘳𝘭𝘺"""

    TAMIL_INFO = """
ஹாய் <a href='tg://settings'>என் நண்பன்</a> 

இப்போது டெலிகிராமிலும் பணம் சம்பாதிக்கலாம்.

தந்தி மூலம் பணம் சம்பாதிக்க உங்களிடம் 1 குழு இருக்க வேண்டும்.
உங்களிடம் குழு இருந்தால், உங்கள் குழுவில் எங்கள் போட்டை சேர்ப்பதன் மூலம் பணம் சம்பாதிக்கலாம்.

உங்கள் குழுவில் அதிக உறுப்பினர்கள் இருந்தால், உங்கள் வருமானம் அதிகமாக இருக்கும்.

எப்படி, என்ன செய்வது

படி 1: இந்த CENTRALFILTER3BOT போட் உங்கள் குழுவிற்கு நிர்வகிக்கவும்

படி 2: உங்கள் இணையதளம் மற்றும் API ஐ சேர்க்கவும்

எடுத்துக்காட்டு: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

வீடியோவைச் சேர்க்கவும்

👇 எப்படி சேர்ப்பது 👇

எடுத்துக்காட்டு: /set_tutorial வீடியோ இணைப்பு

மேலும் உங்கள் பயிற்சி உங்கள் குழுவில் சேர்க்கப்படும்..."""

    ENGLISH_INFO = """
Hey <a href='tg://settings'>MY FRIEND</a> 

Now you can earn money on Telegram too.

You must have 1 group to earn money by telegram.
If you have a group, you can earn money by adding our bot to your group.

The more members you have in your group, the higher your income will be.

How and what to do

Step 1: Administer this CENTRALFILTER3BOT bot to your group

Step 2: Add your website and API

Example: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

Add a video

👇 How to add 👇

Example: /set_tutorial video link

Also your tutorial will be Added Your Group..."""

    TELUGU_INFO = """
హే <a href='tg://settings'>నా స్నేహితుడు</a> 

ఇప్పుడు మీరు టెలిగ్రామ్‌లో కూడా డబ్బు సంపాదించవచ్చు.

టెలిగ్రామ్ ద్వారా డబ్బు సంపాదించడానికి మీరు తప్పనిసరిగా 1 గ్రూప్‌ని కలిగి ఉండాలి.
మీకు గ్రూప్ ఉన్నట్లయితే, మా బాట్‌ను మీ గ్రూప్‌కి జోడించడం ద్వారా మీరు డబ్బు సంపాదించవచ్చు.

మీ గ్రూప్‌లో ఎంత ఎక్కువ మంది సభ్యులు ఉంటే మీ ఆదాయం అంత ఎక్కువగా ఉంటుంది.

ఎలా మరియు ఏమి చేయాలి

దశ 1: ఈ CENTRALFILTER3BOT బాట్‌ని మీ సమూహానికి నిర్వహించండి

దశ 2: మీ వెబ్‌సైట్ మరియు APIని జోడించండి

ఉదాహరణ: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

వీడియోను జోడించండి

👇 ఎలా జోడించాలి 👇

ఉదాహరణ: /set_tutorial వీడియో లింక్

అలాగే మీ ట్యుటోరియల్ మీ గ్రూప్‌లో చేర్చబడుతుంది..."""

    HINDI_INFO = """
अरे <a href='tg://settings'>मेरे मित्र</a> 

अब आप टेलीग्राम पर भी पैसे कमा सकते हैं।

टेलीग्राम से पैसे कमाने के लिए आपके पास 1 ग्रुप होना चाहिए।
यदि आपके पास एक समूह है, तो आप हमारे बॉट को अपने समूह में जोड़कर पैसा कमा सकते हैं।

आपके समूह में जितने अधिक सदस्य होंगे, आपकी आय उतनी ही अधिक होगी।

कैसे और क्या करना है

चरण 1: इस CENTRALFILTER3BOT बॉट को अपने समूह में प्रशासित करें

चरण 2: अपनी वेबसाइट और एपीआई जोड़ें

उदाहरण: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

एक वीडियो जोड़ें

👇कैसे जोड़ें 👇

उदाहरण: /set_tutorial वीडियो लिंक

साथ ही आपका ट्यूटोरियल आपके समूह में जोड़ा जाएगा..."""

    MALAYALAM_INFO = """
ഹായ് <a href='tg://settings'>എൻ്റെ സുഹൃത്ത്</a> 

ഇപ്പോൾ നിങ്ങൾക്ക് ടെലിഗ്രാമിലും പണം സമ്പാദിക്കാം.

ടെലിഗ്രാം വഴി പണം സമ്പാദിക്കാൻ നിങ്ങൾക്ക് ഒരു ഗ്രൂപ്പ് ഉണ്ടായിരിക്കണം.
നിങ്ങൾക്ക് ഒരു ഗ്രൂപ്പ് ഉണ്ടെങ്കിൽ, നിങ്ങളുടെ ഗ്രൂപ്പിലേക്ക് ഞങ്ങളുടെ ബോട്ട് ചേർത്തുകൊണ്ട് നിങ്ങൾക്ക് പണം സമ്പാദിക്കാം.

നിങ്ങളുടെ ഗ്രൂപ്പിൽ കൂടുതൽ അംഗങ്ങൾ ഉണ്ടെങ്കിൽ, നിങ്ങളുടെ വരുമാനം ഉയർന്നതായിരിക്കും.

എങ്ങനെ, എന്ത് ചെയ്യണം

ഘട്ടം 1: ഈ CENTRALFILTER3BOT ബോട്ട് നിങ്ങളുടെ ഗ്രൂപ്പിലേക്ക് നൽകുക

ഘട്ടം 2: നിങ്ങളുടെ വെബ്‌സൈറ്റും API-യും ചേർക്കുക

ഉദാഹരണം: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

ഒരു വീഡിയോ ചേർക്കുക

👇 എങ്ങനെ ചേർക്കാം 👇

ഉദാഹരണം: /set_tutorial വീഡിയോ ലിങ്ക്

നിങ്ങളുടെ ട്യൂട്ടോറിയൽ നിങ്ങളുടെ ഗ്രൂപ്പിൽ ചേർക്കും..."""

    URDU_INFO = """
ہائے <a href='tg://settings'>میرے دوست</a> 

اب آپ ٹیلی گرام پر بھی پیسے کما سکتے ہیں۔

ٹیلی گرام کے ذریعے پیسے کمانے کے لیے آپ کے پاس 1 گروپ ہونا ضروری ہے۔
اگر آپ کا کوئی گروپ ہے، تو آپ ہمارے بوٹ کو اپنے گروپ میں شامل کر کے پیسے کما سکتے ہیں۔

آپ کے گروپ میں جتنے زیادہ ممبر ہوں گے آپ کی آمدنی اتنی ہی زیادہ ہوگی۔

کیسے اور کیا کرنا ہے۔

مرحلہ 1: اپنے گروپ میں اس CENTRALFILTER3BOT بوٹ کا انتظام کریں۔

مرحلہ 2: اپنی ویب سائٹ اور API شامل کریں۔

مثال: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

ایک ویڈیو شامل کریں۔

👇 کیسے شامل کریں 👇

مثال: /set_tutorial ویڈیو لنک

نیز آپ کے ٹیوٹوریل کو آپ کے گروپ میں شامل کر دیا جائے گا..."""

    GUJARATI_INFO = """
હેય <a href='tg://settings'>મારા મિત્ર</a> 

હવે તમે ટેલિગ્રામ પર પણ પૈસા કમાઈ શકો છો.

ટેલિગ્રામ દ્વારા પૈસા કમાવવા માટે તમારી પાસે 1 જૂથ હોવું આવશ્યક છે.
જો તમારી પાસે જૂથ છે, તો તમે અમારા બોટને તમારા જૂથમાં ઉમેરીને પૈસા કમાઈ શકો છો.

તમારા જૂથમાં તમારા જેટલા વધુ સભ્યો હશે તેટલી તમારી આવક વધુ હશે.

કેવી રીતે અને શું કરવું

પગલું 1: તમારા જૂથમાં આ CENTRALFILTER3BOT બોટનું સંચાલન કરો

પગલું 2: તમારી વેબસાઇટ અને API ઉમેરો

ઉદાહરણ: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

વિડિઓ ઉમેરો

👇 કેવી રીતે ઉમેરવું 👇

ઉદાહરણ: /set_tutorial વિડિઓ લિંક

તેમજ તમારું ટ્યુટોરીયલ તમારું ગ્રુપ ઉમેરાશે..."""

    KANNADA_INFO = """
ಹಾಯ್ <a href='tg://settings'>ನನ್ನ ಸ್ನೇಹಿತ</a> 

ಈಗ ನೀವು ಟೆಲಿಗ್ರಾಮ್‌ನಲ್ಲಿಯೂ ಹಣ ಗಳಿಸಬಹುದು.

ಟೆಲಿಗ್ರಾಮ್ ಮೂಲಕ ಹಣ ಗಳಿಸಲು ನೀವು 1 ಗುಂಪನ್ನು ಹೊಂದಿರಬೇಕು.
ನೀವು ಗುಂಪನ್ನು ಹೊಂದಿದ್ದರೆ, ನಮ್ಮ ಬೋಟ್ ಅನ್ನು ನಿಮ್ಮ ಗುಂಪಿಗೆ ಸೇರಿಸುವ ಮೂಲಕ ನೀವು ಹಣವನ್ನು ಗಳಿಸಬಹುದು.

ನಿಮ್ಮ ಗುಂಪಿನಲ್ಲಿ ನೀವು ಹೆಚ್ಚು ಸದಸ್ಯರನ್ನು ಹೊಂದಿದ್ದರೆ, ನಿಮ್ಮ ಆದಾಯವು ಹೆಚ್ಚಾಗುತ್ತದೆ.

ಹೇಗೆ ಮತ್ತು ಏನು ಮಾಡಬೇಕು

ಹಂತ 1: ಈ CENTRALFILTER3BOT ಬೋಟ್ ಅನ್ನು ನಿಮ್ಮ ಗುಂಪಿಗೆ ನಿರ್ವಹಿಸಿ

ಹಂತ 2: ನಿಮ್ಮ ವೆಬ್‌ಸೈಟ್ ಮತ್ತು API ಸೇರಿಸಿ

ಉದಾಹರಣೆ: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

ವೀಡಿಯೊ ಸೇರಿಸಿ

👇 ಸೇರಿಸುವುದು ಹೇಗೆ 👇

ಉದಾಹರಣೆ: /set_tutorial ವೀಡಿಯೊ ಲಿಂಕ್

ನಿಮ್ಮ ಟ್ಯುಟೋರಿಯಲ್ ಅನ್ನು ನಿಮ್ಮ ಗುಂಪಿಗೆ ಸೇರಿಸಲಾಗುತ್ತದೆ..."""

    BANGLADESH_INFO = """
হাই <a href='tg://settings'>আমার বন্ধু</a> 

এখন আপনি টেলিগ্রামেও অর্থ উপার্জন করতে পারেন।

টেলিগ্রামের মাধ্যমে অর্থ উপার্জন করতে আপনার অবশ্যই 1টি গ্রুপ থাকতে হবে।
আপনার যদি একটি গ্রুপ থাকে, আপনি আপনার গ্রুপে আমাদের বট যোগ করে অর্থ উপার্জন করতে পারেন।

আপনার গ্রুপে যত বেশি সদস্য থাকবেন আপনার আয় তত বেশি হবে।

কিভাবে এবং কি করতে হবে

ধাপ 1: আপনার গ্রুপে এই CENTRALFILTER3BOT বট পরিচালনা করুন

ধাপ 2: আপনার ওয়েবসাইট এবং API যোগ করুন

উদাহরণ: /shortlink earnwithlink.com 14de6aaacf1601fe7b7c1de78d154dacb970dbe4

একটি ভিডিও যোগ করুন

👇 কিভাবে যোগ করবেন 👇

উদাহরণ: /set_tutorial ভিডিও লিঙ্ক

এছাড়াও আপনার টিউটোরিয়ালটি আপনার গ্রুপে যুক্ত করা হবে..."""

    DEVELOPER_TXT = """
Special Thanks To ❤️ Developers -

- Dev 1 [Owner of this bot]<a href='https://t.me/Thiyaku_Suriya'>VJ</a>

- Dev 2 <a href='https://t.me/Central_Links'>Central Links</a>
"""

    RENAME_TXT = """
🌌 <b><u>HOW TO SET THUMBNAIL</u></b>
  
• /set_thumb - send any picture to automatically set thumbnail.
• /del_thumb use this command and delete your old thumbnail.
• /view_thumb use this command view your current thumbnail.

📑 <b><u>HOW TO SET CUSTOM CAPTION</u></b>

• /set_caption - set a custom caption
• /see_caption - see your custom caption
• /del_caption - delete custom caption

Example:- /set_caption 📕 File Name: {filename}
💾 Size: {filesize}
⏰ Duration: {duration}

✏️ <b><u>HOW TO RENAME A FILE</u></b>

• /rename - send any file and click rename option and type new file name and then select [document, video, audio]
"""

    STREAM_TXT = """
<b><u>HOW TO GET STREAM AND DOWNLOAD LINK :</u>

/stream - get streamable and downloadable link of any file</b>
"""
