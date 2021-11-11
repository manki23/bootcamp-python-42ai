class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        if self.check_corruption(account):
            print("Error: corrupted account")
        else:
            self.account.append(account)

    def check_transfer_arguments(self, origin, dest, amount):
        if not type(origin) in [int, str]:
            print("InputError: origin must be int(id) or str(name)")
            return False
        elif not type(dest) in [int, str]:
            print("InputError: dest must be int(id) or str(name)")
            return False
        elif not isinstance(amount, float) or amount <= 0:
            print("InputError: amount must be a strictly positive float")
            return False
        else:
            return True

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest: int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        if self.check_transfer_arguments(origin, dest, amount):
            origin_account = self.get_account_in_bank(origin)
            dest_account = self.get_account_in_bank(dest)
            print(f"Attempting transfert...")
            if (
                not isinstance(origin_account, Account) or
                not isinstance(dest_account, Account) or
                self.check_corruption(origin_account) or
                self.check_corruption(dest_account) or
                origin_account.value < amount
            ):
                if (
                    isinstance(origin_account, Account) and
                    origin_account.value < amount
                ):
                    print(f"Not enough money in origin account to make this "
                          + "transfert: {origin_account.value} < {amount}")
                else:
                    print("Error: data corrupted, transfer canceled")
                return False
            else:
                origin_account.transfer(-amount)
                dest_account.transfer(amount)
                print("Transfert successfully done !")
                return True
        else:
            return False

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return True if success, False if an error occured
        """
        bank_acc = self.get_account_in_bank(account)
        if bank_acc is None:
            print(f"InputError: account <{account}> not found.")
            return
        fix_account_data(bank_acc)

    def fix_account_data(self, account):
        print("Attempting to fix <{account}> bank account...")
        retry = 0
        while retry < 3 and self.is_corrupted(account):
            if any(attr.startswith('b') for attr in account.__dict__.keys()):
                dict_account_copy = dict(account.__dict__.items())
                for (key, value) in dict_account_copy.items():
                    if key.startswith('b'):
                        print(f"Forbiden key found: [{key}], deleting it...")
                        delattr(account, key)
                        print(f"Key <{key}> deleted")
            account_keys = account.__dict__.keys()
            if not any(attr.startswith('zip') for attr in account_keys):
                print("Error found: no attribute starting with <zip> found")
                print("Creating one.")
                account.zip = 0
            account_keys = account.__dict__.keys()
            if not any(attr.startswith('addr') for attr in account_keys):
                print("Error found: no attribute starting with <addr> found")
                print("Creating one.")
                account.addr = ""
            if not any(attr == 'id' for attr in account.__dict__.keys()):
                print("Error found: no attribute <id> found, creating one")
                account.id = account.ID_COUNT
            if not any(attr == 'name' for attr in account.__dict__.keys()):
                print("Error found: no attribute <name> found, creating one")
                name = input("Choose name:\n>> ")
                if len(name) > 0:
                    account.name = name
                else:
                    print("Error: name cannot be empty.")
            if not any(attr == 'value' for attr in account.__dict__.keys()):
                print("Error found: no attribute <value> found, creating one")
                value = input("Choose bank account value:\n>> ")
                if value.isnumeric():
                    account.value = int(value)
                else:
                    print("Error: value must be a positive number.")
            if len(account.__dict__) % 2 == 0:
                print("Error found: even number of account attributes:")
                print(account.__dict__)
                print("Choose a key of an attribute to delete:")
                del_attr_name = input(">> ")
                if del_attr_name not in account.__dict__.keys():
                    print("InputError: this attribute doesn't exists")
                elif del_attr_name in ['id', 'name', 'value']:
                    print("InputError: you cannot delete attributes "
                          + "<id>, <name> and <value>")
                else:
                    delattr(account, del_attr_name)
                    print(f"Attribute <{del_attr_name}> deleted")
            retry += 1
        if retry == 3 and self.is_corrupted(account):
            print(f"Failure: fix of account <{account.name}> data failed.")

    def is_corrupted(self, account):
        if not isinstance(account, Account):
            return True
        account_keys = account.__dict__.keys()
        if (
            len(account.__dict__) % 2 == 0 or
            any(attr.startswith('b') for attr in account_keys) or
            not any(attr.startswith('zip') for attr in account_keys) or
            not any(attr.startswith('addr') for attr in account_keys) or
            not any(attr in ['id', 'name', 'value'] for attr in account_keys)
        ):
            return True
        else:
            return False

    def check_corruption(self, account):
        if self.is_corrupted(account):
            self.fix_account_data(account)
            if self.is_corrupted(account):
                return True
            else:
                return False
        else:
            return False

    def get_account_in_bank(self, account_name_or_id):
        if isinstance(account_name_or_id, str):
            name = account_name_or_id
            for elem in self.account:
                if elem.name == name:
                    return elem
        elif isinstance(account_name_or_id, int):
            id = account_name_or_id
            for elem in self.account:
                if elem.id == id:
                    return elem
        else:
            print(f"InputError: account <{account_name_or_id}>"
                  + "doesn't exist in this bank.")
            return None
