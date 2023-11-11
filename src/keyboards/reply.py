from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def replyKeyboard(text: list[str], one_time_keyboard: bool) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text=text[i]) for i in range(len(text))
            ]
        ], True, one_time_keyboard 
    )