# Virtual Mouse Controller

A Python script that allows you to control your computer's mouse cursor using real-time hand tracking and gestures. This project leverages OpenCV for video capture, MediaPipe for hand landmark detection, and PyAutoGUI to execute mouse movements and clicks natively on your operating system.


##  Features
* **Cursor Movement:** Accurately moves the mouse cursor by tracking the center of your palm.
* **Pinch-to-Click:** Performs a left mouse click when the distance between your index finger tip and thumb tip falls below a specific threshold.
* **Stabilization:** Implements a customizable "dead zone" to prevent jittery, unintended cursor movements when your hand is relatively still.

##  Prerequisites
* Python 3.x
* A working webcam

##  Installation

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/Karun2codes/Virtual-Mouse-Controller.git](https://github.com/Karun2codes/Virtual-Mouse-Controller.git)
   cd Virtual-Mouse-Controller
