class Customer:
    def __init__(self, first_name, last_name, age):
        self.age = age
        self.fullname = first_name + " " + last_name

    def full_name(self):
        return self.fullname

    def entry_fee(self):
        if self.age < 20:
            result = 1000
        elif 20 >= self.age < 65:
            result = 1500
        else:
            result = 1200
        return result


t = Customer("tom", "ford", 20)
print(t.entry_fee())

o = Customer("flanky", "dejo", 19)
print(o.entry_fee())

p = Customer("Arnold", "Schwa", 65)
print(p.entry_fee())
