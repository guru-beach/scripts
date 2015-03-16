# Calculate the increase per customer if all wage increases are passed on

# Current minimum wage
wage = 9.32
# New minimum wage
new_wage = 15
# Employees working
employees = 3
# Average price per transaction
# Units are monetary (e.g. $)
avg_price = 4
# Customers per hour
customers_per_hour = 20
# Additional support manhours per day
# This adds in downstream cost for services provided by outside vendors
downstream_manhours_per_day = 5
operating_hours = 8

def wage_increase(wage, new_wage, employees, avg_price, customers_per_hour, downstream_manhours_per_day, operating_hours):
  wage_delta = float(new_wage - wage)
  downstream_manhours_per_hour = float(downstream_manhours_per_day)/float(operating_hours)
  internal_increase_per_hour = float(wage_delta * employees)
  downstream_increase_per_hour = float(wage_delta * downstream_manhours_per_hour)
  increase_per_hour = float(internal_increase_per_hour + downstream_increase_per_hour)
  hourly_income = customers_per_hour * avg_price
  hourly_income_target =  hourly_income + increase_per_hour
  increase_per_customer =  (hourly_income_target/customers_per_hour) - avg_price
  pct_increase_customer = (increase_per_customer/avg_price) * 100
  
  print "Current Minimum Wage               = ${}".format(wage)
  print "New Minimum Wage                   = ${}".format(new_wage)
  print "Wage difference per hour           = ${}".format(wage_delta)
  print "Number of employees                = {}".format(employees)
  print "Additional downstream manhours     = {}".format(downstream_manhours_per_day)
  print "Downstream wage cost per hour      = ${:03.2f}".format(downstream_increase_per_hour)
  print "Total Increased wage cost per hour = ${:03.2f}".format(increase_per_hour)
  print "Average price per transaction      = ${}".format(avg_price)
  print "Customers per hour                 = {}".format(customers_per_hour)
  print "Curent Hourly Income               = ${}".format(hourly_income)
  print "New revenue target                 = ${:03.2f}".format(hourly_income_target)
  print "Increase per customer              = ${:03.2f}".format(increase_per_customer)
  print "Percentage Increase per customer   = %{:03.2f}".format(pct_increase_customer)


if __name__ == "__main__":
  wage_increase(wage, new_wage, employees, avg_price, customers_per_hour, downstream_manhours_per_day, operating_hours)
