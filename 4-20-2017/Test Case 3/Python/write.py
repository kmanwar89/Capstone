# Import libraries
import base64

# Picture Processing
f=open("abc.jpg","rb") # file is in the same directory, relative path
fileContent=f.read()
byteArr = base64.b64encode(fileContent)
f.close()

text = open ("test.txt","w")
text.write(str(byteArr))
text.close()

print("Base64-encoded image written to text file")
