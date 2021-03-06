### Install miniconda3 and packages jupyter, numpy & pandas
``` bash
git clone git@github.com:manki23/dotfiles.git ; ./dotfiles/python_setup
```

### Dark mode on Linux 
``` bash
/usr/bin/gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'
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

### module04
Other solution for ex0 :
``` python
# data = self.df[self.df[categorical_var].notna()]
# data = data.pivot(columns=categorical_var, values=numerical_var)
# data.plot.hist(subplots=True)
# plt.xlabel(numerical_var)
self.df.hist(column=numerical_var, by=categorical_var)
plt.show()
...
# self.df.boxplot(column=numerical_var, by=categorical_var)
# plt.show()
```

## Useful links

### module00/ex00 yield, generator, comprehensions
https://realpython.com/introduction-to-python-generators/
### module03/ex04 K-means
https://realpython.com/k-means-clustering-python/