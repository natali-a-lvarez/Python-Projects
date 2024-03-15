try:
    with open('file.txt') as file:
        print(file.read())
except:
    print('oops there was an error :(')