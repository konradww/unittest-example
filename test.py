import unittest
from employee import Employee
class TestEmployee(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.employee1  = Employee('Janusz', 'Kowalski', 10000)
        self.employee2 = Employee('Martynka', 'Jasic', 20000)
        self.employee3 = Employee('Edward', 'Kolonko', 15000)

    def tearDown(self):
        pass
        
    def test_email(self):
        # self.employee1  = Employee('Janusz','Kowalski',10000)
        # self.employee2 = Employee('Martynka', 'Jasic', 20000)
        # self.employee3 = Employee('Edward', 'Kolonko', 15000)

        self.assertEqual(self.employee1.email,'Janusz.Kowalski@email.com')
        self.assertEqual(self.employee2.email, 'Martynka.Jasic@email.com')
        self.assertEqual(self.employee3.email, 'Edward.Kolonko@email.com')

    def test_fullname(self):
        # self.employee1  = Employee('Janusz', 'Kowalski', 10000)
        # self.employee2 = Employee('Martynka', 'Jasic', 20000)
        # self.employee3 = Employee('Edward', 'Kolonko', 15000)

        self.assertEqual(self.employee1.fullname, 'Janusz Kowalski')
        self.assertEqual(self.employee2.fullname, 'Martynka Jasic')
        self.assertEqual(self.employee3.fullname, 'Edward Kolonko')

        self.employee1.first = 'Test'
        self.employee1.last = 'Test'

        self.assertEqual(self.employee1.fullname, 'Test Test')

    def test_apply_raise(self):
        # self.employee1  = Employee('Janusz', 'Kowalski', 10000)
        # self.employee2 = Employee('Martynka', 'Jasic', 20000)
        # self.employee3 = Employee('Edward', 'Kolonko', 15000)

        self.employee1.apply_raise()
        self.employee2.apply_raise()
        self.employee3.apply_raise()

        self.assertEqual(self.employee1.pay,11500)
        self.assertEqual(self.employee2.pay,23000)
        self.assertEqual(self.employee3.pay,17250)

#
# if __name__ == '__main__':
#     unittest.main()









