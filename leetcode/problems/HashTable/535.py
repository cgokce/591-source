'''
Encode and Decode TinyURL
<t> HashMap


# We need a hashmap to longUrl -> small_index
# Also reverse hmap small_index -> longUrl

# hash func will handle longUrl <-> shortUrl

# easier solution is having a db

index -> long_url

can be queried using long_url or index


'''


import base64

class Codec:

    hmap = {}
    count = 0
    rev_hmap = {}
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.hmap:
            index = self.hmap[longUrl]
        else:
            index = self.count
            self.rev_hmap[str(index)] = longUrl
            self.hmap[longUrl] = index
            self.count += 1
        
        return base64.b16encode(str(index))
        
        
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        index = base64.b16decode(shortUrl)
        return self.rev_hmap[index]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))