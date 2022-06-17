import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is 'Bonjour'.
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')  # test when 'Goodbye' is given as input the output is 'Au revoir'.
        self.assertNotEqual(english_to_french('Hello'), 'Au revoir')  # test when 'Hello' is given as input the output is not 'Au revoir'.

        self.assertIsNone(english_to_french(None)) # test when None is given as input

        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye') # test when 'Au revoir' is given as input the output is 'Goodbye'.
        self.assertNotEqual(french_to_english('Au revoir'), 'Hello') # test when 'Au revoir' is given as input the output is not 'Hello'.

        self.assertIsNone(french_to_english(None)) # test when None is given as input



unittest.main()