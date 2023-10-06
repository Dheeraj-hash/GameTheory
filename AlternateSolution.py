from pulp import *

# Create a linear programming problem
prob = LpProblem("RepeatedGame", LpMaximize)

# Define the strategies and their probabilities as variables
p_cc = LpVariable("p_cc", lowBound=0, upBound=1)  # Probability of playing CC
p_cd = LpVariable("p_cd", lowBound=0, upBound=1)  # Probability of playing CD
p_dc = LpVariable("p_dc", lowBound=0, upBound=1)  # Probability of playing DC
p_dd = LpVariable("p_dd", lowBound=0, upBound=1)  # Probability of playing DD

# Objective function: maximize the expected payoff
prob += 3 * (p_cc + p_dc) + 1 * (p_cd + p_dd), "ExpectedPayoff"

# Constraints ensuring probabilities sum up to 1
prob += p_cc + p_cd == 1, "SumConstraint1"
prob += p_dc + p_dd == 1, "SumConstraint2"

# Constraints ensuring optimal responses to opponents' strategies
prob += 5 * p_cd + 2 * p_dd <= 3 * (p_cc + p_dc), "OptimalResponseC"
prob += 5 * p_dc + 2 * p_dd <= 3 * (p_cc + p_cd), "OptimalResponseD"

# Solve the linear programming problem
prob.solve()

# Output the results
print("Status:", LpStatus[prob.status])
print("Optimal Strategies:")
print("Probability of playing CC:", value(p_cc))
print("Probability of playing CD:", value(p_cd))
print("Probability of playing DC:", value(p_dc))
print("Probability of playing DD:", value(p_dd))

