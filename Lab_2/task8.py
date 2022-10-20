money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# Оформить решение
def period(money_capital, salary,spend,month = 0,increase = 0.05):
    while money_capital > 0:
        money_capital = money_capital - spend + salary
        salary *= increase
        month += 1
    print(month)
period(money_capital, salary, spend)