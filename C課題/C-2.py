class Customer:
    def __init__(self, first_name, last_name, age):
        self.age = age
        self.fullname = first_name + " " + last_name

    def full_name(self):
        return self.fullname


t = Customer("tom", "ford", 17)
print(t.age)

p = Customer("Arnold", "Schwa", 74)
print(p.age)
