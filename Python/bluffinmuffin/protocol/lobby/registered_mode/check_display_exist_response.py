from protocol import AbstractResponse
from check_display_exist_command import CheckDisplayExistCommand


class CheckDisplayExistResponse(AbstractResponse):
    def __init__(self, obj):
        super().__init__(obj, CheckDisplayExistCommand(obj['Command']))
        self.exist = obj['Exist']

    def __str__(self):
        return '{0} => {1}'.format(
            super().__str__(),
            self.exist
        )

    def _encode_specific(self, d):
        super()._encode_specific(d)
        d['Exist'] = self.exist
