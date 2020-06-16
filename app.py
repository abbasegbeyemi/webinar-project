import os

import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QThread
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
import face_recognition
import numpy as np
from webinar_ui.AppWindow import *


class AppWindow(QMainWindow, Ui_MainWindow):
    """Entry point into our application"""

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Provide a dictionary of employees. This could be from a database.
        self.employees = {
            "Abbas": "abbas-1.jpg",
            "Ruki": "mamiya.jpg"
        }

        self.current_face = ""
        self.logged_in_employees = []
        self.videoThread = VideoThread(people = self.employees)
        self.feed_running = True
        self.videoThread.frameSignal.connect(self.display_video)
        self.videoThread.start()

        # Connect to the sign in button
        self.button_signin.clicked.connect(self.sign_in_employee)

        # Connect to the face name updater signale
        self.videoThread.namesSignal.connect(self.update_current_face)

    @pyqtSlot(QImage)
    def display_video(self, frame):
        self.label_video_feed.setPixmap(QPixmap.fromImage(frame))

    @pyqtSlot()
    def sign_in_employee(self):
        if self.current_face in list(self.employees.keys()) and self.current_face not in self.logged_in_employees:
            self.logged_in_employees.append(self.current_face)

            # Append to the list widget
            self.listwidget_signed_in.clear()
            self.listwidget_signed_in.addItems(self.logged_in_employees)

    @pyqtSlot()
    def on_button_signout_clicked(self):
        if self.current_face in self.logged_in_employees:
            self.logged_in_employees.remove(self.current_face)

            # Update the list widget
            self.listwidget_signed_in.clear()
            self.listwidget_signed_in.addItems(self.logged_in_employees)

    @pyqtSlot(list)
    def update_current_face(self, list_of_faces):
        self.current_face = ""
        if list_of_faces and list_of_faces[0] != "Unknown":
            self.current_face = list_of_faces[0]


class VideoThread(QThread):
    frameSignal = pyqtSignal(QImage)
    namesSignal = pyqtSignal(list)

    def __init__(self, people):
        QThread.__init__(self)
        self.cap = None
        self.feed = True
        self.people = people

    @pyqtSlot()
    def run(self):
        # Image camera feed capture
        self.cap = cv2.VideoCapture(0)
        # Get the face images from the provided dictionary of faces and names
        faces = []
        # Using the standard for loop
        for _, face in self.people.items():
            faces.append(face)
        # Create face encodings from the face images
        known_face_encodings = create_encodings(faces)
        # Get the names from the dictionary using list comprehension
        names = [name for name, _ in self.people.items()]
        process_this_frame = True

        # Declare s list of face locations
        face_locations = []
        # Declare a list where recognised faces will live
        face_names = []

        while self.feed:
            # Capture frame by frame
            ret, frame = self.cap.read()
            if ret:  # ret returns true of frame was read correctly, or false
                # Find faces and face encodings in the frame
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgb_small_frame = small_frame[:, :, ::-1]

                if process_this_frame:
                    # Get the location of faces in the frame
                    face_locations = face_recognition.face_locations(rgb_small_frame)
                    # Create an encoding using the face found in the frame
                    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                    # Redeclare the face names list to add newly detected faces
                    face_names = []
                    # All the face encodings in the frame should be compared to the ones we already know
                    for face_encoding in face_encodings:
                        # Compare an encoding to the encodings in our list
                        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                        # Name is unknown initially and changes to the actual name if there is a match
                        name = "Unknown"
                        # Euclidean distance is how we compare
                        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                        # Get the index of the best match
                        best_match_idx = np.argmin(face_distances)
                        # If there is something at the index we got
                        if matches[best_match_idx]:
                            # Set the name to the persons name
                            name = names[best_match_idx]
                        # Add the name to our list of faces in that FRAME
                        face_names.append(name)
                # We do not process the nest frame
                process_this_frame = not process_this_frame

                # Now we want to draw boxes and labels around the faces in the frame
                # For each name in ou
                for (top, right, bottom, left), name in zip(face_locations, face_names):
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    # OpenCV rectangle round the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 34), 2)
                    # Draw a label with a name below the face using another rectange
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    # Declare the font to use for the text
                    font = cv2.FONT_HERSHEY_DUPLEX
                    # Add the text top our second rectangle
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                # Convert the edited frame to QIMAGE
                height, width, channels = frame.shape  # RGB is a three dimensional matrix for each channel
                bytesPerLine = 3 * width  # Bytes per line is width * 3 because we have three channels
                # Frame in QIMAGE
                frame_image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_BGR888)
                # EMIT the whole frame
                self.frameSignal.emit(frame_image)
                # EMIT the list of names
                self.namesSignal.emit(face_names)
        # Release the video resource. i.e webcam
        self.cap.release()


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


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    window.raise_()
    sys.exit(app.exec_())
