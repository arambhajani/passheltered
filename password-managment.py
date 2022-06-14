import os.path
import base64

def checkExistence():
    if os.path.exists("pa$$.txt"):
        pass
    else:
        file = open("pa$$", 'w')
        file.close()
def appendNew():
    # This function will append new password in the txt file
    file = open("pa$$.txt", 'a')

    print()
    print()

    userName = input("Please enter the user name: ")
    website = input("Please enter the website address here: ")
    sample_string = input("Please enter the password here: ")
    sample_string_bytes = sample_string.encode("ascii") 
        
    base64_bytes = base64.b64encode(sample_string_bytes) 
    password = base64_bytes.decode("ascii") 

    print()
    print()

    usrnm = "UserName: " + userName + "\n"
    web = "Website: " + website + "\n"
    pwd = "Password: " + password + "\n"

    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(web)
    file.write(pwd)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close
def readPasswords():

    file = open('pa$$.txt', 'r')
    content = file.read()
    file.close()
    print(content)
def decode():
    j=int(input("enter key:-"))
    if j == 2001:
        base64_string =input("enter hashpassword:-")
        base64_bytes = base64_string.encode("ascii") 
            
        sample_string_bytes = base64.b64decode(base64_bytes) 
        sample_string = sample_string_bytes.decode("ascii") 
            
        print(f"Decoded password: {sample_string}")
    else:
        exit()
def main():
    print("----------WELCOME TO Passheltered------------")
    print("\n")
    print("\n1.To add entry \n2.To read entries \n3.To decode password \n4.exit")
    k=int(input(" \nEnter your choice:-"))
    if k == 1:
        appendNew()
        main()
    elif k == 2:
        readPasswords()
        main()
    elif k == 3:
        decode()
        main()
    else:
        exit()

checkExistence()
main()
