class Customer:
    def __init__(self, first_name, last_name, age):
        self.fullname = first_name + " " + last_name
        self.age = age
        if self.age < 4:
            self.entry_tree = 0

        elif self.age < 20:
            self.entry_tree = 1000

        elif self.age < 65:
            self.entry_tree = 1500

        elif self.age < 75:
            self.entry_tree = 1200

        else:
            self.entry_tree = 500

    def full_name(self):
        return self.fullname

    def info_csv(self):
        return '\t'.join([self.fullname, str(self.age), str(self.entry_tree)])


t = Customer("Tom", "Ford", 45)
print(t.info_csv())

p = Customer("Ken", "Tanaka", 35)
print(p.info_csv())

z = Customer("Kezi", "Tanaka", 35)
print(z.info_csv())

q = Customer("Kezi", "Tanakao", 35)
print(q.info_csv())

w = Customer("Ieyasu", "Tokugawa", 12)
print((w.info_csv()))
