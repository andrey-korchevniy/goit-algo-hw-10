import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Змінні
# Кількість виробленого лимонаду
lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Continuous')
# Кількість виробленого фруктового соку
fruit_juice = pulp.LpVariable('fruit_juice', lowBound=0, cat='Continuous')

# Функція цілі (Максимізація прибутку)
model += lemonade + fruit_juice, "Total_Production"

# Додавання обмежень
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
model += 1 * lemonade <= 50, "Sugar"
model += 1 * lemonade <= 30, "Lemon_Juice"
model += 2 * fruit_juice <= 40, "Fruit_Puree"

# Розв'язання моделі
model.solve()

# Виведення статусу розв'язання
print(f"Status: {pulp.LpStatus[model.status]}")

# Виведення результатів
print(f"Кількість виробленого лимонаду = {pulp.value(lemonade)}")
print(f"Кількість виробленого фруктового соку = {pulp.value(fruit_juice)}")
print(f"Загальна кількість вироблених продуктів = {pulp.value(model.objective)}")