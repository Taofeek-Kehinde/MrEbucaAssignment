"""
PSEUDOCODE:
1. Ask for total bill amount
2. Ask if customer is member (yes or no)
3. If bill is $1000 or more AND customer is member:
   - Discount = 10%
   - Final amount = bill - (bill x 0.10)
   - Message = "10% member discount applied"
4. If bill is $1000 or more BUT not member:
   - Discount = 5%
   - Final amount = bill - (bill x 0.05)
   - Message = "5% discount applied"
5. Else:
   - No discount
   - Final amount = bill
   - Message = "No discount applied"
6. Print final amount and message
"""

total_bill = float(input("Enter total bill amount: $"))
is_member = input("Are you a member? (yes/no): ")

if total_bill >= 1000 and is_member == "yes":
    discount = 0.10
    final_amount = total_bill * (1 - discount)
    message = "10% member discount applied"
elif total_bill >= 1000:
    discount = 0.05
    final_amount = total_bill * (1 - discount)
    message = "5% discount applied"
else:
    discount = 0
    final_amount = total_bill
    message = "No discount applied"

print(f"Original amount: ${total_bill:.2f}")
print(f"Final amount: ${final_amount:.2f}")
print(f"Message: {message}")
