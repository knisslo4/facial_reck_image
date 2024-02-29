from PIL import Image, ImageDraw
import face_recognition

import os
file_path = 'logan_face.jpg'
if os.path.isfile(file_path):
    image = face_recognition.load_image_file(file_path)
else:
    print(f"The file {file_path} does not exist")

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("logan_face.jpg")

# Find all the faces in the image
face_locations = face_recognition.face_locations(image, model="cnn")

print("I found {} face(s) in this photograph.".format(len(face_locations)))

# Create a PIL image object from the numpy array
pil_image = Image.fromarray(image)

# Create a Pillow ImageDraw Draw object to draw with
draw = ImageDraw.Draw(pil_image)

# Loop over each face found in the image to draw a box around it
for top, right, bottom, left in face_locations:
    # Draw a box around the face
    draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0))

# Remove the drawing library from memory as per the Pillow documentation
del draw

# Save the image with boxes around the faces
pil_image.save('/root/facial_reck_image/detected_faces.jpg')

'''
for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
'''
