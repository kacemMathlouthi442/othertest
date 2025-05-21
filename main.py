import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keepalive import app
from aiogram.types import FSInputFile
from aiogram import Bot
from aiogram.types import ChatMember
from aiogram.enums.chat_member_status import ChatMemberStatus
import os


bot = Bot(token=os.environ.get('token'))
dp = Dispatcher()



async def is_user_subscribed(bot: Bot, user_id, channel , vouches):
    try:
        member: ChatMember = await bot.get_chat_member(chat_id=channel, user_id=user_id)
        member1: ChatMember = await bot.get_chat_member(chat_id=vouches, user_id=user_id)
        return member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.CREATOR, ChatMemberStatus.ADMINISTRATOR] and member1.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.CREATOR, ChatMemberStatus.ADMINISTRATOR]
    except:
        return True


@dp.message(Command("black"))
async def send_local_video(message: Message):
    user_id = message.from_user.id
    if user_id == 7674917466 or user_id == 7575518830:
        args = message.text.split(maxsplit=1)
        with open("blacklist.txt", 'a') as f:
            f.write(f"{args[1]}\n")
        await bot.send_message(chat_id=7674917466,text='user added to black list successfully!')

        for msg_id in range(message.message_id - 100, message.message_id):
            try:
                await bot.delete_message(chat_id=int(args[1]), message_id=msg_id)
            except:
                pass
@dp.message(Command("start"))
async def send_local_video(message: Message):
    iduser = str(message.from_user.id)
    with open("blacklist.txt", 'r') as f:
        blacklist = set(line.strip() for line in f.readlines())
    if iduser not in blacklist:
        name = message.from_user.first_name
        if message.from_user.username:
            username = "@"+message.from_user.username
        else:
            username='None'
        with open("users.txt", 'r') as f:
            users = set(line.strip() for line in f.readlines())
        if iduser not in users:
            with open("users.txt", 'a') as f:
                f.write(f"{iduser}\n")
            await bot.send_message(chat_id=7674917466,text='🆕 New user\nUsername: '+username+'\nName: '+name+'\nUser ID: '+iduser+'\nTotal users: '+str(len(users)+1))
        keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
            ],
            [
                InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
                InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1"),
            ],
            [
                InlineKeyboardButton(text="⚙️ Commands", callback_data="Commands"),
                InlineKeyboardButton(text="🧠 Features", callback_data="Features")
            ],
            [
                InlineKeyboardButton(text="💳 Purchase", callback_data="Purchase")
            ],
            [
                InlineKeyboardButton(text="🎯 Enter Bot", callback_data="enter")
            ]
        ]
        )
        video = FSInputFile("img.jpg")  # Path to your local file
        await message.answer_photo(video, caption="""*The Ultimate Spoofing Experience*
                                
    Hello *"""+name+"""*\, Welcome to *DRAGON OTP v2\.0* 🐲\.                         
    *DRAGON OTP* is the \#1 Telegram\-based OTP spoofing system built for professionals\.

    Powered by advanced *AI*\, global *voice routing*\, and *real\-time control*\, it delivers unmatched OTP grabbing performance\.

    ✅ *Lightning\-fast execution*
    ✅ *Stealth\-grade spoofing*
    ✅ *Full automation tools*
    ✅ *Global reach with 100% uptime*

    Whether you're *testing*\, *analyzing*\, or *automating* — DRAGON OTP gives you the *precision*\, *power*\, and *stealth* you need to *dominate*\.""", reply_markup=keyboard,parse_mode='MarkdownV2')

