import random

lower="qwertyuiopasdfghjklzxcvbnm"
upper="QWERTYUIOPASDFGHJKLZXCVBNM"
number="1234567890"
symbols="!@#$%^&*"
all=lower + upper + number + symbols
length =8
password="".join(random.sample(all,length))
print("password is =",password)