import itertools


class ListString:

    def __init__(self, path):
        self.path = path

    def get_list(self):
        """Получение списка строк из файла"""
        with open(self.path, 'r', encoding='utf-8') as text:
            full_string = text.read().split('\n')
        return full_string


class Filter:

    def __init__(self, ru, en):
        self.ru = ru
        self.en = en
        self.new_text_ru = []
        self.new_text_en = []

    def filter_text(self):
        """Фильтрация списков"""
        for (r, e) in zip(self.ru, self.en):
            if len(r.split()) <= 10 and len(e.split()) <= 10:
                self.new_text_ru.append(r)
                self.new_text_en.append(e)
        return [self.new_text_ru, self.new_text_en]


class SaveText:

    def __init__(self, list_text, name):
        self.list_text = list_text
        self.name = name

    def text_save(self):
        """Сохранение в файл"""
        with open(self.name, 'w', encoding='utf-8') as file:
            for line in self.list_text:
                file.write(line + '\n')
