from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication,QTableView, QTableWidget, QTableWidgetItem, QLineEdit
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QTransform, QFont
import PyQt5.QtGui
from random import uniform
import json

ap = QApplication([])

auth_window = QWidget()
auth_window.setFixedSize(735, 700)
auth_window.setWindowTitle("вход в 'warehouse control'")
auth_window.setStyleSheet("background-image:url(space_sardelka.jpg)")

line_auth_login = QLineEdit(parent=auth_window)
line_auth_login.setGeometry(100, 45, 259, 25)
fonttt = QFont()
fonttt.setFamily("Papyrus")
fonttt.setPixelSize(30)

line_login = QLabel(parent=auth_window, text="Логин")
line_login.move(14, 45)




line_welcome = QLabel(parent=auth_window, text="Welcome to warehouse control ! ")
line_welcome.move(200, 350)
line_welcome.setFont(fonttt)

line_auth_password = QLineEdit(parent=auth_window)
line_auth_password.setGeometry(100, 70, 259, 25)
line_auth_password.setEchoMode(QLineEdit.Password)

line_password = QLabel(parent=auth_window, text="Пароль")
line_password.move(14, 70)

button_rose = QPushButton()
button_rose.setParent(auth_window)
button_rose.setGeometry(350, 600, 60, 40)
button_rose.setText("Войти")

button_rose.setStyleSheet("color:white")
button_rose.setStyleSheet("background-image:url(background--=-=.jpg)")
line_auth_login.setStyleSheet("background-image:url(background--=-=.jpg)")
line_auth_password.setStyleSheet("background-image:url(background--=-=.jpg)")


line_welcome.setStyleSheet("color:white")
line_password.setStyleSheet("color:white")
line_login.setStyleSheet("color:white")
window = QWidget()

def close_error1():
    modal_error1.hide()

modal_error1 = QWidget()
modal_error1.setFixedSize(200,100)
error_modal_lable1 = QLabel()
error_modal_lable1.setParent(modal_error1)
error_modal_lable1.move(35,10)
modal_window_error_button1 = QPushButton()
modal_window_error_button1.setParent(modal_error1)
modal_window_error_button1.setText("ok")
modal_window_error_button1.move(50,70)
modal_window_error_button1.clicked.connect(close_error1)






modal_error1.setStyleSheet("background-image:url(background--=-=.jpg)")

aut = {"Timur_Khuzin": "861485", "Aidar":"884374", " ":" "}
def show_hide():
    login = line_auth_login.text()
    password = line_auth_password.text()
    if login in aut.keys():
        if password == aut[login]:
            window.show()
            auth_window.hide()
        else:
            error_modal_lable1.setText("Не верный пароль")
            modal_error1.show()
    else:
        error_modal_lable1.setText("Такого логина нет в базе")
        modal_error1.show()

button_rose.clicked.connect(show_hide)



window.setWindowTitle("warehouse control")
window.setFixedSize(735, 700)
window.setStyleSheet("background-image:url(photoshopa.jpg)")
modal_window_add = QWidget()
modal_window_add.setWindowTitle("добавление")
modal_window_add.setFixedSize(400,245)
modal_window_add.setStyleSheet("background-image:url(photoshopa.jpg)")
auth_window.show()
def close_error_modal_add():
    modal_window_error.hide()

modal_window_error = QWidget()
modal_window_error.setFixedSize(200,100)
modal_window_error.setStyleSheet("background-image:url(photoshopa.jpg)")
error_modal_lable = QLabel()
error_modal_lable.setText("Заполните все поля")
error_modal_lable.setParent(modal_window_error)
error_modal_lable.move(35,10)
modal_window_error_button = QPushButton()
modal_window_error_button.setParent(modal_window_error)
modal_window_error_button.setText("ok")
modal_window_error_button.move(50,70)
modal_window_error_button.clicked.connect(close_error_modal_add)
add_line_name = QLineEdit(parent=modal_window_add)
add_line_name.setGeometry(100, 20, 259, 25)

