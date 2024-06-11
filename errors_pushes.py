from PyQt5.QtWidgets import QMessageBox

# Здесь находятся функции для вызова уведомлений и ошибок


def city_not_finded():
    error = QMessageBox()
    error.setWindowTitle('Ошибка')
    error.setIcon(QMessageBox.Warning)
    error.setText('К сожалению такой город не найден!')
    error.exec()


def begin_page_error():
    erorr = QMessageBox()
    erorr.setWindowTitle('Уведомление')
    erorr.setIcon(QMessageBox.Warning)
    erorr.setText('Вы уже находитесь на 1-ой странице')
    erorr.exec()


def page_end_error():
    erorr = QMessageBox()
    erorr.setWindowTitle('Уведомление')
    erorr.setIcon(QMessageBox.Warning)
    erorr.setText('Конец страницы')
    erorr.exec()


def error_when_saved():
    erorr = QMessageBox()
    erorr.setWindowTitle('Ошибка')
    erorr.setIcon(QMessageBox.Warning)
    erorr.setText('Сначала выберите достопримечательность')
    erorr.exec()


def error_saved_UI():
    erorr = QMessageBox()
    erorr.setWindowTitle('Ошибка')
    erorr.setIcon(QMessageBox.Warning)
    erorr.setText('У вас нету сохраненных мест')
    erorr.exec()


def push_when_saved():
    push = QMessageBox()
    push.setWindowTitle('Уведомление')
    push.setIcon(QMessageBox.Information)
    push.setText('Успешно добавлено в сохраненные')
    push.exec()


def push_when_delete():
    push = QMessageBox()
    push.setWindowTitle('Уведомление')
    push.setIcon(QMessageBox.Information)
    push.setText('Удалено из сохраненных')
    push.exec()


def push_when_go_to_saved():
    push = QMessageBox()
    push.setWindowTitle('Уведомление')
    push.setIcon(QMessageBox.Information)
    push.setText('Вы перешли в режим сохраенных мест')
    push.exec()


def push_when_go_to_menu():
    push = QMessageBox()
    push.setWindowTitle('Уведомление')
    push.setIcon(QMessageBox.Information)
    push.setText('Вы перешли в режим для просмотра достопримечательностей')
    push.exec()


def push_info():
    push = QMessageBox()
    push.setWindowTitle('Информация о проекте')
    push.setText('''
        "Tourcity" - это приложение, предназначенное для любознательных путешественников. 
        Просто введите название города, и приложение предоставит вам впечатляющую подборку красивых и уникальных достопримечательностей 
        этого места. Исследуйте города мира и открывайте для себя их культурное наследие, архитектурные шедевры и удивительные места. 
        Путеводитель в ваших руках - "Tour-City" делает путешествия легкими и захватывающими!
    ''')
    push.exec()