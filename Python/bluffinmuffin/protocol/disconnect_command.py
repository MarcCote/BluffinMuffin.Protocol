from protocol import AbstractCommand
from bluffin_command_enum import BluffinCommandEnum


class DisconnectCommand(AbstractCommand):
    def __init__(self, obj):
        super().__init__(obj, BluffinCommandEnum.General)
