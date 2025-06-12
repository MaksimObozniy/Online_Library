import json

from jinja2 import Environment, FileSystemLoader
from livereload import Server
from more_itertools import chunked

def main():


    with open('meta_data.json', 'r', encoding='utf-8') as f:
        books = json.load(f)

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    rows = list(chunked(books, 2))

    output = template.render(books=books, rows=rows)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(output)

if __name__ == '__main__':
    main()

    server = Server()
    server.watch('template.html', main)
    server.serve(root='.', default_filename='index.html')
