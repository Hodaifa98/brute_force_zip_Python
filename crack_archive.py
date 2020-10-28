#Import required modules.
import zipfile

#Zip name.
zip_name = "secret.zip"

#Length of password.
pass_length = 4

#A list of characters to attempt to combine.
charlist = "abcdefghijklmnopqrstuvwxyz"

#An empty array to fill with potential passwords.
complete = []

for current in range(pass_length):
    #Getting all the characters.
    a = [i for i in charlist]
    for x in range(current):
        #Using list comprehension to build the combinations.
        a = [y + i for i in charlist for y in a]
    #Add password to list.
    complete = complete + a

#Open the zip file.
z = zipfile.ZipFile(zip_name, "r")

#Hold number of tries it took to find the password.
tries = 0

#Iterate through the passwords in the complete array.
for password in complete:
    try:
        tries += 1
        #Set the password and extract all files from the zip archive.
        z.setpassword(password.encode("ascii"))
        z.extractAll()
        print(f"Password was found: {password}\nTries: {tries}")
        break
    except:
        #If the extraction failed, simply pass because the password was incorrect.
        pass
