import cv2
import mediapipe as mp
import time
from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import messagebox


# ---------- TRACKERS ----------

class Tracker(ABC):

    @abstractmethod
    def get_data(self):
        pass


class EyeTracker(Tracker):

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.mp_face = mp.solutions.face_mesh
        self.face_mesh = self.mp_face.FaceMesh()

    def get_data(self):

        ret, frame = self.cap.read()
        if not ret:
            return None

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                eye = face_landmarks.landmark[159]
                return eye.y

        return None


# ---------- DETECTORS ----------

class Detector(ABC):

    @abstractmethod
    def check(self, data):
        pass


class DoomscrollDetector(Detector):

    def __init__(self):
        self.start_time = time.time()

    def check(self, eye_position):

        if eye_position is None:
            return False

        time_spent = time.time() - self.start_time

        if eye_position > 0.6 and time_spent > 20:
            return True

        return False


class BlinkDetector(Detector):

    def __init__(self):
        self.blink_count = 0

    def check(self, eye_position):

        if eye_position is None:
            return False

        if eye_position < 0.3:
            self.blink_count += 1

        if self.blink_count < 2:
            return True

        return False


class AttentionDetector(Detector):

    def __init__(self):
        self.focus_time = time.time()

    def check(self, eye_position):

        if eye_position is None:
            return False

        if eye_position > 0.5:
            if time.time() - self.focus_time > 15:
                return True
        else:
            self.focus_time = time.time()

        return False


# ---------- ALERTS ----------

class Alert(ABC):

    @abstractmethod
    def show(self):
        pass


class PopupAlert(Alert):

    def show(self):

        root = tk.Tk()
        root.withdraw()

        messagebox.showwarning(
            "Doomscroll Warning",
            "⚠️ Možná doomscrolluješ.\nDej si pauzu."
        )


class ConsoleAlert(Alert):

    def show(self):
        print("⚠️ Doomscrolling detected. Take a break.")


# ---------- MAIN APP ----------

class App:

    def __init__(self):

        self.tracker = EyeTracker()

        self.detectors = [
            DoomscrollDetector(),
            BlinkDetector(),
            AttentionDetector()
        ]

        self.alert = PopupAlert()

    def run(self):

        while True:

            data = self.tracker.get_data()

            for detector in self.detectors:

                if detector.check(data):
                    self.alert.show()
                    return


app = App()
app.run()