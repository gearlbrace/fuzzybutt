# WilliamButcherBot — Command Reference

Every command exposed by the bot and its companion userbot session, grouped by what it's for. Bot commands use `/`; userbot-only commands run through the operator's own account, typically with a `.` prefix. Both prefixes are accepted by their respective sessions.

**112 commands · 7 categories · 4 access tiers**

## Access tiers

| Badge | Meaning |
|---|---|
| **Open** | Anyone can run it |
| **Admin** | Requires the matching chat-admin permission (anonymous admins always pass) |
| **Sudo** | Bot developers/sudoers only |
| **Userbot** | Runs through the operator's personal account (the linked userbot session), gated to developers/sudoers |

Reply-required commands must be sent as a reply to another message. A few commands (`kang`, `reverse`, `paste`, `webss`) have a matching userbot-side equivalent under the same name — noted inline rather than listed twice.

---

## Getting Started

Orientation commands anyone can run, in PM or in a group.

| Command | Description | Access | Usage |
|---|---|---|---|
| `/start` | Opens the bot's PM menu (groups get a "PM me" button instead); also resolves deep links for rules and per-module help. | Open | `/start` |
| System Stats (button) | Shows live CPU/RAM/disk/uptime as an alert popup. Not a slash command — it's the "System Stats" button on `/start` and on the group "PM me" prompt. | Open | tap the button — no direct command |
| `/help [module]` | Shows the help menu, or a button linking to help for one module. | Open | `/help [module]` |
| `/info [user]` | Shows details about a user — ID, DC, Premium status, global-ban and karma status. | Open | `/info [user]` — or reply |
| `/chat_info [chat]` | Shows details about a chat. | Open | `/chat_info <username|id>` |
| `/rules` | Sends a button linking to the chat's rules. | Open | `/rules` — group only |
| `/karma` | Shows the chat's karma leaderboard, or a replied user's karma. | Open | `/karma` — group only |
| `/inline` | Shows buttons demonstrating the bot's inline-mode features. | Open | `/inline` |
| `@BotUsername …` | Inline mode: alive check, search, speedtest, pmpermit, ping, info, tasks. | Open | `@BotUsername <query>` |

## Moderation & Admin Actions

Group policing — bans, mutes, warnings, permission locks. Requires the matching admin right unless marked Sudo.

| Command | Description | Access | Usage |
|---|---|---|---|
| `/purge [n]` | Deletes messages from a replied message up to now, or the last n. | Admin | `/purge [n]` — reply required |
| `/kick`, `/dkick` | Kicks a member (dkick also deletes their triggering message). | Admin | `/kick <user> [reason]` |
| `/ban`, `/dban`, `/tban` | Bans, delete+bans, or timed-bans a member. | Admin | `/tban <user> <time> [reason]` |
| `/unban` | Lifts a ban on a member. | Admin | `/unban <user>` |
| `/del` | Deletes the replied message. | Admin | `/del` — reply required |
| `/promote`, `/fullpromote` | Grants admin rights (fullpromote = every right the bot itself has). | Admin | `/promote <user>` |
| `/demote` | Strips a member's admin rights. | Admin | `/demote <user>` |
| `/pin`, `/unpin` | Pins or unpins the replied message. | Admin | `/pin` — reply required |
| `/mute`, `/tmute` | Mutes or timed-mutes a member. | Admin | `/tmute <user> <time> [reason]` |
| `/unmute` | Lifts a mute. | Admin | `/unmute <user>` |
| `/ban_ghosts` | Bans every deleted account currently in the chat. | Admin | `/ban_ghosts` |
| `/warn`, `/dwarn` | Issues a warning; auto-bans at 3 warnings. | Admin | `/warn <user> [reason]` |
| `/rmwarns` | Clears all warnings for the replied user. | Admin | `/rmwarns` — reply required |
| `/warns` | Shows a user's current warning count. | Open | `/warns [user]` |
| `/report`, `@admin(s)` | Pings all chat admins about the replied message or user. | Open | `/report` — reply required |
| `/invite` | Sends the chat's invite link. | Admin | `/invite` |
| `/lock`, `/unlock` | Locks or unlocks a permission type (or "all" for lock). | Admin | `/lock <type>` |
| `/locks` | Shows which permissions are currently unlocked. | Open | `/locks` |
| `/blacklist` | Adds a word or sentence that gets auto-deleted (sender muted 60 min). | Admin | `/blacklist <word|sentence>` |
| `/blacklisted` | Lists blacklisted words for the chat. | Open | `/blacklisted` |
| `/whitelist` | Removes a blacklisted word. | Admin | `/whitelist <word|sentence>` |
| `/antiservice` | Toggles auto-deletion of service messages (joins, pins, etc.). | Admin | `/antiservice [enable|disable]` |
| `/fast` | Toggles auto-ban of joining members found on the FAST scammer list. | Admin | `/fast [enable|disable]` |
| `/fastpurge` | Scans current members against the FAST list and bans matches. | Admin | `/fastpurge` |
| `/set_chat_title` | Renames the group. | Admin | `/set_chat_title <name>` |
| `/set_user_title` | Sets a custom title for the replied admin. | Admin | `/set_user_title <title>` — reply required |
| `/set_chat_photo` | Sets the chat photo from a replied photo/document. | Admin | `/set_chat_photo` — reply required, ≤5MB |
| `/listban` | Bans a user across every group referenced in a linked message. | Sudo | `/listban <user> <msg_link> <reason>` |
| `/listunban` | Reverses `/listban`. | Sudo | `/listunban <user> <msg_link>` |

