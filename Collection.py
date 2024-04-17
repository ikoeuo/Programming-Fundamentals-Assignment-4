import json

data_file = 'data.json'

def load_data():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=3)

def create_item(data, category, title, author, genre):
    data[category] = {'Title': title, 'Author': author, 'Genre': genre}
    save_data(data)
    print(f'\n{category} has been added/updated!')

def list_items(data):
    print('\nBooks | Movies | Songs:\n')
    print(json.dumps(data, indent=4))

def delete_item(data, category):
    if category in data:
        del data[category]
        save_data(data)
        print(f'\n{category} has been deleted.')
    else:
        print(f'\nInvalid: {category}')
