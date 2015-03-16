# Calculate the increase per customer if all wage increases are passed on

# Current minimum wage
wage = 9.32
# New minimum wage
new_wage = 15
# Employees working
employees = 10
# Average price transaction
avg_price = 40
# Customers per hour
turnover = 20

def wage_increase(wage, new_wage, employees, avg_price, turnover):
  wage_delta = (new_wage - wage)
  increase_per_hour =  (new_wage - wage) * employees
  hour_income = turnover * avg_price
  new_revenue_target =  hour_income + increase_per_hour
  increase_per_customer =  new_revenue_target/turnover - avg_price
  pct_increase_customer = increase_per_customer/avg_price * 100
  
  print "Current Minimum Wage = ${}".format(wage)
  print "New Minimum Wage = ${}".format(new_wage)
  print "Wage difference per hour: ${}".format(wage_delta)
  print "Number of employees = {}".format(employees)
  print "Total Increased wage cost per hour = ${}".format(increase_per_hour)
  print "Average price per transaction = ${}".format(avg_price)
  print "Customers per hour = {}".format(turnover)
  print "Curent Hourly Income: ${}".format(hour_income)
  print "New revenue target = ${}".format(new_revenue_target)
  print "Increase per customer = ${}".format(increase_per_customer)
  print "Percentage Increase per customer = %{}".format(pct_increase_customer)


if __name__ == "__main__":
  wage_increase(wage, new_wage, employees, avg_price, turnover)
