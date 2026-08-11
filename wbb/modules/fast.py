"""
MIT License

Copyright (c) 2026 gearlbrace

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

from pyrogram import StopPropagation, filters
from pyrogram.enums import ChatMemberStatus as CMS
from pyrogram.types import ChatMemberUpdated

from wbb import LOG_GROUP_ID, SUDOERS, app, log
from wbb.core.decorators.errors import capture_err
from wbb.core.decorators.permissions import adminsOnly
from wbb.utils.dbfunctions import fast_off, fast_on, is_fast_on
from wbb.utils.filter_groups import fast_group
from wbb.utils.http import get

__MODULE__ = "FAST"
__HELP__ = """
/fast [ENABLE|DISABLE] - Enable/Disable automatic banning of joining
members found on the FAST (Furry Assisted Scam Tracking) list,
maintained by https://countersign.chat. Disabled by default.

/fastpurge - Check every current member of this chat against the
FAST list and ban any matches. [ADMIN ONLY]

Note: the list is a bare set of user IDs with no attached reason or
evidence. Every ban is also posted to the log group so it can be
reviewed and reversed if it turns out to be a false positive.
"""

FAST_LIST_URL = "https://countersign.chat/api/scammer_ids.json"
REFRESH_INTERVAL = 1800  # 30 minutes

fast_ids = set()


async def refresh_fast_list():
    global fast_ids
    try:
        data = await get(FAST_LIST_URL)
        fast_ids = {int(i) for i in data}
        log.info(f"FAST list refreshed: {len(fast_ids)} entries")
    except Exception as e:
        log.warning(f"Failed to refresh FAST list: {e}")


async def _refresh_loop():
    while True:
        await refresh_fast_list()
        await asyncio.sleep(REFRESH_INTERVAL)


asyncio.get_running_loop().create_task(_refresh_loop())


async def ban_and_log(chat, user_id: int, mention: str, reason: str):
    await chat.ban_member(user_id)
    notice = f"🚫 **{mention}** [`{user_id}`] banned - {reason}, matched the FAST scammer list."
    await app.send_message(chat.id, notice)
    if LOG_GROUP_ID:
        await app.send_message(
            LOG_GROUP_ID,
            f"{notice}\n**Chat:** {chat.title} [`{chat.id}`]",
        )


@app.on_chat_member_updated(filters.group, group=fast_group)
async def fast_check(_, cmu: ChatMemberUpdated):
    if not (
        cmu.new_chat_member
        and cmu.new_chat_member.status not in {CMS.RESTRICTED, CMS.BANNED}
        and not cmu.old_chat_member
    ):
        return

    member = cmu.new_chat_member.user if cmu.new_chat_member else cmu.from_user
    if not member or member.is_bot or member.id in SUDOERS:
        return
    if member.id not in fast_ids:
        return
    if not await is_fast_on(cmu.chat.id):
        return

    try:
        await ban_and_log(cmu.chat, member.id, member.mention, "joined")
    except Exception as e:
        log.warning(f"Failed to ban FAST-listed user {member.id}: {e}")
        return

    raise StopPropagation


@app.on_message(filters.command("fast") & ~filters.private)
@adminsOnly("can_restrict_members")
@capture_err
async def fast_toggle(_, message):
    usage = "**Usage:**\n/fast [ENABLE|DISABLE]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    chat_id = message.chat.id
    if state == "enable":
        await fast_on(chat_id)
        await message.reply_text(
            "Enabled FAST scammer auto-ban for this chat."
        )
    elif state == "disable":
        await fast_off(chat_id)
        await message.reply_text(
            "Disabled FAST scammer auto-ban for this chat."
        )
    else:
        await message.reply_text(usage)


@app.on_message(filters.command("fastpurge") & ~filters.private)
@adminsOnly("can_restrict_members")
@capture_err
async def fast_purge(_, message):
    if not fast_ids:
        return await message.reply_text(
            "The FAST list hasn't loaded yet, try again shortly."
        )
    m = await message.reply_text("Scanning members against the FAST list...")
    chat = message.chat
    banned = []
    async for member in app.get_chat_members(chat.id):
        user = member.user
        if user.id not in fast_ids or user.is_bot or user.id in SUDOERS:
            continue
        try:
            await ban_and_log(chat, user.id, user.mention, "found in chat")
            banned.append(user.id)
        except Exception as e:
            log.warning(f"Failed to ban FAST-listed user {user.id}: {e}")
    if not banned:
        return await m.edit("No FAST-listed scammers found in this chat.")
    ids = ", ".join(f"`{i}`" for i in banned)
    await m.edit(f"Banned {len(banned)} known scammer(s): {ids}")
