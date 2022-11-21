class InvalidUrl(Exception):
    def __init__(self, url):
        super().__init__(f"Invalid Url: {url}")


class ObjectNotFound(Exception):
    def __init__(self, key):
        super().__init__(f"Object not found: {key}")
