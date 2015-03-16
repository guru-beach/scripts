wage = 9.32
new_wage = 15
employees = 3
avg_meal = 4
turnover = 20

def main(wage, new_wage, employees, avg_meal, turnover):
  wage_delta = (new_wage - wage)
  increase_per_hour =  (new_wage - wage) * employees
  hour_income = turnover * avg_meal
  new_revenue_target =  hour_income + increase_per_hour
  increase_per_customer =  new_revenue_target/turnover - avg_meal
  pct_increase_customer = increase_per_customer/avg_meal * 100
  
  print "Current Minimum Wage = ${}".format(wage)
  print "New Minimum Wage = ${}".format(new_wage)
  print "Wage difference per hour: ${}".format(wage_delta)
  print "Number of employees = {}".format(employees)
  print "Increased salary cost per hour = ${}".format(increase_per_hour)
  print "Average cost per meal = ${}".format(avg_meal)
  print "Customer turnover per hour = {}".format(turnover)
  print "Curent Hourly Income: ${}".format(hour_income)
  print "New revenue target = ${}".format(new_revenue_target)
  print "Increase per customer = ${}".format(increase_per_customer)
  print "Percentage Increase per customer = %{}".format(pct_increase_customer)


if __name__ == "__main__":
  main(wage, new_wage, employees, avg_meal, turnover)
