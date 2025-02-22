from PIL import Image, ImageDraw, ImageFont


text = "THERITIKSUTHAR"


width, height = 800, 400
image = Image.new("RGB", (width, height), "blue")


draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", 40)   

bbox = draw.textbbox((0, 0), text, font=font)  
text_width = bbox[2] - bbox[0]  
text_height = bbox[3] - bbox[1] 

x = (width - text_width) // 2
y = (height - text_height) // 2

draw.text((x, y), text, fill="black", font=font)


image.save("text_image.png")
image.show()
