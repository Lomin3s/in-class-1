def main():

    try:

        price = float(input("Enter the price: "))

        blackFriday = str(input("Is it black friday [y/n]: "))
        coupon = str(input("Do you have a coupon [y/n]: "))
        empDiscount = str(input("Do you have an employee discount [y/n]: "))

        if blackFriday == "y":
            price = price * 0.60
        if coupon == "y":
            price = price * 0.95
        if empDiscount == "y":
            price = price * 0.80

        print(f'The final price is: $ {price:.2f}')

    except:
        print("Invalid input")
        main()

main()        
    
