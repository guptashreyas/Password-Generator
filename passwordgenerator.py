import random
import string
digit1 = random.randint(0,9)
digit2 = random.randint(0,9)
upper1 = random.choice(string.ascii_uppercase)
upper2 = random.choice(string.ascii_uppercase)
lower1 = random.choice(string.ascii_lowercase)
lower2 = random.choice(string.ascii_lowercase)
punc1 = random.choice(string.punctuation)
punc2 = random.choice(string.punctuation)

password =[digit1,digit2,upper1,upper2,lower1,lower2,punc1,punc2]
random.shuffle(password)
print("your Generated Password:",end = " ")
for i in password:
  print(i,end = " ")





