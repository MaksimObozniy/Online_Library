import json
from jinja2 import Environment, FileSystemLoader


def main():


    with open('meta_data.json', 'r', encoding='utf-8') as f:
        books = json.load(f)

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    output = template.render(books=books)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(output)

if __name__ == '__main__':
    main()
