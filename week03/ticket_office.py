import csv
from pathlib import Path

summary_headers = (
    "Tickets sold",
    "Total revenue (TRY)",
    "Average price (TRY)",
    "Free tickets",
)
summary_path = Path.home() / "Desktop" / "Daily_summary.csv"

total_revenue = 0.0
tickets_sold = 0
free_tickets = 0

if summary_path.exists():
    with summary_path.open(newline="", encoding="utf-8") as summary_file:
        existing_rows = list(csv.reader(summary_file, delimiter=";"))
    if existing_rows and tuple(existing_rows[0]) != summary_headers:
        raise ValueError(f"Unexpected CSV format in {summary_path}")
    for row in existing_rows[1:]:
        tickets_sold += int(row[0])
        total_revenue += float(row[1])
        free_tickets += int(row[3])

while True:
    name = input("Customer name (or q to quit): ").strip()
    if name.lower() == "q":
        break

    #Age check
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid age.")
        continue
    if age < 0 or age > 120:
        print("Invalid age.")
        continue

    #Day of the week check
    day = input("Day (weekday/weekend): ").strip().lower()
    if day not in ("weekday", "weekend"):
        print("Invalid day.")
        continue

    #Student discount check
    student = input("Student (yes/no): ").strip().lower()
    if student not in ("yes", "no"):
        print("Please answer yes or no.")
        continue

    #Standard ticket price
    base = 200 if day == "weekday" else 250

    #Customer can only use one highest discount
    if age < 6:
        discount, label = 1.00, "Free"
    elif age >= 65:
        discount, label = 0.50, "Senior"
    elif 6 <= age <= 12:
        discount, label = 0.40, "Child"
    elif student == "yes" and age <= 25:
        discount, label = 0.30, "Student"
    else:
        discount, label = 0.0, "Standard"

    price = base * (1 - discount)

    print(f"{name}: {price:.2f} TRY ({label})")

    tickets_sold += 1
    total_revenue += price
    if price == 0:
        free_tickets += 1

#Summary part
#If we are losers and didn't sell any tickets
if tickets_sold == 0:
    print("No tickets sold.")

else:
    print(f"Tickets sold: {tickets_sold}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {total_revenue / tickets_sold:.2f} TRY")
    print(f"Free tickets: {free_tickets}")

#Same as before, but now we save the daily summary to a CSV file on the desktop
summary_path.parent.mkdir(parents=True, exist_ok=True)
summary = [
    summary_headers,
    (
        tickets_sold,
        f"{total_revenue:.2f}",
        f"{total_revenue / tickets_sold:.2f}" if tickets_sold else "0.00",
        free_tickets,
    ),
]

mode = "w" if summary_path.exists() else "x"
with summary_path.open(mode, newline="", encoding="utf-8") as summary_file:
    csv.writer(summary_file, delimiter=";").writerows(summary)

print(f"Summary saved to: {summary_path}")

#PROGRAM WON'T WRITE "NO TICKETS SOLD" IF YOU HAVE A .CSV FILE ALREADY CREATED. IT WILL JUST WRITE THE DATA FROM THE CSV FILE
#YOU CAN ONLY GET "NO TICKETS SOLD" IF YOU DELETE THE .CSV FILE AND RUN THE PROGRAM AGAIN.