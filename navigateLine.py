filename = input("Please enter the file name: ")    #prompts for the file name 
f = open(filename, 'r')     #opens the file in read mode
l = f.readlines()           #all the lines are added to the list l
while(1):                   #enters into the loop
    print("There are", len(l), "lines in file.")    #displays no.of lines in file
    n = int(input("Please enter the line number you want: "))   #prompts for the line number
    if(n == 0):             #if n is zeror
        break               #break from the loop and quit the program
    else:                   #else
        print(l[n-1])       #prints that particular line(as list index starts from 0, we took n-