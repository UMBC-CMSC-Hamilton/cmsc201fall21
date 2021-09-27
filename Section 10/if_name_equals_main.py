# __name__ has 4 underscores (2 before and 2 after)
# if the file you are running python blah_file.py
# main is a string followed and preceded by two underscores
# __name__ is a 'hidden' variable that python sets for us.

# import the_other_file


# don't use this...
def main():
    pass

print(__name__)
if __name__ == '__main__':
    print('hello i am the main file')
