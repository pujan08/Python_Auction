from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

dicitonary={}
maxbid=0
winner=""

print(art.logo)
print("Welcome to the secret aution program.")
while True:
  name=input("What is your name?: ").lower()
  bid=int(input("what's your bid?: $"))
  checker=input("Are there any other bidders? Type 'yes' or 'no'").lower()
  if checker=="yes":
    dicitonary[name]=bid
  elif checker=="no":
    clear()
    dicitonary[name]=bid
    for key in dicitonary:
      amount=dicitonary[key]
      if amount>maxbid:
        maxbid=amount
        winner=key
    print(f"Winner is {winner} with a bid of ${maxbid}")
    break
  