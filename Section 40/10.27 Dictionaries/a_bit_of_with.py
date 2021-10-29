with open('my_file.awesome', 'r') as the_read_file:
    # the_read_file = open('my_file.awesome', 'r')
    for line in the_read_file:
        print(line, end='')
    # actually happens = the_read_file.close()
    # helper stuff to prevent you from forgetting to close your files

# guess: when i read from a file that has the cursor at the end, i get
# empty string, so we're ok = we were wrong to guess this
# won't call this because it reads from a closed file
# the_read_file.readline()
