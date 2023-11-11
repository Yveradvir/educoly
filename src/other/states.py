from aiogram.dispatcher.filters.state import State, StatesGroup


class StatesForNewClasses(StatesGroup):
    waitForNameOfClass = State()
    waitForStatus      = State()
    waitForConfirm     = State()
    