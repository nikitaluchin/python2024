def task_5(string):
    dates = []
    for month in ("января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"):
        while string.find(" " + month + " ") != -1:
            index = string.find(" " + month + " ")

            if string[index-1:index].isnumeric():
                if string[index-2:index].isnumeric() and int(string[index-2:index]) < 32:
                    day = string[index-2:index]
                else:
                    day = string[index-1]
            else:
                string = string[:index] + string[index+1:]
                continue
            if string[index+2+len(month):index+2+len(month)+4].isnumeric() and len(string[index+2+len(month):index+2+len(month)+4]) == 4:
                dates += [day + " " + month + " " + string[index+2+len(month):index+2+len(month)+4]]
                string = string.replace(day + " " + month + " " + string[index+2+len(month):index+2+len(month)+4], "")
            else:
                string = string[:index] + string[index+1:]
                continue
    return dates

print(task_5("Привет. Сегодня 5 января 2047 года. Кто я такой? Зачем я живу? 42 декабря 1918 и кто. 13 марта 198467. 13 февраля 2013. жжж 13 января 1918 жж"))