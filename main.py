def main():
    print("This program converts US dollars to Pound Sterling")
    print()

    dollars = eval(input("Amount in Dollars: "))
    pounds = convert_to_pounds(dollars)

    print("That is ", pounds, "pounds")


convert_to_pounds = lambda dollars: dollars * 0.82

main()
