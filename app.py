import cv2
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from utils import label_frame, qimage_frame, create_encodings, format_frame, recognise_faces
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
        }

        self.current_face = ""
        self.logged_in_employees = []

        # Define the thread for the video feed
        self.videoThread = VideoThread(people=self.employees)
        self.videoThread.frameSignal.connect(self.display_video)
        self.videoThread.start()

        # Connect to the face name updater signal
        self.videoThread.namesSignal.connect(self.update_current_face)

        # Connect to the sign in button
        self.button_signin.clicked.connect(self.sign_in_employee)

        # Connect to the sign in button
        self.button_signout.clicked.connect(self.sign_out_employee)

    def display_video(self, frame):
        self.label_video_feed.setPixmap(QPixmap.fromImage(frame))

    def sign_in_employee(self):
        """Funcion for doing checks and signing in the exployee"""
        employee_names = list(self.employees.keys())

        if self.current_face in employee_names and self.current_face not in self.logged_in_employees:
            self.logged_in_employees.append(self.current_face)

            # Append to the list widget
            self.listwidget_signed_in.clear()
            self.listwidget_signed_in.addItems(self.logged_in_employees)

    def sign_out_employee(self):
        """Function for doing checks and signing out the employee"""
        if self.current_face in self.logged_in_employees:
            self.logged_in_employees.remove(self.current_face)

            # Update the list widget
            self.listwidget_signed_in.clear()
            self.listwidget_signed_in.addItems(self.logged_in_employees)

    def update_current_face(self, list_of_faces):
        """Function to set the name of the current face in the camera view"""
        self.current_face = ""
        if list_of_faces and list_of_faces[0] != "Unknown":
            self.current_face = list_of_faces[0]


class VideoThread(QThread):
    frameSignal = pyqtSignal(QImage)
    namesSignal = pyqtSignal(list)

    def __init__(self, people):
        QThread.__init__(self)
        self.cap = None
        self.people = people
        self.feed = True

    def run(self):
        # Image camera feed capture
        self.cap = cv2.VideoCapture(0)

        # Get the face images from the provided dictionary of faces and names
        faces = []
        names = []

        # Add the face images to a list of faces
        for name, face in self.people.items():
            faces.append(face)
            names.append(name)

        # Create face encodings from the face images
        known_face_encodings = create_encodings(faces)

        # We want to process every other frame
        process_this_frame = True

        # Declare a list for already detected faces, and names
        face_locations = []
        face_names = []

        while self.feed:
            # Capture frame by frame
            ret, mac_frame = self.cap.read()

            # Flip the frame, and crop to 1:1 aspect ratio
            frame = format_frame(mac_frame)

            if ret:  # ret returns true if frame was read correctly, or false

                # Resize the frame by interpolating down, so we have less pixels to parse
                small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

                # Get the RGB grids, and ignore alpha if it is there.
                rgb_small_frame = small_frame[:, :, ::-1]

                if process_this_frame:
                    face_locations, face_names = recognise_faces(known_face_encodings, small_frame, names)

                # We do not process the next frame
                process_this_frame = not process_this_frame

                # Now we want to draw boxes and labels around the faces in the frame
                # For each name in ou
                label_frame(frame, face_locations, face_names)

                # Qt will only read a QImage, so we convert
                frame_image = qimage_frame(frame)

                # EMIT the altered frame
                self.frameSignal.emit(frame_image)

                # EMIT the list of names
                self.namesSignal.emit(face_names)

        # Release the video resource. i.e webcam
        self.cap.release()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    window.raise_()
    sys.exit(app.exec_())
