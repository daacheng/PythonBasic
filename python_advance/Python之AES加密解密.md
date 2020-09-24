# Python之AES加密解密
## 一、AES/CBC/PKCS5Padding加密解密
```python
from Cryptodome.Cipher import AES, DES
import base64
class AESCrypter():
    """
        AES.MODE_CBC
        PKCS5Padding
        PKCS5Padding：填充的原则是，如果长度少于16个字节，需要补满16个字节，补(16-len)个(16-len)例如：
        huguozhen这个节符串是9个字节，16-9= 7,补满后如：huguozhen+7个\x07，如果刚好是倍数，那么补16个\x10
        由于加密过程有补齐操作，因此不适用于按块加密文件，加密前后文件大小改变了，无法按块还原
        文件加密，逐包加解密，还是可行的
    """

    def __init__(self, key, iv=None):
        """
        :param key: 16*n个字节，bytes
        """
        self.key = key
        if iv:
            self.iv = iv
        else:
            self.iv = key
        self.mode = AES.MODE_CBC
        self.BS = len(key)
        # 如果刚好是s是BS的倍数，那么补一组
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS).encode()
        self.unpad = lambda s: s[0:-s[-1]]
        self.generator_en = AES.new(self.key, self.mode, self.iv)
        self.generator_de = AES.new(self.key, self.mode, self.iv)

    def encrypt(self, en_data):
        """
        :param en_data: bytes
        :return: bytes
        """
        return self.generator_en.encrypt(self.pad(en_data))

    def decrypt(self, de_data):
        """
        :param de_data: bytes
        :return: bytes
        """
        return self.unpad(self.generator_de.decrypt(de_data))


if __name__ == '__main__':
    key = b'0' * 16
    iv = b'12345678' * 2

    data = '你好，这个数据好很重要，要加密！！！'
    aes = AESCrypter(key, iv)
    en_data = base64.b64encode(aes.encrypt(data.encode('utf-8')))
    print(en_data)  # b'lqDad0GkXYwNxf+jxoXg4661qhSk9cTKqDPPOtAjXGd1aru61grhjpQw9qIxitcarfePNiDnL06yJqglcwPuDg=='
    de_data = aes.decrypt(base64.b64decode(en_data)).decode('utf-8')
    print(de_data)
```

## 二、DES/CBC/PKCS5Padding加密解密

```python
from Cryptodome.Cipher import DES
import base64


class DESCrypter():

    def __init__(self, key, iv=None):
        self.key = key
        if iv:
            self.iv = iv
        else:
            self.iv = key
        self.mode = DES.MODE_CBC
        self.BS = len(key)
        # 如果刚好是s是BS的倍数，那么补一组
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS).encode()
        self.unpad = lambda s: s[0:-s[-1]]
        self.generator_en = DES.new(self.key, self.mode, self.iv)
        self.generator_de = DES.new(self.key, self.mode, self.iv)

    def encrypt(self, en_data):
        return self.generator_en.encrypt(self.pad(en_data))

    def decrypt(self, de_data):
        return self.unpad(self.generator_de.decrypt(de_data))


if __name__ == '__main__':
    key = b'00000000'
    iv = b'12345678'
    des = DESCrypter(key, iv)
    data = '这个数据要加密！！！！'

    en_data = base64.b64encode(des.encrypt(data.encode('utf-8')))
    print(en_data)  # b'p1AmnxW64yb8E7RdU3gq7nk/gDQ407yLFs5Ziilq2r/gBXBPUcOeyw=='

    de_data = des.decrypt(base64.b64decode(en_data)).decode('utf-8')
    print(de_data)

```
