print("Hey,Do you want to chose card")
import random

cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
sign =  ["❤️","♠️","♣️","♦️"]

def pullCard():

    return random.choice(cards), random.choice(sign)


rank, suit = pullCard()
print(f"Pulled card: {rank}{suit}")

value = 0


if rank == "A":
    value += 1
elif rank == "J":
    value += 11
elif rank == "Q":
    value += 12
elif rank == "K":
    value += 13
else:
    value += int(rank)  


if suit == "❤️":
    value += 0
elif suit == "♦️":
    value += 10
elif suit == "♣️":
    value += 20
elif suit == "♠️":
    value += 30

print(f"Total calculated value: {value}")

if value>=21:
   print("You win")
else:
      print("You lose")
