class Employee:
    """unitest"""
    raiseForEmployees = 1.15

    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.last,self.first)

    @property
    def fullname(self):
        return '{} {}'.format(self.last, self.first)

    def apply_raise(self):
        self.pay = int(self.pay * self.raiseForEmployees)







