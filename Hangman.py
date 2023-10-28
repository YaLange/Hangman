import random

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play():

    condition = True
    while condition:
        word_list = ["PYTHON", "JAVA", "CPLUSPLUS", "JAVASCRIPT", "HTML", "CSS"]
        word = random.choice(word_list).upper()     # загадываем слово
        word_copy = word                            # копия для использования в программе
        word_completion = '_' * len(word)           # строка, с символами _ вместо букв
        tries = 6                                   # количество попыток

        print('Давайте играть в угадайку слов!')
        print(display_hangman(tries))
        print(word_completion)

        while tries != 0 and word_completion != word:  # игровой цикл            
            letter_or_word = input('Введите букву или слово целиком''\n').upper() # ввод значения           
            while not letter_or_word.isalpha():  # проверяем что строка только из букв
                letter_or_word = input('Введите букву или слово').upper()

            if len(letter_or_word) > 1:  # если ввели слово               
                if letter_or_word == word:
                    word_completion = word
                    print('Поздравляем, вы угадали слово! Вы победили!')               
                else:
                    tries -= 1
                    print('Количество попыток:', tries)
                    print(display_hangman(tries))
                    print(word_completion)

            elif len(letter_or_word) == 1:  # если ввели букву                                
                if letter_or_word in word:  # если угадали
                    while letter_or_word in word_copy:  # находим все индексы и ставим туда букву                        
                        ind = word_copy.find(letter_or_word) # находим индекс буквы                        
                        word_completion = list(word_completion) # ставим букву вместо _
                        word_completion[ind] = letter_or_word
                        word_completion = ''.join(word_completion)                        
                        word_copy = list(word_copy) # убираем букву из копии для работы цикла
                        word_copy[ind] = '_'
                        word_copy = ''.join(word_copy)                                                
                        print(word_completion)               

                elif letter_or_word not in word:  # если не угадали
                    tries -= 1
                    print('Количество попыток:', tries)
                    print(display_hangman(tries))
                    print(word_completion)

                if tries > 0 and word_completion == word:
                    print('Поздравляем, вы угадали слово! Вы победили!')

        if tries == 0:
            print('Виселица... Словом было:', word)

        restart = input('Желаете сыграть еще раз? Введите: "да" или "нет"''\n')
        while restart != 'да' and restart != "нет":    
            restart = input('Моя твоя не понимать:(''\n''Введите "да" или "нет":''\n').lower() 

        if restart == 'да':
            condition = True
        elif restart == 'нет':
            condition = False
            return 'Спасибо, что играли в угадайку слов. Ещё увидимся!'   

print(play())