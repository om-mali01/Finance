"""
    Finance Mananger system
"""
import json

def data_year(data):
    total_saving = 0
    for saving in data.values():
        total_saving += saving.get("Gross Saved",0)
    print(f"Your total saving in this year is {total_saving}\n")

def save_data(data, filename):
    '''To save the data'''
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_data(filename):
    '''To load data in the files'''
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

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
    bucket: dict = {}
    choice = input("\nDo you want to allocate some money to other things (yes/no): ")
    if choice not in ["yes", "YES", "Y", "y"]:
        return {}, 0
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


def print_info(month, income, expenses, remaining_amount, bucket, bucket_total):
    """
    Display the final information
    """
    print(f"\n-----{month}'s summery-----")
    print(f"Your Income is {income}")
    print(f"Your Expenses is {expenses}")
    print(f"Your remaining amount after expeses {remaining_amount}")
    if not bucket:
        print("Bucket is empty")
        print(f"Your bucket total is {bucket_total}")
        print(f"Gross saved amount in {month}: {remaining_amount - bucket_total}\n")
        return
    print("Your bucket list: ")
    for key, value in bucket.items():
        print(f"{key}: {value}")
    print(f"Your bucket total is {bucket_total}")
    print(f"Gross saved amount in {month}: {remaining_amount - bucket_total}\n")


def main():
    '''main'''
    month, income, expenses = input_info()

    if income < expenses:
        return print("Invalid")
    
    remaining_amount = income - expenses
    print(f"Your remaining amount is {remaining_amount}")

    filename = "finance_data.json"
    data = load_data(filename)
    
    if month in data:
        existing_data = data[month]
        choice = input("\nThis month is already added !!! Do you want to update the data? (y/n): ")
        if choice not in ['y','yes','Yes',"YES"]:
            print_info(month, existing_data['income'], existing_data['expenses'], existing_data['remaining_amount'], existing_data['bucket'], existing_data['bucket_total'])
            data_year(data)
            return
        
        existing_data = data[month]
        existing_income = existing_data['income']
        existing_expenses = existing_data['expenses']
            # Check if the existing income and expenses match the new input
        if existing_income == income and existing_expenses == expenses:
            print("Data for this month already exists and is up to date.")
        else:
            print("Updating existing data for this month.")
            data[month]['income'] = income
            data[month]['expenses'] = expenses
            remaining_amount = income - expenses
            data[month]['remaining_amount'] = remaining_amount
            bucket, bucket_total = bucket_info(remaining_amount)
            data[month]['bucket'] = bucket
            data[month]['bucket_total'] = bucket_total
            data[month]['Gross Saved'] = remaining_amount - bucket_total
            save_data(data, filename)
            print_info(month, income, expenses, remaining_amount, data[month]['bucket'], data[month]['bucket_total'])
            data_year(data)

    remaining_amount = income - expenses
    bucket, bucket_total = bucket_info(remaining_amount)
    data[month] = {
            'month' : month,
            'income' : income,
            'expenses' : expenses,
            'remaining_amount':remaining_amount,
            'bucket':bucket,
            'bucket_total':bucket_total,
            'Gross Saved':remaining_amount - bucket_total
    }
    save_data(data, filename)
    print_info(month, income, expenses, remaining_amount, bucket, bucket_total)
    data_year(data)

if __name__ == "__main__":
    main()
