import copy

import src.functions as fnct


def ui_add_transaction(account, day, amount, type_of_trans, description):
    fnct.add(account, day, amount, type_of_trans, description)


def ui_insert_transaction(account, day, amount, type_of_trans, description):
    fnct.insert(account, day, amount, type_of_trans, description)


def ui_remove_day(account, day):
    new_account = fnct.remove_day(account, day)
    return new_account


def ui_remove_period(account, day_start, day_end):
    new_account = fnct.remove_period(account, day_start, day_end)
    return new_account


def ui_remove_type(account, type_of_trans):
    new_account = fnct.remove_type(account, type_of_trans)
    return new_account


def ui_replace(account, day, type_of_trans, description, new_amount):
    new_amount = fnct.replace_value(account, day, type_of_trans, description, new_amount)
    return new_amount


def print_list_of_transactions(account):
    for i in account:
        print("Day: " + str(i[0]) + " | Amount: " + str(i[1]) + " | Type:" + str(i[2]) + " | Description:" + str(i[3]))


def ui_list(account):
    temp = account[::]
    for i in range(len(temp) - 1):
        for j in range(i + 1, len(temp)):
            if temp[i][0] > temp[j][0]:
                temp[i], temp[j] = temp[j], temp[i]
    for i in temp:
        print("Day: " + str(i[0]) + " | Amount: " + str(i[1]) +
              " | Type:" + str(i[2]) + " | Description: " + str(i[3]))


def ui_list_type(account, given_type):
    temp = account[::]
    for i in range(len(temp) - 1):
        for j in range(i + 1, len(temp)):
            if temp[i][0] > temp[j][0]:
                temp[i], temp[j] = temp[j], temp[i]
    for i in temp:
        if i[2] == given_type:
            print("Day: " + str(i[0]) + " | Amount: " + str(i[1]) +
                  " | Type:" + str(i[2]) + " | Description: " + str(i[3]))


def ui_list_value(account, symbol, amount):
    temp = account[::]
    for i in range(len(temp) - 1):
        for j in range(i + 1, len(temp)):
            if temp[i][0] > temp[j][0]:
                temp[i], temp[j] = temp[j], temp[i]
    if symbol == "<":
        for i in temp:
            if i[1] < amount:
                print("Day: " + str(i[0]) + " | Amount: " + str(i[1]) +
                      " | Type:" + str(i[2]) + " | Description: " + str(i[3]))
    if symbol == "=":
        for i in temp:
            if i[1] == amount:
                print("Day: " + str(i[0]) + " | Amount: " + str(i[1]) +
                      " | Type:" + str(i[2]) + " | Description: " + str(i[3]))
    if symbol == ">":
        for i in temp:
            if i[1] > amount:
                print("Day: " + str(i[0]) + " | Amount: " + str(i[1]) +
                      " | Type:" + str(i[2]) + " | Description: " + str(i[3]))


def ui_balance(account, day):
    balance = 0
    for i in account:
        if i[0] <= day:
            if i[2] == "in":
                balance += i[1]
            elif i[2] == "out":
                balance -= i[1]
    print("Balance at the end of day", day, "is", balance)


def ui_filter_type(account, type_of_transactions):
    account = fnct.filter_type(account, type_of_transactions)
    return account


def ui_filter_type_value(account, type_of_transactions, value):
    account = fnct.filter_type_value(account, type_of_transactions, value)
    return account


def ui():
    changes = 1
    current_day = 21
    account = []
    accounthistory = []
    fnct.generate_trans(account)
    ui_list(account)
    while True:
        if changes:
            accounthistory.append(copy.deepcopy(account))
        opt = input("Enter command: ")
        opt = opt.split()
        if opt[0] == "exit":
            break
        try:
            if opt[0] == "add":
                changes = 1
                amount = int(opt[1])
                type_of_trans = opt[2]
                description = opt[3]
                day = current_day
                ui_add_transaction(account, day, amount, type_of_trans, description)
            elif opt[0] == "insert":
                changes = 1
                day = int(opt[1])
                amount = int(opt[2])
                type_of_trans = opt[3]
                description = opt[4]
                ui_insert_transaction(account, day, amount, type_of_trans, description)
            elif opt[0] == "remove":
                changes = 1
                if len(opt) == 2:
                    if opt[1] == "in" or opt[1] == "out":
                        type_of_trans = opt[1]
                        account = ui_remove_type(account, type_of_trans)
                    elif int(opt[1]):
                        day = int(opt[1])
                        account = ui_remove_day(account, day)
                elif len(opt) == 4 and opt[2] == "to":
                    day_start = int(opt[1])
                    day_end = int(opt[3])
                    account = ui_remove_period(account, day_start, day_end)
            elif opt[0] == "replace" and len(opt) == 5 and opt[3] == "with":
                changes = 1
                day = int(opt[1])
                type_of_trans = opt[2]
                description = opt[3]
                new_amount = int(opt[5])
                account = ui_replace(account, day, type_of_trans, description, new_amount)
            elif opt[0] == "list":
                changes = 0
                if len(opt) == 1:
                    ui_list(account)
                elif len(opt) == 2:
                    type_of_transactions = opt[1]
                    ui_list_type(account, type_of_transactions)
                elif opt[1] == "balance" and len(opt) == 3 and int(opt[2]):
                    day = int(opt[2])
                    ui_balance(account, day)
                elif opt[1] in "<=>" and len(opt) == 3 and int(opt[2]):
                    value = int(opt[2])
                    symbol = opt[1]
                    ui_list_value(account, symbol, value)

            elif opt[0] == "filter":
                changes = 1
                if len(opt) == 2 and opt[1] in "inout":
                    type_of_transactions = opt[1]
                    account = ui_filter_type(account, type_of_transactions)
                elif len(opt) == 3 and opt[1] in "inout" and int(opt[2]):
                    type_of_transactions = opt[1]
                    value = int(opt[2])
                    account = ui_filter_type_value(account, type_of_transactions, value)
            elif opt[0] == "undo":
                changes = 0
                if len(accounthistory) >= 2:
                    accounthistory.pop()
                account = accounthistory[-1]
            else:
                print("Invalid command!")
        except:
            print("Invalid command!")
