import re #импорт модуль re
def insert_words(input_file, output_file, sentence): #функция с 3 аргументами (входной, выходной и предложение с шифром)
    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out: #открытие файлов с кодировкой utf-8, r - чтение, w - запись
        text = f_in.read() #считывает весь текст из файла и присваивает в переменную
        count = 0 #счетчик местоимений
        words = sentence.split() #разбивает предложение на список слов и сохраняет в переменную
        word_index = 0 #инициализирует индекс слов предложения для отслеживания
        result = [] #создает пустой список, в который будут добавляться слова модифицированного текста
        for word in text.split(): #цикл который проходит по каждому слову в тексте, разделяя его пробелами
            if re.match(r'^(я|ты|он|она|оно|мы|они|вы)$', word, re.IGNORECASE): #проверяет каждое слово, яв-ся ли оно местоимением, игнорируя регистр слов
                result.append(word) #добавляет местоимение в список
                count += 1 #увеличивает счетник
                if word_index < len(words): #проверяет не достигнут ли конец списка
                    result.append(words[word_index]) #если не достигнут, добавляет слово в список
                    word_index += 1 #увеличивает индекс на 1 слово, чтобы перейти к следующему слову предложения
            else:
                result.append(word) #если не местоимение,то просто добавляет его в список
        f_out.write(' '.join(result)) #записывает все слова из списка в выходной файл
        print(f"Kol-vo: {count}") #выводит кол-во местоимений

input_file = 'Z:/input.txt' #устанавливает имя входного файла
output_file = 'Z:/output.txt' #устанавливает имя выходного файла
sentence = "я хочу получить пять" #предложение, которое будет использовано для вставки слов

insert_words(input_file, output_file, sentence) #вызов функции
