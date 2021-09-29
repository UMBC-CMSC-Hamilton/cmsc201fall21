print('i am the non-main file')
# the __name__ of any imported file is just the file name
# the only one that gets changed is __main__
print(__name__)

if __name__ == '__main__':
    print('i am not supposed to print')