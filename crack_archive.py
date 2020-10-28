#Import required modules.
import zipfile
import rarfile

charlist = "abcdefghijklmnopqrstuvwxyz"
complete = []

for current in range(4):
    #Getting all the characters.
    a = [i for i in charlist]
    for x in range(current):
        #Using list comprehension to build the combinations.
        a = [y + i for i in charlist for y in a]
    complete = complete + a

z = zipfile.ZipFile("secret.zip", "r", zipfile.)

tries = 0

for password in complete:
    try:
        tries += 1
        z.setpassword(password.encode("ascii"))
        z.extract("password.txt")
        print(f"Password was found: {password}\nTries: {tries}")
        break
    except Exception as ex:
        print (ex)
        break;