@dp.message(Command("redeem"))
async def send_local_video(message: Message): #NEED WORK
    user_id = str(message.from_user.id)
    with open("blacklist.txt", 'r') as f:
        blacklist = set(line.strip() for line in f.readlines())
    if user_id not in blacklist:
        args = message.text.split(maxsplit=1)
        with open("subscribers.txt", 'r') as f:
            subscribers = set(line.strip() for line in f.readlines())
        with open("API.txt", 'r') as f:
            APIs = set(line.strip() for line in f.readlines())
        if len(args) > 2:
            await message.answer("❌ You must provide only one argument. /redeem [activation key]")
        elif len(args) < 2:
            await message.answer("❌ Please add your activation key. /redeem [activation key]")
        elif args[1] == 'PTd82e519c42cc97d5066b4423c718c8a132ebaf07dab24d32':
            with open("API.txt", 'a') as f:
                f.write(f"{user_id}\n")
            await message.answer("✅ API Token redeemed successfuly!")
        elif user_id not in APIs:
            keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
            ]])
            await message.answer("⚠️ Sorry, we facing a problem in your account, you have to buy an APi token.\n\nContact the support to buy one.",reply_markup=keyboard)
        else:
            if args[1] == 'DRAGONOTP-F4awb4Vf1KJp7P4LhCa1':
                if user_id not in subscribers:
                    with open("subscribers.txt", 'a') as f:
                        f.write(f"{user_id}\n")
                await message.answer("✅ 1-Day key redeemed successfuly!")
            elif args[1] == 'DRAGONOTP-F4awb4Vf1KJp7P4LhCa2':
                await message.answer("✅ 2-Days key redeemed successfuly!")
                if user_id not in subscribers:
                    with open("subscribers.txt", 'a') as f:
                        f.write(f"{user_id}\n")
            elif args[1] == 'DRAGONOTP-F4awb4Vf1KJp7P4LhCa7':
                await message.answer("✅ 1-Week key redeemed successfuly!")
                if user_id not in subscribers:
                    with open("subscribers.txt", 'a') as f:
                        f.write(f"{user_id}\n")
            elif args[1] == 'DRAGONOTP-F4awb4Vf1KJp7P4LhC14':
                await message.answer("✅ 2-Weeks key redeemed successfuly!")
                if user_id not in subscribers:
                    with open("subscribers.txt", 'a') as f:
                        f.write(f"{user_id}\n")
            elif args[1] == 'DRAGONOTP-F4awb4Vf1KJp7P4LhC30':
                await message.answer("✅ 1-Month key redeemed successfuly!")
                if user_id not in subscribers:
                    with open("subscribers.txt", 'a') as f:
                        f.write(f"{user_id}\n")
            elif args[1] == 'DRAGONOTP-F4awb4Vf1KJp7P4LhC60':
                await message.answer("✅ 2-Months key redeemed successfuly!")
                if user_id not in subscribers:
                    with open("subscribers.txt", 'a') as f:
                        f.write(f"{user_id}\n")
            elif args[1] == 'DRAGONOTP-C4awb4Vf1KJp7P4LhCaN':
                await message.answer("✅ Custum key redeemed successfuly!")
                if user_id not in subscribers:
                    with open("subscribers.txt", 'a') as f:
                        f.write(f"{user_id}\n")
            elif args[1] == 'DRAGONOTP1-C4awb4Vf1KJp7P4LhCaN':
                await message.answer("✅ Premium access key redeemed successfuly!")
                if user_id not in subscribers:
                    with open("blacklist.txt", 'a') as f:
                        f.write(f"{user_id}\n")
            else:
                await message.answer("❌ Unavailable or expired key.")