add_line_amount = QLineEdit(parent=modal_window_add)
add_line_amount.setGeometry(100, 45, 259, 25)

add_line_IP = QLineEdit(parent=modal_window_add)
add_line_IP.setGeometry(100, 70, 259, 25)

add_line_sold = QLineEdit(parent=modal_window_add)
add_line_sold.setGeometry(100, 95, 259, 25)

line_name = QLabel(parent=modal_window_add, text="Название")
line_name.move(14, 20)

line_amount = QLabel(parent=modal_window_add, text="Кол-во")
line_amount.move(14, 45)

line_IP = QLabel(parent=modal_window_add, text="ИП")
line_IP.move(14, 70)

line_sold = QLabel(parent=modal_window_add, text="Цена")
line_sold.move(14, 95)

def add():
    name = add_line_name.text()
    amount = add_line_amount.text()
    IP = add_line_IP.text()
    sold = add_line_sold.text()
    rating = uniform(1,5)
    rating = round(rating, 1)
    if add_line_name.text() == ""or add_line_amount.text() == ""or add_line_IP.text() == ""or add_line_sold.text() == "":

        modal_window_error.show()
    else:
        data.append([name, amount, IP, sold, rating])
        with open("data_base.json", "w", encoding='utf-8') as f:
            json.dump(data, f, indent=6)
        num_rows = len(data)
        table_widget.setRowCount(num_rows)
        for row in range(num_rows):
            for col in range(5):
                item = QTableWidgetItem(str(data[row][col]))
                table_widget.setItem(row, col, item)
        add_line_name.setText("")
        add_line_amount.setText("")
        add_line_IP.setText("")
        add_line_sold.setText("")



def delll():
    print(table_widget.currentRow())
    del data[table_widget.currentRow()]
    with open("data_base.json", "w", encoding='utf-8') as f:
        json.dump(data, f, indent=6)
    num_rows = len(data)
    table_widget.setRowCount(num_rows)

    for row in range(num_rows):
        for col in range(5):
            item = QTableWidgetItem(str(data[row][col]))
            table_widget.setItem(row, col, item)
