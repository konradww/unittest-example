import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def email_test(self):
        employee1 = Employee('Janusz','Kowalski',10000)

        self.assertEqual(employee1.email,'Janusz.Kowalski@email.com')



