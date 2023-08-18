# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию
# изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и
# общем времени выполнения программы.
#НОГОПОТОЧНЫЙ ПОДХОД
import os
import threading
import time

import requests

urls = [
    'https://usatiki.ru/wp-content/uploads/2017/04/anekdoty-pro-kotov-i-koshek.jpg',
    'https://santreyd.ru/upload/staff/upload/staff/vplate/all_photos/06d31a32a4b0897cc298aaa1a68945ac225c9284.jpg'
]


def download(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        filename = url.rsplit('/', 1)[-1]
        filename = os.path.join('images', filename)
        with open(filename, 'wb') as f:
            f.write(content)
        print(f'Загружен файл {filename}')
        print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


start_time = time.time()


def main(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=download, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main(urls)
