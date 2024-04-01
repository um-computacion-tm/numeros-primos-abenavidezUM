import unittest

def prime(num):
    for x in range(2, num):
        if num % x == 0:
            print("No es primo")
            return False 
    print("Es primo")
    return True 



class TestIsPrime(unittest.TestCase):
    def test_with_1(self):
        result = prime(1)
        self.assertTrue(result)
    
    def test_with_2(self):
        result = prime(2)
        self.assertTrue(result)
    
    def test_with_3(self):
        result = prime(3)
        self.assertTrue(result)
    
    def test_with_4(self):
        result = prime(4)
        self.assertFalse(result)
    
    def test_with_5(self):
        result = prime(5)
        self.assertTrue(result)

unittest.main()