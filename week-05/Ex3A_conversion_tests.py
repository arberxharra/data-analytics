# Description: This script tests various numeric
#              conversion techniques
# Author: Arber Xharra

a = " 101.1 "
b = "55"
c = "402 Stevens"
d = "Number 5 "

# 3. Convert each variable to an integer
# a_int = int(a)  # ValueError: a contains a decimal point.
b_int = int(b)
# c_int = int(c)  # ValueError: c contains text.
# d_int = int(d)  # ValueError: d contains text.

# 3. Convert each variable to a float
a_float = float(a)
b_float = float(b)
# c_float = float(c)  # ValueError: c contains text.
# d_float = float(d)  # ValueError: d contains text.

# 3. Convert a to float, then to integer
a_float_int = int(float(a))

# 5. Slice out the numeric parts, then convert them to integers
a_number = int(float(a.strip()))
b_number = int(b)
c_number = int(c[0:3])
d_number = int(d[7:8])

# 5. Remove leading/trailing spaces from a and d and display the results
print(a.strip())
print(d.strip())

# int(b) works and gives 55.
# int(a) gives a ValueError because "101.1" includes a decimal point.
# float(a) works and gives 101.1; float(b) gives 55.0.
# Converting a to float and then int gives 101; int() drops the decimal part.
# c and d cannot be converted directly to int or float because they contain words.
# c[0:3] extracts "402"; d[7:8] extracts "5".
# strip() removes the extra spaces around a and d.