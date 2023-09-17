print(
    "If you have the price of one NFT and want to calculate the collection's total earnings, then press: A"
)
print(
    "If you have the total price of the collection and want to calculate the one NFT price and tax earnings, then press: B"
)
print(
    "If you have the artist's cut of the collection and want to calculate the one NFT price and tax earnings, then press: C"
)
cal = input("Enter A, B, or C: ")

size_collection = int(input("Enter size of collection: "))
total_er = float()

if cal == "A":
    # user input part of section A
    print("Enter amount in INR")
    one_nft = int(input("Enter the price of one NFT: "))
    print("Give answer in Y or N")
    charity = input("Does this club have charity or not: ")

    # calculation part of section A
    # er = earning
    # r = reduction
    # ra = tax deducted amount
    # am = amount
    total_er = one_nft * size_collection
    tax_r = total_er * (30 / 100)
    tax_ra = total_er - tax_r
    if charity == "y":
        artist_er = tax_ra / 2
        charity_am = artist_er
        print(f"Total earning of this collection is: {total_er:.2f} INR")
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club after 50% charity: {artist_er:.2f} INR")
        print(f"Your charity is: {charity_am:.2f} INR")
    elif charity == "Y":
        artist_er = tax_ra / 2
        charity_am = artist_er
        print(f"Total earning of this collection is: {total_er:.2f} INR")
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club after 50% charity: {artist_er:.2f} INR")
        print(f"Your charity is: {charity_am:.2f} INR")
    elif charity == "n":
        artist_er = tax_ra
        print(f"Total earning of this collection is: {total_er:.2f} INR")
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club: {artist_er:.2f} INR")
    elif charity == "N":
        artist_er = tax_ra
        print(f"Total earning of this collection is: {total_er:.2f} INR")
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club: {artist_er:.2f} INR")
    else:
        print("Enter Y or N for calculation")
elif cal == "a":
    # user input part of section A
    print("Enter amount in INR")
    one_nft = int(input("Enter the price of one NFT: "))
    print("Give answer in Y or N")
    charity = input("Does this club have charity or not: ")

    # calculation part of section A
    # er = earning
    # r = reduction
    # ra = tax deducted amount
    # am = amount

    total_er = one_nft * size_collection
    tax_r = total_er * (30 / 100)
    tax_ra = total_er - tax_r
    if charity == "y":
        artist_er = tax_ra / 2
        charity_am = artist_er
        print(f"Total earning of this collection is: {total_er:.2f} INR")
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club after 50% charity: {artist_er:.2f} INR")
        print(f"Your charity is: {charity_am:.2f} INR")
    elif charity == "Y":
        artist_er = tax_ra / 2
        charity_am = artist_er
        print(f"Total earning of this collection is: {total_er:.2f} INR")
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club after 50% charity: {artist_er:.2f} INR")
        print(f"Your charity is: {charity_am:.2f} INR")
    elif charity == "n":
        artist_er = tax_ra
        print(f"Total earning of this collection is: {total_er:.2f} INR")
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club: {artist_er:.2f} INR")
    elif charity == "N":
        artist_er = tax_ra
        print(f"Total earning of this collection is: {total_er:.2f} INR")
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club: {artist_er:.2f} INR")
    else:
        print("Enter Y or N for calculation")
