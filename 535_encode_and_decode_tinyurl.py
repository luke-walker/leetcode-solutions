import uuid

class Codec:

    def __init__(self):
        self.table = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short = str(uuid.uuid4()).split("-")[0]
        self.table[short] = longUrl
        return short
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.table[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))