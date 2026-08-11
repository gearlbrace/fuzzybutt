"""
MIT License

Copyright (c) 2024 TheHamkerCat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import asyncio
import sys
from contextlib import suppress
from sys import version as pyver
from time import ctime, time

from motor import version as mongover
from pykeyboard import InlineKeyboard
from pyrogram import __version__ as pyrover
from pyrogram import enums, filters
from pyrogram.raw.functions import Ping
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InlineQueryResultCachedDocument,
    InputTextMessageContent,
)
from search_engine_parser import GoogleSearch

from wbb import (
    BOT_USERNAME,
    SUDOERS,
    USERBOT_ID,
    USERBOT_NAME,
    USERBOT_USERNAME,
    app,
    app2,
)
from wbb.core.keyboard import ikb
from wbb.core.tasks import _get_tasks_text, all_tasks, rm_task
from wbb.modules.info import get_chat_info, get_user_info
from wbb.utils.functions import test_speedtest

keywords_list = [
    "speedtest",
    "search",
    "ping",
    "info",
    "google",
    "music",
]


async def inline_help_func(__HELP__):
    buttons = InlineKeyboard(row_width=4)
    buttons.add(
        *[
            (InlineKeyboardButton(text=i, switch_inline_query_current_chat=i))
            for i in keywords_list
        ]
    )
    answerss = [
        InlineQueryResultArticle(
            title="Inline Commands",
            description="Help Related To Inline Usage.",
            input_message_content=InputTextMessageContent(
                "Click A Button To Get Started."
            ),
            thumb_url="https://hamker.me/cy00x5x.png",
            reply_markup=buttons,
        ),
        InlineQueryResultArticle(
            title="Github Repo",
            description="Get Github Respository Of Bot.",
            input_message_content=InputTextMessageContent(
                "https://github.com/thehamkercat/WilliamButcherBot"
            ),
            thumb_url="https://hamker.me/gjc9fo3.png",
        ),
    ]
    answerss = await alive_function(answerss)
    return answerss


async def alive_function(answers):
    buttons = InlineKeyboard(row_width=2)
    bot_state = "Dead" if not await app.get_me() else "Alive"
    ubot_state = "Dead" if not await app2.get_me() else "Alive"
    buttons.add(
        InlineKeyboardButton("Stats", callback_data="stats_callback"),
        InlineKeyboardButton(
            "Go Inline!", switch_inline_query_current_chat=""
        ),
    )

    msg = f"""
