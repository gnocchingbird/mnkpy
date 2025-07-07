class Player(object):
    def __init__(self, alias: str, ip: str = "127.0.0.1"):
        self.alias = alias
        self.ip = ip

    def __repr__(self):
        return f"Player [{self.alias}]"