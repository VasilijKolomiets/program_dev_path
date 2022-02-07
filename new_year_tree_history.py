"""
Рассказ о лучшем структурировании программы на примере 
задаче рисования новогодней елки


Общая практика такая.
Для модульного подхода.
1. Главная функция состоит исключительно из вызовов других функций. 
2. Каждая функция решает только одну задачу, которую можно описать словами без союзов "И"
3. Размер функции не более двух экранов. Как правило - не более одного экрана
4. Функции решающие вопросы одного типа, группируются в модули.  То есть отдельные файлы. Например:
  а) чтение-запись
  б) получение-отправка
  в) проверка-очистка полученных данных
  г) обработка данных
  д) отображение-визуализация результатов.
5. Название функции начинается с глагола и поясняет, что она собственно собирается делать.

Это так, на примере анализа данных.

MVC - Model View Control для сайтов и иже с ними я упоминал.



03 - empty functions
"""
def input_data_for_nyt():
  ...


def built_segments_nyt():
  def my_fun():
    ...
  ...


def built_root_nyt():
  ...

def place_stars_on_segments_nyt():
  ...

def output_nyt():
  print("Ok!")


if __name__ == "__main__":
    # input data for NYTree
    input_data_for_nyt()
    # built segments in loop for  NYTree 
    built_segments_nyt()
    # stars NYTree
    place_stars_on_segments_nyt()
    # built root NYTree
    built_root_nyt()
    # output NYTree
    output_nyt()
    