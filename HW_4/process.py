from multiprocessing import Process
import os
import time

import requests

urls = [
    'https://krasivosti.pro/uploads/posts/2021-07/1626140697_28-krasivosti-pro-p-koti-leopardovogo-okrasa-koti-krasivo-foto-28.jpg',
    'https://krasivosti.pro/uploads/posts/2021-07/1626140752_55-krasivosti-pro-p-koti-leopardovogo-okrasa-koti-krasivo-foto-58.jpg',
    'https://putidorogi-nn.ru/images/stories/afrika/egipet/krasnoe_more_4.jpg'
]


def download(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        filename = url.rsplit('/', 1)[-1]
        filename = os.path.join('images_process', filename)
        with open(filename, 'wb') as f:
            f.write(content)
        print(f'Загружен файл {filename}')
        print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


processes = []
start_time = time.time()
if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
