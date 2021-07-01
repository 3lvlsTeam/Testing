import time
from urllib.request import urlopen
from PIL import Image
import requests
import base64


################################################################
s = requests.Session()
url1 = "http://127.0.0.1:5000/login"
url2 = "http://127.0.0.1:5000/loginF2"
url3 = "http://127.0.0.1:5000/loginF3"

start_time = time.time()
longin_data = {"username": "user1", "password": "!k5sh4jpxo@s"}
response = requests.post(url1, data=longin_data)
response = s.post(url1, longin_data)
###############################################################################################################


key = "Capture1.PNGCapture_2.PNGScreenshot_1.pngScreenshot_2.pngScreenshot_3.png"
longin_data1 = {"img_password": key}

r = s.post(url2, longin_data1)
with open('file.txt', 'w') as file:
    file.write(r.text)
    file.close

line = ''
width = 0
height = 0
f = open("file.txt", "r")

for a in f:
    b = str(a)
    if 'canvas' in b:
        line = b
        width = int(str(b.split('width="')[1]).split('"')[0])
        height = int(str(b.split('height="')[1]).split('"')[0])
        break

block_size = 40

image = Image.new(mode="RGBA", size=(block_size, block_size), color=(0, 0, 0))

white_img = Image.new("RGBA", (width, height), (255, 255, 255))
white_img.save("images/0.png")

block_number = int(white_img.width / block_size)
conter = 1

for i in range(2**(block_number*block_number)):
    for x in range(block_number):
        for y in range(block_number):
            new_image = Image.open("images/"+str(i)+".png")
            new_image.paste(image, (y*block_size, x*block_size), image)
            new_image.save("images/"+str(conter)+".png")
            encoded = base64.b64encode(
                open("images/"+str(conter)+".png", "rb").read()).decode()
            img_src = str('data:image/png;base64,{}'.format(encoded))
            conter = conter + 1
            longin_data3 = {"img_src": img_src}
            r = s.post(url3, longin_data3)
            if "Well done ! " in str(r.text):
                print("CRACKED!!!")
                print("the key: "+img_src)
                print("--- %sscronds ---" % (time.time() - start_time))
                exit()
