import random

from PIL import Image, ImageDraw, ImageFont


def image():
    name = str(input("Enter Your Full Name: "))
    if name:
        try:
            # split the name if there are more than one word.
            split = name.split(' ')
            # get the fist letter from first two words.
            text = '{}{}'.format(split[0][0], split[1][0])
        except:
            # if the name has one word then get the first letter.
            text = name[0]

        color_list = [
            (153, 102, 255),
            (000, 102, 255),
            (000, 000, 000),
            (255, 000, 000),
            (255, 153, 000),
            (000, 153, 51),
            (102, 51, 000),
            (204, 000, 153),
        ]
        # get random background colors.
        color = random.choice(color_list)
        image = Image.new('RGB', (288, 288), color=color)
        font_type = ImageFont.truetype(font='Roboto-Bold.ttf', size=150)
        draw = ImageDraw.Draw(image)
        # get height & weight of the text.
        w, h = draw.textsize(text.upper(), font_type)
        draw.text(((288-w)/2, 50), text=text.upper(),
                  fill=(255, 255, 255), font=font_type)

        image.show()
        image.save("picture", "PNG")

image()
