import json
from collections import defaultdict

data_file = 'data.json'

data = defaultdict(list)

def save_data():
    with open(data_file, 'w') as file:
        json.dump(data, file)

def load_data():
    try:
        with open(data_file, 'r') as file:
             return json.load(file)

    except FileNotFoundError:
        return defaultdict(list)

def create_item(category, title, author, genre):
    item = {'Title': title, 'Author': author, 'Genre': genre}
    data[category].append(item)
    save_data()
    print(f'{category} has been added!')


def list_items(category):
    items = data[category]
    if not items:
        print(f'{category} not found')
    else:
        for i, item in enumerate(items, start=1):
            print(f'{category} {i}: {item}')

def update_item(category, index, title, author, genre):
    items = data[category]
    if 0 <= index < len(items):
        item = items[index]
        item['Title'] = title
        item['Author'] = author
        item['Genre'] = genre
        save_data()
        print(f'{category} has been updated')

    else:
        print(f'Invalid {category}')
    

def delete_item(category, index):
    items = data[category]
    if 0 <= index < len(items):
        del items[index]
        save_data()
        print(f'{category} has been deleted.')
    else:
        print(f'Invalid {category}')