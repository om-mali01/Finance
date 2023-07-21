month = input("enter the month: ")
income = int(input("Enter the Income per month: "))
expenses = int(input("Enter the expenses per month: "))
if expenses < income:
    remaining_total = income - expenses
    print(f"Your remaining amount after expenses is {remaining_total}")

    bucket = {}
    bucket_total = 0
    choice = input("Do you want to allocate some money for other things (yes/no): ")
    if choice == 'yes':
        while True:
            name = input("enter the name or exit: ")
            if name == 'exit':
                break
            amount = int(input("enter the amount: "))
            if amount <= remaining_total - bucket_total:
                bucket[name] = amount
                bucket_total += amount
            else:
                print(f"You don't have enough money. You can only allocate {remaining_total - bucket_total} to the bucket for {name}.")
    
        print(f"\n------{month}'s summery------")
        print(f"Total income: {income}")
        print(f"Total expense: {expenses}")
        print(f"The remaining amount after expenses is {remaining_total}")
        print("bucket list: ")
        for key, value in bucket.items():
            print(f"{key} : {value}")
        print(f"Total bucket amount: {bucket_total}")
        # print(f"Total remaining amount is {remaining_total}")
        print(f"Gross remaining in {month} is {remaining_total - bucket_total}")

    else:
        print(f"\n------{month}'s summery------")
        print(f"Total income: {income}")
        print(f"Total expense: {expenses}")
        print(f"Total bucket amount: {bucket_total}")
        print(f"Total remaining amount is {remaining_total}")
else:
    print("Invalide")