## Group Setup & Automation

Configuring how a group behaves — welcomes, captchas, filters, notes, flood control, AFK.

| Command | Description | Access | Usage |
|---|---|---|---|
| `/captcha` | Enables, disables or switches the mode (text/emoji) of new-member captcha. | Admin | `/captcha [enable|disable|mode]` |
| `/set_welcome` | Sets the welcome message shown to new members. | Admin | `/set_welcome` — reply to text/photo/gif |
| `/get_welcome` | Previews the current welcome message, including its raw source. | Admin | `/get_welcome` |
| `/del_welcome` | Deletes the welcome message. | Admin | `/del_welcome` |
| `/autoapprove` | Configures join-request auto-approval: off, automatic, or manual-with-buttons. | Admin | `/autoapprove` — group only |
| `/clear_pending` | Clears the chat's pending join-request list. | Admin | `/clear_pending` |
| `/flood` | Toggles anti-flood auto-mute (10 consecutive messages → 1hr mute). | Admin | `/flood [enable|disable]` |
| `/filter` | Saves an auto-reply triggered by a keyword. | Admin | `/filter <name> <content>` — or reply |
| `/filters` | Lists all keyword filters in the chat. | Open | `/filters` |
| `/stop` | Deletes a keyword filter. | Admin | `/stop <name>` |
| `/stopall` | Deletes every filter in the chat, with confirmation. | Admin | `/stopall` |
| `/save` | Saves a chat note, retrievable later with `#name`. | Admin | `/save <name> <content>` — or reply |
| `/notes` | Lists all saved note names. | Open | `/notes` |
| `/delete` | Deletes a note. | Admin | `/delete <name>` |
| `/deleteall` | Deletes every note in the chat, with confirmation. | Admin | `/deleteall` |
| `/karma_toggle` | Turns the karma system on or off for the chat. | Admin | `/karma_toggle [enable|disable]` |
| `/afk` | Marks you as AFK, with an optional reason or media. | Open | `/afk [reason]` — or reply to media |
| `/afkdel` | Toggles auto-deletion of AFK status messages after 1 minute. | Admin | `/afkdel [enable|disable]` |
| `/setrules` | Sets the chat's rules text. | Admin | `/setrules <text>` — or reply |
| `/clearrules` | Clears the chat's rules, with confirmation. | Admin | `/clearrules` |

## Federation Network

Cross-group ban lists ("federations") that link multiple chats under shared moderation.

| Command | Description | Access | Usage |
|---|---|---|---|
| `/newfed` | Creates a federation you own. | Open | `/newfed <name>` — PM only |
| `/delfed` | Deletes a federation you own, with confirmation. | Admin | `/delfed <fed_id>` — PM only, fed owner |
| `/fedtransfer` | Transfers federation ownership to another user, with confirmation. | Admin | `/fedtransfer <user> <fed_id>` — PM only |
| `/myfeds` | Lists federations you own. | Open | `/myfeds` |
| `/renamefed` | Renames a federation. | Admin | `/renamefed <fed_id> <name>` — fed owner |
| `/setfedlog`, `/unsetfedlog` | Sets or unsets the federation's log channel. | Admin | `/setfedlog [channel_id] <fed_id>` — fed owner |
| `/chatfed` | Shows which federation the current chat belongs to. | Admin | `/chatfed` |
| `/joinfed` | Joins the current chat to a federation. | Admin | `/joinfed <fed_id>` — chat owner |
| `/leavefed` | Removes the current chat from its federation. | Admin | `/leavefed` — chat owner |
| `/fedchats` | Lists chats in a federation. | Admin | `/fedchats <fed_id>` — PM only, fed owner/admin |
| `/fedinfo` | Shows a federation's name, owner, and admin/ban/chat counts. | Open | `/fedinfo [fed_id]` |
| `/fedadmins` | Lists a federation's admins. | Open | `/fedadmins [fed_id]` |
| `/fpromote`, `/fdemote` | Promotes or demotes a federation admin. | Admin | `/fpromote <user>` — fed owner |
| `/fban`, `/sfban` | Bans a user across every chat in the federation (sfban = silent). | Admin | `/fban <user> <reason>` — fed admin |
| `/unfban`, `/sunfban` | Reverses a federation ban. | Admin | `/unfban <user> <reason>` — fed admin |
| `/fedstat` | Checks a ban status for yourself or a user across federations. | Open | `/fedstat [user] [fed_id]` — PM only |
| `/fbroadcast` | Broadcasts the replied message to every chat in the federation. | Admin | `/fbroadcast` — reply required, fed admin |

