money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

month = 0  # количество месяцев без долгов
budget = money_capital + salary  # бюджет в текущем (1-ом) месяце
balance = budget - spend  # остаток в конце 1-го месяца

while spend <= budget:
    month += 1
    budget = balance + salary  # бюджет в начале следующего месяца
    spend *= (increase+1)  # траты в следующем месяце
    balance = budget - spend  # остаток в конце следующего месяца

print("Количество месяцев, которое можно протянуть без долгов:", month)
