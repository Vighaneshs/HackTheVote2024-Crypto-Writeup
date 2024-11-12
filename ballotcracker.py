from pwn import *
from Crypto.Util.Padding import pad
import codecs

import json

attempts = 255

for i in range(attempts):

    target = remote("zerovote.chal.hackthe.vote", 1337)
    target.recvuntil("3) Exit")
    pt = b'1'

    target.sendline(pt)
    target.recvuntil("c) Carol")
    pt = b'c'

    target.sendline(pt)

    target.recvuntil("Here's your ballot: ")
    tmp = target.recvuntil("}}")
    data = json.loads(tmp.decode('utf-8'))

    while 1 > 0:
        try:
            print(target.recvuntil("3) Exit"))
        except:
            print(target.recvall())

        try:
            pt = b'2'
            target.sendline(pt)
            data['a']['count']['point'][i] = abs(data['a']['count']['point'][i] -1)%255
            data['b']['count']['point'][i] = abs(data['b']['count']['point'][i] -2)%255

            newd = json.dumps(data)

            target.sendline(newd.encode('utf-8'))
        except:
            break

