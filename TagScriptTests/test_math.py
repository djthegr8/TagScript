import TagScriptEngine
from unittest import TestCase

class test_math_functionality(TestCase):

    def setUp(self):
        """ Sets up engine and other variables that might be needed between tests """
        self.engine = TagScriptEngine.Engine()
    def tearDown(self):
        """ Cleans the plate to make tests consistent """
        self.engine.Clear_Variables()
        self.engine = None

    # Actual tests below
    # ======

    def test_weird_math(self):
        """Had problems with numbers like these."""
        self.engine.Add_Variable("unix", "1504891344.454338")
        self.engine.Process("m{$unix/10 - 1504891220}")

    def test_negative_math(self):
        """Should handle negative math with some grace."""
        self.assertEqual(self.engine.Process("m{10-20}"), "-10.0")

    def test_basic_math(self):
        """Basic math, adds 10 and 10 to see if it returns 20."""
        self.assertEqual(self.engine.Process("m{10+10}"), "20.0", "adds 10 and 10")

    def test_basic_float_math(self):
        """Basic float math"""
        self.assertEqual(self.engine.Process("m{1/2}"), "0.5", "can divide into fractions")

    def test_advanced_math(self):
        """Advanced math, has nested math expressions that should add up to 40"""
        exp = "m{(10+10)+10+10}"
        self.assertEqual(self.engine.Process(exp), "40.0", "adds complex nested math")

    def test_basic_operators(self):
        """Basically a check for all the operators I'd expect to work"""
        exp = "m{100-9*2}"
        self.assertEqual(self.engine.Process(exp), "82.0")

        exp = "m{100+110}"
        self.assertEqual(self.engine.Process(exp), "210.0")

    def test_apply_order(self):
        """Should apply math in the correct order."""
        self.assertEqual(self.engine.Process("m{10*30^2}"), "9000.0", "applies correct order")

    def test_variable_math(self):
        """Should have no problem using a number provided through variables."""
        phrase = self.engine.Process("""!{x=100}\nm{$x+1}""")
        self.assertEqual(phrase, "101.0")