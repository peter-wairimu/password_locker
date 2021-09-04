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
        self.new_user = Password("peter chege","wairimu254")

    def test_init(self):
            '''
            test_init test case to test if the object is initialized properly

            '''
            self.assertEqual(self.new_user.username,"peter chege")
            self.assertEqual(self.new_user.password,"wairimu254")
           
            

    











if __name__ == '__main__':
    unittest.main()
