from bluffinmuffin.protocol.interfaces import AbstractGameCommand


class TableClosedCommand(AbstractGameCommand):

    def __init__(self, obj):
        super().__init__(obj)
