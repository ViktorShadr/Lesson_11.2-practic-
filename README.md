# Lesson_11.2-practic-
## Задачи

Создайте декоратор 
@positive_integers
, который проверяет, что все аргументы функции — положительные целые числа. Если аргумент — неположительное число, выбрасывается исключение ValueError с сообщением 
All arguments must be positive integers.

**Пример использования:**
```
@positive_integers
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

multiply(2, 3, 4) # Вывод: 24
multiply(2, 0, 4) # Выбрасывает исключение ValueError с сообщением "All arguments must be positive integers"
```


Создайте декоратор 
@is_palindrome
, который проверяет, что аргумент функции является палиндромом (строкой, которая читается одинаково слева направо и справа налево). Если аргумент не является палиндромом, выбрасывается исключение ValueError с сообщением 
Argument must be a palindrome
.
Пример использования:
```
@is_palindrome
def reverse_string(string):
    return string[::-1]

reverse_string('racecar') # "racecar"
reverse_string('Racecar') # "racecaR"
reverse_string('hello') # Выбрасывает исключение ValueError с сообщением "Argument must be a palindrome"
```

Создайте декоратор 
@logging
, который будет логировать вызовы функции и ее результат. Лог должен выводиться на экран.
Пример вывода:
```commandline
@logging
def multiply(x, y):
    return x * y
multiply(2, 3) 
>>> Function multiply called with args: (2, 3) and kwargs: {}. Result: 6
```