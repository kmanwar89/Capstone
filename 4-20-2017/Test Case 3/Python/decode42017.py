import base64

def convert(image):
    convert = base64.b64decode(string)

    t = open("example.png", "w+")
    t.write(convert)
    t.close()
