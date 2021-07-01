from PIL import Image
import base64
i = 1

while True:

    encoded = base64.b64encode(
        open("images/"+str(i)+".png", "rb").read()).decode()
    print('data:image/png;base64,{}'.format(encoded))
    i = i+1
