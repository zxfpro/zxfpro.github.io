# 加密算法
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class CryptoAlgorithm:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        iv = os.urandom(16)  # 生成随机初始化向量(IV)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        return iv + ciphertext

    def decrypt(self, ciphertext):
        iv = ciphertext[:16]
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext[16:]) + decryptor.finalize()
        return plaintext
if __name__ == '__main__':

    # 使用示例
    key = b'0123456789abcdef'  # 16字节密钥
    plaintext = b'This is a secret message.'

    crypto = CryptoAlgorithm(key)
    ciphertext = crypto.encrypt(plaintext)
    print("Encrypted:", ciphertext)

    decrypted = crypto.decrypt(ciphertext)
    print("Decrypted:", decrypted)