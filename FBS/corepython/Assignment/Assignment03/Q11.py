### Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.
persion1 = int(input("Enter the age of persion no 1 :"))
persion2 = int(input("Enter the age of persion no 2 :"))
persion3 = int(input("Enter the age of persion no 3 :"))
persion4 = int(input("Enter the age of persion no 4 :"))
persion5 = int(input("Enter the age of persion no 5 :"))

ticket_price = int(input("Enter the ticket price:"))

if(persion1 < 12):
    ticket_price1 = ticket_price * (30 /100)
    ticket_price1 = ticket_price - ticket_price1
elif(persion1 > 59):
    ticket_price1 = ticket_price * (50 /100)
    ticket_price1 = ticket_price - ticket_price1
else:
    ticket_price1 = ticket_price

if(persion2 < 12):
    ticket_price2 = ticket_price * (30 /100)
    ticket_price2 = ticket_price - ticket_price2
elif(persion2 > 59):
    ticket_price2 = ticket_price * (50 /100)
    ticket_price2 = ticket_price - ticket_price2
else:
    ticket_price2 = ticket_price

if(persion3 < 12):
    ticket_price3 = ticket_price * (30 /100)
    ticket_price3 = ticket_price - ticket_price3
elif(persion3 > 59):
    ticket_price3 = ticket_price * (50 /100)
    ticket_price3 = ticket_price - ticket_price3
else:
    ticket_price3 = ticket_price

if(persion4 < 12):
    ticket_price4 = ticket_price * (30 /100)
    ticket_price4 = ticket_price - ticket_price4
elif(persion4 > 59):
    ticket_price4 = ticket_price * (50 /100)
    ticket_price4 = ticket_price - ticket_price4
else:
    ticket_price4 = ticket_price

if(persion5 < 12):
    ticket_price5 = ticket_price * (30 /100)
    ticket_price5 = ticket_price - ticket_price5
elif(persion5 > 59):
    ticket_price5 = ticket_price * (50 /100)
    ticket_price5 = ticket_price - ticket_price5
else:
    ticket_price5 = ticket_price

total_ticket_price = ticket_price1 + ticket_price2 + ticket_price3 + ticket_price4 + ticket_price5
print(f"Total ticket price of five preson is {total_ticket_price}")