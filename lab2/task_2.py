salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

months_copy = months
money_capital = 0
while (months_copy := months_copy - 1) >= 0:
    money_capital += spend - salary
    spend *= 1 + increase
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
