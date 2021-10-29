class StringGiver:
    def __init__(self):
        self.the_string = 'hello i am a string'
    
    def __enter__(self):
        return self.the_string
    
    def __exit__(self, *args):
        print('i am leaving now')
    
"""
    cool people way to write:
    ->>test_file = open('test_file.txt', 'r')
    do something here
    ->>test_file.close()
"""

with open('test_file.txt', 'r') as test_file:
    # file object will return the "file handle" thing to you
    print(test_file)
    print(test_file.read())
    
    """secret line of code gets executed here
        test_file.close()
    """

# this results in a ValueError who knows why...
# test_file.readline()
s = StringGiver()
with s as the_string:
    print(the_string)

print('after the with statement')