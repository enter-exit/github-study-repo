# print('1'.center(100,'-'))
# import socket
# import asyncio
#
#
# async def waiter(conn, loop):
#     while True:
#         try:
#             data = await loop.sock_recv(conn, 1024)
#             if not data:
#                 break
#             await loop.sock_sendall(conn, data.upper())
#             print(data.decode('utf-8'))
#         except:
#             break
#     conn.close()
#
#
# async def main(ip, port):
#     s = socket.socket()
#     s.bind((ip, port))
#     s.listen(2)
#     s.setblocking(False)
#     loop = asyncio.get_running_loop()
#     while True:
#         conn, addr = await loop.sock_accept(s)
#         loop.create_task(waiter(conn, loop))
#
#
# if __name__ == '__main__':
#     asyncio.run(main('127.0.0.1', 5000))
from tkinter import BaseWidget

from certifi.core import where

# print('2'.center(100,'-'))
# import socket
# import asyncio
# async def waiter(loop,conn):
#     while True:
#         try:
#             data = await loop.sock_recv(conn,1024)
#             if not data:
#                 break
#             print(data.decode('utf-8'))
#             await loop.sock_sendall(conn,data.upper())
#         except:
#             break
#     conn.close()
# async def main(ip,port):
#     s = socket.socket()
#     s.bind((ip,port))
#     s.listen(2)
#     s.setblocking(False)
#     loop = asyncio.get_running_loop()
#     while True:
#         conn,addr = await loop.sock_accept(s)
#         asyncio.create_task(waiter(loop,conn))
#
# if __name__ == '__main__':
#     asyncio.run(main('127.0.0.1',5003))

# print('3'.center(100,'-'))
#
# import socket
# import asyncio
# async def waiter(loop,conn):
#     while True:
#         try:
#             data = await loop.sock_recv(conn,1024)
#             if not data:
#                 break
#             print(data.decode('utf-8'))
#             await loop.sock_sendall(conn,data.upper())
#         except:
#             break
#     conn.close()
#
# async def main(ip,port):
#     s = socket.socket()
#     s.bind((ip,port))
#     s.listen(3)
#     s.setblocking(False)
#     loop = asyncio.get_running_loop()
#     while True:
#         conn,addr = await loop.sock_accept(s)
#         await loop.create_task(waiter(loop,conn))
#
# if __name__ == '__main__':
#     asyncio.run(main('127.0.0.1',5007))

# print('4'.center(100,'-'))
# import socket
# import datetime
# import asyncio
# async def waiter(loop,conn):
#     while True:
#         try:
#             data = await loop.sock_recv(conn,1024)
#             if not data:
#                 break
#             print(data.decode('utf-8'))
#             await asyncio.sleep(0.5)
#             print(datetime.datetime.now())
#             await loop.sock_sendall(conn,data.upper())
#         except:
#             break
#     conn.close()
# async def main(ip,port):
#     loop = asyncio.get_running_loop()
#     s = socket.socket()
#     s.bind((ip,port))
#     s.listen(3)
#     s.setblocking(False)
#     while True:
#         conn,addr = await loop.sock_accept(s)
#         asyncio.create_task(waiter(loop,conn))
#
# if __name__ == '__main__':
#     asyncio.run(main('127.0.0.1',6000))

print('5'.center(100,'-'))

import asyncio
import socket,random

async def waiter(conn,loop):
    while True:
        try:
            data = await loop.sock_recv(conn,1024)
            if not data:
                break
            await loop.sock_sendall(conn,data.upper())
            print(random.randint(1000,9999),data.decode('utf-8'))
        except:
            break
    conn.close()

async def main(ip,port):
    s = socket.socket()
    s.bind((ip,port))
    s.listen(2)
    s.setblocking(False)
    loop = asyncio.get_running_loop()
    while True:
        conn,addr = await loop.sock_accept(s)
        asyncio.create_task(waiter(conn,loop))

if __name__ == '__main__':
    asyncio.run(main('127.0.0.1',5000))







































