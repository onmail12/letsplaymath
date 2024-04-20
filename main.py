import datetime
import random
import sys
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QProgressBar, QMainWindow, \
    QTableWidgetItem, QHeaderView
from menu import Ui_Form


class MainMenu(QWidget, Ui_Form):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.setWindowTitle("Let's Play MATH")
        self.setupUi(self)
        self.btn_quiz_add.clicked.connect(lambda: self.open_quiz("+"))
        self.btn_quiz_subtract.clicked.connect(lambda: self.open_quiz("-"))
        self.btn_quiz_multiply.clicked.connect(lambda: self.open_quiz("*"))
        self.btn_quiz_divide.clicked.connect(lambda: self.open_quiz("/"))

        self.setup_table()

    def setup_table(self):
        self.table_scores.setHorizontalHeaderLabels(["Waktu", "Skor"])
        self.table_scores.verticalHeader().setVisible(False)
        self.table_scores.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table_scores.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.table_scores.setColumnWidth(1, 60)

        with open("scores.json", "r") as file:
            data = json.load(file)

            row = 0
            for item in data:
                time = item.get("time", "")
                score = item.get("score", "")

                self.table_scores.insertRow(row)
                self.table_scores.setItem(row, 0, QTableWidgetItem(time))
                self.table_scores.setItem(row, 1, QTableWidgetItem(str(score)))

                row += 1

    def open_quiz(self, operation):
        self.quiz = MyWidget()
        self.quiz.setup_quiz(operation)
        self.quiz.show()
        self.hide()  # Optionally hide the current window


