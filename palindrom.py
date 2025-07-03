def is_palindrome(func):
    def wrapper(*args):
        result = func(*args)
        result = result.lower()
        if result != result[:: -1]:
            raise ValueError("Argument must be a palindrome")
        return func(*args)
    return wrapper


@is_palindrome
def reverse_string(string):
    return string[::-1]

print(reverse_string('racecar')) # "racecar"
print(reverse_string('Racecar')) # "racecaR"
print(reverse_string('hello')) # Выбрасывает исключение ValueError с сообщением "Argument must be a palindrome"