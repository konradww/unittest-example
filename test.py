import unittest
from employee import Employee
class TestEmployee(unittest.TestCase):

    def test_email(self):
        employee1 = Employee('Janusz','Kowalski',10000)
        employee2 = Employee('Martynka', 'Jasic', 20000)
        employee3 = Employee('Edward', 'Kolonko', 15000)

        self.assertEqual(employee1.email,'Janusz.Kowalski@email.com')
        self.assertEqual(employee2.email, 'Martynka.Jasic@email.com')
        self.assertEqual(employee3.email, 'Edward.Kolonko@email.com')

    def test_fullname(self):
        employee1 = Employee('Janusz', 'Kowalski', 10000)
        employee2 = Employee('Martynka', 'Jasic', 20000)
        employee3 = Employee('Edward', 'Kolonko', 15000)

        self.assertEqual(employee1.fullname, 'Janusz Kowalski')
        self.assertEqual(employee2.fullname, 'Martynka Jasic')
        self.assertEqual(employee3.fullname, 'Edward Kolonko')

        employee1.first = 'Test'
        employee1.last = 'Test'

        self.assertEqual(employee1.fullname, 'Test Test')

    def test_apply_raise(self):
        employee1 = Employee('Janusz', 'Kowalski', 10000)
        employee2 = Employee('Martynka', 'Jasic', 20000)
        employee3 = Employee('Edward', 'Kolonko', 15000)

        employee1.apply_raise()
        employee2.apply_raise()
        employee3.apply_raise()

        self.assertEqual(employee1.pay,11500)
        self.assertEqual(employee2.pay,23000)
        self.assertEqual(employee3.pay,17250)

#
# if __name__ == '__main__':
#     unittest.main()









