
'''  
1. Create a function named calculate_discount(price, 
discount_percent) that calculates 
the final price after applying a 
discount. The function should take 
the original price (price) and 
the discount percentage (discount_percent) 
as parameters. If the discount is 20% or 
higher, apply the discount; otherwise, 
return the original price.


'''

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price     



'''  
2. Using the calculate_discount function,
 prompt the user to enter the original price 
 of an item and the discount percentage. 
 Print the final price after applying the discount, 
 or if no discount was applied, print the original price.


'''   

def main():
    

    while True:
        original_price = input("enter the original price:")
        discount_percent = input("enter the discount percent:")
        try:
            price_original = int(original_price)
            discount_percentage = int(discount_percent)
            break
        except ValueError:
            print("You did not enter the original price!")
            print("You did not enter the discount!")


    if discount_percent >=20:
        return calculate_discount()
    else:
        return original_price

            
main()  