@dp.message(Command("Phonelist"))
async def send_local_video(message: Message):
    user_id = message.from_user.id
    with open("blacklist.txt", 'r') as f:
        blacklist = set(line.strip() for line in f.readlines())
    if user_id not in blacklist:
        channel_username = "@dragonotpchannel"
        vouches = "@DragonOtp_Vouches1"
        if await is_user_subscribed(bot, user_id, channel_username,vouches):
            with open("subscribers.txt", 'r') as f:
                subscribers = set(line.strip() for line in f.readlines())
            if user_id in subscribers:
                keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
                ]
            ]
            )
                await message.answer("""🐲 *Spoofing Numbers*

            》 bank \| `\+12025550100`
            》 chase \| `\+12025550101`   
            》 wfc \| `\+12025550102`  
            》 boa \| `\+12025550103`  
            》 citizens \| `\+12025550104`  
            》 AccNo \| `\+12025550105`  
            》 RT \| `\+12025550106`                                                              
            》 applepay \| `\+12025550107`  
            》 coinbase \| `\+12025550108`  
            》 amazon \| `\+12025550109`  
            》 paypal \| `\+12025550110`  
            》 venmo \| `\+12025550111`                                   
            》 cashapp \| `\+12025550112`  
            》 quadpay \| `\+12025550113`  
            》 carrier \| `\+12025550114` """,parse_mode='MarkdownV2',reply_markup=keyboard)
            else:
                keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="💳 Purchase Subscription", callback_data="Purchase")
            ],
            [
                InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
            ]
        ]
        )
            await message.answer("❌ You have to Subscribe first to use this command!")
        else:
            keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
                InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1")
            ],
            [
                InlineKeyboardButton(text="📍 I've Subscribed", callback_data="start")
            ]
        ]
        )
            await message.answer("""⚠️ *You are not subscribed to our channels*

    To use the bot, please subscribe to the required channels and group\.

    👇 Click the buttons below to reach our channels\:""",parse_mode='MarkdownV2', reply_markup=keyboard)

@dp.callback_query(F.data.in_(["start"]))
async def send_local_video(callback: CallbackQuery):
    user_id = callback.from_user.id
    channel_username = "@dragonotpchannel"
    vouches = "@DragonOtp_Vouches1"
    if await is_user_subscribed(bot, user_id, channel_username,vouches):
        await callback.message.delete()
        keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
            ],
            [
                InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
                InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1"),
            ],
            [
                InlineKeyboardButton(text="⚙️ Commands", callback_data="Commands"),
                InlineKeyboardButton(text="🧠 Features", callback_data="Features")
            ],
            [
                InlineKeyboardButton(text="💳 Purchase Subscription", callback_data="Purchase")
            ],
            [
                InlineKeyboardButton(text="🎯 Enter Bot", callback_data="enter")
            ]
        ]
        )
        video = FSInputFile("img.jpg")  # Path to your local file
        await callback.message.answer_photo(video, caption="""🐲 *DRAGON OTP v2\.0* \- Ultimate Spoofing Experience

    *DRAGON OTP* is the \#1 Telegram\-based OTP spoofing system built for professionals\.

    It combines cutting\-edge AI, global voice routing, and real\-time control to deliver the most advanced OTP grabbing experience on the market\.

    Whether you're testing, analyzing, or automating — DRAGON OTP gives you the tools to dominate with speed, stealth, and precision\.""", reply_markup=keyboard,parse_mode='MarkdownV2')
    else:
        await callback.message.delete()
        await callback.message.answer("""⚠️ *You didn't subscribe yet*

To use the bot, please subscribe to the required channels and group\.

👇 Click the buttons below to reach our channels\:""",parse_mode='MarkdownV2', reply_markup=keyboard)
    await callback.answer() 


