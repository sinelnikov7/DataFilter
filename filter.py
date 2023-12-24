from tkinter import Tk, NSEW
from tkinter import ttk
from tkinter import filedialog

from service import ListString, Filter, SaveText


root = Tk()
root.title("FilterSet")
root.geometry("250x200")
list_string_ru = None
list_string_en = None


def open_file(lang):
    """Открытие файла и создание списка строк"""
    global list_string_ru
    global list_string_en
    filepath = filedialog.askopenfilename()
    if filepath != '':
        file = ListString(filepath)
        if lang == 'ru':
            list_string_ru = file.get_list()
        if lang == 'en':
            list_string_en = file.get_list()
    if (list_string_ru and list_string_en) != None:
        filter_button.configure(state='active')


def filter_text():
    """Фильтр англ и руского текста и сохранение в файлы"""
    filter = Filter(list_string_ru, list_string_en)
    feltered_lists = filter.filter_text()
    text_ru = SaveText(feltered_lists[0], 'Результат фильтрации(русский текст).txt')
    text_ru.text_save()
    text_en = SaveText(feltered_lists[1], 'Результат фильтрации(английский текст).txt')
    text_en.text_save()
    root.destroy()


open_button_ru = ttk.Button(text="Выбрать русский текст", command=lambda: open_file('ru'))
open_button_ru.grid(column=0, row=1, sticky=NSEW, padx=10)
open_button_en = ttk.Button(text="Выбрать английский текст", command=lambda: open_file('en'))
open_button_en.grid(column=0, row=2, sticky=NSEW, padx=10)
filter_button = ttk.Button(text="Фильтровать", command=filter_text, state='disabled')
filter_button.grid(column=0, row=3, sticky=NSEW, padx=10)
root.mainloop()
