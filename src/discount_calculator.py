product_name = "Camiseta"
original_price = 50.00
discount_percent = 20

discount_amount = original_price * (discount_percent / 100)
final_price = original_price - discount_amount

print(f"Product: {product_name}")
print(f"Original price: R$ {original_price:.2f}")
print(f"Discount percentage: {discount_percent}%")
print(f"Discount amount: R$ {discount_amount:.2f}")
print(f"Final price: R$ {final_price:.2f}")
