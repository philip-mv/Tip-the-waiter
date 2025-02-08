def tc(bill_amount,tip_perc):
    total = (bill_amount*tip_perc /100) + bill_amount
    print(f"Please pay rupees{total}")


bill_amount = int(input("Please enter the bill amount : "))
tip_perc = int(input("PLease enter tip percentage : "))
tc(bill_amount,tip_perc)