
beers = int(input("How many beers?"))
while beers > 100:
    beers = int(input("How many beers? Enter a number not greater than 100"))

for i in range(beers,0,-1):
    print(f"{i} bottles of beer on the wall!")


