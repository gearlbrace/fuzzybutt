import os
import random
import uuid

from PIL import Image, ImageDraw, ImageFont

EMOJI_FONT_PATH = "AppleColorEmoji.ttf"
CACHE_DIR = "assets/cache"

SUPPORTED_EMOJIS = [
    "🃏", "🎤", "🎥", "🎨", "🎩", "🎬", "🎭", "🎮", "🎯", "🎱", "🎲", "🎷", "🎸",
    "🎹", "🎾", "🏀", "🏆", "🏈", "🏉", "🏐", "🏓", "💠", "💡", "💣", "💨", "💸",
    "💻", "💾", "💿", "📈", "📉", "📊", "📌", "📍", "📎", "📏", "📐", "📞", "📟",
    "📠", "📡", "📢", "📣", "📦", "📹", "📺", "📻", "📼", "📽", "🖥", "🖨", "🖲",
    "🗂", "🗃", "🗄", "🗜", "🗝", "🗡", "🚧", "🚨", "🛒", "🛠", "🛢", "🧀", "🌭",
    "🌮", "🌯", "🌺", "🌻", "🌼", "🌽", "🌾", "🌿", "🍊", "🍋", "🍌", "🍍", "🍎",
    "🍏", "🍚", "🍛", "🍜", "🍝", "🍞", "🍟", "🍪", "🍫", "🍬", "🍭", "🍮", "🍯",
    "🍺", "🍻", "🍼", "🍽", "🍾", "🍿", "🎊", "🎋", "🎍", "🎏", "🎚", "🎛", "🎞",
    "🐌", "🐍", "🐎", "🐚", "🐛", "🐝", "🐞", "🐟", "🐬", "🐭", "🐮", "🐯", "🐻",
    "🐼", "🐿", "👛", "👜", "👝", "👞", "👟", "💊", "💋", "💍", "💎", "🔋", "🔌",
    "🔪", "🔫", "🔬", "🔭", "🔮", "🕯", "🖊", "🖋", "🖌", "🖍", "🥚", "🥛", "🥜",
    "🥝", "🥞", "🦊", "🦋", "🦌", "🦍", "🦎", "🦏", "🌀", "🌂", "🌑", "🌕", "🌡",
    "🌤", "⛅️", "🌦", "🌧", "🌨", "🌩", "🌰", "🌱", "🌲", "🌳", "🌴", "🌵", "🌶",
    "🌷", "🌸", "🌹", "🍀", "🍁", "🍂", "🍃", "🍄", "🍅", "🍆", "🍇", "🍈", "🍉",
    "🍐", "🍑", "🍒", "🍓", "🍔", "🍕", "🍖", "🍗", "🍘", "🍙", "🍠", "🍡", "🍢",
    "🍣", "🍤", "🍥", "🍦", "🍧", "🍨", "🍩", "🍰", "🍱", "🍲", "🍴", "🍵", "🍶",
    "🍷", "🍸", "🍹", "🎀", "🎁", "🎂", "🎃", "🎄", "🎈", "🎉", "🎒", "🎓", "🎙",
    "🐀", "🐁", "🐂", "🐃", "🐄", "🐅", "🐆", "🐇", "🐕", "🐉", "🐓", "🐖", "🐗",
    "🐘", "🐙", "🐠", "🐡", "🐢", "🐣", "🐤", "🐥", "🐦", "🐧", "🐨", "🐩", "🐰",
    "🐱", "🐴", "🐵", "🐶", "🐷", "🐸", "🐹", "👑", "👒", "👠", "👡", "👢", "💄",
    "💈", "🔗", "🔥", "🔦", "🔧", "🔨", "🔩", "🔰", "🔱", "🕰", "🕶", "🕹", "🖇",
    "🚀", "🤖", "🥀", "🥁", "🥂", "🥃", "🥐", "🥑", "🥒", "🥓", "🥔", "🥕", "🥖",
    "🥗", "🥘", "🥙", "🦀", "🦁", "🦂", "🦃", "🦄", "🦅", "🦆", "🦇", "🦈", "🦉",
    "🦐", "🦑", "⭐️", "⏰", "⏲", "⚠️", "⚡️", "⚰️", "⚽️", "⚾️", "⛄️", "⛅️", "⛈",
    "⛏", "⛓", "⌚️", "☎️", "⚜️", "✏️", "⌨️", "☁️", "☃️", "☄️", "☕️", "☘️", "☠️",
    "♨️", "⚒", "⚔️", "⚙️", "✈️", "✉️", "✒️",
]


def generate_rnd_id() -> str:
    return uuid.uuid4().hex


def make_captcha_markup(markup, emoji: str, indicator: str):
    for row in markup:
        for button in row:
            if button.text == emoji:
                button.text = indicator
                button.callback_data = "HeHe"
                return markup
    return markup


def make_captcha(captcha_id: str):
    background = Image.open("assets/background.png")
    font = ImageFont.truetype(EMOJI_FONT_PATH, 137)

    emojis = random.sample(SUPPORTED_EMOJIS, 6)

    draw = ImageDraw.Draw(background)
    position = [(20, 20), (180, 20), (310, 20), (20, 160), (180, 160), (310, 160)]
    for i, emoji in enumerate(emojis):
        text_layer = Image.new("RGBA", (274, 274), (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_layer)
        draw.text(
            xy=(0, 0),
            text=emoji,
            fill=(255, 255, 255),
            embedded_color=True,
            font=font,
        )
        img = text_layer.rotate(
            random.randint(0, 360), resample=Image.BICUBIC, expand=True
        )
        img.thumbnail((200, 200), Image.Resampling.LANCZOS)
        background.paste(img, position[i], img)

    os.makedirs(CACHE_DIR, exist_ok=True)
    image_path = f"{CACHE_DIR}/{captcha_id}.png"
    background.save(image_path, "PNG", quality=100)

    answer = "Answer: " + " ".join(emojis)
    return answer, image_path