class MyWidget(QMainWindow):
    def __init__(self):
        self.main_v_layout = None
        self.sound_correct = QSound("audio/correct.wav")
        self.sound_incorrect = QSound("audio/correct.wav")
        self.progress_bar_value = 0
        self.window_width = 972
        self.window_height = 610
        self.user_correct_answers = 0
        self.current_question = 0

    def setup_quiz(self, operation):
        super().__init__()
        self.setWindowTitle(f"Let's Play MATH")
        self.operation = operation
        self.resize(self.window_width, self.window_height)
        self.parentWidget = QtWidgets.QWidget(self)
        self.parentWidget.setGeometry(QtCore.QRect(50, 140, 871, 271))
        self.main_v_layout = QtWidgets.QVBoxLayout(self.parentWidget)
        self.main_v_layout.setContentsMargins(16, 40, 16, 40)
        self.setCentralWidget(self.parentWidget)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 10)
        self.progress_bar.setValue(self.progress_bar_value)
        self.progress_bar.setFormat("0/10")
        self.main_v_layout.addWidget(self.progress_bar)

        self.question_h_layout = QtWidgets.QHBoxLayout()
        self.question_h_layout.setSpacing(16)
        self.main_v_layout.addLayout(self.question_h_layout)

        self.spacer_left = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.spacer_right = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                  QtWidgets.QSizePolicy.Minimum)
        self.question_h_layout.addItem(self.spacer_left)

        self.labelFirstNumber = QtWidgets.QLabel(self.parentWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelFirstNumber.setFont(font)
        self.question_h_layout.addWidget(self.labelFirstNumber)

        self.labelOperation = QtWidgets.QLabel(self.parentWidget)
        self.labelOperation.setFont(font)
        self.question_h_layout.addWidget(self.labelOperation)
        self.labelSecondNumber = QtWidgets.QLabel(self.parentWidget)
        self.labelSecondNumber.setFont(font)
        self.question_h_layout.addWidget(self.labelSecondNumber)

        self.labelEqual = QtWidgets.QLabel(self.parentWidget)
        self.labelEqual.setFont(font)
        self.labelEqual.setText("=")
        self.question_h_layout.addWidget(self.labelEqual)
        self.question_h_layout.addItem(self.spacer_right)

        self.answers_g_layout = QtWidgets.QGridLayout()
        self.answers_g_layout.setSpacing(40)
        self.btn_answer1 = QtWidgets.QPushButton(self.parentWidget)
        self.btn_answer1.setMinimumSize(QtCore.QSize(200, 100))
        self.btn_answer1.setText("btn 1")
        self.btn_answer2 = QtWidgets.QPushButton(self.parentWidget)
        self.btn_answer2.setMinimumSize(QtCore.QSize(200, 100))
        self.btn_answer3 = QtWidgets.QPushButton(self.parentWidget)
        self.btn_answer3.setMinimumSize(QtCore.QSize(200, 100))
        self.btn_answer4 = QtWidgets.QPushButton(self.parentWidget)
        self.btn_answer4.setMinimumSize(QtCore.QSize(200, 100))

        self.btn_answer1.clicked.connect(lambda: self.check_answer(self.btn_answer1.text()))
        self.btn_answer2.clicked.connect(lambda: self.check_answer(self.btn_answer2.text()))
        self.btn_answer3.clicked.connect(lambda: self.check_answer(self.btn_answer3.text()))
        self.btn_answer4.clicked.connect(lambda: self.check_answer(self.btn_answer4.text()))

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.answers_g_layout.addItem(spacerItem2, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.answers_g_layout.addItem(spacerItem3, 0, 0, 1, 1)
        self.main_v_layout.addLayout(self.answers_g_layout)

        self.generate_question()

    def shuffle_buttons(self):
        coordinates = [(0, 2, 1, 1), (1, 1, 1, 1), (0, 1, 1, 1), (1, 2, 1, 1)]
        buttons = [self.btn_answer1, self.btn_answer2, self.btn_answer3, self.btn_answer4]
        random.shuffle(coordinates)

        for button, coordinate in zip(buttons, coordinates):
            self.answers_g_layout.addWidget(button, *coordinate)

    def generate_question(self):
        if self.current_question >= 10:
            self.game_finished()

        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)

        self.labelOperation.setText(self.operation)

        if self.operation == '+':
            correct_answer = first_number + second_number
        elif self.operation == '-':
            correct_answer = first_number - second_number
        elif self.operation == '*':
            correct_answer = first_number * second_number
        elif self.operation == '/':
            first_number = second_number * random.randint(1, 20)
            correct_answer = first_number / second_number
            print(first_number, second_number, correct_answer)

        self.labelFirstNumber.setText(str(first_number))
        self.labelSecondNumber.setText(str(second_number))

        self.correct_answer = correct_answer

        # set buttons text
        incorrect_answers = []
        while len(incorrect_answers) < 3:
            random_answer = random.randint(correct_answer - 10, correct_answer + 10)
            if random_answer != correct_answer and random_answer not in incorrect_answers:
                incorrect_answers.append(random_answer)

        self.btn_answer1.setText(str(correct_answer).replace(".0", ""))
        self.btn_answer2.setText(str(incorrect_answers[0]))
        self.btn_answer3.setText(str(incorrect_answers[1]))
        self.btn_answer4.setText(str(incorrect_answers[2]))

        self.shuffle_buttons()

    def check_answer(self, user_answer):
        user_answer = int(float(user_answer))
        if user_answer == self.correct_answer:
            self.user_correct_answers += 1
            self.progress_bar_value += 1
            self.progress_bar.setValue(self.progress_bar_value)
            self.progress_bar.setFormat(f"{self.progress_bar_value}/10")

            self.sound_correct.play()
            self.current_question += 1
            self.generate_question()
        else:
            pass



    def game_finished(self):
        # save skor ke file json
        data = {
            "time": str(datetime.datetime.now()).split(".")[0],
            "score": self.user_correct_answers
        }

        existing_data = []
        with open("scores.json", "r") as file:
            existing_data = json.load(file)
        existing_data.append(data)

        with open("scores.json", "w") as file:
            json.dump(existing_data, file)

        # menampilkan pesan pop up
        message_box = QtWidgets.QMessageBox()
        message_box.setText("Game selesai")
        message_box.setInformativeText(f"Kamu dapat {self.user_correct_answers} jawaban benar!")
        message_box.setStyleSheet(
            "QLabel{min-width:500 px; font-size: 24px;} QPushButton{ width:250px; font-size: 18px; }")
        message_box.exec()

        # Kembali ke menu awal
        self.main_menu = MainMenu()
        self.main_menu.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainMenu()
    main_window.show()
    sys.exit(app.exec_())
