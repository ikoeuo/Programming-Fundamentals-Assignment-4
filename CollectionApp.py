import Collection

def run():
    
    global data
    data = Collection.load_data()

    while True:
        
        print('\n1. Create/Update Item \n2. List Item(s) \n3. Delete Item \n4. Exit App\n')
        choice = input('What would you like to do (1-4): ')

        if choice == '1':
            while True:
                category = input('\nEnter category (book/movie/song): ').lower()
                if category in ['book', 'movie', 'song']:
                    number = ''
                    while number.isdigit() == False:
                        number = input('Enter #: ')
                    title = input('Enter title: ')
                    author = input('Enter author: ')
                    genre = input('Enter genre: ')
                    category = category+str(number)
                    Collection.create_item(data, category, title, author, genre)
                    break
                else: 
                    print('\nInvalid category, Enter (book/card/cd)\n')

        elif choice == '2':
                Collection.list_items(data)

        elif choice == '3':
            while True:
                category = input('\nEnter category (book/movie/song): ').lower()
                if category in ['book', 'movie', 'song']:
                    number = ''
                    while number.isdigit() == False:
                        number = input('Enter #: ')
                    category = category+str(number)
                    Collection.delete_item(data,category)
                    break
                else:
                    print('\nInvalid category\n')

        elif choice == '4':
            print('\nThank you for using my app!')
            break

        else:
            print('\nInvalid selection.')

run()