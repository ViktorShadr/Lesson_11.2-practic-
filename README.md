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