## Media, Files & Converters

Turning messages into images, audio, screenshots, and paste links.

| Command | Description | Access | Usage |
|---|---|---|---|
| `/carbon` | Renders replied text as a "carbon" code-style image. | Open | `/carbon` — reply to text |
| `/pdf` | Converts replied image(s), or a whole media group, into a PDF. | Open | `/pdf [name]` — reply to image(s) |
| `/ytmusic` | Downloads audio from a YouTube link or search query via yt-dlp. | Open | `/ytmusic <link or query>` — one at a time, ≤30 min |
| `/webss` | Takes a screenshot of a website. | Open | `/webss <url> [full=yes]` — also on the userbot as `.webss` |
| `/telegraph` | Posts replied text to Telegraph. | Open | `/telegraph [page name]` — reply to text |
| `/paste` | Pastes replied text or a document to a pastebin. | Open | `/paste` — reply required, also on the userbot |
| `/reverse` | Reverse-image-searches a replied image, sticker or document via Google. | Open | `/reverse` — reply required, also on the userbot |
| `/tts` | Converts replied text to speech (auto-detects language). | Open | `/tts` — reply to text |
| `/sticker_id` | Shows the file_id of a replied sticker. | Open | `/sticker_id` — reply required |
| `/get_sticker` | Sends a replied sticker back as a photo and a document. | Open | `/get_sticker` — reply required |
| `/kang` | Adds a replied sticker or image to your own sticker pack. | Open | `/kang [emoji]` — reply required, also on the userbot |

## Owner / Sudo Control

The bot's own control plane — running these requires being listed as a developer/sudoer.

| Command | Description | Access | Usage |
|---|---|---|---|
| `/gban`, `/ungban` | Globally bans or unbans a user across every served chat. | Sudo | `/gban <user> <reason>` |
| `/broadcast`, `/ubroadcast` | Broadcasts the replied message to every served chat, or every served user's PM. | Sudo | `/broadcast` — reply required |
| `/update` | Pulls the latest code from git and restarts the bot. | Sudo | `/update` |
| `/restart` | Restarts the bot. | Sudo | `/restart` |
| `/blacklist_chat`, `/whitelist_chat` | Blacklists or restores a chat ID at the bot level. | Sudo | `/blacklist_chat [chat_id]` |
| `/blacklisted_chats` | Lists chats blacklisted at the bot level. | Sudo | `/blacklisted_chats` |
| `/gstats` | Shows global bot and userbot statistics. | Sudo | `/gstats` |
| `/clean_db` | Removes chats the bot is no longer a member of from the database. | Sudo | `/clean_db` |
| `/backup` | Dumps and zips the MongoDB database, sent as a document. | Sudo | `/backup` — PM only |
| `/activate_pipe`, `/deactivate_pipe` | Creates or removes a message-forwarding pipe between two chats. | Sudo | `/activate_pipe <from> <to> <bot|userbot>` |
| `/pipes` | Lists currently active forwarding pipes. | Sudo | `/pipes` |

## Userbot-Only Tools

Run through the operator's own Telegram account (the linked "userbot" session), gated to developers/sudoers only.

| Command | Description | Access | Usage |
|---|---|---|---|
| `.alive` | Sends the bot's "alive" inline card and deletes the trigger. | Userbot | `.alive` |
| `.anonymize` | Randomizes the userbot's own profile photo and first name. | Userbot | `.anonymize` |
| `.impersonate` | Clones a target user's name, bio and photo onto the userbot. | Userbot | `.impersonate <user>` — reply or username/id |
| `.create` | Creates a basicgroup, supergroup or channel from the userbot account. | Userbot | `.create (b|s|c) Name` |
| `.save`, `.notes`, `.get`, `.delete` | Manages personal notes stored under the userbot account (separate from group notes). | Userbot | `.save <name> <content>` |
| `.approve`, `.disapprove` | Approves or revokes a user's permission to PM the userbot. | Userbot | `.approve` — reply required |
| `.block`, `.unblock` | Blocks or unblocks a user on the userbot account. | Userbot | `.block` — reply required |
| `.help` | Sends a link to the full userbot command list. | Userbot | `.help` |
| `.purgeme` | Deletes the userbot's own last N messages in a chat. | Userbot | `.purgeme <n>` |
| `.parse_preview` | Inspects the link-preview metadata of a replied message. | Userbot | `.parse_preview` — reply required |
| `.useradd`, `.userdel` | Adds or removes a user from the sudoers list. | Userbot | `.useradd` — reply required |
| `.sudoers` | Lists current sudo users. | Userbot | `.sudoers` |
| `.eval` | Executes arbitrary Python code in the userbot's context. | Userbot | `.eval <code>` |
| `.sh` | Executes an arbitrary shell command on the host. | Userbot | `.sh <command>` |
| `.reserve` | Creates and reserves a channel with a given username. | Userbot | `.reserve <username>` |
