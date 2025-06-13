import os
import json
import math
import shutil

from jinja2 import Environment, FileSystemLoader
from livereload import Server
from more_itertools import chunked


BOOKS_PER_PAGE = 10


def main():

    with open('meta_data.json', 'r', encoding='utf-8') as f:
        books = json.load(f)


    total_books = len(books)
    total_pages = math.ceil(total_books / BOOKS_PER_PAGE)

    pages = list(chunked(books, BOOKS_PER_PAGE))

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    os.makedirs('pages', exist_ok=True)


    for i, page_books in enumerate(pages, start=1):
        rows = list(chunked(page_books, 2))

        output = template.render(
            rows=rows,
            current_page=i,
            total_pages=total_pages
            )

        with open(f'pages/index{i}.html', 'w', encoding='utf-8') as f:
            f.write(output)

if __name__ == '__main__':

    main()

    server = Server()
    server.watch('template.html', main)
    server.serve(root='pages', default_filename='index1.html')
