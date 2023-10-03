#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions.
# The end of this file contains tests.
#
import random as rand


def get_day(account):
    return account[0]


def get_amount(account):
    return account[1]


def get_type(account):
    return account[2]


def get_descrition(account):
    return account[3]


def set_descrition(account, new_description):
    account[3] = new_description


def set_type(account, new_type):
    account[2] = new_type


def set_amount(account, new_amount):
    account[1] = new_amount


def set_day(account, new_day):
    account[0] = new_day


def generate_trans(account):
    list_of_descr = ["water", "pizza", "rent", "bills", "internet", "beer", "groceries", "coffee"]
    for i in range(10):
        description = list_of_descr[rand.randint(0, len(list_of_descr)-1)]
        type_of_trans = rand.randint(0,1)
        if type_of_trans == 1:
            type_of_trans = "out"
        else:
            type_of_trans = "in"
        add(account, rand.randint(1, 30), rand.randint(1, 3000), type_of_trans, description)


def add(account, day, amount, type_of_trans, description):
    """
    adds a transaction in the list in the current day
    :param account: list of trans
    :param day: current date
    :param amount: ammount of money
    :param type_of_trans: in/out
    :param description: what was paid or received
    :return:
    """
    try:
        account.append([day, amount, type_of_trans, description])
    except:
        raise ValueError


def insert(account, day, amount, type_of_trans, description):
    """
    inserts a transaction in the list in a chosen date
    :param account: list of trans
    :param day: chosen day
    :param amount: ammount of money
    :param type_of_trans: in/out
    :param description: what was paid or received
    :return:
    """
    try:
        account.append([day, amount, type_of_trans, description])
    except:
        raise ValueError


def remove_day(account, day):
    """
    this function removes transactions from a certain day
    :param account: list of transactions
    :param day: given day
    :return:processed list of transations
    """
    try:
        i = 0
        while i < len(account):
            if day == get_day(account[i]):
                account.pop(i)
                i -= 1
            i += 1
        return account
    except:
        raise ValueError


def remove_period(account, day_start, day_finish):
    """
    function removes transactions from a given interval of days
    :param account: list of trans
    :param day_start: start day
    :param day_finish: end day
    :return:processed list of transations
    """
    try:
        i = 0
        while i < len(account):
            if day_finish >= get_day(account[i]) >= day_start:
                account.pop(i)
                i -= 1
            i += 1
        return account
    except:
        raise ValueError

def remove_type(account, type):
    """
    function removes transactions of a certain type
    :param account: list of transactions
    :param type: given type in/out
    :return:processed list of transations
    """
    try:
        i = 0
        while i < len(account):
            if get_type(account[i]) == type:
                account.pop(i)
                i -= 1
            i += 1
        return account
    except:
        raise ValueError


def replace_value(account, day, type_of_trans, description, new_amount):
    """
    this function identifies a transaction based on its day, type and description and replaces its value with a new one
    :param account: list of transactions
    :param day: given day
    :param type_of_trans: given type of transaction
    :param description: description
    :param new_amount: new value to be replaced
    :return: processed list of transations
    """
    try:
        for i in account:
            if get_day(i) == day and get_type(i) == type_of_trans and get_descrition(i) == description:
                set_amount(i, new_amount)
        return account
    except:
        raise ValueError


def filter_type(account, type):
    """
    this function deletes all the transactions of a different type than the given one
    :param account: list of transactions
    :param type: given type
    :return: processed list of transations
    """
    try:
        i = 0
        while i < len(account):
            if get_type(account[i]) != type:
                account.pop(i)
                i -= 1
            i += 1
        return account
    except:
        raise ValueError


def filter_type_value(account, type, value):
    """
    this function deletes all the transactions of a different type than the given one and of a lower value
    than the given one
    :param account: list of transactions
    :param type: given type
    :param value: given limit amount
    :return:processed list of transations
    """
    try:
        i = 0
        while i < len(account):
            if get_type(account[i]) != type or get_amount(account[i]) >= value:
                account.pop(i)
                i -= 1
            i += 1
        return account
    except:
        raise ValueError


def test_add_transaction():
    account = []
    add(account, 7, 5, "in", "compensation")
    assert account[0][1] == 5


test_add_transaction()


def test_insert_transaction():
    account = []
    add(account, 3, 150, "out", "bills")
    add(account, 7, 350, "out", "food")
    insert(account, 5, 500, "in", "salary")
    assert account[2][2] == "in"


test_insert_transaction()


def test_remove_day():
    account = []
    add(account, 7, 5, "in", "compensation")
    add(account, 17, 900, "in", "salary")
    remove_day(account, 7)
    assert account[0][1] == 900

test_remove_day()

def test_remove_period():
    account = []
    add(account, 7, 5, "in", "compensation")
    add(account, 17, 900, "in", "salary")
    add(account, 23, 1005, "out", "debt")
    add(account, 27, 223, "in", "salary")
    remove_period(account, 15, 26)
    assert account[1][1] == 223


test_remove_period()


def test_remove_type():
    account = []
    generate_trans(account)
    remove_type(account, "out")
    for i in account:
        assert i[2] == "in"

test_remove_type()


def test_replace():
    account = []
    add(account, 7, 500, "in", "birthday")
    replace_value(account, 7, "in", "birthday", 700)
    assert account[0][1] == 700
    replace_value(account, 7, "out", "not_birthday", 600)
    assert account[0][1] == 700


test_replace()