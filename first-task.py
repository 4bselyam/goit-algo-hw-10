from pulp import *

limonad = LpVariable("Limonad_units", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_juice_units", lowBound=0, cat="Integer")

prob = LpProblem("Production Optimization", LpMaximize)

prob += limonad + fruit_juice, "Total Products"

prob += 2 * limonad + fruit_juice <= 100, "Water"
prob += limonad + fruit_juice <= 50, "Sugar"
prob += limonad <= 30, "Lemon juice"
prob += 2 * fruit_juice <= 40, "Fruit puree"

prob += 2 * limonad + fruit_juice <= 100
prob += limonad + fruit_juice <= 50
prob += limonad <= 30
prob += 2 * fruit_juice + limonad <= 40

prob.solve()

print("Optimization Result:")
for v in prob.variables():
    print(v.name, "=", v.varValue)

print("Total Production =", value(prob.objective))
