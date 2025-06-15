
print('Convert int to decimal')
import decimal
a= 12345
print(decimal.Decimal(a))
print(type(decimal.Decimal(a)))
print()

print('Convert String of Int into decimal')
string = '12345'
print(type(string))
print(decimal.Decimal(string))
print(type(decimal.Decimal(string)))