@dp.callback_query(F.data.in_(["Commands"]))
async def handle_vote(callback: CallbackQuery, bot: Bot):
    user_id = callback.from_user.id
    channel_username = "@dragonotpchannel"
    vouches = "@DragonOtp_Vouches1"
    if await is_user_subscribed(bot, user_id, channel_username,vouches):
        keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
        ]
    ]
    )
        await callback.message.delete()
        await callback.message.answer("""🐲 DRAGON OTP v2.0  - 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 ( INTERNATIONAL CALLS )
  ❓ 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 
    🔑 》/redeem | 𝙍𝙚𝙙𝙚𝙚𝙢 𝙖 𝙠𝙚𝙮
    📲 》/call | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 𝘼𝙣𝙮 𝙘𝙤𝙙𝙚 
    📱 》/Phonelist | Check List of Latest Spoof Numbers  
                                                 
  📞 Available Services For /call command                 
    🏦 》 bank | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 𝙗𝙖𝙣𝙠 𝙊𝙏𝙋 𝙘𝙤𝙙𝙚
    🏦 》 chase | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 𝘾𝙝𝙖𝙨𝙚 𝙊𝙏𝙋 𝙘𝙤𝙙𝙚   
    🏦 》 wfc | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 𝙒𝙚𝙡𝙡𝙨 𝙁𝙖𝙧𝙜𝙤 𝙊𝙏𝙋 𝙘𝙤𝙙𝙚 
    🏦 》 boa | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 𝘽𝙖𝙣𝙠 𝙤𝙛 𝘼𝙢𝙚𝙧𝙞𝙘𝙖 𝙊𝙏𝙋 𝙘𝙤𝙙𝙚 
    🏦 》 citizens | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 𝘾𝙞𝙩𝙞𝙯𝙚𝙣𝙨 𝙊𝙏𝙋 𝙘𝙤𝙙𝙚
    💼 》 AccNo | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 𝘼𝙘𝙘𝙤𝙪𝙣𝙩 𝙉𝙪𝙢𝙗𝙚𝙧 
    💼 》 RT | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 𝙍𝙤𝙪𝙩𝙞𝙣𝙜 𝙉𝙪𝙢𝙗𝙚𝙧                                                              
    🍏 》 applepay | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 𝙊𝙏𝙋 𝘾𝙧𝙚𝙙𝙞𝙩 𝘾𝙖𝙧𝙙
    🔵 》 coinbase | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 2𝙁𝘼 𝘾𝙤𝙙𝙚
    📦 》 amazon | 𝘼𝙥𝙥𝙧𝙤𝙫𝙖𝙡 𝘼𝙪𝙩𝙝𝙚𝙣𝙩𝙞𝙘𝙖𝙩𝙞𝙤𝙣
    🅿️ 》 paypal | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 𝙋𝙖𝙮𝙥𝙖𝙡 𝘾𝙤𝙙𝙚
    🏦 》 venmo | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 𝙑𝙚𝙣𝙢𝙤 𝘾𝙤𝙙𝙚                                   
    💵 》 cashapp | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 𝘾𝙖𝙨𝙝𝙖𝙥𝙥 𝘾𝙤𝙙𝙚
    💳 》 quadpay | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 𝙦𝙪𝙖𝙙𝙥𝙖𝙮 𝘾𝙤𝙙𝙚
    📟 》 carrier | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 𝙘𝙖𝙧𝙧𝙞𝙚𝙧 𝘾𝙤𝙙𝙚""",reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
            InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1")
        ],
        [
            InlineKeyboardButton(text="📍 I've Subscribed", callback_data="start")
        ]
    ]
    )
        await callback.message.delete()
        await callback.message.answer("""⚠️ *You are not subscribed to our channels*

To use the bot, please subscribe to the required channels and group\.

👇 Click the buttons below to reach our channels\:""",parse_mode='MarkdownV2', reply_markup=keyboard)
    await callback.answer() 


@dp.message(Command("call"))
async def send_local_video(message: Message):
    user_id = str(message.from_user.id)
    with open("blacklist.txt", 'r') as f:
        blacklist = set(line.strip() for line in f.readlines())
    if user_id not in blacklist:
        channel = "@dragonotpchannel"
        vouches = "@DragonOtp_Vouches1"
        with open("subscribers.txt", 'r') as f:
            subscribers = set(line.strip() for line in f.readlines())
        if user_id in subscribers:
            keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
            ],
            [
                InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
            ]
        ]
        )
            await message.answer("❌ Sorry your country doesen't support the spofing.\n\nYou have to Buy a premium access.\n\n❕ the call from your country it's soo expensive in the premium access you will get a full control of the bot but you have to cost more.\nSorry for your time and thanks for your attention.\nContact the support to buy a premium subscription.",reply_markup=keyboard)
        elif is_user_subscribed(bot, user_id, channel, vouches):
            keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="💳 Purchase Subscription", callback_data="Purchase")
            ],
            [
                InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
            ]
        ]
        )
            await message.answer("❌ You have to Subscribe first to use this command!")
        else:
            keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
                InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1")
            ],
            [
                InlineKeyboardButton(text="📍 I've Subscribed", callback_data="start")
            ]
        ]
        )
            await message.answer("""⚠️ *You are not subscribed to our channels*

    To use the bot, please subscribe to the required channels and group\.

    👇 Click the buttons below to reach our channels\:""",parse_mode='MarkdownV2', reply_markup=keyboard)

