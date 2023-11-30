import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program"""
        input = """
                    class Program {
                        func @main():void {
                            var i: [5]int = [1.1,2.2,null];
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

