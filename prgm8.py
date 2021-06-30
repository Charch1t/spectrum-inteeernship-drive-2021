#To print the given star pattern


char = "* "
no_of_rows = 5

for i in range(no_of_rows):
    print(" "*i + char*(no_of_rows - i))
for j in range(2 , no_of_rows + 1):
    print(" "*(no_of_rows - j) + char*j)
