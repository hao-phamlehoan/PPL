import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        input = """
                    var i: [5]int = [1.1,2.2,3.3] ; 
                """
        expect = "____a,,,a_b,:,boolean,=,true,,,false,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 101))
