from PIL import Image

# RGB values for recoloring.
darkBlue= (0, 51, 76)
red = (217, 26, 33)
lightblue = (112, 150, 158)
yellow= (252, 227, 166)

# Import image.
my_image = Image.open("haik.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

colorpixels = list(my_image.getdata())
list_length=len(colorpixels)
#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
for i in range(list_length):
	redapples = colorpixels[i][0]
	blueapples = colorpixels[i][1]
	greenapples = colorpixels[i][2]
	sum = redapples + blueapples + greenapples
	
	print(sum)
	if sum < 182:
		colorpixels[i] = darkBlue
	elif sum >= 182 and sum < 364:
		colorpixels[i] = red
	elif sum >= 364 and sum< 546:
		colorpixels[i] = lightblue
	else:
		colorpixels[i]= yellow 

my_image.putdata(colorpixels)
my_image.show()
# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"