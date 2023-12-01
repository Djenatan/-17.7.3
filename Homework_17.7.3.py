per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Enter the amount of money you plan to deposit: "))
deposit = [money * rate / 100 for rate in per_cent.values()]
max_deposit = max(deposit)
print(f"The maximum deposit value is: {max_deposit}")