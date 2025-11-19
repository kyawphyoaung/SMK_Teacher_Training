def calculate_bill():
    print("--- Online Shop Checkout ---")
    try:
        order_total = int(input("Enter Order Total (MMK): "))
        is_member = input("Is the customer a Member? (yes/no): ").lower()

        # Input Validation
        if order_total < 0:
            print("Error: Order total cannot be negative.")
            return

        # 1. Calculate Delivery Fee
        delivery_fee = 2000
        if is_member == "yes":
            delivery_fee = 0
        
        # 2. Calculate Discount
        discount = 0
        if order_total >= 20000:
            calculated_discount = order_total * 0.10  
            if calculated_discount > 3000:
                discount = 3000
            else:
                discount = calculated_discount

        # 3. Final Calculation
        final_amount = order_total - discount + delivery_fee

        print(f"\n--- Bill Summary ---")
        print(f"Order Amount: {order_total} MMK")
        print(f"Delivery Fee: {delivery_fee} MMK")
        print(f"Discount:    -{int(discount)} MMK")
        print(f"To Pay:       {int(final_amount)} MMK")

    except ValueError:
        print("Error: Please enter a valid number.")

calculate_bill()