**[William✨](https://github.com/thehamkercat/WilliamButcherBot):**
**MainBot:** `{bot_state}`
**UserBot:** `{ubot_state}`
**Python:** `{pyver.split()[0]}`
**Pyrogram:** `{pyrover}`
**MongoDB:** `{mongover}`
**Platform:** `{sys.platform}`
**Profiles:** [BOT](t.me/{BOT_USERNAME}) | [UBOT](t.me/{USERBOT_USERNAME})
"""
    answers.append(
        InlineQueryResultArticle(
            title="Alive",
            description="Check Bot's Stats",
            thumb_url="https://static2.aniimg.com/upload/20170515/414/c/d/7/cd7EEF.jpg",
            input_message_content=InputTextMessageContent(
                msg, disable_web_page_preview=True
            ),
            reply_markup=buttons,
        )
    )
    return answers


async def google_search_func(answers, text):
    gresults = await GoogleSearch().async_search(text)
    limit = 0
    for i in gresults:
        if limit > 48:
            break
        limit += 1

        with suppress(KeyError):
            msg = f"""
[{i['titles']}]({i['links']})
{i['descriptions']}"""

            answers.append(
                InlineQueryResultArticle(
                    title=i["titles"],
                    description=i["descriptions"],
                    input_message_content=InputTextMessageContent(
                        msg, disable_web_page_preview=True
                    ),
                )
            )
    return answers


async def tg_search_func(answers, text, user_id):
    if user_id not in SUDOERS:
        msg = "**ERROR**\n__THIS FEATURE IS ONLY FOR SUDO USERS__"
        answers.append(
            InlineQueryResultArticle(
                title="ERROR",
                description="THIS FEATURE IS ONLY FOR SUDO USERS",
                input_message_content=InputTextMessageContent(msg),
            )
        )
        return answers
    if str(text)[-1] != ":":
        msg = "**ERROR**\n__Put A ':' After The Text To Search__"
        answers.append(
            InlineQueryResultArticle(
                title="ERROR",
                description="Put A ':' After The Text To Search",
                input_message_content=InputTextMessageContent(msg),
            )
        )

        return answers
    text = text[0:-1]
    async for message in app2.search_global(text, limit=49):
        buttons = InlineKeyboard(row_width=2)
        buttons.add(
            InlineKeyboardButton(
                text="Origin",
                url=message.link if message.link else "https://t.me/telegram",
            ),
            InlineKeyboardButton(
                text="Search again",
                switch_inline_query_current_chat="search",
            ),
        )
        name = (
            message.from_user.first_name
            if message.from_user.first_name
            else "NO NAME"
        )
        caption = f"""
**Query:** {text}
**Name:** {str(name)} [`{message.from_user.id}`]
**Chat:** {str(message.chat.title)} [`{message.chat.id}`]
**Date:** {ctime(message.date)}
**Text:** >>

{message.text.markdown if message.text else message.caption if message.caption else '[NO_TEXT]'}
"""
        result = InlineQueryResultArticle(
            title=name,
            description=message.text if message.text else "[NO_TEXT]",
            reply_markup=buttons,
            input_message_content=InputTextMessageContent(
                caption, disable_web_page_preview=True
            ),
        )
        answers.append(result)
    return answers


async def music_inline_func(answers, query):
    chat_id = -1001445180719
    group_invite = "https://t.me/joinchat/vSDE2DuGK4Y4Nzll"
    try:
        messages = [
            m
            async for m in app2.search_messages(
                chat_id, query, filter=enums.MessagesFilter.AUDIO, limit=100
            )
        ]
    except Exception as e:
        print(e)
        msg = f"You Need To Join Here With Your Bot And Userbot To Get Cached Music.\n{group_invite}"
        answers.append(
            InlineQueryResultArticle(
                title="ERROR",
                description="Click Here To Know More.",
                input_message_content=InputTextMessageContent(
                    msg, disable_web_page_preview=True
                ),
            )
        )
        return answers
    messages_ids_and_duration = []
    for f_ in messages:
        messages_ids_and_duration.append(
            {
                "id": f_.id,
                "duration": f_.audio.duration if f_.audio.duration else 0,
            }
        )
    messages = list(
        {v["duration"]: v for v in messages_ids_and_duration}.values()
    )
    messages_ids = [ff_["id"] for ff_ in messages]
    messages = await app.get_messages(chat_id, messages_ids[0:48])
    return [
        InlineQueryResultCachedDocument(
            document_file_id=message_.audio.file_id,
            title=message_.audio.title,
        )
        for message_ in messages
    ]


async def speedtest_init(query):
    answers = []
    user_id = query.from_user.id
    if user_id not in SUDOERS:
        msg = "**ERROR**\n__THIS FEATURE IS ONLY FOR SUDO USERS__"
        answers.append(
            InlineQueryResultArticle(
                title="ERROR",
                description="THIS FEATURE IS ONLY FOR SUDO USERS",
                input_message_content=InputTextMessageContent(msg),
            )
        )
        return answers
    msg = "**Click The Button Below To Perform A Speedtest**"
    button = InlineKeyboard(row_width=1)
    button.add(
        InlineKeyboardButton(text="Test", callback_data="test_speedtest")
    )
    answers.append(
        InlineQueryResultArticle(
            title="Click Here",
            input_message_content=InputTextMessageContent(msg),
            reply_markup=button,
        )
    )
    return answers


# CallbackQuery for the function above


@app.on_callback_query(filters.regex("test_speedtest"))
async def test_speedtest_cq(_, cq):
    if cq.from_user.id not in SUDOERS:
        return await cq.answer("This Isn't For You!")
    inline_message_id = cq.inline_message_id
    await app.edit_inline_text(inline_message_id, "**Testing**")
    loop = asyncio.get_running_loop()
    download, upload, info = await loop.run_in_executor(None, test_speedtest)
    msg = f"""
**Download:** `{download}`
**Upload:** `{upload}`
**Latency:** `{info['latency']} ms`
**Country:** `{info['country']} [{info['cc']}]`
**Latitude:** `{info['lat']}`
**Longitude:** `{info['lon']}`
"""
    await app.edit_inline_text(inline_message_id, msg)


async def pmpermit_func(answers, user_id, victim):
    if user_id != USERBOT_ID:
        return
    caption = f"Hi, I'm {USERBOT_NAME}, What are you here for?, You'll be blocked if you send more than 5 messages."
    buttons = InlineKeyboard(row_width=2)
    buttons.add(
        InlineKeyboardButton(
            text="To Scam You", callback_data="pmpermit to_scam_you a"
        ),
        InlineKeyboardButton(
            text="For promotion",
            callback_data="pmpermit to_scam_you a",
        ),
        InlineKeyboardButton(
            text="Approve me", callback_data="pmpermit approve_me a"
        ),
        InlineKeyboardButton(
            text="Approve", callback_data=f"pmpermit approve {victim}"
        ),
        InlineKeyboardButton(
            text="Block & Delete",
            callback_data=f"pmpermit block {victim}",
        ),
    )
    answers.append(
        InlineQueryResultArticle(
            title="do_not_click_here",
            reply_markup=buttons,
            input_message_content=InputTextMessageContent(caption),
        )
    )
    return answers


async def ping_func(answers):
    ping = Ping(ping_id=app.rnd_id())
    t1 = time()
    await app.invoke(ping)
    t2 = time()
    ping = f"{str(round((t2 - t1) * 1000, 2))} ms"
    answers.append(
        InlineQueryResultArticle(
            title=ping,
            input_message_content=InputTextMessageContent(f"__**{ping}**__"),
        )
    )
    return answers


async def info_inline_func(answers, peer):
    not_found = InlineQueryResultArticle(
        title="PEER NOT FOUND",
        input_message_content=InputTextMessageContent("PEER NOT FOUND"),
    )
    try:
        user = await app.get_users(peer)
        caption, _ = await get_user_info(user, True)
    except IndexError:
        try:
            chat = await app.get_chat(peer)
            caption, _ = await get_chat_info(chat, True)
        except Exception:
            return [not_found]
    except Exception:
        return [not_found]

    answers.append(
        InlineQueryResultArticle(
            title="Found Peer.",
            input_message_content=InputTextMessageContent(
                caption, disable_web_page_preview=True
            ),
        )
    )
    return answers


async def task_inline_func(user_id):
    if user_id not in SUDOERS:
        return

    tasks = all_tasks()
    text = await _get_tasks_text()
    keyb = None

    if tasks:
        keyb = ikb(
            {i: f"cancel_task_{i}" for i in list(tasks.keys())},
            row_width=4,
        )

    return [
        InlineQueryResultArticle(
            title="Tasks",
            reply_markup=keyb,
            input_message_content=InputTextMessageContent(
                text,
            ),
        )
    ]


@app.on_callback_query(filters.regex("^cancel_task_"))
async def cancel_task_button(_, query: CallbackQuery):
    user_id = query.from_user.id

    if user_id not in SUDOERS:
        return await query.answer("This is not for you.")

    task_id = int(query.data.split("_")[-1])
    await rm_task(task_id)

    tasks = all_tasks()
    text = await _get_tasks_text()
    keyb = None

    if tasks:
        keyb = ikb({i: f"cancel_task_{i}" for i in list(tasks.keys())})

    await app.edit_inline_text(
        query.inline_message_id,
        text,
    )

    if keyb:
        await app.edit_inline_reply_markup(
            query.inline_message_id,
            keyb,
        )
