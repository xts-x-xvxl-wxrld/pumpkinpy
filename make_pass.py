import secrets
import string

alpha = string.ascii_letters
digit = string.digits

collection = alpha + digit

psw_len = 9

password = ''

for i in range(psw_len):
    password += ''.join(secrets.choice(collection))

print(password)