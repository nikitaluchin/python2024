# https://www.programiz.com/python-programming/regex
from re import match

def check_URL(URL):
    # один \ - экранирование Python, второй \ и символ s (т.е. \\s) - экранирование спецсимвола regexp s ($, ^, и т.д.) ИЛИ
    # ИЛИ \\b - особое выражение, напр-р: \b - Matches if the specified characters are at the beginning or end of a word.

    # ^ - присутствие в начале, $ - присутствие в конце
    # () - группа, | - или
    # [] - множество
    # \\+ - экранировали спецсимвол '+'
    # [-a-zA-Z0-9@:%._\\+~#?&/=] повторяется от 2 до 256 раз
    # \\. - экранировали спецсимвол '.'
    # .[a-z] от 2 до 6 раз
    # \b - граница слова
    # [-a-zA-Z0-9@:%._\\+~#?&/=] 0 или более раз (параметры) (обернули в (), чтобы * применялась именно к [-a-zA-Z0-9@:%._\\+~#?&/=])

    regexp = "^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&/=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&/=]*)$"
    # если первая группа не совпадает с исходной строкой, то регулярка не прошла
    if not match(regexp, URL):
        return False
    if match(regexp, URL).group(0) != URL:
        return False
    return True

def test_func(URL):
    if not check_URL(URL):
        raise Exception("AAAAAAAAAAAAAAAAAAA")
    return URL


print(test_func("https://www.something.com/"))
print(test_func("http://www.something.com/"))
print(test_func("https://www.something.edu.co.in"))
print(test_func("http://www.url-with-path.com/path"))
print(test_func("https://www.url-with-querystring.com/?url=has-querystring"))
print(test_func("http://url-without-www-subdomain.com/"))
print(test_func("https://mail.google.com"))
try:
    print(test_func("httRp://www.url-with-path.com/path"))
except Exception as e:
    print(e)
try:
    print(test_func("httrp://www.url-with-path.com/path\\vjv"))
except Exception as e:
    print(e)