# # Display each line in a file
# fileopener = open('inputFile.txt', 'r')
# print(fileopener.read())
# fileopener.close()

## Display each line in a file with counter
# fileopener = open('inputFile.txt', 'r')
# for count, line in enumerate(fileopener):
#     pass
#     print(count,line)
# fileopener.close()

# # Display each line in a file
# fileopener = open('inputFile.txt', 'r')
# for line in fileopener:
#     line_split = line.split()
#     if line_split[2] == 'P':
#         print(line)
# fileopener.close()

## or use a context manager to shorten the lines of code and remove boilerplate.
# with open('inputFile.txt', 'r') as fileopener:
#     for line in fileopener:
#         line_split = line.split() #This splits each item in an element into 'columns'
#         if line_split[2] == 'F':
#             print(line)

# # Print only a specific line from a text file
# with open('inputFile.txt', 'r') as fileopener:
#     number_of_lines = fileopener.readlines()
#     print('The First Line is:', number_of_lines[43])

# # Print a range of specific lines from a text file
# with open('inputFile.txt','r') as fileopener:
#     specified_lines = [0, 1, 2, 41, 42]
#     for line_number, output_lines in enumerate(fileopener):
#         if line_number in specified_lines:
#             print (output_lines)


## Writing files
with open('inputFile.txt', 'r') as fileopener:
    passFile = open('passFile.txt', 'w')
    failFile = open('failFile.txt', 'w')
    for line in fileopener:
        line_split = line.split() #This splits each item in an element into 'columns'
        if line_split[2] == 'P':
            passFile.write(line)
        else:
            failFile.write(line)
