from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def inlineKeyboard(text: list[str], callback: list[str]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text[i], callback_data=callback[i] 
                ) for i in range(len(text))
            ]
        ]        
    )