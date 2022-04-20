# !/usr/bin/env python3
# Created by: Jedidiah
# Created on: April 18 2022


def main():

    try:
        # input
        year = int(input("Enter the year: "))
        # process
        remainder = year % 4
        # output
        if year > 0:
            if remainder == 0:
                print("{} is leap year".format(year))
        if year < 0:
            print("the year cannot be negative")
            print("")
        if remainder > 0:
            print("{} is not a leap year".format(year)) 
    # error control
    except ValueError:
        print ("that is not an integer")
    else:
        print("")
    finally:
        print("done.")


if __name__ == "__main__":
    main()
