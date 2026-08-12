"""
Stand-in for the real pyrogram's `pyrogram.emoji` module.

kurigram (the pyrogram fork this project runs on -- see pyproject.toml's
override-dependencies, which blocks the real "pyrogram" package from being
installed at all to avoid it colliding with kurigram's identically-named
import path) does not ship `pyrogram.emoji`. pykeyboard's `InlineKeyboard`
does `from pyrogram.emoji import *` and only actually uses these flag
constants, so that's all this provides. Registered as `pyrogram.emoji` in
`sys.modules` by wbb/__init__.py before anything imports pykeyboard.
"""

FLAG_BELARUS = "\U0001f1e7\U0001f1fe"
FLAG_CHINA = "\U0001f1e8\U0001f1f3"
FLAG_GERMANY = "\U0001f1e9\U0001f1ea"
FLAG_SPAIN = "\U0001f1ea\U0001f1f8"
FLAG_FRANCE = "\U0001f1eb\U0001f1f7"
FLAG_UNITED_KINGDOM = "\U0001f1ec\U0001f1e7"
FLAG_INDONESIA = "\U0001f1ee\U0001f1e9"
FLAG_ITALY = "\U0001f1ee\U0001f1f9"
FLAG_SOUTH_KOREA = "\U0001f1f0\U0001f1f7"
FLAG_RUSSIA = "\U0001f1f7\U0001f1fa"
FLAG_TURKEY = "\U0001f1f9\U0001f1f7"
FLAG_UKRAINE = "\U0001f1fa\U0001f1e6"
FLAG_UZBEKISTAN = "\U0001f1fa\U0001f1ff"
