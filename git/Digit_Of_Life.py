date = input("Enter a date of your birthday as a set of 8 digits: ")
if len(date) != 8 or not date.isdigit():
    print("Your entered invalid query, please try again ")
else:
    while len(date) > 1:
        sum = 0
        for dig in date:
            sum += int(dig)
        print(date)
        date = str(sum)
    print("Your Digit Of Life is: " + date)
