f = open("hello.txt" , "r")
print(f.read())
f.close()

#print(f.read(5)) - how many characters u want to return 
#print(f.readline()) - writing this line multiple times add lines in output 

#with the help of for loop
f = open("hello.txt" , "r")

for x in f:
    print(x)

#t = for edit txt 
#r = for read only 
#error occurs if the file does not exists

#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content

f = open("hello.txt" , "a")
f.write("adding extra lines in the file PepegaLaugh")
f.close()

f =open("hello.txt" , "r")
print(f.read())
