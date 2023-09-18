from PIL import Image, ImageDraw, ImageFont
import os
import sys

#####################################################################
ean  = 4002846034504        # set EAN code
size = "big"              # "small" or "big" --> Width of the Code
#####################################################################


line_width = 2
font_size = 23
line_height = 100
margin = 40

# Codes
letter_code_before_middle_odd = ["0001101","0011001","0010011","0111101","0100011","0110001","0101111","0111011","0110111","0001011"]
letter_code_before_middle_even = ["0100111","0110011","0011011","0100001","0011101","0111001","0000101","0010001","0001001","0010111"]
letter_code_after_middle = ["1110010","1100110","1101100","1000010","1011100","1001110","1010000","1000100","1001000","1110100"]
even_odd = ["uuuuuu","uugugg","uuggug","uugggu","uguugg","ugguug","uggguu","ugugug","uguggu","uggugu"]

barcode_values_13 = [0] * 95                    # initialize list with 95 zeros
barcode_values_8 = [0] * 67                     # initialize list with 67 zeros


# Functions
def ean_thirteen(width, height, off, barcode_plain):
    # Fill Numbers
    for plain in range(1, 13):      # for each figure in the code
        for num in range(0, 7):
            if plain < 7:
                order = even_odd[int(barcode_plain[0])]
                if order[plain - 1] == "u":
                    barcode_values_13[(plain - 1) * 7 + 3 + num] = int(letter_code_before_middle_odd[int(barcode_plain[plain])][num])
                else:
                    barcode_values_13[(plain - 1) * 7 + 3 + num] = int(letter_code_before_middle_even[int(barcode_plain[plain])][num])
            else:
                barcode_values_13[plain * 7 + 1 + num] = int(letter_code_after_middle[int(barcode_plain[plain])][num])

def ean_eight(width, height, barcode_plain):
    # Fill Numbers
    for plain in range(0, 8):      # for each figure in the code
        for num in range(0, 7):
            if plain < 4:
                barcode_values_8[plain * 7 + 3 + num] = int(letter_code_before_middle_odd[int(barcode_plain[plain])][num])
            else:
                barcode_values_8[plain * 7 + 8 + num] = int(letter_code_after_middle[int(barcode_plain[plain])][num])

def set_size(size, barcode_plain):
    global line_width
    global font_size
    if size == "small":
        font_size = 23
        line_width = 2
    elif size == "big":
        line_width = 4
        font_size = 34

def save(standard, width, height, off, barcode_plain, save_path):

    try:
        os.remove(save_path)
    except:
        pass

    try:
        fnt = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", font_size)
    except:
        fnt = None

    image_width = width * 102 + off
    img = Image.new("RGB", (image_width, height + 40), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    if standard == 8 and (any(c.isalpha() for c in barcode_plain)) is False:
        for i in range(0,67):
            x = (image_width - 67 * width) / 2 + i * width
            if barcode_values_8[i] == 0:
                draw.line((x,10,x,height), width=width, fill="#FFFFFF")
            if barcode_values_8[i] == 1:
                draw.line((x,10,x,height), width=width, fill="#000000")
            if i==0 or i==2 or i==32 or i==34 or i==64 or i==66:
                draw.line((x,10,x,height+15), width=width, fill="#000000")
        draw.text(((image_width - 67 * width) / 2 + width*17 - font_size, height),barcode_plain[0:4], font=fnt,fill="#000000")
        draw.text(((image_width - 67 * width) / 2 + width* 49 - font_size, height),barcode_plain[4:8], font=fnt,fill="#000000")
        img.save(save_path)

    elif standard == 13 and (any(c.isalpha() for c in barcode_plain)) is False:
        for i in range(0,95):
            x = i * width + off
            if barcode_values_13[i] == 0:
                draw.line((x,10,x,height), width=width, fill="#FFFFFF")
            if barcode_values_13[i] == 1:
                draw.line((x,10,x,height), width=width, fill="#000000")
            if i==0 or i==2 or i==46 or i==48 or i==92 or i==94:
                draw.line((x,10,x,height+15), width=width, fill="#000000")
        draw.text((off - 25, height), barcode_plain[0], font=fnt, fill="#000000")
        draw.text((off + width * 24 - font_size * 3/2, height),barcode_plain[1:7], font=fnt, fill="#000000")
        draw.text((off + width* 70 - font_size * 3/2, height),barcode_plain[7:13], font=fnt, fill="#000000")
        img.save(save_path)
    elif any(c.isalpha() for c in barcode_plain):
        print("Error", "Only numbers allowed!")
    else:
        print("Error", "Please enter valid EAN first!")


def main(plain, size, path):
    ln = len(plain)

    # encoding the ean
    if ln == 8:
        ean_eight(line_width, line_height, plain)
    elif ln == 13:
        ean_thirteen(line_width, line_height, margin, plain)

    # specify the width of the image
    set_size(size, plain)

    # genereate and save file
    save(ln, line_width, line_height, margin, plain, path)

if __name__ == '__main__': 

    # looking for commandline arguments
    arguments = sys.argv[1:]
    for arg in arguments:
        if str(arg).isdigit():
            if len(arg) == 8 or len(arg) == 13:
                ean = arg
            else:
                print("invalid length of EAN")
                main(str(ean), size, 'invalid_length_of_EAN.jpg')
        elif arg == "--small" or arg == "--big":
            size = arg.strip("-")

    main(str(ean), size, str(ean) + '.jpg')