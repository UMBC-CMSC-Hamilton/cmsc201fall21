if __name__ == '__main__':
    # open(filename, read_or_write)
    hamlet_file = open('dune.txt', 'r')
    count = 0
    for line in hamlet_file:
        # the line still has the endline from the file
        # unlike input, getting a line from a file won't remove
        # any endlines
        # calling hamlet_file.readline()
        print(line, end='')
        if 'horatio' in line.lower():
            count += 1
            
    print('\nhoratio count', count)

    hamlet_file.close()
    
    # if you don't set a mode it defaults to read mode
    hamlet_file = open('dune.txt')
    # the endlines here are coming from the file
    print(hamlet_file.read())
    
    hamlet_file.close()
    
    extra_credit_file = open('../something')
    print(extra_credit_file.read())
    extra_credit_file.close()
    
    rando_file = open('inside_dir/something_else.txt', 'r')
    # very nice very convenient
    print(rando_file.readlines())
    
    """
        1) use a loop, secretly call readline
        2) use readline() directly and you'll get a single line from the file
        3) use readlines() and you'll get a list of lines
        4) use read() - reads the whole file and returns a string
        
        none of these strip the final \n off of things...
        
        remember to be nice to the operating system and close your files.
    """
    
    """
        How do we write into a file?
        
        two write modes =   'w' opens the file blanks it out.
                            
                            'a' append mode appends to the end of the file
                                sets the "file pointer" (cursor) to the very end
    """
    
    write_file = open('my_file.txt', 'a')

    write_list = []
    s = input()
    while s != 'quit':
        write_list.append(s + '\n')
        s = input()

    write_file.writelines(write_list)
    
    write_file.close()
    
    