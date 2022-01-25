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


t = Customer("Tom", "Ford", 3)
print(t.entry_tree)

p = Customer("Ken", "Tanaka", 4)
print(p.entry_tree)

z = Customer("Kezi", "Tanaka", 74)
print(z.entry_tree)

q = Customer("Kezi", "Tanakao", 75)
print(q.entry_tree)

w = Customer("Ieyasu", "Tokugawa", 12)
print(w.entry_tree)
