class InvalidUrl(Exception):
    def __init__(self, url):
        super().__init__(f"Invalid Url: {url}")


class ObjectNotFound(Exception):
    def __init__(self, key):
        super().__init__(f"Object not found: {key}")


class AlreadyRegistered(Exception):
    def __init__(self, username):
        super().__init__(f"User with {username} already registered")
