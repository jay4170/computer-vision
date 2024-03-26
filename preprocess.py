
import cv2
import csv
image = cv2.imread('o5.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
for i in range(0, image_rgb.shape[0]):
    for j in range(0, image_rgb.shape[1]):
        pixel = image_rgb[i, j]
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]
        
        # Print the RGB values (Optional)
        print(f"Pixel at ({i}, {j}) - Red: {red}, Green: {green}, Blue: {blue}")
with open('other5.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Red", "Green", "blue"])
    
    
    for row in image:
        for pixel in row:
            r, g, b = pixel
            writer.writerow([r, g, b])