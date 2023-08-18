import asyncio
import os
import aiofiles

import aiohttp
import time

urls = ['https://putidorogi-nn.ru/images/stories/afrika/egipet/krasnoe_more_5.jpg',
        'https://putidorogi-nn.ru/images/stories/afrika/egipet/krasnoe_more_7.jpg',
        'https://putidorogi-nn.ru/images/stories/afrika/egipet/krasnoe_more_8.jpg'
        ]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
        #response = await session.get(url)
            cont = await response.read()
            filename = url.rsplit('/', 1)[-1]
            filename = os.path.join('images_async', filename)
            with open(filename, 'wb') as f:
                f.write(cont)
            print(f'Загружен файл {filename}')
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