def eidittt():
    with open("data_base.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    print(table_widget.currentRow())
    print(data[table_widget.currentRow()])
    red_line_name.setText(data[table_widget.currentRow()][0])
    red_line_amount.setText(data[table_widget.currentRow()][1])
    red_line_IP.setText(data[table_widget.currentRow()][2])
    red_line_sold.setText(data[table_widget.currentRow()][3])
    red_line_rait.setText(str(data[table_widget.currentRow()][4]))
def editttt_modal():
    name = red_line_name.text()
    amount = red_line_amount.text()
    IP = red_line_IP.text()
    sold = red_line_sold.text()
    rait = red_line_rait.text()
    if name == "" or amount == "" or IP == "" or sold == "" or rait == "":
        modal_window_error.show()
    else:
        data[table_widget.currentRow()] = [name, amount, IP, sold, rait]
        num_rows = len(data)
        with open("data_base.json", "w", encoding="utf-8")as file:
            json.dump(data, file, indent=6)
        for row in range(num_rows):
            for col in range(5):
                item = QTableWidgetItem(str(data[row][col]))
                table_widget.setItem(row, col, item)


modal_window_del = QWidget()
modal_window_del.setWindowTitle("удаление")
modal_window_del.setFixedSize(400,245)
modal_window_del.setStyleSheet("background-image:url(photoshopa.jpg)")
modal_window_del_label = QLabel()
modal_window_del_label.setParent(modal_window_del)
modal_window_del_label.setText("Вы точно хотите удолить товар?")
modal_window_del_label.move(105, 100)
modal_window_redact = QWidget()
modal_window_redact.setWindowTitle("редактирование")
modal_window_redact.setFixedSize(400,245)
modal_window_redact.setStyleSheet("background-image:url(photoshopa.jpg)")
red_line_name = QLineEdit(parent=modal_window_redact)
red_line_name.setGeometry(100, 20, 259, 25)

red_line_amount = QLineEdit(parent=modal_window_redact)
red_line_amount.setGeometry(100, 45, 259, 25)

red_line_IP = QLineEdit(parent=modal_window_redact)
red_line_IP.setGeometry(100, 70, 259, 25)

red_line_sold = QLineEdit(parent=modal_window_redact)
red_line_sold.setGeometry(100, 95, 259, 25)

red_line_rait = QLineEdit(parent=modal_window_redact)
red_line_rait.setGeometry(100, 120, 259, 25)

line_name = QLabel(parent=modal_window_redact, text="Название")
line_name.move(14, 20)

line_amount = QLabel(parent=modal_window_redact, text="Кол-во")
line_amount.move(14, 45)

line_IP = QLabel(parent=modal_window_redact, text="ИП")
line_IP.move(14, 70)

line_sold = QLabel(parent=modal_window_redact, text="Цена")
line_sold.move(14, 95)

line_rait = QLabel(parent=modal_window_redact, text="Рейтинг")
line_rait.move(14, 120)
window.setWindowIcon(QtGui.QIcon('icon_wb.jpg'))
table_widget = QTableWidget()
table_widget.setParent(window)
with open("data_base.json", encoding='utf-8') as f:
    data = json.load(f)


headers = ["название", "в наличии", "ИП", "цена", "рейтинг"]
num_rows = len(data)
num_columns = 5


btn_add = QPushButton()
btn_add.setParent(window)
btn_add.resize(100,73)
btn_add.move(70,600)
btn_add.setText("Добавить")


btn_del = QPushButton()
btn_del.setParent(window)
btn_del.resize(100,73)
btn_del.move(350, 600)
btn_del.setText("Удалить")


btn_redact = QPushButton()
btn_redact.setParent(window)
btn_redact.resize(100,73)
btn_redact.move(610, 600)
btn_redact.setText("Редактировать")
btn_redact.clicked.connect(eidittt)


btn_add.clicked.connect(modal_window_add.show)
btn_del.clicked.connect(modal_window_del.show)
btn_redact.clicked.connect(modal_window_redact.show)


btn_add_modal = QPushButton()
btn_add_modal.setParent(modal_window_add)
btn_add_modal.resize(65,30)
btn_add_modal.move(170,190)
btn_add_modal.setText("добавить")
btn_add_modal.clicked.connect(add)


btn_del_modal_yes = QPushButton()
btn_del_modal_yes.setParent(modal_window_del)
btn_del_modal_yes.resize(90,30)
btn_del_modal_yes.move(100,190)
btn_del_modal_yes.setText("Да, удалить")
btn_del_modal_yes.clicked.connect(delll)
btn_del_modal_yes.clicked.connect(modal_window_del.hide)


btn_del_modal_no = QPushButton()
btn_del_modal_no.setParent(modal_window_del)
btn_del_modal_no.resize(90,30)
btn_del_modal_no.move(200,190)
btn_del_modal_no.setText("Нет")
btn_del_modal_no.clicked.connect(modal_window_del.hide)


btn_redact_modal = QPushButton()
btn_redact_modal.setParent(modal_window_redact)
btn_redact_modal.resize(65,30)
btn_redact_modal.move(170,190)
btn_redact_modal.setText("Редакт")
btn_redact_modal.clicked.connect(editttt_modal)


table_widget.setRowCount(num_rows)
table_widget.setColumnCount(num_columns)
table_widget.setHorizontalHeaderLabels(headers)
table_widget.resize(735,400)
table_widget.setColumnWidth(0,167)
table_widget.setColumnWidth(2, 170)
for row in range(num_rows):
    for col in range(5):
        item = QTableWidgetItem(str(data[row][col]))
        table_widget.setItem(row, col, item)


#window.show()





ap.exec()