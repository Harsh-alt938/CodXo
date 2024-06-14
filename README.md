Alarm Clock
This is a simple alarm clock application built using Python and the Tkinter library for the graphical user interface. The application allows users to set an alarm, which will play a sound at the specified time. It also displays a countdown timer until the alarm time and shows the current time and date.

Features
Set an alarm time in 24-hour format.
Displays a countdown timer until the alarm time.
Shows the current time and date.
Plays an alarm sound at the set time.
Allows stopping the alarm sound manually.
Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.x installed on your machine.
The following Python libraries installed:
tkinter
pygame
Pillow
You can install the required libraries using pip:

bash
Copy code
pip install pygame pillow
Installation
Clone this repository:
bash
Copy code
git clone https://github.com/yourusername/alarm-clock.git
Navigate to the project directory:
bash
Copy code
cd alarm-clock
Ensure you have a sound file named sound.wav in the project directory for the alarm sound.

Ensure you have an image file named clock_image.png in the project directory for the UI enhancement.

Usage
Run the following command to start the application:

bash
Copy code
python alarm_clock.py
Code Overview
Here's a brief overview of the main parts of the code:

Libraries: Imports necessary libraries including tkinter, pygame, PIL (Pillow), and standard libraries like datetime and threading.

Global Variables: Initializes global variables and pygame mixer for playing sound.

Functions:

alarm(set_alarm_timer): Checks the current time against the alarm time and plays the alarm sound if they match.
actual_time(): Validates the input time and starts the alarm and countdown in separate threads.
stop_alarm(): Stops the alarm sound.
show_current_time(): Shows the current time and date in a message box.
countdown(set_alarm_timer): Displays the countdown timer until the alarm time.
UI Components: Sets up the main window, labels, entry widgets, and buttons using Tkinter.
