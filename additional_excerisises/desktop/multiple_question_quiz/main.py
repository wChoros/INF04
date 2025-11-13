from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys

class Question():
    def __init__(self, image_path: str, question: str, answers: list[str], correct_answer_index: int):
        if len(answers) != 4:
            raise ValueError("there should be 4 answers")
        if not (0 <= correct_answer_index < 4):
            raise ValueError("correct_answer_index should be in range 0-3")
        self.img_path = image_path
        self.question = question
        self.answers = answers
        self.correct_answer_index = correct_answer_index


questions = [
    Question("./images/6_zer.jpg", "Ile zer chce mieć taco z ,,Umowy o dzieło\"?", ["4", "5", "6", "7"], 2),
    Question("./images/marmur.jpg", "Gdzie znajduje się hotel Marmur?", ["Bieszczady", "Złotoryje", "Kamionki", "Sopot"], 3),
    Question("./images/pocztowka.jpg", "Co robi Taco Hemingway w piątki?", ["Dłubie w nosie", "Wysyła pocztówki", "Leży w wannie", "Gotuje"], 2),
    Question("./images/szlugi_kalafiory.jpg", "Co otwiera główny bohater Trójkąta warszawskiego w rozmowie ze śmiercią\"?", ["Neseser", "Pudełko z mielonym mięsem", "Portfel", "Lodówkę"], 0),
    Question("./images/young_hems.jpg", "Jak nazywa się pierwszy mixtape Taco Hemingwaya?", ["Young Hems", "Trójkąt warszawski", "Umowa o dzieło", "Szprycer"], 0),
    Question("./images/taco.jpg", "Jak nazywa się kultowa przeróbka autorstwa Filipa Szcześniaka z 2009 roku?", ["Kaczyński sam w domu", "Hitler w poszukiwaniu elektro", "Kuce z Mokotowa", "Napad na kebaba"], 1),
    Question("./images/mix_salat.jpg", "Kto jest na feacie u Taco w piosence ,,Mix Sałat\"?", ["Grzegorz Turnau", "Schafter", "Daria Zawiałow", "Oki"], 2),
    Question("./images/taconafide.jpg", "Dlaczego z Quebo już koniec przyjaźni?", ["Bo ma za dużo dziar", "Bo śpiewa pop", "Bo chleje", "Bo to kurwa"], 3),
]


class MainWindow(QMainWindow):
    def load_curr_question(self):
        for i, button in enumerate(self.buttons):
            button.setText(questions[self.curr_question].answers[i])
        self.question_label.setText(questions[self.curr_question].question)
        self.img_label.setPixmap(QPixmap(questions[self.curr_question].img_path))


    def finish_game(self):
        score = round((self.correct_answers / (len(questions))) * 100, 2)
        text = ""
        if score<50:
            text = "Jesteś jebaną sezonówą, wypierdalaj"
        elif score<75:
            text = "Średnio cwelku, musisz się jeszcze troche podszkolic"
        elif score<95:
            text = "Jesteś lepszy niz wiekszosc sezonówek, ale mozesz się jeszcze poprawić"
        else:
            text = "Mega sigiemka, widać ze OG fan taco!"

        dialog = QMessageBox()
        dialog.setStyleSheet("font-size: 20px;")
        dialog.setText(text + f"\nTwój wynik to: {self.correct_answers}/{len(questions)}. Czyli {score}%")
        dialog.exec()

        self.curr_question = 0
        self.correct_answers = 0
        self.load_curr_question()



    def go_to_next_question(self, answer):
        self.correct_answers += 1 if answer == questions[self.curr_question].correct_answer_index else 0
        print(answer == questions[self.curr_question].correct_answer_index)
        if self.curr_question == len(questions) - 1:
            self.finish_game()
        else:
            self.curr_question += 1
            self.load_curr_question()


        

    def init_ui(self):
        self.setStyleSheet("""
QMainWindow{
    background-color: #2e3440;
}
QLabel{
    font-size: 25px;
    color: #eceff4;
}
QPushButton {
    background-color: #eceff4;
    color: #2e3440;
    font-size: 15px;
}
""")
        self.setGeometry(50,50, 1000, 600)
        self.img_label = QLabel(self)
        self.img_label.setGeometry(250, 10, 500, 200)
        self.img_label.setPixmap(QPixmap("./images/main.png"))
        self.img_label.setScaledContents(True)

        self.question_label = QLabel("Question", self)
        self.question_label.setGeometry(0, 175, 1000, 200)
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buttons: list[QPushButton] = []

        for i in range(2):
            for j in range(2):    
                self.buttons.append(QPushButton(f"button_{2*i+j + 1}", self))
                self.buttons[-1].setGeometry(j * 500 + 100 ,i * 110 + 350, 300, 100)
                self.buttons[-1].clicked.connect(lambda _, index=(2*i+j) : self.go_to_next_question(index))

        self.load_curr_question()



    def __init__(self):
        super().__init__()
        self.curr_question = 0
        self.correct_answers = 0
        self.init_ui()



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())