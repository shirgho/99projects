import unittest
import weather

class testWeatherFunctions(unittest.TestCase):

    def setUp(self):
        self.retrievedIP = "<html><head><title>Current IP Check</title></head><body>Current IP Address: 58.186.207.117</body></html>"

    def test_parseIP(self):
        self.myIP = weather.parseIP(self.retrievedIP)
        self.assertEqual(self.myIP, "58.186.207.117")

if __name__ == '__main__':
    unittest.main()
        
        
