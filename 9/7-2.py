from csv import DictReader
from datetime import datetime


months = {"Январь": 1, "Февраль": 2, "Март": 3, "Апрель": 4, "Май": 5, "Июнь": 6, "Июль": 7, "Август": 8, "Сентябрь": 9, "Октябрь": 10, "Ноябрь": 11, "Декабрь": 12}
f = open("7 - 2.csv", encoding="utf8")
completed = {}
reader = DictReader(f)
for row in reader:
    if row["Фамилия"] == "Среднее по группе":
        break
    try:
        score = float(row["Оценка/100,00"].replace(",", "."))
    except ValueError:
        continue
    date = row["Тест начат"].split()[:-1]
    date += row["Тест начат"].split()[-1].split(":")
    date[1] = months[date[1]]
    date = list(map(int, date))
    currdate = datetime(date[2], date[1], date[0], date[3], date[4])
    # print(currdate)
    # будут записаны только первые попытки
    if row["Фамилия"] + " " + row["Имя"] not in completed or completed[row["Фамилия"] + " " + row["Имя"]][0] > currdate:
        if score >= 60:
            completed[row["Фамилия"] + " " + row["Имя"]] = (currdate, True)
        else:
            completed[row["Фамилия"] + " " + row["Имя"]] = (currdate, False)
completed = [key for key, value in completed.items() if value[1]]
print(len(completed))
print(completed)