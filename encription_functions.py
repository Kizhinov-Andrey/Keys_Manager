import hashlib
import os
import random
from Crypto.Cipher import DES


def create_password_hash(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt, key


def check_password_hash(password, salt, key):
    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key == new_key


def generate_password():
    password = ""
    chars = "1234567890abcdefghijklmnoprstuvxyzABCDEFGHIJKLMNOPRSTUVXYZ%$#@!?&"
    for i in range(16):
        ch = random.choice(chars)
        while i != 0 and password[i - 1] == ch:
            ch = random.choice(chars)
        password += ch
    return password


def encrypt_password(password):
    key = os.urandom(8)
    while len(password) % 8 != 0:
        password += ' '
    password = password.encode()
    des = DES.new(key, DES.MODE_ECB)
    password = des.encrypt(password)
    return key, password


def decrypt_password(key, password):
    des = DES.new(key, DES.MODE_ECB)
    return des.decrypt(password).decode('utf-8')
