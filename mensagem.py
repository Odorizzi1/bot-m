from datetime import datetime, timedelta
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import pytz

mensagens = [
    """
    ✅ GREENBET CONFIRMA ✅
    🔁 Tentativas: 3
    🛡 Aposte com: 3 💣

    💣 💣 💣 💎 💣
    💎 💣 💣 💎 💣
    💣 💣 💣 💣 💣
    💣 💣 💣 💣 💣
    💣 💣 💣 💣 💎


    ➡️ [CADASTRE\-SE]({url_mines})
    """,
    """
    ✅ GREENBET CONFIRMA ✅
    🔁 Tentativas: 3
    🛡 Aposte com: 4 💣

    💣 💣 💣 💎 💎
    💣 💣 💣 💣 💎
    💣 💣 💣 💣 💣
    💣 💣 💣 💣 💎
    💣 💣 💣 💣 💣

    ➡️ [CADASTRE\-SE]({url_mines})
    """,
    """
    ✅ GREENBET CONFIRMA ✅
    🔁 Tentativas: 3
    🛡 Aposte com: 3 💣

    💣 💣 💎 💣 💣
    💣 💣 💎 💣 💣
    💣 💣 💣 💣 💣
    💣 💣 💎 💣 💣
    💣 💣 💣 💣 💎

    ➡️ [CADASTRE\-SE]({url_mines})
    """,
    """
    ✅ GREENBET CONFIRMA ✅
    🔁 Tentativas: 3
    🛡 Aposte com: 4 💣

    💣 💣 💎 💣 💣
    💣 💣 💣 💣 💣
    💎 💣 💎 💣 💣
    💣 💣 💣 💣 💣
    💣 💣 💎 💣 💣

    ➡️ [CADASTRE\-SE]({url_mines})
    """,
    """
    ✅ GREENBET CONFIRMA ✅
    🔁 Tentativas: 3
    🛡 Aposte com: 3 💣

    💣 💣 💣 💣 💣
    💣 💣 💣 💣 💣
    💣 💣 💣 💎 💎
    💣 💣 💎 💣 💣
    💣 💣 💣 💣 💎


    ➡️ [CADASTRE\-SE]({url_mines})
    """,
    """
    ✅ GREENBET CONFIRMA ✅
    🔁 Tentativas: 3
    🛡 Aposte com: 4 💣

    💣 💣 💣 💣 💣
    💣 💣 💣 💣 💣
    💣 💎 💎 💣 💣
    💣 💣 💣 💣 💣
    💣 💎 💎 💣 💣

    ➡️ [CADASTRE\-SE]({url_mines})
    """,
    """
    ✅ GREENBET CONFIRMA ✅
    🔁 Tentativas: 3
    🛡 Aposte com: 3 💣

    💣 💣 💣 💣 💎
    💣 💣 💣 💣 💎
    💣 💣 💣 💣 💣
    💣 💣 💎 💣 💣
    💣 💣 💣 💣 💎


    ➡️ [CADASTRE\-SE]({url_mines})
    """,
    """
    ✅ GREENBET CONFIRMA ✅
    🔁 Tentativas: 3
    🛡 Aposte com: 4 💣

    💎 💣 💣 💣 💣
    💣 💣 💣 💣 💣
    💣 💣 💣 💎 💣
    💣 💣 💣 💣 💎
    💣 💣 💎 💣 💣

    ➡️ [CADASTRE\-SE]({url_mines})
    """,
]