import unittest
from decimal_to_roman import decimal_to_roman


class TestDecimalToRoman(unittest.TestCase):
    
    def test_1 (self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, "I")
    
    def test_10 (self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, "X")
    
    def test_5(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, "V")
    
    def test_2(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, "II")
    
    def test_3(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, "III")
    
    def test_6(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, "VI")
    
    def test_7(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado, "VII")
    
    def test_4(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, "IV")

    def test_9(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, "IX")

    def test_10(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, "X")

    def test_40(self):
        resultado = decimal_to_roman(40)
        self.assertEqual(resultado, "XL")
    
    def test_60(self):
        resultado = decimal_to_roman(60)
        self.assertEqual(resultado, "LX")
    
    def test_66(self):
        resultado = decimal_to_roman(66)
        self.assertEqual(resultado, "LXVI")

    def test_90(self):
        resultado = decimal_to_roman(90)
        self.assertEqual(resultado, "XC")
    
    def test_99(self):
        resultado = decimal_to_roman(99)
        self.assertEqual(resultado, "XCIX")
    
    def test_100(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, "C")
    
    def test_200(self):
        resultado = decimal_to_roman(200)
        self.assertEqual(resultado, "CC")
    
    def test_400(self):
        resultado = decimal_to_roman(400)
        self.assertEqual(resultado, "CD")
    
    def test_500(self):
        resultado = decimal_to_roman(500)
        self.assertEqual(resultado, "D")
    
    def test_600(self):
        resultado = decimal_to_roman(600)
        self.assertEqual(resultado, "DC")
    
    def test_700(self):
        resultado = decimal_to_roman(700)
        self.assertEqual(resultado, "DCC")
    
    def test_900(self):
        resultado = decimal_to_roman(900)
        self.assertEqual(resultado, "CM")
    
    def test_999(self):
        resultado = decimal_to_roman(999)
        self.assertEqual(resultado, "CMXCIX")
    
    def test_1000(self):
        resultado = decimal_to_roman(1000)
        self.assertEqual(resultado, "M")
    
    
if  __name__ == "__main__":
    unittest.main()