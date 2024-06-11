import sqlite3
from PyQt5.QtWidgets import QMessageBox
from errors_pushes import push_when_saved, push_when_delete


def get_cityinfo(city):
    # Делаем запрос к БД и полученную информацию и возвращаем переменные
    with sqlite3.connect('Cities.db') as db:
        cursor = db.cursor()

        result = cursor.execute(
            'SELECT * FROM Cities WHERE city =?', (city,)).fetchone()

        if result is None:
            return

        title1 = result[2]
        info1 = result[3]
        image1 = result[4]

        title2 = result[5]
        info2 = result[6]
        image2 = result[7]

        title3 = result[8]
        info3 = result[9]
        image3 = result[10]

    return title1, info1, image1, title2, info2, image2, title3, info3, image3


def get_saved_places():
    # Получаем информацию из сохраненных мест пользователем
    with sqlite3.connect('SavedCities.db') as db:
        cursor = db.cursor()

        result = cursor.execute(
            'SELECT title, info, image FROM SavedCities').fetchall()

        if result is None:
            return
        return result


def show_warning_dialog(title):
    # Если место уже присутсвует спрашиваем у пользователя удаляем или нет, если да, то вызываем функцию
    # для удаления места из БД
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText(
        'Такая достопримечательность уже присутсвует в сохраненных. Хотите удалить?')

    yes_button = msg_box.addButton('Да', QMessageBox.YesRole)
    no_button = msg_box.addButton('Нет', QMessageBox.NoRole)

    msg_box.exec()

    if msg_box.clickedButton() == yes_button:
        delete_from_saved(title)


def delete_from_saved(title):
    # Удаляем место по названию
    with sqlite3.connect('SavedCities.db') as db:
        cursor = db.cursor()

        cursor.execute('DELETE FROM SavedCities WHERE title = ?', (title,))

        push_when_delete()


def save_place(title, info, image_bytes):
    # Функция которая проверяет есть ли место уже в БД. Если да,
    # то вызываем уведомление хотим мы удалить или нет. Иначе добавляем место в БД
    with sqlite3.connect('SavedCities.db') as db:
        cursor = db.cursor()

        result = cursor.execute(
            'SELECT * FROM SavedCities WHERE title = ?', (title,)).fetchone()

        if result:
            show_warning_dialog(title)
        else:
            cursor.execute(
                'INSERT INTO SavedCities(title, info, image) VALUES (?, ?, ?)', (title, info, image_bytes))
            push_when_saved()