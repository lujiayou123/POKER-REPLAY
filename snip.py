from PIL import Image

def index_to_card(i):
    if i==0:
        return "A"
    elif i==1:
        return "K"
    elif i==2:
        return "Q"
    elif i==3:
        return "J"
    elif i==4:
        return "T"
    elif i==5:
        return "9"
    elif i==6:
        return "8"
    elif i==7:
        return "7"
    elif i==8:
        return "6"
    elif i==9:
        return "5"
    elif i==10:
        return "4"
    elif i==11:
        return "3"
    elif i==12:
        return "2"

def index_to_token(i):
    if i==0:
        return "s"
    elif i==1:
        return "c"
    elif i==2:
        return "d"
    elif i==3:
        return "h"

img = Image.open("./deck/deck.png")
print(img.size)

height = 210
width = 140
for i in range(4):
    token = index_to_token(i)#花色设定
    upper = i*height
    lower = (i+1)*height
    for j in range(13):
        card = index_to_card(j)
        left = j*width
        right = (j+1)*width
        cropped = img.crop((left,upper,right,lower))  # (left, upper, right, lower)(0,0,140,210)
        cropped.save("./deck/"+ card + token + ".png")