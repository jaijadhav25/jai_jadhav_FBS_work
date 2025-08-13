### Accept no. of passengers from user and per ticket cost. Then accept age of each
#   passenger and then calculate total amount to ticket to travel for all of them 
#   based on following condition :
#   a. Children below 12 = 30% discount
#   b. Senior citizen (above 59) = 50% discount
#   c. Others need to pay full.

no_of_passanger = int(input("Enter the number of passanger:"))
ticket_cost = int(input("Enter the price of ticket:"))
total_ticket = 0
for i in range(1,no_of_passanger + 1):
    age = int(input(f"Enter the age of {i}:"))
    if(age < 12):
        ticket = ticket_cost * (30/100)
        ticket = ticket_cost - ticket
        print(ticket)
    elif(age > 59):
        ticket = ticket_cost * (50/100)
        ticket = ticket_cost - ticket
        print(ticket)
    else:
        ticket = ticket_cost
        print(ticket)
    total_ticket = total_ticket + ticket
print(f"Total ticket price is {total_ticket}")