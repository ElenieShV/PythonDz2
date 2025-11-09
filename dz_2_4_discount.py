price=float(input("Enter price:"))
discount_percent=float(input("Enter discount percent:"))
discount=price * discount_percent/100
final_price=price - discount
print("Final price", final_price)