@dp.callback_query(F.data.in_(["Purchase"]))
async def handle_vote1(callback: CallbackQuery, bot: Bot):
    user_id = callback.from_user.id
    channel_username = "@dragonotpchannel"
    vouches = "@DragonOtp_Vouches1"
    if await is_user_subscribed(bot, user_id, channel_username,vouches):
        keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
        ],
        [
            InlineKeyboardButton(text="💲 USDT", callback_data="usdt"),
            InlineKeyboardButton(text="♢ ETH", callback_data="eth")
        ],
        [
            InlineKeyboardButton(text="𝑳 LTC", callback_data="ltc"),
            InlineKeyboardButton(text="◎ SOL", callback_data="sol")
        ],
        [
            InlineKeyboardButton(text="₿ BTC", callback_data="btc")
        ]
    ]
    )
        await callback.message.delete()
        await callback.message.answer("""🐲 *DRAGON OTP v2\.0* Prices list 💰
━━━━━━━━━━━━━━━━
• 1 Day Plan *\(25$\)*
• 2 Days Plan *\(30$\)*
• 1 Week Plan *\(40$\)*
• 2 Weeks Plan *\(55$\)* 
• 1 Month Plan *\(70$\)*
• 2 Months Plan *\(100$\)*
━━━━━━━━━━━━━━━━
 
📩 After payment\, send a screenshot to SUPPORT to verify your subscription\.
❓ Need help or a different wallet\? Contact SUPPORT\.""",parse_mode='MarkdownV2',reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
            InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1")
        ],
        [
            InlineKeyboardButton(text="📍 I've Subscribed", callback_data="start")
        ]
    ]
    )
        await callback.message.delete()
        await callback.message.answer("""⚠️ *You are not subscribed to our channels*

To use the bot, please subscribe to the required channels and group\.

👇 Click the buttons below to reach our channels\:""",parse_mode='MarkdownV2', reply_markup=keyboard)
    await callback.answer() 


@dp.callback_query(F.data.in_(["Features"]))
async def handle_vote1(callback: CallbackQuery, bot: Bot):
    user_id = callback.from_user.id
    channel_username = "@dragonotpchannel"
    vouches = "@DragonOtp_Vouches1"
    if await is_user_subscribed(bot, user_id, channel_username,vouches):
        keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
        ]
    ]
    )
        await callback.message.delete()
        video = FSInputFile("img.jpg")  # Path to your local file
        await callback.message.answer_photo(video, caption="""🐉 *UNIQUE FEATURES*

🚀 Lightning Fast OTP Delivery  
🎭 Custom Caller ID \(Spoofing Mode\)  
🔊 AI Voice Calls with Human Detection  
📞 Call Any Number Worldwide  
📦 Multiple OTP Services Supported  
📁 Live Call Recording \& Logs  
📊 Real\-Time Dashboard \& Analytics  
🔐 Encrypted Access \& Security  
📲 Use Anywhere Anytime""",parse_mode='MarkdownV2',reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
            InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1")
        ],
        [
            InlineKeyboardButton(text="📍 I've Subscribed", callback_data="start")
        ]
    ]
    )
        await callback.message.delete()
        await callback.message.answer("""⚠️ *You are not subscribed to our channels*

To use the bot, please subscribe to the required channels and group\.

👇 Click the buttons below to reach our channels\:""",parse_mode='MarkdownV2', reply_markup=keyboard)
    await callback.answer() 


