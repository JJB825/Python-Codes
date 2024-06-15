import os
def create_file(filename):
    try:
        with open(filename,'w') as handle:
            handle.write("Hi, how are you ?\n")
        print("File",filename,"created successfully.\n")
    except IOError:
        print("Unable to create file",filename,".\n")
    handle.close()
def delete_file(filename):
    try: 
        os.remove(filename)
        print(filename,"deleted successfully.\n")
    except:
        print("File",filename,"doesn't exists.\n")
def rename_file(old_filename,new_filename):
    try:
        os.rename(old_filename,new_filename)
        print("File renamed successfully.\n")
    except IOError:
        print("Unable to rename file.\n")
def read_file(filename):
    try:
        with open(filename,'r') as handle:
            print(handle.read())
            handle.close()
    except IOError:
        print("Unable to read file",filename,".\n")
def add_content(filename,content):
    try:
        with open(filename,'a') as handle:
            handle.write(content+'\n')
        print("Content added successfully to file",filename,".\n")
        handle.close()
    except IOError:
        print("Unable to append content to",filename,".\n")
def delete_entire_content(filename):
    try:
        with open(filename,'w') as handle:
            handle.truncate(0)
            handle.close()
        print("Entire content deleted successfully from file",filename,".\n")
    except IOError:
        print("Unable to delete content from file",filename,".\n")
def delete_particular_line(filename,line_number):
    try:
        with open(filename,'r') as handle:
            text=handle.readlines()
        handle.close()
        if(1<=line_number<=len(text)):
            with open(filename,'w') as handle:
                del text[line_number-1]
                handle.writelines(text)
            print("Line number",line_number,"deleted successfully.\n")
            handle.close()    
        else:
            print("Line",line_number,"is not in file",filename,".")
            print("File",filename,"has",len(text),"lines.\n")
    except IOError:
        print("Unable to delete from file",filename,".\n")
def delete_particular_word(filename,word):
    try:
        with open(filename,'r') as handle:
            text=handle.read()
            handle.close()
        text=text.replace(word,'')
        with open(filename,'w') as handle:
            handle.write(text)
        handle.close()
    except IOError:
        print("Unable to delete from file",filename,".\n")

while True:
    print('Choose anyone from following : \n1. Create file\n2. Rename file\n3. Delete file\n4. Read file\n5. Add content\n6. Delete content\n7. Exit\n')
    choice=int(input('Enter your choice : '))
    if choice==1:
        name=input('Enter name of file : ')
        create_file(name)
    elif choice==2:
        old_name=input('Enter name of file : ')
        new_name=input('Enter new name of file : ')
        rename_file(old_name,new_name)
    elif choice==3:
        name=input('Enter name of file : ')
        delete_file(name)
    elif choice==4:
        name=input('Enter name of file : ')
        read_file(name)
    elif choice==5:
        name=input('Enter name of file : ')
        content=input('Write what you want to add : \n')
        add_content(name,content)
    elif choice==6:
        print('Choose any one : \n1. Entire content\n2. Particular line\n3. Particular word\n')
        ch=int(input('Enter your choice : '))
        if ch==1:
            name=input('Enter name of file : ')
            delete_entire_content(name)
        elif ch==2:
            name=input('Enter name of file : ')
            num=int(input('Which line is to be deleted ? : '))
            delete_particular_line(name,num)
        elif ch==3:
            name=input('Enter name of file : ')
            word=input('Which word needs to be deleted ? : ')
            delete_particular_word(name,word)
        else:
            print("Invalid choice\n")
    elif choice==7:
        c=input("Do you wish to continue ? (y/n) : ")
        if c=='n':
            break
        else:
            continue