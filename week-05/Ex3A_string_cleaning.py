name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

# Convert the names to lowercase
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# Convert the names to title case
print(name_1.title())
print(name_2.title())
print(name_3.title())

# Remove the dollar signs
salary_1_no_dollar = salary_1.replace("$", "")
salary_2_no_dollar = salary_2.replace("$", "")

print(salary_1_no_dollar)
print(salary_2_no_dollar)

# These values are still strings, so they need conversion before math.
print(type(salary_1_no_dollar))
print(type(salary_2_no_dollar))

# Remove the comma and convert salary_1 to an integer
salary_1_number = int(salary_1_no_dollar.replace(",", ""))

print(salary_1_number)
print(type(salary_1_number))