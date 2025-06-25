# Check if year is leap year
year = int(input("Enter the year:"))
if year % 400 == 0 or year % 4 == 0:
    print(year, "is leap year")