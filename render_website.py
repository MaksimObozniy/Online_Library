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

    output_dir = 'docs'
    os.makedirs(output_dir, exist_ok=True)

    for i, page_books in enumerate(pages, start=1):
        rows = list(chunked(page_books, 2))
        rendered_page = template.render(
            rows=rows,
            current_page=i,
            total_pages=total_pages
        )

        filename = 'index.html' if i == 1 else f'index{i}.html'
        with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
            f.write(rendered_page)


    for folder in ['books', 'img', 'bootstrap']:
        src = folder
        dst = os.path.join(output_dir, folder)
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)

    if os.path.exists('favicon.ico'):
        shutil.copy('favicon.ico', os.path.join(output_dir, 'favicon.ico'))


if __name__ == '__main__':
    main()
