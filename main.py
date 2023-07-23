"""
    Finance Mananger system
"""


def input_info():
    """
    Taking input from user
    """
    month = input("Enter the month: ")
    income = int(input("Enter the income per month: "))
    expenses = int(input("Enter the expenses per month: "))

    return month, income, expenses


def bucket_info(remaining_amount):
    """
    Allocating money to bucket
    """
    bucket_total = 0
    bucket:dict = {}
    choice = input("\nDo you want to allocate some money to other things (yes/no): ")
    if choice in ["yes","YES","Y","y"]:
        while True:
            name = input("\nEnter the name or exit: ")
            if name == "exit":
                break
            amount = int(input(f"Enter the allocation amount to {name}: "))
            if amount <= remaining_amount - bucket_total:
                bucket[name] = amount
                bucket_total = bucket_total + amount
            else:
                print(
                    f"\nYou dont have enough money. You can allocate only {remaining_amount-bucket_total}"
                )
        return bucket, bucket_total
    else:
        return {}, 0


def print_info(month, income, expenses, remaining_amount, bucket, bucket_total):
    """
    Display the final information
    """
    print(f"\n-----{month}'s summery-----")
    print(f"Your Income is {income}")
    print(f"Your Expenses is {expenses}")
    print(f"Your remaining amount after expeses {remaining_amount}")
    print("Your bucket list is ")
    if bucket == {}:
        print("NULL")
    else:
        for key, value in bucket.items():
            print(f"{key}: {value}")
    print(f"Your bucket total is {bucket_total}")
    print(f"Gross saved amount in {month}: {remaining_amount - bucket_total}\n")


def main():
    "This is main"
    month, income, expenses = input_info()

    if income > expenses:
        remaining_amount = income - expenses
        print(f"Your remaining amount is {remaining_amount}")
        bucket, bucket_total = bucket_info(remaining_amount)
        print_info(month, income, expenses, remaining_amount, bucket, bucket_total)
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
