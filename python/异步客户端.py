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




print('*'*100)
import socket
import asyncio


async def main(ip,port,data):
    while 1:
        c = socket.socket()
        loop = asyncio.get_running_loop()
        await loop.sock_connect(c,(ip,port))
        await loop.sock_sendall(c,data.encode('utf-8'))
        res = await loop.sock_recv(c,1024)
        await asyncio.sleep(2)
        print(res.decode('utf-8'))
    c.close()


if __name__ == '__main__':
    asyncio.run(main('127.0.0.1',5000,'abc'))




































