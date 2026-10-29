"""
Self-Assessment

1. Tracing order_total = 350 through the discount tiers:
   First it checks if the total is at least $500. It isn't, so it moves on.
   Next it checks if it's at least $200. It is, so the discount gets set to 10%
   and it stops checking the rest (the $100 tier never even gets looked at).
   Then the final price is 350 x 0.90 = $315.00. For the approval flag,
   $315 isn't over $1000, so the status comes out as auto_approved.

2. "if total > 100 and total < 500:" is one check where both things have to be
   true before the code inside runs. Two separate if statements each get checked
   on their own, so each block runs whenever its own condition is true. They
   don't always give the same result. With a total of 50, the "and" version
   does nothing, but a separate "if total < 500" would still run because 50 is
   less than 500. They only match if the second if is nested inside the first.

3. I see this all the time. Tax brackets are the obvious one, especially as a
   finance major. Online shopping has free shipping once you hit a certain
   amount, and Chick-fil-A One has reward tiers based on how much you spend in
   a year. Now I kind of picture them as if/elif chains in my head. It also made
   me realize how much the details matter, like whether a cutoff is > or >=,
   and which tier gets checked first.
"""

# Exercise 1
total = 250  # test value (would normally be float(input("Enter cart total: $")))

if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0

final = total * (1 - discount)
print(f"Discount: {discount*100:.0f}%")
print(f"Final price: ${final:.2f}")

# Exercise 2
if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"

print(f"Status: {status}")

# Exercise 3
total = 250
region = "South"

if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0

if region == "South" and total >= 100:
    discount += 0.02
    print("Region bonus applied: additional 2% off")

final = total * (1 - discount)
print(f"Final discount: {discount*100:.0f}%")
print(f"Final price: ${final:.2f}")

# Exercise 4
customer_type = "wholesale"
extra_discount = 0

# The flat version is easier to read and test because every condition is on
# one line, so you can see right away what has to be true for the discount.
# There's no deep indentation to follow, and there's only one place to check.
if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03

print(f"Extra discount: {extra_discount*100:.0f}%")

# Exercise 5
amount = 15000  # also tested with -50 (SUSPICIOUS) and 500 (NORMAL)

if amount <= 0:
    print("SUSPICIOUS")
elif amount >= 10000:
    print("LARGE — REVIEW REQUIRED")
else:
    print("NORMAL")

# Exercise 6
total_spent = 2500
order_count = 4
outstanding_balance = 0

# VIP if they spent over $2000 OR placed more than 10 orders
qualifies = total_spent > 2000 or order_count > 10

# Excluded if they have any outstanding balance
if qualifies and not outstanding_balance > 0:
    print("VIP upgrade: approved")
else:
    print("VIP upgrade: not eligible")