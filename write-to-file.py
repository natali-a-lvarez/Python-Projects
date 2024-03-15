try:
    f = open("file.txt", "a")
    f.write("new content")
except:
    print('oops there was an error :(')