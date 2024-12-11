import logging
import unittest

#logging.basicConfig(filename="Testing.log",filemode="a",format="%(name)s %(levelname)s")

#logging.critical("this me from python code")

class MyTestCase9(unittest.TestCase) :
    def testOne(self):
        self.assertTrue(100 > 90 ,"Should be true")
    def testTow(self):
        self.assertEqual(40 +60 , 100 , "Should be 100")
    def testThree(self):
        self.assertGreater(100, 90, "Should be true")
if __name__ == "__main__" :
    unittest.main()