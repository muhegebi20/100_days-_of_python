print("Welcome to the secret auction program.")
bids = {}
while True:
    b_name = input("What is your name? ")
    bid = int(input("your bid: $"))
    bids[f"{b_name}"] = bid
    another_bidder = input("are there any other bidders? Type 'yes' or 'no' ").lower()
    if another_bidder == "no":
        break
    print("\n"*100)
allbids = []
m_min = 0
min_name = ""
for b in bids:
    if bids[b] > m_min:
        min_name = ""
        m_min = bids[b]
        min_name+=b
print(f"winner is {min_name} with the bid of ${m_min}")