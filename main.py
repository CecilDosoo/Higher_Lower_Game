from replit import clear
import random
from art import logo,vs
from game_data import data

print(logo)

def acc(acc):
  name = acc["name"]
  country = acc["country"]
  description = acc["description"]
  return f"{name}, a {description}, from {country}"

#print(acc1())

acc1 = random.choice(data)
acc2 = random.choice(data)


print(f"Compare A: {acc(acc1)}")
print(vs)
print(f"Against B: {acc(acc2)}")

A = acc1["follower_count"]
B = acc2["follower_count"]



score = 0
gameover = False
while not gameover:
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  if A > B and guess == "a":
    score += 1
    print(f"Thats right! Current score: {score}")
    clear()
    print(logo)
    print(f"Compare A: {acc(acc2)}")
    print(vs)
    acc3 = random.choice(data)
    B = acc3["follower_count"]
    print(f"Against B: {acc(acc3)}")
  elif B > A and guess == "b":
    score += 1
    print(f"Thats right! Current score: {score}")
    clear()
    print(logo)
    print(f"Compare A: {acc(acc2)}")
    print(vs)
    acc3 = random.choice(data)
    print(f"Against B: {acc(acc3)}")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    gameover = True













