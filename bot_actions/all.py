from bot_actions.my_id import MyId
from bot_actions.my_name import MyName
from bot_actions.speak import Speak

class BotActions(MyId, MyName, Speak):
    """Inherits all functionalities the bot has implemented"""
    pass
