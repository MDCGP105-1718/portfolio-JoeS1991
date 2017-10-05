beerNum = 99

while beerNum >= 3:
    print(f"{beerNum} bottles of beer on the wall, {beerNum} bottles of beer.")
    beerNum = beerNum - 1
    print(f"Take one down, pass it around, {beerNum} bottles of beer on the wall.")
if beerNum == 2: #using an elif statement here was returning an syntax error on the 'i' of elif?
    print(f"{beerNum} bottles of beer on the wall, {beerNum} bottles of beer.")
    beerNum = beerNum - 1
    print(f"Take one down, pass it around, {beerNum} bottle of beer on the wall.")
if beerNum == 1: #I'm sure there's a better method I can use here than two different 'if' statements, but I want it to print different strings for both '2' and '1' bottles left.
    print(f"{beerNum} bottle of beer on the wall, {beerNum} bottle of beer!")
    print("So take it down, pass it around, no more bottles of beer on the wall!")
