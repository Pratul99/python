import csv
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QDateTimeEdit,
    QLineEdit, QTextEdit, QSpacerItem, QSizePolicy,
    QHBoxLayout, QPushButton, QMessageBox
)
from PyQt6.QtCore import QDateTime
import sys


class ReminderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Reminder")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Event date and time
        self.datetime_label = QLabel("Event date and time: ")
        self.datetime_picker = QDateTimeEdit()
        self.datetime_picker.setDateTime(QDateTime.currentDateTime())
        self.datetime_picker.setCalendarPopup(True)

        layout.addWidget(self.datetime_label)
        layout.addWidget(self.datetime_picker)

        # Email
        self.email_label = QLabel("Email: ")
        self.email_input = QLineEdit("pratulbhatt18@gmail.com")

        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        # Reminder
        self.reminder_label = QLabel("Reminder: ")
        self.reminder_input = QTextEdit()

        layout.addWidget(self.reminder_label)
        layout.addWidget(self.reminder_input)

        # Repeat Interval
        self.repeat_interval_label = QLabel("Repeat Interval: ")
        self.repeat_interval_input = QLineEdit()
        self.repeat_interval_input.setPlaceholderText("e.g., 1d, 2w, 3m")

        layout.addWidget(self.repeat_interval_label)
        layout.addWidget(self.repeat_interval_input)

        # Buttons
        button_layout = QHBoxLayout()
        self.submit_button = QPushButton("Add Reminder")
        self.submit_button.clicked.connect(self.save_reminder)
        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)

        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.close_button)
        layout.addLayout(button_layout)

        # Spacer
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.setLayout(layout)

    def save_reminder(self):
        # Collect user input
        dt = self.datetime_picker.dateTime().toString("yyyy-MM-dd hh:mm")
        date, time = dt.split(" ")

        email = self.email_input.text().strip()
        message = self.reminder_input.toPlainText().strip()
        repeat_interval = self.repeat_interval_input.text().strip()

        # Validate
        if not email or not message:
            QMessageBox.warning(self, "Error", "Email and reminder message cannot be empty!")
            return

        try:
            with open("reminders.csv", "a+", newline="") as file:
                file.seek(0, 2)  # go to end of file
                if file.tell() > 0:  # if file not empty
                    file.seek(file.tell() - 1)  # move back 1 char
                    last_char = file.read(1)
                    if last_char != "\n":  # if no newline at end
                        file.write("\n")   # add one

                writer = csv.DictWriter(file, fieldnames=["date", "time", "email", "message", "repeat_interval"])
                if file.tell() == 0:  # if file was empty (no header)
                    writer.writeheader()

                writer.writerow({
                    "date": date,
                    "time": time,
                    "email": email,
                    "message": message,
                    "repeat_interval": repeat_interval
                })

            QMessageBox.information(self, "Success", "Reminder added successfully!")
            self.reminder_input.clear()
            self.repeat_interval_input.clear()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save reminder: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReminderApp()
    window.show()
    sys.exit(app.exec())