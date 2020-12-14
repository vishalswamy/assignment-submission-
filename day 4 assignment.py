                           # day 4 assignment

# 1 python program for opening a file and writing

def filehandlingfuntions():
    #step 1: open/create a new text file, then writing the content into file.
    # append the content into the file if we execute the function the in the second time and so.
    f = open("vishal.txt","a+")
    for num in range(3):
        f.write("hello world from vishal %d\r" %(num + 1))
    f.close()   
        
    #step 2: open the text file agin to read the content, then displaying the content
    # into the terminal area

    f = open("vishal.txt","r")
    if f.mode == 'r':
        filecontents = f.read()
        print (filecontents)
       

   # optino2 : read the file content line by line, then saving into a list
    data = f.readlines()
    for i in data:
       print(i)

    # always close the file at the end each time finished
    f.close()


# 2 factorial program

def print_factors(x):
    print ("the factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
num = 3

print_factors(num)

    
 

