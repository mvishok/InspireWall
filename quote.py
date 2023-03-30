from PIL import Image, ImageDraw, ImageFont


def save(sentence, x1, y1):
    fnt = ImageFont.truetype('Cinzel-Regular.ttf', 30)
    img = Image.new('RGB', (x1, y1), color=(0, 0, 0))
    d = ImageDraw.Draw(img)

    sum = 0
    for letter in sentence:
        sum += d.textsize(letter, font=fnt)[0]

    avg = sum/len(sentence)

    letters = (x1/1.618)/avg
    inc = 0
    final = ''

    for letter in sentence:
        if (letter == '-'):
            final += '\n\n' + letter
        elif (inc < letters):
            final += letter
        else:
            if (letter == ' '):
                final += '\n'
                inc = 0
            else:
                final += letter
        inc += 1

    dim = d.textsize(final, font=fnt)
    x2 = dim[0]
    y2 = dim[1]
    qx = (x1/2 - x2/2)
    qy = (y1/2-y2/2)
    d.text((qx, qy), final, align="center", font=fnt, fill=(200, 200, 200))
    img.save('quote.png')
