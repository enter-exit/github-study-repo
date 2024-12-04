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

print('2'.center(100,'-'))
import socket
import asyncio
async def main(ip,port,data):
    while True:
        c = socket.socket()
        loop = asyncio.get_running_loop()
        await loop.sock_connect(c,(ip,port))
        await loop.sock_sendall(c,data.encode('utf-8'))
        res = await loop.sock_recv(c,1024)
        print(res.decode('utf-8'))
        await asyncio.sleep(0.2)
    c.close()

if __name__ == '__main__':
    asyncio.run(main('127.0.0.1',5005,'abc'))
























