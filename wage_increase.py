# Calculate the increase per customer if all wage increases are passed on

# Current minimum wage
wage = 9.32
# New minimum wage
new_wage = 15
# Employees working
employees = 20
# Average price per transaction
# Units are monetary (e.g. $)
avg_price = 40
# Customers per hour
customers_per_hour = 20

def wage_increase(wage, new_wage, employees, avg_price, customers_per_hour):
  wage_delta = (new_wage - wage)
  increase_per_hour =  (new_wage - wage) * employees
  hourly_income = customers_per_hour * avg_price
  hourly_income_target =  hourly_income + increase_per_hour
  increase_per_customer =  (hourly_income_target/customers_per_hour) - avg_price
  pct_increase_customer = (increase_per_customer/avg_price) * 100
  
  print "Current Minimum Wage               = ${}".format(wage)
  print "New Minimum Wage                   = ${}".format(new_wage)
  print "Wage difference per hour           = ${}".format(wage_delta)
  print "Number of employees                = {}".format(employees)
  print "Total Increased wage cost per hour = ${}".format(increase_per_hour)
  print "Average price per transaction      = ${}".format(avg_price)
  print "Customers per hour                 = {}".format(customers_per_hour)
  print "Curent Hourly Income               = ${}".format(hourly_income)
  print "New revenue target                 = ${}".format(hourly_income_target)
  print "Increase per customer              = ${}".format(increase_per_customer)
  print "Percentage Increase per customer   = %{}".format(pct_increase_customer)


if __name__ == "__main__":
  wage_increase(wage, new_wage, employees, avg_price, customers_per_hour)
