class Customer:
    def __init__(self, first_name, last_name):
        self.fullname = first_name + " " + last_name

    def full_name(self):
        return self.fullname


t = Customer("tom", "ford")
print(t.full_name())
