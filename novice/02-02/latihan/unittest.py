symbol=[('M',1000),('C',900),('D',500),('C D',400),('C',100),('X C',90),('L',50),('X L',40),('X',10),('I X',9),('V',5),('I V',4),('I',1)]

def romannumeral(number):
    outstring = ""
    while number >0:
        for symbol, value in symbol:
            if number-value >=0:
                outstring += symbol
                number = number-value
                continue
    return outstring

class Test(unittest.TestCase):
    def test_9(self):
        self.assertEqual(romannumeral(9),"IX")
    def test_29(self):
        self.assertEqual(romannumeral(29),"XXIX")
    def test_707(self):
        self.assertEqual(romannumeral(707),"DCCVII")
    def tes_1800(self):
        self.assertEqual(romannumeral(1800),"MDCCC")

if __name__== '__main__':
    number_in = raw_input("Enter a number")
    romannumeral(int(number_in))