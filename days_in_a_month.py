"""
See instructions in CSCI111_A4.pdf

Be sure to rename this file Lastname_A4.py, using your last name
in place of "Lastname".

Your name: Keon Hayes

"""

"""
The input function will print "Enter a month (1-12): " and wait for the user to
type their entry. When the user presses the "Enter" key on their keyboard, the
value they typed will be returned as a string-type and to the month variable, and
immediately typecast as an int.
"""

month = int(input("Enter a month (1-12): "))

"""
The input function will print "Enter a year (after 1000): " and wait for the user
to type their entry. When the user presses the "Enter" key on their keyboard, the
value they typed will be returned as a string-type and to the year variable, and
immediately typecast as an int.
"""

year = int(input("Enter a year (after 1000): "))

"""
If  4, 6, 9, or 11 is assigned to the month variable, then the program will print
that the month has 30 days. Otherwise, if 1, 3, 5, 7, 8, 10, or 12 is assigned to
the month variable, then the program will print that the month has 31 days.
"""

if month == 4 or month == 6 or month == 9 or month == 11 :
    print("There are 30 days in ", month, "/", year, ".", sep="")

elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
    print("There are 31 days in ", month, "/", year, ".", sep="")

#February is tested within the leap or non-leap year code.

"""
If an int is assigned to the year variable which is a multiple of 100, which is
also a multiple of 400, or that the year is a multiple of 4, that is not also a
multiple of 100, then the program will print that the year is a leap year, and
that February has 29 days. Otherwise, it will print that the year is not a leap
year, and that February has 28 days.
"""

if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0 :
    if month == 2 :
        print("There are 29 days in ", month, "/", year, ".", sep="")
    print(year, "is a leap year.")

else :
    if month == 2 :
        print("There are 28 days in ", month, "/", year, ".", sep="")
    print(year, "is not a leap year.")
