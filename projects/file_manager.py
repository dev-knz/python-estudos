explorer = list() # based in name app of files of Windows

while True:

    choice = int(input(('1 - Create File\n2 - Delete File\n3 - Show File\n4 - Exit\n>> ')))
    
    if choice == 1:
        file = str(input('Name the file: '))
        validation = 0

        for name in explorer:
            if file == name:
                print('The file name already exists.')
                validation = 1
        
        if validation == 0:
            explorer.append(file)
            print('The file has been added.')

    elif choice == 2:
        file = str(input('Delete file name: '))
        validation = 0

        for name in explorer:
            if file == name:
                print('Deleted.')
                explorer.remove(file)
                validation = 1
        
        if validation == 0:
            print('Error deleting file name.')
    
    elif choice == 3:
        for c, v in enumerate(explorer):
         print(f'{c} - {v}.txt')
    
    elif choice == 4:
        print('Closing File Manager...')
        break