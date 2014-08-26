import string
import base64
from Crypto.Cipher import AES
import time

class CryptoTool(object):

    def __init__(self):
        self.padding = '{'
        self.block_size = 32
        self.pad = lambda s : s + (self.block_size - len(s) % self.block_size) * self.padding
        self.encodedAES = lambda c,s : base64.b64encode(c.encrypt(self.pad(s)))
        self.decodedAES = lambda c,e : c.decrypt(base64.b64decode(e)).rstrip(self.padding)
        self.secretKey = '1234567812345678'
        self.cipher = AES.new(self.secretKey)

    def encryptString(self,stringObject):
        return self.encodedAES(self.cipher,stringObject)

    def decryptedString(self,encodedString):
        return self.decodedAES(self.cipher,encodedString)
                                                         
if __name__ == '__main__':
   tool = CryptoTool()
   timestamp = int(time.time())
   encodedAESString = tool.encryptString('abcdefg'+ str(timestamp))
   print encodedAESString +'\n'
   decodedAESString = tool.decryptedString(encodedAESString)
   print decodedAESString + '\n'
   
