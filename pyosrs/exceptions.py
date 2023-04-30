class InvalidUserException(Exception):
    def __init__(self, username):
        self.username = username
        super().__init__(f"Invalid username: {username}")


class InvalidAPIResponseException(Exception):
    def __init__(self):
        self.message = "A new skill/boss/activity has been added to Oldschool \
            Runescape, and Pyosrs needs to be updated"
        super().__init__(self.message)
