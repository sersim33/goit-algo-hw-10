import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Product", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # Кількість лимонаду
B = pulp.LpVariable('B', lowBound=0, cat='Integer')  # Кількість Фруктового соку


# Функція цілі (Максимізація продукту)
model += A + B, "Total"

# Додавання обмежень
model +=  2 * A + 1 * B <= 100  # Обмеження для води
model +=  1 * A <= 50  # Обмеження для цукру
model +=  1 * A  <= 30  # Обмеження для лимоного соку
model +=  2 * B <= 40  # Обмеження для фруктового пюре

# Розв'язання моделі
model.solve()

# for variable in model.variables():
#     print(f"{variable.name} = {variable.varValue}")

# # Вартість цільової функції
# print(f"Total cost = {pulp.value(model.objective)}")

print(pulp.LpStatus[model.status])

# Вивід результатів
print("Кількість для лимонаду:", A.varValue)
print("Кількість для фруктового соку:", B.varValue)
print("Максимальна можлива загальна кількість вироблених продуктів:", A.varValue + B.varValue)