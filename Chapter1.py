#1_1 unpacking a sequence into separate variables
data = [ "ACME", 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print shares
print price

#1_2 
record = ('Dave', 'deve@example.com', '123123', '456456')
name, email, *phone_numers = record
print email
print phone_numbers