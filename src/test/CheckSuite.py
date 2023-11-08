import unittest
from TestUtils import TestChecker
from AST import *
 
class CheckSuite(unittest.TestCase):
    def test_redeclared_class(self):
        input = """class a {} class b {} class a {}"""
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_attribute(self):
        input = """class a {var a:int;var c:int;var c:int;}"""
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_3(self):
        input = """ class a {var a:int;var c:int;}
                    class b {var a:int;var c:int;var c:int;}
                """
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,402))
    def test_4(self):
        input = """ class a {var a:int;var c:int;}
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,403))
    def test_5(self):
        input = """class a {
                    func main():int {
                        
                    }
                    func main(): float {
                        
                    }
                }"""
        expect = "Redeclared Method: main"
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_6(self):
        input = """class a {
                    func main(): int {
                        
                    }
                    var main: int;
                }"""
        expect = "Redeclared Attribute: main"
        self.assertTrue(TestChecker.test(input,expect,405))
    def test_7(self):
        input = """ class a {var a:int;var c:int;}
                    class b {var a:int;var c:int;}
                    class Program {
                        func @main(): int {
                            
                        }
                    }
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,406))
    def test_8(self):
        input = """ class a {var a:int;var c:int;}
                    class b {var a:int;var c:int;}
                    class test {
                        func @main(): void {
                            
                        }
                    }
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,407))
    def test_9(self):
        input = """ class a {var a:int;var c:int;}
                    class b {var a:int;var c:int;}
                    class Program {
                        func @main(): void {
                            
                        }
                    }
                """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input,expect,408))
    def test_2(self):
        input = """ class a {var a:int;var c:int;}
                    class b {var a:int;var c:int;}
                    class c {var a:int;var c:int;}
                    class d {var a:int;var c:int;}
                    class a {var a:int;var c:int;} 
                """
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,409))
        
    def test_10(self):
        input = """ class Program1 {
                        func getArea():int {
                            return self.length * self.width;
                        }
                        func getArea():int {
                            return self.length * self.width;
                        }
                    }
                    class Program {
                        func @main():void {
                            io.@writeInt(Shape.@numOfShape);
                        }
                    }
                """
        expect = "Redeclared Method: getArea"
        self.assertTrue(TestChecker.test(input,expect,410))
    def test_11(self):
        input = """class Program1 {
                        func getArea():int {
                            return self.length * self.width;
                        }
                        const getArea: string;
                    }
                    class Program {
                        func @main():void {
                            io.@writeInt(Shape.@numOfShape);
                        }
                    }
                """
        expect = "Redeclared Attribute: getArea"
        self.assertTrue(TestChecker.test(input,expect,411))
    def test_12(self):
        input = """class Program {
                        func getArea():int {
                            return self.length * self.width;
                        }
                        
                    }
                    class Program {
                        func @main():void {
                            io.@writeInt(Shape.@numOfShape);
                        }
                    }
                """
        expect = "Redeclared Class: Program"
        self.assertTrue(TestChecker.test(input,expect,412))
    def test_13(self):
        input = """
                    class Program {
                        func constructor() {
                            
                        }
                        func constructor() {
                            
                        }
                        func @main():void {
                            io.@writeInt(Shape.@numOfShape);
                        }
                    }
                """
        expect = "Redeclared Method: constructor"
        self.assertTrue(TestChecker.test(input,expect,413))
    def test_14(self):
        input = """ class Program {
                        func constructor() {
                            
                        }
                        func constructor(a: int) {
                            
                        }
                        func @main():void {
                            io.@writeInt(Shape.@numOfShape);
                        }
                        var @abc: int;
                        var @main: string;
                    }
                """
        expect = "Redeclared Attribute: @main"
        self.assertTrue(TestChecker.test(input,expect,414))
    def test_15(self):
        input = """class Program {
                        func constructor() {
                            
                        }
                        func constructor(a: int) {
                            
                        }
                        func constructor(a,b: int) {
                            
                        }
                        func @main():void {
                            io.@writeInt(Shape.@numOfShape);
                        }
                        var @abc: int;
                        var @main: string;
                    }
                """
        expect = "Redeclared Attribute: @main"
        self.assertTrue(TestChecker.test(input,expect,415))
    def test_16(self):
        input = """ class a {var a:int;var c:int;}
                    class b {var a:int;var c:int;}
                    class Program {
                        func @main(a:float): void {
                            
                        }
                    }
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,416))
    def test_17(self):
        input = """ class a {var a:int;var c:int;}
                    class b {var a:int;var c:int;}
                    class Program {
                        func main(): void {
                            
                        }
                    }
                """
        expect = "No Entry Point"
    def test_18(self):
        input = input = """class Program {
                        func constructor() {
                            
                        }
                        func constructor(a: int) {
                            
                        }
                        func constructor(a,b: int) {
                            
                        }
                        func constructor(a,b: int, c:float) {
                            
                        }
                        func @main():void {
                            io.@writeInt(Shape.@numOfShape);
                        }
                        var @abc: int;
                        var @main: string;
                    }
                """
        expect = "Redeclared Attribute: @main"
        self.assertTrue(TestChecker.test(input,expect,418))
    def test_19(self):
        input = """class a {var a:int;var c:int;}
                    class b {var a:int;var c:int;const d:int;}
                    class c {var a:int;var c:int;const e:int;}
                    class d {
                        const a:int;
                        var d:int;
                        const d:int;}
                """
        expect = "Redeclared Attribute: d"
        self.assertTrue(TestChecker.test(input,expect,419))
    
    # def test_redeclared_class_with_ast(self):
    #     input = Program([ClassDecl(Id("a"),[]),ClassDecl(Id("b"),[]),ClassDecl(Id("a"),[])])
    #     expect = "Redeclared Class: a"
    #     self.assertTrue(TestChecker.test(input,expect,402))
    # def test_redeclared_attribute_with_ast(self):
    #     input = Program([ClassDecl(Id("a"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType()))])])
    #     expect = "Redeclared Attribute: c"
    #     self.assertTrue(TestChecker.test(input,expect,404))    
    