class Customer:
    def __init__(self, first_name, last_name, age):
        self.fullname = first_name + " " + last_name
        self.age = age
        if self.age <= 3:
            self.entry_tree = 0

        elif self.age < 20:
            self.entry_tree = 1000

        elif 20 >= self.age < 65:
            self.entry_tree = 1500

        else:
            self.entry_tree = 1200

    def full_name(self):
        return self.fullname

    def info_csv(self):
        return ','.join([self.fullname, str(self.age), str(self.entry_tree)])


t = Customer("Tom", "Ford", 3)
print(t.info_csv())

p = Customer("Give", "Me", 4)
print(p.info_csv())
