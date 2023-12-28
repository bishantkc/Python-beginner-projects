import requests
from io import BytesIO
from PIL import Image

'''
params = {"q": "pizza"} #its like query parameter changing last in url
r = requests.get("https://www.google.com/", params= params)
print("Status:", r.status_code) #this is to know if any error happen what is it

print(r.url)

f = open("page.html", "w+")
f.write(r.text)
'''

r = requests.get("https://images7.alphacoders.com/132/1329178.png")
print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content)) # BytesIO is used to treat binary data like a file

print(image.size, image.format, image.mode)
path = "./image." + image.format

try:
    image.save(path, image.format)
except:
    print("Cannot save image.")