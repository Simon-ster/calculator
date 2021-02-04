import unittest
import calc as c

class TestCase(unittest.TestCase):

    #addition
    def test_add1(self):
        self.assertEqual(c.add(2, 1),3)

    def test_add2(self):
        self.assertEqual(c.add(3, 1.1),4.1)

    def test_add3(self):
        self.assertEqual(c.add(-1,-4),-5)
    
    def test_add4(self):
        self.assertEqual(c.add(-1,3),2)

    #multiplication
    def test_sub1(self):
        self.assertEqual(c.multiply(2, 1),2)

    def test_mul2(self):
        self.assertEqual(c.multiply(3, 1.1),3.3)

    def test_mul3(self):
        self.assertEqual(c.multiply(-1,-4),4)
    
    def test_mul4(self):
        self.assertEqual(c.multiply(-1,3),-3)

    def test_mul5(self):
        self.assertEqual(c.multiply(0,3),0)

    #subtraction
    def test_sub1(self):
        self.assertEqual(c.subtract(2, 1),1)

    def test_sub2(self):
        self.assertEqual(c.subtract(3, 1.1),1.9)

    def test_sub3(self):
        self.assertEqual(c.subtract(-1,-4),3)
    
    def test_sub4(self):
        self.assertEqual(c.subtract(-1,3),-4)

    def test_sub5(self):
        self.assertEqual(c.subtract(0,3),-3)

    #division
    def test_div1(self):
        self.assertEqual(c.divide(2, 1),2)

    def test_div2(self):
        self.assertEqual(c.divide(3, 1.5),2)

    def test_div3(self):
        self.assertEqual(c.divide(-1,-4),0.25)

    def test_div4(self):
        self.assertEqual(c.divide(0,3),0)

    def test_div5(self):
        with self.assertRaises(ZeroDivisionError):
            c.divide(3,0)

if __name__ == '__main__':
    unittest.main()