import Collection

def run():
    global data
    data = Collection.load_data()

    while True:
        
        print('\n1. Create Item \n2. List Item(s) \n3. Update Item \n4. Delete Item \n5. Exit App\n')
        choice = input('What would you like to do (1-5): ')

        if choice == '1':
            while True:
                category = input('\nEnter category (book/movie/song): ').lower()
                if category in ['book', 'movie', 'song']:
                    title = input('Enter title: ')
                    author = input('Enter author: ')
                    genre = input('Enter genre: ')
                    Collection.create_item(category, title, author, genre)
                    break
                else: 
                    print('Invalid category, Enter (book/card/cd)\n')

        elif choice == '2':
            category = input('Enter category (book/movie/song): ').lower()
            Collection.list_items(category)

        elif choice == '3':
            category = input("Enter category (book/movie/song): ").lower()
            index = int(input(f'Enter what you {category} you would like to update (enter {category} number): ')) - 1
            title = input(f'Enter new {category} title: ')
            author = input(f'Enter new {category} author: ')
            genre = input(f'Enter new {category} genre: ')
            Collection.update_item(category, index, title, author, genre)

        elif choice == '4':
            category = input('Enter category (book/movie/song): ').lower()
            index = int(input(f'Enter {category} to delete: ')) - 1
            Collection.delete_item(category, index)

        elif choice == '5':
            print('Thank you for using my app!')
            break

        else:
            print('Invalid selection.')

run()