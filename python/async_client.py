# print('1'.center(100,'-'))
# import socket
# import asyncio
#
#
# async def main(ip, port, data):
#     while True:
#         c = socket.socket()
#         loop = asyncio.get_running_loop()
#         await loop.sock_connect(c, (ip, port))
#         await loop.sock_sendall(c, data.encode('utf-8'))
#         res = await loop.sock_recv(c, 1024)
#         await asyncio.sleep(1)
#         print(res.decode('utf-8'))
#
#
# if __name__ == '__main__':
#     asyncio.run(main('127.0.0.1', 5000, 'abc'))
from idlelib.colorizer import prog_group_name_to_tag

from typing_extensions import dataclass_transform

# print('2'.center(100,'-'))
# import socket
# import asyncio
# async def main(ip,port,data):
#     while True:
#         c = socket.socket()
#         loop = asyncio.get_running_loop()
#         await loop.sock_connect(c,(ip,port))
#         await loop.sock_sendall(c,data.encode('utf-8'))
#         res = await loop.sock_recv(c,1024)
#         await asyncio.sleep(1)
#         print(res.decode('utf-8'))
#     c.close()
# if __name__ == '__main__':
#     asyncio.run(main('127.0.0.1',5003,'abc'))

# print('3'.center(100,'-'))
# import socket
# import asyncio
# async def main(ip,port,data):
#     while True:
#         c = socket.socket()
#         loop = asyncio.get_running_loop()
#         await loop.sock_connect(c,(ip,port))
#         await loop.sock_sendall(c,data.encode('utf-8'))
#         res = await loop.sock_recv(c,1024)
#         print(res.decode('utf-8'))
#         await asyncio.sleep(0.2)
#     c.close()
#
# if __name__ == '__main__':
#     asyncio.run(main('127.0.0.1',5007,'abc'))

# print('4'.center(100,'-'))
# import socket
# import datetime
# import asyncio
# async def main(ip,port,data):
#     while True:
#         loop = asyncio.get_running_loop()
#         c = socket.socket()
#         await loop.sock_connect(c,(ip,port))
#         await loop.sock_sendall(c,data.encode('utf-8'))
#         res = await loop.sock_recv(c,1024)
#         print(res.decode('utf-8'))
#         print(datetime.datetime.now())
#     c.close()
#
#
# if __name__ == '__main__':
#     asyncio.run(main('127.0.0.1',6000,'abcdefg'))

print('5'.center(100,'-'))
import socket
import time,random
import asyncio


async def main(ip,port,data):
    while True:
        c = socket.socket()
        loop = asyncio.get_running_loop()
        await loop.sock_connect(c,(ip,port))
        await loop.sock_sendall(c,data.encode('utf-8'))
        res = await loop.sock_recv(c,1024)
        await asyncio.sleep(0.5)
        print(random.randint(1000,9999),res.decode('utf-8'))
    c.close()

if __name__ == '__main__':
    asyncio.run(main('127.0.0.1',5000,'abcdefg'))







































