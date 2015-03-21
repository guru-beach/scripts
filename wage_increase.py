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
# Additional support manhours per day
# This adds in downstream cost for services provided by outside vendors
downstream_manhours_per_day = 10
operating_hours = 12

# This varies by state
# WA 2014 rate:
unemployment_insurace_rate = 0.02

def wage_increase(wage, new_wage, employees, avg_price, customers_per_hour, downstream_manhours_per_day, operating_hours, unemployment_insurace_rate):
  # These are mostly static values so setting in the function
  social_security_rate = 0.062
  medicare_tax_rate = 0.0145
  wage_delta = float(new_wage - wage)
  # Increased taxes
  tax_delta = (social_security_rate + medicare_tax_rate + unemployment_insurace_rate) * wage_delta
  # How many manhours/hr used for goods and services consumed by the business
  downstream_manhours_per_hour = float(downstream_manhours_per_day)/float(operating_hours)
  # How much more wages affect wage costs
  internal_increase_per_hour = float(wage_delta * employees)
  # Transferred increase of downstream wages
  downstream_increase_per_hour = float(wage_delta * downstream_manhours_per_hour)
  # Total increase across all dimensions
  increase_per_hour = float(internal_increase_per_hour + downstream_increase_per_hour + tax_delta)
  # Average amount of income per hour
  hourly_income = customers_per_hour * avg_price
  # Income needed to overcome new costs
  hourly_income_target =  hourly_income + increase_per_hour
  # New costs spread across customers
  increase_per_customer =  (hourly_income_target/customers_per_hour) - avg_price
  # Percent cost increase spread across customers
  pct_increase_customer = (increase_per_customer/avg_price) * 100
  
  print "Number of employees                = {}".format(employees)
  print "Downstream manhours per day        = {}".format(downstream_manhours_per_day)
  print "Current Minimum Wage               = ${}".format(wage)
  print "New Minimum Wage                   = ${}".format(new_wage)
  print "Wage difference per hour           = ${}".format(wage_delta)
  print "Downstream wage cost per hour      = ${:03.2f}".format(downstream_increase_per_hour)
  print "Tax increase per hour              = ${:03.2f}".format(tax_delta)
  print "Total Increased wage cost per hour = ${:03.2f}".format(increase_per_hour)
  print "Average price per transaction      = ${}".format(avg_price)
  print "Customers per hour                 = {}".format(customers_per_hour)
  print "Curent Hourly Income               = ${}".format(hourly_income)
  print "New revenue target                 = ${:03.2f}".format(hourly_income_target)
  print "Increase per customer              = ${:03.2f}".format(increase_per_customer)
  print "Percentage Increase per customer   = %{:03.2f}".format(pct_increase_customer)


if __name__ == "__main__":
  wage_increase(wage, new_wage, employees, avg_price, customers_per_hour, downstream_manhours_per_day, operating_hours, unemployment_insurace_rate)
