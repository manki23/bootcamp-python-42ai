### Install miniconda3 and packages jupyter, numpy & pandas
``` bash
https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
cd miniconda3/bin
./conda install -y "jupyter" "numpy" "pandas"
```


### To correct module01/ex05
``` python
# dir(Account)
# print(dir(Account))
bank1 = Bank()
# account1 = Account('Myriam', {'zip': '75', 'address': 'address', 'id': 1, 'value': None})
account1 = Account('user1', **{'zip': '75', 'address': 'address', 'value': 30.0})
account2 = Account('user2', **{'zip': '75', 'address': 'address', 'value': 30.0})
account3 = Account('user3', **{'zip': '75', 'address': 'address', 'value': None})
account4 = Account('user4', **{'zip': '75', 'address': 'address', 'value': None})

account1.transfer(-50)


bank1.add(account1)
bank1.add(account2)
bank1.add(account3)
bank1.add(account4)

del account2.name

print(bank1.transfer(1, 2, 10.0))

# print(account1.__dict__)
# print(len(account1.__dict__))
```