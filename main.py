import random


fortune_number = random.randint(1, 3)
fortune_text = ""

if fortune_number == 1:
    fortune_text = f"You will have a great day!. Your lucky number is {fortune_number}"
elif fortune_number == 2:
    fortune_text = f"You will have a bad day!. Your lucky number is {fortune_number}"
else:
    fortune_text = f"You will have a mediocre day. Your lucky number is {fortune_number}"

print(fortune_text)