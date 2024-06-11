import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from interface import Ui_MainWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from database import *
from errors_pushes import *


class TourCity(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.mode = 'view'

        self.saved_index = 0
        self.num_title = 0
        self.num_info = 1
        self.num_image = 2

    def initUI(self):
        # Инизиализируем и настраиваем интерфейс
        self.setupUi(self)
        self.setFixedSize(998, 661)
        self.setWindowTitle('TourCity')

        background = QPixmap('D:/Qt_project/images/icons/map.png')
        self.background.setScaledContents(True)
        self.background.setPixmap(background)

        # Подключаем события нажатия на кнопку к обработчику
        self.searchButton.clicked.connect(lambda: self.reset_nums())
        self.searchButton.clicked.connect(self.update_display)
        self.rightButton.clicked.connect(self.righButton_clicked)
        self.leftButton.clicked.connect(self.leftButton_clicked)
        self.saveButton.clicked.connect(self.saveButton_clicked)
        self.menuButton.clicked.connect(self.menu_button_clicked)
        self.savedButton.clicked.connect(self.saved_button_clicked)
        self.infoButton.clicked.connect(self.pushInfo_clicked)
        self.clearButton.clicked.connect(self.clear_display)

    def update_display(self):
        # Проверка в каком режиме находиться пользователь и вызов соответствующей функции
        if self.mode == 'view':
            self.update_view_display()

        elif self.mode == 'saved':
            self.update_saved_display()

    def update_view_display(self):
        # Получаем информацию из БД и меняем ее в просмотриваемом режиме. Если города нет вызываем ошибку
        city = self.searchLineEdit.text().capitalize()

        self.cities = get_cityinfo(city)

        try:
            self.headertextLabel.setText(self.cities[self.num_title])

            self.aboutLabel.setWordWrap(True)
            self.aboutLabel.setText(self.cities[self.num_info])

            image = QImage.fromData(self.cities[self.num_image])
            pixmap = QPixmap.fromImage(image)
            self.imageLabel.setPixmap(pixmap)
            self.imageLabel.setScaledContents(True)

        except TypeError:
            return city_not_finded()

    def update_saved_display(self):
        try:
            # Функция для обновления дисплея в сохраненном режиме, если город не найден срабатывает блок except
            self.saved_cities = get_saved_places()

            self.saved_city = self.saved_cities[self.saved_index]

            title = self.saved_city[0]
            info = self.saved_city[1]
            image = self.saved_city[2]

            self.headertextLabel.setText(title)
            self.aboutLabel.setWordWrap(True)
            self.aboutLabel.setText(info)

            image = QImage.fromData(image)
            pixmap = QPixmap.fromImage(image)
            self.imageLabel.setPixmap(pixmap)
            self.imageLabel.setScaledContents(True)
        except TypeError:
            error_saved_UI()

    def keyPressEvent(self, event):
        # Даннаяет дисплей функция реагирует на нажатие кнопки Enter. И в ней же вызывает функцию для обновления дисплея
        if event.key() == Qt.Key_Return:
            self.reset_nums()
            self.update_display()

    def righButton_clicked(self):
        # Обработка события нажатия на кнопку "Вправо": если режим 'saved', вызывается сохраненная функция 
        # если num_title больше или равен 6, вызывается обработчик ошибки
        # в противном случае увеличиваются счетчики и обновляется отображение
        if self.mode == 'saved':
            return self.saved_rightButton()
        if self.num_title >= 6:
            return page_end_error()
        self.num_title += 3
        self.num_info += 3
        self.num_image += 3
        self.update_display()

    def leftButton_clicked(self):
        # Если пользовательно находится в сохран-ом режиме вызываем соответствующую функцию.
        # Иначе проверяем вышел ли пользователь за рамки страницы
        if self.mode == 'saved':
            return self.saved_leftButton()
        if self.num_title <= 0:
            return begin_page_error()
        self.num_title -= 3
        self.num_info -= 3
        self.num_image -= 3
        self.update_display()

    def saved_rightButton(self):
        # Проверка на то подошел ли пользователь к концу, если нет показываем следующее место - (в сохран-ом режиме)
        if self.saved_index >= len(self.saved_cities) - 1:
            return page_end_error()
        self.saved_index += 1
        self.update_saved_display()

    def saved_leftButton(self):
        # Проверка на то, вышел ли пользователь за рамки. Если нет показываем предыдущее место - (в сохран-ом режиме)
        if self.saved_index <= 0:
            return begin_page_error()
        self.saved_index -= 1
        self.update_saved_display()
    
    def saveButton_clicked(self):
        # Функция которая добавляет место в БД
        try:
            save_place(self.cities[self.num_title],
                       self.cities[self.num_info], self.cities[self.num_image])
        except Exception:
            error_when_saved()

    def menu_button_clicked(self):
        # Функция для переключения режима в 'view'
        push_when_go_to_menu()
        self.clear_display()
        self.mode = 'view'
        self.saveButton.setEnabled(True)

    def saved_button_clicked(self):
        # Функция для переключения режима в 'saved' и обновляет дисплей - (показывает сохраненные места)
        push_when_go_to_saved()
        self.clear_display()
        self.mode = 'saved'
        self.saveButton.setEnabled(False)
        self.update_display()
    
    def reset_nums(self):
        # Функция для сброса индексов
        self.num_title = 0
        self.num_info = 1
        self.num_image = 2
        self.saved_index = 0

    def clear_display(self):
        # Функция для очистки дисплея
        self.mode = 'view'
        self.headertextLabel.clear()
        self.aboutLabel.clear()
        self.searchLineEdit.clear()
        self.imageLabel.clear()

    def pushInfo_clicked(self):
        # Фунция которая срабатывает на нажатие кнопку "информация о проекте"
        push_info()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('D:\Qt_project\images\icons\icon.png'))
    ex = TourCity()
    ex.setWindowIcon(QtGui.QIcon('D:\Qt_project\images\icons\icon.png'))
    ex.show()
    push_info()
    sys.exit(app.exec())