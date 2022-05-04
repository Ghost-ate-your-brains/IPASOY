import hashlib


def _encode(text: str):
    return text.encode("utf-8")


class Encryptor:
    def __init__(self, spell):
        self.spell: str = ""

    def encrypt(self, salt=None):
        __ready_spell = hashlib.sha512(_encode(self.spell)).hexdigest()
        return __ready_spell
