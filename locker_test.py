import unittest
from locker import Password

class TestPassword(unittest.TestCase):
    '''
    Test class that defines test cases for the password class behaviour

    '''
    def setUp(self):
        '''
        Set up method to run before each test cases

        '''
        self.new_contact = Password("peter","chege","peterchege@gmail.com")

    def test_init(self):
            '''
            test_init test case to test if the object is initialized properly

            '''
            self.assertEqual(self.new_contact.first_name,"peter")
            self.assertEqual(self.new_contact.last_name,"chege")
            self.assertEqual(self.new_contact.email,"peterchege@gmail.com")

    





if __name__ == '__main__':
    unittest.main()
