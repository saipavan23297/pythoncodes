'''
f= open('filehandlingtutorial.txt', 'a')
f.write("This text is added from the code using append operation")
print(f.read())
'''
import os 
def createfile(filename):
    try:
        with open(filename, 'w') as f:
            f.write('hello, World!\n')
        print("file"+ filename +"created succesfully")
    except:
        print("could not create a file ")
def readfile(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read()) 
            
    except:
        print("could not read the file")
def appendfile(filename, text):
    try: 
        with open(filename, 'a') as f:
            f.write(text)
            print("appended succesully"+filename)
    except:
        print("could not append file ")

def renamefile(filename, newfilename):
    try:
        os.rename(filename, newfilename)
        print("file "+ filename+ " renamed to "+ newfilename + " successfully")
    except:
        print("could not rename")   
def deletefile(filename):
    try:
        os.remove(filename)
        print("removed succesfully "+ filename)
    except:
        print("could not be dleted")

if __name__ =='__main__':
    filename="filehandlingtutorial1.text"
    text = "this is done using append"
    newfilename = "filehandlingtutorial4.txt"

    createfile(filename)
    readfile(filename)
    appendfile(filename,text)
    renamefile(filename, newfilename)    
    readfile(newfilename)
    deletefile(newfilename)
                                               

