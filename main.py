

#"Арифметика": "1st program".
print(9 ** 0.5 * 5)

#"Логика":  "2nd program".
print(9.99 > 9.98 and 1000 != 1000.1)

#"Школьная загадка":  "3rd program".
print(2*2+2 == 2*(2+2))

#"Первый после точки": "4th program".
s = "123.456"
namber = float(s)
shifted_namber = namber * 10
int_part = int(shifted_namber)
first_digit_after_dot = int_part % 10

print(first_digit_after_dot)

