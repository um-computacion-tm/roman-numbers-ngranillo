import unittest


#solucion del profe con diccionario
def decimal_to_roman(decimal):
    x = decimal
    y=0
    num={"1":"I",
       "2":"II",
       "3":"III",
       "4":"IV",
       "5":"V",
       "6":"VI",
       "7":"VII",
       "8":"VIII",
       "9":"IX",
       "10":"X",
       "50":"L",
       "100":"C",
       "500":"D",
       "1000":"M"
        }
    if decimal <= 10:
        romans=num[str(decimal)]
    while x >= 10:
        x= decimal - 10
        y=y+1
    if y == 4:
        romans = "XL"
    if 6 <= y <= 8:
        y = y - 5
        romans = num["50"] + (num["10"] * y)
    return romans



#def decimal_to_roman(decimal):
#    I = "I" * decimal
#    X = "I" * 5
#    if decimal == 5:
#        I = "V"
#    elif 5 <= decimal <= 8:
#        I = I - X
#        I = "v" + I
#    elif decimal == 10:
#        I = "X"
#    return I


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
        


if  __name__ == "__main__":
    unittest.main()