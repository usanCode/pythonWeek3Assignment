
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
        original_price = input("Enter the original price: ")
        discount_percent = input("Enter the discount percent: ")
        try:
            price_original = float(original_price)  # Use float for prices

            discount_percentage = float(discount_percent)  # Use float for percentages
            break
        except ValueError:
            print("Invalid input! Please enter numeric values for price and discount.")

    if discount_percentage >= 20:
        final_price = calculate_discount(price_original, discount_percentage)
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {price_original:.2f}") 

# Call the function
main()
