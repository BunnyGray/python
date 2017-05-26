from time import sleep
# for i in range(10):
#     for x in range(i+1):
#         print('.', end='', flush=True)
#
# -*-coding:utf-8-*-
"""
ayou
"""
import aiohttp
import asyncio
async def print_page(url, num_retries=3):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=60) as response:
                print("access!")
                # raise_for_status(),如果不是200会抛出HttpProcessingError错误
                response.raise_for_status()
                body = await response.text()
        except aiohttp.http.HttpProcessingError as e:
            body = None
            if num_retries > 0:
                # 如果不是200就重试，每次递减重试次数
                return await print_page(url, num_retries - 1)
                # 不存在URL会抛出ClientResponseError错误
        except aiohttp.ClientResponseError as e:
            return e
    session.close()
    print(body)
    return body


def main():
    # 这是一个不存在URL
    # url = 'http://httpbin.org/status/404111'
    # 这是一个404的URL
    # url = 'http://www.baidu.com'
    url = 'http://www.dytt8.net/html/gndy/dyzz/20151015/49284.html'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_page(url))
    loop.close()


if __name__ == '__main__':
    main()