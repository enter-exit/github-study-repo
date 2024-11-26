# print('1'.center(100,'-'))

# import asyncio
#
#
# async def work(x):
#     print('当前接受的参数为：',x)
#     await asyncio.sleep(1)
#     return f'当前任务的返回值为：{x}'
# async def main():
#     tasks = [asyncio.create_task(work(i)) for i in range(10)]
#     res = await asyncio.gather(*tasks)
#     print(res)
#     # done,pending = await asyncio.wait(tasks)
#     # for item in done:
#     #     print(item.result())
#
#
#
# if __name__ == '__main__':
#     asyncio.run(main())

print('2'.center(100,'-'))
import asyncio
async def work(x):
    print('当前接受的参数为：',x)
    await asyncio.sleep(1)
    return f'当前任务的返回值为：{x}'
async def main():
    tasks = [asyncio.create_task(work(i)) for i in range(10)]
    res = await asyncio.gather(*tasks)
    print(res)

if __name__ == '__main__':
    asyncio.run(main())