elif cal == "B":
    print("Enter amount in INR")
    total_er = int(input("Enter total earning of collection: "))
    one_nft = total_er / size_collection
    tax_r = total_er * (30 / 100)
    tax_ra = total_er - tax_r
    print("Give answer in Y or N")
    charity = input("Does this club have charity or not: ")
    if charity == "y":
        artist_er = tax_ra / 2
        charity_am = artist_er
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club after 50% charity: {artist_er:.2f} INR")
        print(f"Your charity is: {charity_am:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    elif charity == "Y":
        artist_er = tax_ra / 2
        charity_am = artist_er
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club after 50% charity: {artist_er:.2f} INR")
        print(f"Your charity is: {charity_am:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    elif charity == "n":
        artist_er = tax_ra
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club: {artist_er:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    elif charity == "N":
        artist_er = tax_ra
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club: {artist_er:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    else:
        print("Enter Y or N for calculation")
elif cal == "b":
    print("Enter amount in INR")
    total_er = int(input("Enter total earning of collection: "))
    one_nft = total_er / size_collection
    tax_r = total_er * (30 / 100)
    tax_ra = total_er - tax_r
    print("Give answer in Y or N")
    charity = input("Does this club have charity or not: ")
    if charity == "y":
        artist_er = tax_ra / 2
        charity_am = artist_er
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club after 50% charity: {artist_er:.2f} INR")
        print(f"Your charity is: {charity_am:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    elif charity == "Y":
        artist_er = tax_ra / 2
        charity_am = artist_er
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club after 50% charity: {artist_er:.2f} INR")
        print(f"Your charity is: {charity_am:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    elif charity == "n":
        artist_er = tax_ra
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club: {artist_er:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    elif charity == "N":
        artist_er = tax_ra
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Artist earning from this club: {artist_er:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    else:
        print("Enter Y or N for calculation")
elif cal == "C":
    print("Enter amount in INR")
    artist_cut = float(input("Enter amount of artist cut: "))
    print("Give answer in Y or N")
    charity = input("Does this club have charity or not: ")
    if charity == "y":
        artist_er = artist_cut
        charity_am = artist_er
        tax_ra = artist_cut + artist_er
        tax_r = ((tax_ra * 100) / 70) * (30 / 100)
        total_er = tax_r + tax_ra
        one_nft = total_er / size_collection
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Total erning from this club with 50% charity: {total_er:.2f} INR")
        print(f"Your charity is: {charity_am:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    elif charity == "Y":
        artist_er = artist_cut
        charity_am = artist_er
        tax_ra = artist_cut + charity_am
        tax_r = ((tax_ra * 100) / 70) * (30 / 100)
        total_er = tax_r + tax_ra
        one_nft = total_er / size_collection
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Total erning from this club with 50% charity: {total_er:.2f} INR")
        print(f"Your charity is: {charity_am:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    elif charity == "n":
        artist_er = artist_cut
        tax_ra = artist_er
        tax_r = ((tax_ra * 100) / 70) * (30 / 100)
        total_er = tax_r + tax_ra
        one_nft = total_er / size_collection
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Total erning from this club without charity: {total_er:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    elif charity == "N":
        artist_er = artist_cut
        tax_ra = artist_er
        tax_r = ((tax_ra * 100) / 70) * (30 / 100)
        total_er = tax_r + tax_ra
        one_nft = total_er / size_collection
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Total erning from this club without charity: {total_er:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    else:
        print("Enter Y or N for calculation")
elif cal == "c":
    print("Enter amount in INR")
    artist_cut = float(input("Enter amount of artist cut: "))
    print("Give answer in Y or N")
    charity = input("Does this club have charity or not: ")
    if charity == "y":
        artist_er = artist_cut
        charity_am = artist_er
        tax_ra = artist_er + charity_am
        tax_r = ((tax_ra * 100) / 70) * (30 / 100)
        total_er = tax_r + tax_ra
        one_nft = total_er / size_collection
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Total erning from this club with 50% charity: {total_er:.2f} INR")
        print(f"Your charity is: {charity_am:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    elif charity == "Y":
        artist_er = artist_cut
        charity_am = artist_er
        tax_ra = artist_er + charity_am
        tax_r = ((tax_ra * 100) / 70) * (30 / 100)
        total_er = tax_r + tax_ra
        one_nft = total_er / size_collection
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Total erning from this club with 50% charity: {total_er:.2f} INR")
        print(f"Your charity is: {charity_am:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    elif charity == "n":
        artist_er = artist_cut
        tax_ra = artist_er
        tax_r = ((tax_ra * 100) / 70) * (30 / 100)
        total_er = tax_r + tax_ra
        one_nft = total_er / size_collection
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Total erning from this club without charity: {total_er:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    elif charity == "N":
        artist_er = artist_cut
        tax_ra = artist_er
        tax_r = ((tax_ra * 100) / 70) * (30 / 100)
        total_er = tax_r + tax_ra
        one_nft = total_er / size_collection
        print(f"Your tax reduction is: {tax_r:.2f} INR")
        print(f"Total erning from this club without charity: {total_er:.2f} INR")
        print(f"Price of one NFT: {one_nft:.2f} INR")
    else:
        print("Enter Y or N for calculation")
else:
    print("Enter A , B or C to calculate revenue of your NFT collection")