@dp.callback_query(F.data.in_(["enter"]))
async def handle_vote1(callback: CallbackQuery, bot: Bot):
    user_id = str(callback.from_user.id)
    channel_username = "@dragonotpchannel"
    vouches = "@DragonOtp_Vouches1"
    if await is_user_subscribed(bot, user_id, channel_username,vouches):
        with open("subscribers.txt", 'r') as f:
            subscribers = set(line.strip() for line in f.readlines())
        if user_id in subscribers:
            keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
            ]
        ]
        )
            await callback.message.delete()
            video = FSInputFile("img.jpg")  # Path to your local file
            await callback.message.answer_photo(video, caption="""🐲 *Dragon OTP v2\.0 Bot*
📡 *Status*\: Fully Operational \| ⏱️ *Uptime: 100%*

🚀 *Limited Access*\: Only few spots remaining\!

⚠️ Active License Detected\!""",parse_mode='MarkdownV2',reply_markup=keyboard)
        else:
            keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="💳 Purchase Subscription", callback_data="Purchase")
            ],
            [
                InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
            ]
        ]
        )
            await callback.message.delete()
            video = FSInputFile("img.jpg")  # Path to your local file
            await callback.message.answer_photo(video, caption="""🐲 *Dragon OTP v2\.0 Bot*
📡 *Status*\: Fully Operational \| ⏱️ *Uptime: 100%*

🚀 *Limited Access*\: Only few spots remaining\!

⚠️ No Active License Detected\!

🔐 To activate the bot, you must first purchase a license\.
💸 We recommend getting a [LICENSE BUNDLE](https\://t\.me/dragonotpowner) for exclusive features and the best discounted price\!""",parse_mode='MarkdownV2',reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
            InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1")
        ],
        [
            InlineKeyboardButton(text="📍 I've Subscribed", callback_data="start")
        ]
    ]
    )
        await callback.message.delete()
        await callback.message.answer("""⚠️ *You are not subscribed to our channels*

To use the bot, please subscribe to the required channels and group\.

👇 Click the buttons below to reach our channels\:""",parse_mode='MarkdownV2', reply_markup=keyboard)
    await callback.answer()

@dp.callback_query(F.data.in_(["btc"]))
async def handle_vote1(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
        ],
        [
            InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
        ]
    ]
    )
    await callback.message.delete()
    await callback.message.answer("""*Bitcoin \(BTC\)*
                                  
• `bc1q98y83fh28y6ysklu9qmla7enuegldmgdcdawvk`""",parse_mode='MarkdownV2', reply_markup=keyboard)


@dp.callback_query(F.data.in_(["usdt"]))
async def handle_vote1(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
        ],
        [
            InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
        ]
    ]
    )
    await callback.message.delete()
    await callback.message.answer("""*USDT \(TRC20\)*
                                  
• `TRRVAuPEGJ4EgE33u1pV6gNUXxM1R5v1aY`""",parse_mode='MarkdownV2', reply_markup=keyboard)


@dp.callback_query(F.data.in_(["sol"]))
async def handle_vote1(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
        ],
        [
            InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
        ]
    ]
    )
    await callback.message.delete()
    await callback.message.answer("""*Solana \(SOL\)*
                                  
• `8Ra9HKVrKNakEeQfqDzrVn1sFoQoFmbR51UHMRweT9hY`""",parse_mode='MarkdownV2', reply_markup=keyboard)


@dp.callback_query(F.data.in_(["eth"]))
async def handle_vote1(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
        ],
        [
            InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
        ]
    ]
    )
    await callback.message.delete()
    await callback.message.answer("""*Ethereum \(ETH\)*
                                  
• `0xc76acc06684b2e2a2d43b9ba3b5f2618cd7a6307`""",parse_mode='MarkdownV2', reply_markup=keyboard)


@dp.callback_query(F.data.in_(["ltc"]))
async def handle_vote1(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
        ],
        [
            InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
        ]
    ]
    )
    await callback.message.delete()
    await callback.message.answer("""*Litecoin \(LTC\)*
                                  
• `LRJ8n55djedy4jyKP3Kkqi6iEy3BYC1FLt`""",parse_mode='MarkdownV2', reply_markup=keyboard)



async def run_bot():
    await dp.start_polling()

def start_bot():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_running_loop()

    loop.create_task(run_bot())

start_bot()
