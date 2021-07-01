from PIL import Image
import base64


block_size = 50

image = Image.new(mode="RGBA", size=(block_size, block_size), color=(0, 0, 0))

white_img = Image.new("RGBA", (300, 300), (255, 255, 255))
white_img.save("images/0.png")

block_number = int(white_img.width / block_size)
conter = 1

for i in range(2**(block_number*block_number)):
    for x in range(block_number):
        for y in range(block_number):
            new_image = Image.open("images/"+str(i)+".png")
            new_image.paste(image, (y*block_size, x*block_size), image)
            new_image.save("images/"+str(conter)+".png")
            conter = conter + 1

    print(conter)
