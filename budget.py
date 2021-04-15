class Budget:


    def __init__(self,**categories):
        self.categories = categories


    def deposit(self,amount,category): # depositing to a category
        self.categories[category]= self.categories[category] + amount
        accountBalance = 5000
        print ('A deposit of ' + str(amount) + ' naira was made to ' + category + ' category' )
        print('Current account balance is now ' + str(accountBalance - amount) + ' naira')

    def withdraw(self,amount,category):# withdrawing from a category
        if amount > self.categories[category]:
            print ('There is not enough money in ' + self.categories[category])
        else:
            self.categories[category] = self.categories[category] - amount
            print(str(amount)+ ' naira has been withdrawn from ' + category + ' category' )

    #transfer of funds from one category to another
    def transfer(self,amount, db,cr):#db represents category performing debit and cr represents category performing credit

        if amount > self.categories[db]:
            print('There is not enough money in ' + db)
        else:
            self.categories[db] = self.categories[db] - amount
            self.categories[cr] = self.categories[cr] + amount
            print(str(amount) + ' naira was transferred from ' + db + ' category to ' +cr + ' category')

    #Available balance left after transaction
    def available_balance(self,category):#
        print ('Your ' + category + ' budget balance is ' + str(self.categories[category])+ ' naira')


budget = Budget(food=200, clothing=250, entertainment=400)
budget.deposit(500, 'food')
budget.withdraw(100, 'clothing')
budget.transfer(200, 'entertainment','food')
budget.available_balance('entertainment')
budget.available_balance('food')
budget.available_balance('clothing')