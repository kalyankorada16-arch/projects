# ATM code

details = { "Name" : "Ekanth",
            "ATM PIN" : "2005",
            "Balance" : 100000,
            "Transaction" : []}
print("-----------WELCOME------------")
print()
count = 1
attempt = 3
while attempt>0:
    user_pin = input("pls enter your 4 digit pin: ")
    if len(user_pin) == 4:
        if user_pin in details['ATM PIN']:
            while count==1:
                choice = int(input("\n1.Withdraw \n2.Deposit \n3.Balance \n4.Pin change \n5.Transaction \nEnter your choice: "))
                if choice == 1:
                    withdraw_m = int(input("pls enter amount to withdraw: "))
                    if withdraw_m <= details['Balance'] and withdraw_m%100 == 0:
                        details['Balance'] -= withdraw_m
                        details['Transaction'].append(f"withdraw:{withdraw_m}")
                        print(f"succesfully withdraw {withdraw_m} and balance is {details['Balance']}")
                    else:
                        print("entered amount is insufficient or change is not withdrawed")
                elif choice == 2:
                    deposit_m = int(input("pls enter amount to deposit: "))
                    if deposit_m%100 == 0:
                        details['Balance'] += deposit_m
                        details['Transaction'].append(f"deposit:{deposit_m}")
                        print(f"succesfully deposit {deposit_m} and balance is {details['Balance']}")
                    else:
                        print("change is not Deposited")
                elif choice == 3:
                    print(f"Your balance is {details['Balance']}")
                elif choice == 4:
                    re_attempt = 3
                    while re_attempt>0:
                        old_password = input("pls enter your old password: ")
                        if old_password in details['ATM PIN']:
                            new_password = input("pls enter your new password: ")
                            if len(new_password) == 4:
                                np_attempt = 3
                                while np_attempt > 0:
                                    confirm_password = input("pls enter your confirm password: ")
                                    if confirm_password == new_password:
                                        details['ATM PIN'] = new_password
                                        details['Transaction'].append(f"pin chnage:{new_password}")
                                        print("You have succesfully change your pin")
                                        break
                                    else:
                                        np_attempt -= 1
                                        if np_attempt > 0:
                                            print(f"mismatch with new password and you have {np_attempt} left.")
                                        else:
                                            print("your attempts are over")
                                            break
                                if details["ATM PIN"] == new_password:
                                    break
                            else:
                                print("please enter 4 digits only..")
                                break
                            
                        else:
                            re_attempt -= 1
                            if re_attempt > 0:
                                print(f"mismatch with old password and you have {re_attempt} left.")
                            else:
                                print("your attempts are over")
                                break
                elif choice == 5:
                    print("\n------ Transaction History ------")
                    if len(details['Transaction']) == 0:
                        print("No Transactions.")
                    else:
                        print(details['Transaction'])   
                    print()
                else:
                    print("Invalid choice")
                count = int(input("\n1.Home \n2.exit \nEnter your choice: "))
            else:
                print("Thank you for using our ATM...")
                break      
        else:
            attempt -= 1
            if attempt > 0:
                print(f"Incorrect pin and you have {attempt} left.")
            else:
                print("Your card is blocked and contact the bank.")
                break
    else:
        print("pls enter only 4 digit pin")



