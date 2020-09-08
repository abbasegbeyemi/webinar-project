import cv2
import face_recognition
import numpy as np
from PIL import Image
from PyQt5.QtGui import QImage


def qimage_frame(frame):
    # Convert the edited frame to QIMAGE
    height, width, channels = frame.shape  # RGB is a three dimensional matrix for each channel
    bytesPerLine = 3 * width  # Bytes per line is width * 3 because we have three channels
    # Frame in QIMAGE
    frame_image = QImage(frame, width, height, bytesPerLine, QImage.Format_BGR888)
    return frame_image


def label_frame(frame, face_locations, face_names):
    """This function draws a box around the face in the frame, and puts the name below the box"""
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2

        # Our BGR color for the box
        col = (97, 205, 252)

        # OpenCV rectangle round the face
        cv2.rectangle(frame, (left, top), (right, bottom), col, 2)
        # Draw a label with a name below the face using another rectange
        cv2.rectangle(frame, (left, bottom + 5), (right, bottom + 40), col, cv2.FILLED)
        # Declare the font to use for the text
        font = cv2.FONT_HERSHEY_DUPLEX
        # Add the text top our second rectangle
        cv2.putText(frame, name, (left + 6, (bottom + 40) - 6), font, 1.0, (0, 0, 0), 1)


def format_frame(frame_in):
    """This function filps the frame to make it look more natural, and crops to a 1:1 aspect ratio"""
    frame_flipped = cv2.flip(frame_in, 1)

    # If vertical is 5, we can make horizontal range from 1 - 5 to give us 5:5  square video
    frame_height = frame_flipped.shape[0]
    hor_multiplier = 5  # This can range from 1 - 5 to give a 5:1, 5:2, 5:3 etc aspect ratio

    # Convert to PIL image so we can crop
    pil_frame = Image.fromarray(frame_flipped)

    # Define the area we want to crop (0, 0) is the top left
    cropped_pil_area = (0, 0, hor_multiplier / 5 * frame_height, frame_height)
    cropped_img = pil_frame.crop(cropped_pil_area)

    frame_out = np.array(cropped_img)
    return frame_out


def create_encodings(images: list) -> list:
    """This function creates a list of face encodings, from the provided image files"""
    # Initialise a list that will store our encodings
    encodings = []
    # Loop through the list of images provided
    for img in images:
        # Create the encoding
        f_img = face_recognition.load_image_file(img)
        encoding = face_recognition.face_encodings(f_img)[0]
        # Add it to  our initialised list
        encodings.append(encoding)
        # Return the list of encodings
    return encodings


def recognise_faces(known_face_encodings, rgb_small_frame, names):
    # Get the location of faces in the frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    # Create an encoding using the face found in the frame
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    # Overwrite the face names from the previous frame
    face_names = []
    # All the face encodings in the frame should be compared to the ones we already know
    for face_encoding in face_encodings:

        # Compare an encoding to the encodings in our list
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, 0.5)

        # Name is unknown initially and changes to the actual name if there is a match
        name = "Unknown"

        # Euclidean distance is how we compare
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

        # Get the index of the best match. We only want the index of the face with the lowest
        # eucliudean distance so it is safe to cast it to int.
        best_match_idx = int(np.argmin(face_distances))

        # If there is something at the index we got
        if matches[best_match_idx]:
            # Set the name to the persons name
            name = names[best_match_idx]

        # Add the name to our list of faces in that FRAME
        face_names.append(name)
    return face_locations, face_names
