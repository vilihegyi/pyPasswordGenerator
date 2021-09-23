import random

lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
upper_case_letters = "ABCDEFGHJIKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "[]{}()*;/,_-!@#$%^&|"

all_chars = lower_case_letters + upper_case_letters + digits + symbols
length = int(input("How long would you like the password to be? "))
password = "".join(random.sample(all_chars, length))
print("Generated password:\n", password)
