import clear

logo = logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)


is_person = True
bids = {}
n = 0
while is_person:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    new_bid = {}
    new_bid["name"] = name
    new_bid["bid"] = bid

    bids[n] = new_bid
    n +=1
    another_person = input("Are there any other bidders? 'yes' or 'no'").lower()

    if another_person == "yes":
        is_person = True
    else:
        is_person = False


highest_bidder = ""
highest_bidder_price = 0

for key in bids:
    if bids[key]["bid"] > highest_bidder_price:
        highest_bidder_price = bids[key]["bid"]
        highest_bidder = bids[key]["name"]

print(f"The Winner is {highest_bidder}")