salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# Оформить решение
def money (salary,spend,months,increase = 0.03,need_money = 0):
    for i in range(months):
        if i >= 1:
            spend += spend * increase
        summa = spend - salary
        need_money += summa
    print(round(need_money))

money(salary,spend,months)
