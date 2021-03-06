from protocol import AbstractLobbyCommand


class CreateUserCommand(AbstractLobbyCommand):
    def __init__(self, obj):
        super().__init__(obj)
        self.username = obj['Username']
        self.password = obj['Password']
        self.email = obj['Email']
        self.display_name = obj['DisplayName']

    def __str__(self):
        return '{0} ({1} : {2}, {3}, {4})'.format(
            super().__str__(),
            self.username,
            self.password,
            self.email,
            self.display_name
        )

    def _encode_specific(self, d):
        super()._encode_specific(d)
        d['Username'] = self.username
        d['Password'] = self.password
        d['Email'] = self.email
        d['DisplayName'] = self.display_name
