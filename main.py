import string
import random

long = True
while long:
    pass_length = int(input('Довжина паролю від 4 символів: '))
    if pass_length >= 4:
        long = False

pass_letters = input('Включити цифри? [y/N]: ').strip().lower()
pass_letters_bool = pass_letters == 'yes' or pass_letters == 'y'

pass_punctuation = input('Включити спеціальні символи? [y/N]: ').strip().lower()
pass_punctuation_bool = pass_punctuation == 'yes' or pass_punctuation == 'y'

def make_pass(length = 8, letters = False, punctuation = False):
    if not letters and not punctuation:
        my_password = ''.join(random.choices(string.ascii_letters, k=length))
        print('[ Тест ] Генерація паролю без цифр, без спец символів [', not letters, ']')
        return my_password
    elif letters and not punctuation:
        while True:
            my_password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            letters = any(char.isdigit() for char in my_password)
            print('[ Тест ] Перебір згенерованого паролю, щоб був з цифрами [', letters, ']')
            if letters:
                return my_password
    elif punctuation and not letters:
        while True:
            my_password = ''.join(random.choices(string.ascii_letters + string.punctuation, k=length))
            punctuation = any(char in string.punctuation for char in my_password)
            print('[ Тест ] Перебір згенерованого паролю, щоб був з спеціальними символами [', punctuation, ']')
            if punctuation:
                return my_password
    else:
        while True:
            my_password = ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k=length))
            punctuation = any(char in string.punctuation for char in my_password)
            letters = any(char.isdigit() for char in my_password)
            print('[ Тест ] Перебір згенерованого паролю, щоб був з цифрами і з спеціальними символами [', letters, punctuation, ']')
            if punctuation and letters:
                return my_password

print(make_pass(pass_length, pass_letters_bool, pass_punctuation_bool))
