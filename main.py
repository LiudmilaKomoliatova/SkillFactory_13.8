# Input
ticket_counter = int(input("Введите количество билетов: "))
ages = [int(input(f"Введите возраст посетителя {value}: ")) for value in range(1, ticket_counter+1)]

# Price rules
prices = {
	18: 0,
	25: 990,
	999: 1390}
discount_count = 3
discount_percent = 10

# Variables
discount = 0
price = 0

# Calculation
for age in ages:
	for i, cnt in prices.items():
		if age <= i:
			price += cnt
			break

if ticket_counter > discount_count:
	discount = price * discount_percent / 100
  price -= discount

ages_str = ",".join(list(map(str, ages)))

# Output
print("Всего билетов {0} (возраст участников: {1})".format(ticket_counter, ages_str))
if discount > 0:
	print("Сумма к оплате (включая скидку {0}% - {1} руб.): {2} руб.".format(discount_percent, discount, price))
else:
	print("Сумма к оплате: {0} руб.".format(price))
