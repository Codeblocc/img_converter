from PIL import Image, ImageFilter

img = Image.open('./images/kg.jpg')
filtered_img = img.convert('L')

resize = filtered_img.resize((300,300))
resize.save('grey.png', 'png')
