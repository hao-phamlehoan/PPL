
# MSSV 2013093

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
                        func @main(a,b: int, c:float): void {
                            
                        }
                    }
                """
        expect = "No Entry Point"
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
                        var @main: string;
                        func @main():void {
                            io.@writeInt(Shape.@numOfShape);
                        }
                        var @abc: int;
                    }
                """
        expect = "Redeclared Method: @main"
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
        self.assertTrue(TestChecker.test(input,expect,417))
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
                        const d:string;}
                """
        expect = "Redeclared Attribute: d"
        self.assertTrue(TestChecker.test(input,expect,419))
    def test_20(self):
        input = """class a {var a:int;var c:int;}
                    class b {var m:no;var c:int;const d:int;}
                    class c {var a:int;var c:int;const e:int;}
                    class d {
                        const a:int;
                        var d:int;
                        const d:int;}
                """
        expect = "Undeclared Class: no"
        self.assertTrue(TestChecker.test(input,expect,420))
    def test_21(self):
        input = """ class cl {var a:int;var c:int;}
                    class b {var a:cl;var c:int;const d:int;}
                    class c {var a:int;var c:int;const e:int;}
                    class d {
                        const a:int;
                        var d:int;
                        const d:int;}
                """
        expect = "Redeclared Attribute: d"
        self.assertTrue(TestChecker.test(input,expect,421))
    def test_22(self):
        input = """ class cl {var a:int;var c:int;}
                    class b {var a,c,c:cl;const d:int;}
                    class c {var a:int;var c:int;const e:int;}
                    class d {
                        const a:int;
                        var d:int;
                        const d:int;}
                """
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,422))
    def test_23(self):
        input = """ class cl {var a:int;var c:int;}
                    class cl <- b {var a,c:cl;const d:int;}
                    class c {var a,a:int;var c:int;const e:int;}
                """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,423))
    def test_23(self):
        input = """ class cl {var a:int;var c:int;}
                    class cl1 <- b {var a,c:cl;const d:int;}
                    class c {var a,a:int;var c:int;const e:int;}
                """
        expect = "Undeclared Class: cl1"
        self.assertTrue(TestChecker.test(input,expect,423))
    def test_24(self):
        input = """ class cl {var a:int;var c:int;}
                    class cl <- b {var a: float = self.a;}
                    class c {var a,a:int;var c:int;const e:int;}
                """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,424))
    def test_25(self):
        input = """ class cl {var a:int;var c:int;}
                    class cl <- b {var a: float = 3.4 * 5;}
                    class c {var a,a:int;var c:int;const e:int;}
                """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,425))
    def test_26(self):
        input = """ 
                    class b {var a: float = 3.4 * 5;}
                    class Program {
                        func @main():void {
                            io.@writeInt(3.6);
                        }
                    }
                """
        expect = "Type Mismatch In Statement: Call(Id(io),Id(@writeInt),[FloatLit(3.6)])"
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_27(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var a:int;
                            var b:int = a;
                            var b:float;
                        }
                    }
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_28(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var b:int = a;
                            var b:float;
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_29(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var a:int;
                            var b:int = 3*4+6.0;
                            var b:float;
                        }
                    }
                """
        expect = "Type Mismatch In Declaration: VarDecl(Id(b),IntType,BinaryOp(+,BinaryOp(*,IntLit(3),IntLit(4)),FloatLit(6.0)))"
        self.assertTrue(TestChecker.test(input,expect,429))
    def test_30(self):
        input = """ 
                    class Program {
                        func @main():void {
                            break;
                        }
                    }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_31(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var i:int;
                            for i := 0; i < 10; i := i + 1 {
                                break;
                            }
                            continue;
                        }
                    }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_32(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var i:int;
                            for i := 0; i < 10; i := i + 1 {
                            }
                            continue;
                        }
                    }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,432))
    def test_33(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var i,j:int;
                            for i := 0; i < 10; i := i + 1 {
                                if {i := 0;} j > i {
                                    j := j - 1;
                                    continue;
                                } else {j := j + 1;}
                            }
                            {
                                {
                                    
                                    continue;
                                }
                            }
                        }
                    }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,433))
    def test_34(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var i: [5]int = [1.1,2.2,3.3];
                        }
                    }
                """
        expect = "Type Mismatch In Declaration: VarDecl(Id(i),ArrayType(5,IntType),[FloatLit(1.1),FloatLit(2.2),FloatLit(3.3)])"
        self.assertTrue(TestChecker.test(input,expect,434))
    def test_35(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var i: [5]int = [1.1,2.2,null];
                        }
                    }
                """
        expect = "Illegal Array Literal: [FloatLit(1.1),FloatLit(2.2),NullLiteral()]"
        self.assertTrue(TestChecker.test(input,expect,435))
    def test_36(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var i: [5]int = [1.1,2.2,1];
                        }
                    }
                """
        expect = "Illegal Array Literal: [FloatLit(1.1),FloatLit(2.2),IntLit(1)]"
        self.assertTrue(TestChecker.test(input,expect,436))
    def test_37(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var i: [5]float = [1.1,2.2,"string"];
                        }
                    }
                """
        expect = "Illegal Array Literal: [FloatLit(1.1),FloatLit(2.2),StringLit(string)]"
        self.assertTrue(TestChecker.test(input,expect,437))
    def test_38(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var i: [5]int = [1.1,true,null];
                        }
                    }
                """
        expect = "Illegal Array Literal: [FloatLit(1.1),BooleanLit(True),NullLiteral()]"
        self.assertTrue(TestChecker.test(input,expect,438))
    def test_39(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var i: [5]int = [1,2.2];
                        }
                    }
                """
        expect = "Illegal Array Literal: [IntLit(1),FloatLit(2.2)]"
        self.assertTrue(TestChecker.test(input,expect,439))
    def test_40(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var i: [5]int = [1.2];
                        }
                    }
                """
        expect = "Type Mismatch In Declaration: VarDecl(Id(i),ArrayType(5,IntType),[FloatLit(1.2)])"
        self.assertTrue(TestChecker.test(input,expect,440))
    def test_41(self):
        input = """ 
                    class Program {
                        func @main():void {
                            const i: int;
                        }
                    }
                """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(i),IntType,None)"
        self.assertTrue(TestChecker.test(input,expect,441))
    def test_42(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var i: int = 2.3;
                        }
                    }
                """
        expect = "Type Mismatch In Declaration: VarDecl(Id(i),IntType,FloatLit(2.3))"
        self.assertTrue(TestChecker.test(input,expect,442))
    def test_43(self):
        input = """ class ABC {
                        
                    }
                    class Program {
                        func @main():void {
                            var i: ABC = null;
                            var a: ABC = 1;
                        }
                    }
                """
        expect = "Type Mismatch In Declaration: VarDecl(Id(a),ClassType(Id(ABC)),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,443))
    def test_44(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var i: bool = true;
                            var n: bool = 1;
                        }
                    }
                """
        expect = "Type Mismatch In Declaration: VarDecl(Id(n),BoolType,IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,444))
    def test_45(self):
        input = """ 
                    class A {
                        
                    }
                    class Program {
                        func @main():void {
                            var i: A ;
                            var b: A = i;
                            var i: int;
                        }
                    }
                """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,445))
    def test_46(self):
        input = """ 
                    class Program {
                        var a : int;
                        func @main():void {
                            var a: int = self.a;
                            var i,i: float;
                        }
                    }
                """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,446))
    def test_47(self):
        input = """ 
                    class Program {
                        var a : int;
                        func @main():void {
                            var a: int = a;
                            var i,i: float;
                        }
                    }
                """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,447))
    def test_48(self):
        input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[],VoidType(),Block([ConstDecl(Id("i"),VoidType(),None)]))])])
        expect = "Type Mismatch In Declaration: ConstDecl(Id(i),VoidType,None)"
        self.assertTrue(TestChecker.test(input,expect,448))
    def test_49(self):
        input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[],VoidType(),Block([VarDecl(Id("i"),VoidType())]))])])
        expect = "Type Mismatch In Declaration: VarDecl(Id(i),VoidType)"
        self.assertTrue(TestChecker.test(input,expect,449))
    def test_50(self):
        input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[VarDecl(Id("i"),VoidType())],VoidType(),Block([VarDecl(Id("i"),VoidType())]))])])
        expect = "Type Mismatch In Declaration: VarDecl(Id(i),VoidType)"
        self.assertTrue(TestChecker.test(input,expect,450))
    def test_51(self):
        input = Program([ClassDecl(Id("Program"),[AttributeDecl(VarDecl(Id("a"),VoidType())),MethodDecl(Id("@main"),[],VoidType(),Block([VarDecl(Id("i"),VoidType())]))])])
        expect = "Type Mismatch In Declaration: VarDecl(Id(a),VoidType)"
        self.assertTrue(TestChecker.test(input,expect,451))
    def test_52(self):
        input = Program([ClassDecl(Id("Program"),[AttributeDecl(ConstDecl(Id("a"),VoidType(),None)),MethodDecl(Id("@main"),[],VoidType(),Block([VarDecl(Id("i"),VoidType())]))])])
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),VoidType,None)"
        self.assertTrue(TestChecker.test(input,expect,452))       
    def test_53(self):
        input = """ 
                    class Program {
                        var a : int;
                        func @main():void {
                            var a: int = 1;
                            const b: int;
                        }
                    }
                """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(b),IntType,None)"
        self.assertTrue(TestChecker.test(input,expect,453))
    def test_54(self):
        input = """ 
                    class Program {
                        const b: int;
                        var a : int;
                        func @main():void {
                            var a: int = a;
                            var i,i: float;
                        }
                    }
                """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(b),IntType,None)"
        self.assertTrue(TestChecker.test(input,expect,454))
    def test_55(self):
        input = """ 
                    class Program {
                        func sum(): int {
                            return 1;
                        }
                        func @main():void {
                            var a: int = self.sum();
                            var i,i: float;
                        }
                    }
                """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,455))
    def test_56(self):
        input = """ 
                    class Program {
                        func sum(): float {
                            return 1.1;
                        }
                        func @main():void {
                            var a: int = self.sum();
                            var i,i: float;
                        }
                    }
                """
        expect = "Type Mismatch In Declaration: VarDecl(Id(a),IntType,CallExpr(Self(),Id(sum),[]))"
        self.assertTrue(TestChecker.test(input,expect,456))
    def test_57(self):
        input = """ 
                    class Program {
                        func sum(): void {
                            return 1.1;
                        }
                        func @main():void {
                            var a: int = self.sum();
                            var i,i: float;
                        }
                    }
                """
        expect = "Type Mismatch In Statement: Return(FloatLit(1.1))"
        self.assertTrue(TestChecker.test(input,expect,457))
    def test_58(self):
        input = """ 
                    class Program {
                        func sum(): void {
                            return;
                        }
                        func @main():void {
                            var a: int = self.sum();
                            var i,i: float;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: CallExpr(Self(),Id(sum),[])"
        self.assertTrue(TestChecker.test(input,expect,458))
    def test_59(self):
        input = """ 
                    class Program {
                        func sum(): void {
                            return;
                        }
                        func @main():void {
                            var a: string = "123";
                            { 
                                var a: int;
                                { 
                                    var a: int;
                                }
                                { 
                                    var a: int;
                                }
                            }
                            var i,i: float;
                        }
                    }
                """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,459))
    def test_60(self):
        input = """ 
                    class Program {
                        func sum(): void {
                            return;
                        }
                        func @main():void {
                            var a: string = "123";
                            { 
                                var a: int = a;
                                { 
                                    var a: int;
                                }
                                { 
                                    var a: int;
                                }
                            }
                            var i,i: float;
                        }
                    }
                """
        expect = "Type Mismatch In Declaration: VarDecl(Id(a),IntType,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,460))
    def test_61(self):
        input = """ 
                    class Program {
                        func sum(): void {
                            return;
                        }
                        func @main():void {
                            var a: string = "123";
                            { 
                                var a: int;
                                { 
                                    var a: int = a;
                                }
                                { 
                                    var a: int = a;
                                }
                            }
                            var i,i: float;
                        }
                    }
                """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,461))
    def test_62(self):
        input = """ 
                    class Program {
                        func sum(): void {
                            return;
                        }
                        func @main():void {
                            var a: string = "123";
                            { 
                                var a: int;
                                { 
                                    var a: int = a;
                                }
                                { { { 
                                    var a: int = a;
                                } } }
                            }
                            var i,i: float;
                        }
                    }
                """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,462))
    def test_63(self):
        input = """ 
                    class Program {
                        func sum(): void {
                            return;
                        }
                        func @main():void {
                            var a: string = "123";
                            { 
                                { 
                                    var a: int = 1;
                                }
                                { { { {
                                    var a: int = a;
                                } } } }
                            }
                            var i,i: float;
                        }
                    }
                """
        expect = "Type Mismatch In Declaration: VarDecl(Id(a),IntType,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,463))
    def test_64(self):
        input = """ 
                    class Program {
                        func sum(): void {
                            return;
                        }
                        func @main():void {
                            var a: string = "123";
                            { 
                                var a: int;
                                { 
                                    var a: int;
                                }
                                { { { {
                                    var a: int = a;
                                } } } }
                                const a: int;
                            }
                        }
                    }
                """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input,expect,464))
    def test_65(self):
        input = """ 
                    class Program {
                        func @main():void {
                            const a: float = 3.2;
                            a := 1;
                        }
                    }
                """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,465))
    def test_66(self):
        input = """ 
                    class ABC {
                        
                    }
                    class Program {
                        func @main():void {
                            const bc: ABC = null;
                            bc := 1;
                        }
                    }
                """
        expect = "Cannot Assign To Constant: AssignStmt(Id(bc),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,466))
    def test_67(self):
        input = """ 
                    class Program {
                        func @main():void {
                            const i:int  = 00;
                            for i := 0; i < 10; i := i + 1 {
                                io.@writeInt(i);
                            }
                        }
                    }
                """
        expect = "Cannot Assign To Constant: AssignStmt(Id(i),IntLit(0))"
        self.assertTrue(TestChecker.test(input,expect,467))
    def test_68(self):
        input = """ 
                    class Program {
                        var a:int;
                        const b:int = 12;
                        func @main():void {
                            self.b := 1;
                        }
                    }
                """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(b)),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,468))
    def test_69(self):
        input = """ 
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            const l: [3]int = [2,4,5];
                            l[1] :=  2;
                            const a: [3]int = [2,4,5];
                            l := a;
                            
                        }
                    }
                """
        expect = "Cannot Assign To Constant: AssignStmt(Id(l),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,469))
    def test_70(self):
        input = """ 
                    class A {
                        func abc(): [5]int {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var a: A;
                            var k: [3]int = [2,4,5];
                            k[1] := 0;
                            const l: [3]int = [2,4,5];
                            a.abc()[1] := k[2];
                            a := c;
                        }
                    }
                """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,470))
    def test_71(self):
        input = """ 
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var k: [3]int = [2,4,5];
                            k[1.1] := 0;
                            const l: [3]int = [2,4,5];
                            l[1] :=  2;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(k),FloatLit(1.1))"
        self.assertTrue(TestChecker.test(input,expect,471))
    def test_72(self):
        input = """ 
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var k: float;
                            k[1] := 0.2;
                            const l: [3]int = [2,4,5];
                            l[1] :=  2;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(k),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,472))
    def test_73(self):
        input = """ 
                    class Program {
                        func @main():void {
                            var a: int;
                            var b: int = a.e();
                        }
                    }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(e),[])"
        self.assertTrue(TestChecker.test(input,expect,473))
    def test_74(self):
        input = """ 
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var a: int;
                            var b: int = self.b + a.e;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: FieldAccess(Id(a),Id(e))"
        self.assertTrue(TestChecker.test(input,expect,474))
    def test_75(self):
        input = """ 
                    class A {
                        func constructor (a: int, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: A;
                            b := new A(1,2.3);

                            var b: float;
                        }
                    }
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,475))
    def test_76(self):
        input = """ 
                    class A {
                        func constructor (a: int, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: A;
                            b := new A(1,2);

                            var b: float;
                        }
                    }
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,476))
    def test_77(self):
        input = """ 
                    class A {
                        func constructor (a: int, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: A;
                            b := new A(1.1,2.3);

                            var b: float;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: NewExpr(Id(A),[FloatLit(1.1),FloatLit(2.3)])"
        self.assertTrue(TestChecker.test(input,expect,477))
    def test_78(self):
        input = """ 
                    class A {
                        func constructor (a: int, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: A;
                            b := new A(1,2.3,1);

                            var b: float;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: NewExpr(Id(A),[IntLit(1),FloatLit(2.3),IntLit(1)])"
        self.assertTrue(TestChecker.test(input,expect,478))
    def test_79(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: A;
                            b := new A(b, 1.1);

                            var b: float;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: NewExpr(Id(A),[Id(b),FloatLit(1.1)])"
        self.assertTrue(TestChecker.test(input,expect,479))
    def test_80(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: A;
                            var c: B;
                            b := new A(c, 1.1);

                            var b: float;
                        }
                    }
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,480))
    def test_81(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                        func constructor (a: B) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: A;
                            var c: B;
                            b := new A(c);

                            var b: float;
                        }
                    }
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,481))
    def test_82(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                        func nonvoid (a: int, b: string): void {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: A;
                            var c: B;
                            b.nonvoid(2, "");
                            c := b.nonvoid(3,"");

                            var b: float;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(b),Id(nonvoid),[IntLit(3),StringLit()])"
        self.assertTrue(TestChecker.test(input,expect,482))
    def test_83(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                        func nonvoid (a: int, b: string): void {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: A;
                            var c: B;
                            b.nonvoid(2, "");
                            c := b.nonvoid(3);

                            var b: float;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(b),Id(nonvoid),[IntLit(3)])"
        self.assertTrue(TestChecker.test(input,expect,483))
    def test_84(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                        func nonvoid (a: int, b: [2]string): B {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: A;
                            var c: B;
                            var s: [2]string;
                            c := b.nonvoid(3,s);

                            var b: float;
                        }
                    }
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,484))
    def test_85(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                        func nonvoid (a: int, b: [5]string): B {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: A;
                            var c: B;
                            var s: [2]string;
                            c := b.nonvoid(3,s);

                            var b: float;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(b),Id(nonvoid),[IntLit(3),Id(s)])"
        self.assertTrue(TestChecker.test(input,expect,485))
    def test_86(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: A;
                            var d: A;
                            var c: B;
                            b := new A(d, 1.1);

                            var b: float;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: NewExpr(Id(A),[Id(d),FloatLit(1.1)])"
        self.assertTrue(TestChecker.test(input,expect,486))
    def test_87(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:[3]float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: A;
                            var c: B;
                            const a: [3]bool = [true, false,false];
                            b := new A(c, a);

                            var b: float;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: NewExpr(Id(A),[Id(c),Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,487))
    def test_88(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                    }
                    class Program {
                        func @main():void {
                            var b: float = 3.3 + 4;
                            var c: float = 3 + 4;
                            var d: float = 3 * 4;
                            var e: float = 3 - 4;
                            var b: int;
                        }
                    }
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,488))
    def test_89(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                    }
                    class Program {
                        func @main():void {
                            const f:float = 3/5; 
                            const i:int = 3/5; 
                        }
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(/,IntLit(3),IntLit(5))"
        self.assertTrue(TestChecker.test(input,expect,489))
    def test_90(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: int = 3.3%3;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(%,FloatLit(3.3),IntLit(3))"
        self.assertTrue(TestChecker.test(input,expect,490))
    def test_91(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: int ;
                            b := 3.3 || 3;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(||,FloatLit(3.3),IntLit(3))"
        self.assertTrue(TestChecker.test(input,expect,491))
    def test_92(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: int ;
                            b := 3.3 && true;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(&&,FloatLit(3.3),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,492))
    def test_93(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: bool ;
                            b := true || false;
                            b := ! false;
                            b := 1;
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,493))
    def test_94(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            const a:string  = "123";
                            var b:string  = "123";
                            b := b^a;
                            b := b \ 3;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(\,Id(b),IntLit(3))"
        self.assertTrue(TestChecker.test(input,expect,494))
    def test_95(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            const a:string  = "123";
                            var b:string  = "123";
                            b := b^1;
                            b := b \ 3;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(^,Id(b),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,495))
    def test_96(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: int ;
                            var c: bool ;
                            c := 3.4 > 3;
                            b := 3.4 > 3;
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),BinaryOp(>,FloatLit(3.4),IntLit(3)))"
        self.assertTrue(TestChecker.test(input,expect,496))
    def test_97(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: int ;
                            var c: bool ;
                            c := true == false;
                            b := true == false;
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),BinaryOp(==,BooleanLit(True),BooleanLit(False)))"
        self.assertTrue(TestChecker.test(input,expect,497))
    def test_98(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var c: bool ;
                            c := 3.4 != 3;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(!=,FloatLit(3.4),IntLit(3))"
        self.assertTrue(TestChecker.test(input,expect,498))
    def test_99(self):
        input = """ 
                    class B { }
                    class A {
                        func constructor (a: B, b:float) {
                            
                        }
                    }
                    class Program {
                        const b:int = 12;
                        func @main():void {
                            var b: int ;
                            var c: float ;
                            c := - 3.33333;
                            b := - true;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: UnaryOp(-,BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,499))
    def test_100(self):
        input = """ 
                    class B { }
                    class B <- A {
                        
                    }
                    class Program {
                        func @main():void {
                            var a: A ;
                            var b: B ;
                            b := a;
                            var b:int;
                        }
                    }
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,500))
    def test_101(self):
        input = """ 
                    class B { }
                    class B <- A {
                        
                    }
                    class Program {
                        func @main():void {
                            var i, j :int;
                            if {i := 0;} j > i {j := j - 1;} else {j := j + 1;}
                            var i:int;
                        }
                    }
                """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,501))
    def test_102(self):
        input = """ 
                    class B { }
                    class B <- A {
                        
                    }
                    class Program {
                        func @main():void {
                            var i, j :int;
                            if {i := 0;} j + i {j := j - 1;} else {j := j + 1;}
                            var i:int;
                        }
                    }
                """
        expect = "Type Mismatch In Statement: If(Block([AssignStmt(Id(i),IntLit(0))]),BinaryOp(+,Id(j),Id(i)),Block([AssignStmt(Id(j),BinaryOp(-,Id(j),IntLit(1)))]),Block([AssignStmt(Id(j),BinaryOp(+,Id(j),IntLit(1)))]))"
        self.assertTrue(TestChecker.test(input,expect,502))
    def test_103(self):
        input = """ 
                    class B { }
                    class B <- A {
                        
                    }
                    class Program {
                        func @main():void {
                            var i:int = 0;
                            for i := 0; i * 10; i := i + 1 {
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Statement: For(AssignStmt(Id(i),IntLit(0)),BinaryOp(*,Id(i),IntLit(10)),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Block([])])"
        self.assertTrue(TestChecker.test(input,expect,503))
    def test_104(self):
        input = """ 
                    class B { }
                    class B <- A {
                        func abc() :void {
                            
                        }
                    }
                    class Program {
                        func @main():void {
                            var i: [5]int;
                            var b: A;
                            i := [1,2,3,4,6];
                            i := [1,2,3,4];
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(i),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])"
        self.assertTrue(TestChecker.test(input,expect,504))
    def test_105(self):
        input = """ 
                    class B { }
                    class B <- A {
                        func abc() :int {
                            
                        }
                    }
                    class Program {
                        func @main():void {
                            var i: [5]int;
                            var b: A;
                            b.abc();
                        }
                    }
                """
        expect = "Type Mismatch In Statement: Call(Id(b),Id(abc),[])"
        self.assertTrue(TestChecker.test(input,expect,505))
    def test_106(self):
        input = """ 
                    class B { }
                    class B <- A {
                        func abc() :int {
                            
                        }
                    }
                    class Program {
                        func @main():void {
                            var i: [5]int;
                            var b: A;
                            b.abc(1.2);
                        }
                    }
                """
        expect = "Type Mismatch In Statement: Call(Id(b),Id(abc),[FloatLit(1.2)])"
        self.assertTrue(TestChecker.test(input,expect,506))
    def test_107(self):
        input = """ 
                    class B { }
                    class B <- A {
                        func abc() : [5]int {
                            return [12,4,5,7,2];
                        }
                    }
                    class Program {
                        func @main():void {
                            var i: [5]int;
                            var b: A;
                            b.abc();
                        }
                    }
                """
        expect = "Type Mismatch In Statement: Call(Id(b),Id(abc),[])"
        self.assertTrue(TestChecker.test(input,expect,507))
    def test_108(self):
        input = """ 
                    class B { }
                    class B <- A {
                        func abc() : [5]int {
                            return [12,4,5,2];
                        }
                    }
                    class Program {
                        func @main():void {
                            var i: [5]int;
                            var b: A;
                            b.abc();
                        }
                    }
                """
        expect = "Type Mismatch In Statement: Return([IntLit(12),IntLit(4),IntLit(5),IntLit(2)])"
        self.assertTrue(TestChecker.test(input,expect,508))
    def test_109(self):
        input = """ 
                    class B { 
                        var a: int;
                    }
                    class B <- A {
                        
                    }
                    class Program {
                        func @main():void {
                            var a: A ;
                            var b: B ;
                            b := a;
                            b.a := a.a;
                            var b:int;
                        }
                    }
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,509))
    def test_110(self):
        input = """ 
                    class Shape {
                    var @numOfShape: int = 0;
                    const immutableAttribute: int = 0;
                    var length, width: int;
                    func @getNumOfShape():int {
                    return @numOfShape;
                    }
                    }
                    class Shape <- Retangle {
                    func getArea():int {
                    return self.length * self.width;
                    }
                    }
                    class Program {
                    func @main():void {
                    io.@writeInt(Shape.@numOfShape);
                    var b,b:int;
                    }
                    }
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,510))
    def test_111(self):
        input = """ 
                    class B { 
                        var a: int;
                    }
                    class B <- A {
                        const My1stCons, My2ndCons: int = 1 + 5, 2;
var @x, @y : int = 0, 0;
                    }
                    class Program {
                        func @main():void {
                    var b,b:int;
                            
                        }
                    }
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,511))
    def test_112(self):
        input = """ 
                    class B { 
                        var a: int;
                    }
                    class B <- A {
                        func foo(a: int):int {
                            
                        }
                    }
                    class Program {
                        func @main():void {
                            var x: A;
                            var a: [5]float;
                            var b: [4]int;
                            a[3+x.foo(2)] := a[b[2]] +3;
                            var b,b:int;
                        }
                    }
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,512))
    def test_113(self):
        input = """ 
                    class B { 
                        var a: int;
                    }
                    class B <- A {
                        func foo(a: int):int {
                            
                        }
                    }
                    class Program {
                        func @main():void {
                            var x: A;
                            var a: [5]float;
                            var b: [4]float;
                            a[3+x.foo(2)] := a[b[2]] +3;
                            var b,b:int;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2)))"
        self.assertTrue(TestChecker.test(input,expect,513))
    def test_114(self):
        input = """ 
                    class B { 
                        var a: int;
                    }
                    class B <- A {
                        func foo(a: int):int {
                            
                        }
                    }
                    class Program {
                        func @main():void {
                            var x: A;
                            var a: [5]float;
                            var b: [4]int;
                            a[3+x.foo(2)] := a[b[2]] + "s123";
                            var b,b:int;
                        }
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2))),StringLit(s123))"
        self.assertTrue(TestChecker.test(input,expect,514))
    def test_115(self):
        input = """ 
                    class B { 
                        var a: int;
                    }
                    class B <- A {
                        func foo(a: int):int {
                            
                        }
                    }
                    class Program {
                        func @main():void {
                            var x: A;
                            var a: [5]int;
                            var b: [4]int;
                            a[3+x.foo(2)] := a[b[2]] +3.3;
                            var b,b:int;
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2))),FloatLit(3.3)))"
        self.assertTrue(TestChecker.test(input,expect,515))
    def test_116(self):
        input = """ 
                    class B { 
                        var a: int;
                    }
                    class B <- A {
                        var b: [5]string;
                        func m(): [7]string{
                            
                        }
                    }
                    class Program {
                        func @main():void {
                            var x: A;
                            x.b[2] := x.m()[3];
                            var x: int;
                        }
                    }
                """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,516))
    def test_117(self):
        input = """ 
                    class B { 
                        var a: int;
                    }
                    class B <- A {
                        var b: [5]int;
                        func m(): [7]string{
                            
                        }
                    }
                    class Program {
                        func @main():void {
                            var x: A;
                            x.b[2] := x.m()[4];
                            var x: int;
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(FieldAccess(Id(x),Id(b)),IntLit(2)),ArrayCell(CallExpr(Id(x),Id(m),[]),IntLit(4)))"
        self.assertTrue(TestChecker.test(input,expect,517))
    def test_118(self):
        input = """ 
                    class B { 
                        var a: int;
                    }
                    class B <- A {
                        var b: [5]float;
                        func m(): [7]int{
                            
                        }
                    }
                    class Program {
                        func @main():void {
                            var x: A;
                            x.b[2] := x.m()[4];
                            var x: int;
                        }
                    }
                """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,518))
    def test_119(self):
        input = """ 
                    class C {
                        
                    }
                    class C <-B { 
                        var a: int;
                    }
                    class B <- A {
                        
                    }
                    class Program {
                        func @main():void {
                            var c: C;
                            var b: A;
                            c := b;
                            var b: string;
                        }
                    }
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,519))
    def test_120(self):
        input = """ 
                    class C {
                        
                    }
                    class C <-B { 
                        var a: int;
                    }
                    class A {
                        
                    }
                    class Program {
                        func @main():void {
                            var c: C;
                            var b: A;
                            c := b;
                            var b: string;
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,520))
    def test_121(self):
        input = """ 
                    class C {
                        
                    }
                    class C <-B { 
                        var a: int;
                    }
                    class A {
                        
                    }
                    class Program {
                        var myPi: int;
                        func @main():void {
                            {
                            var r, s: int;
                            r := 2.0;
                            var a, b: [5]int;
                            s := r * r * self.myPI;
                            a[0] := s;
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(r),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input,expect,521))
    def test_122(self):
        input = """ 
                    class C {
                        
                    }
                    class C <-B { 
                        var a: int;
                    }
                    class A {
                        
                    }
                    class Program {
                        var myPI: int;
                        func @main():void {
                            {
                            var r, s: int;
                            r := 2;
                            var a, b: [5]int;
                            s := r * r * self.myPI;
                            a[0] := s;
                            var i,i:int;
                            }
                        }
                    }
                """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,522))
    def test_123(self):
        input = Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],VoidType(),Block([
                    VarDecl(Id("a"),ClassType(Id("c"))),
                    VarDecl(Id("b"),ClassType(Id("d")))]))]),
            ClassDecl(Id("c"),[])])
        expect = "Undeclared Class: d"
        self.assertTrue(TestChecker.test(input,expect,523))
    def test_124(self):
        input = """ 
                    class C {
                        
                    }
                    class C <-B { 
                        var @a: int;
                    }
                    class A {
                        
                    }
                    class Program {
                        func @main():void {
                            var c: int;
                            var b: A;
                            c := B.@a;
                            var b: string;
                        }
                    }
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,524))
    def test_125(self):
        input = """ 
                    class C {
                        
                    }
                    class C <-B { 
                        var @a: int;
                    }
                    class A {
                        
                    }
                    class Program {
                        var @abc: float;
                        func @main():void {
                            var c: C;
                            var b: A;
                            @abc := B.@a;
                            var b: string;
                        }
                    }
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,525))
    def test_126(self):
        input = """ 
                    class B <- C {
                        
                    }
                    class C <-B { 
                        var a: int;
                    }
                    class A {
                        
                    }
                    class Program {
                        func @main():void {
                            var c: C;
                            var b: A;
                            c := b;
                            var b: string;
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,526))
    def test_127(self):
        input = """ 
                    class C {
                        
                    }
                    class C <-B { 
                        var a: B;
                    }
                    class A {
                        
                    }
                    class Program {
                        func @main():void {
                            var c: C;
                            var b: A;
                            c := b;
                            var b: string;
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,527))
    def test_128(self):
        input = """ 
                    class C {
                        
                    }
                    class C <-B { 
                        var a: A;
                    }
                    class A {
                        
                    }
                    class Program {
                        func @main():void {
                            var c: C;
                            var b: A;
                            c := b;
                            var b: string;
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,528))
    def test_129(self):
        input = """ 
                    class C {
                        
                    }
                    class C <-B { 
                        var a: D;
                    }
                    class A {
                        
                    }
                    class Program {
                        func @main():void {
                            var c: C;
                            var b: A;
                            c := b;
                            var b: string;
                        }
                    }
                """
        expect = "Undeclared Class: D"
        self.assertTrue(TestChecker.test(input,expect,529))
    def test_130(self):
        input = """ 
                    class C {
                        
                    }
                    class C <-B { 
                        var a: int;
                    }
                    class A {
                        
                    }
                    class Program {
                        var a: string;
                        func @main():void {
                            var c: C;
                            var b: A;
                            var d: string;
                            d := a;
                            c :=a;
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,530))
    def test_131(self):
        input = """ 
                    class C {
                    }
                    class C <-BC { 
                    }
                    class io {
                        
                    }
                    class Program {
                        func @main():void {
                            var i: int;
                            var f: float;
                            var s: string;
                            var b: bool;
                            
                            var ia: [4]int;
                            var fa: [4]float;
                            var sa: [4]string;
                            var ba: [4]bool;
                            
                            var err: int = err;
                        }
                    }
                """
        expect = "Redeclared Class: io"
        self.assertTrue(TestChecker.test(input,expect,531))
    def test_132(self):
        input = """ 
                    class C {
                    }
                    class C <-BC { 
                    }
                    class Program {
                        func @main():void {
                            var i: int;
                            var f: float;
                            var s: string;
                            var b: bool;
                            
                            var ia: [4]int;
                            var fa: [4]float;
                            var sa: [4]string;
                            var ba: [4]bool;
                            
                            io.@writeFloat(1);
                            var err: int = err;
                        }
                    }
                """
        expect = "Undeclared Identifier: err"
        self.assertTrue(TestChecker.test(input,expect,532))
    
    def test_133(self):
        input = """ 
                    class C {
                        func constructor() {
                        }
                    }
                    class C <-BC { 
                        func constructor() {
                        }
                    }
                    class A {
                        var abc : int;
                        func constructor(i:int, c: C) {
                            var a :int = abc;
                        }
                        func call (fa: [4]float, s: string) : float {
                            
                            const f: float = fa[1];
                            
                            return f;
                        }
                    }
                    class Program {
                        func @main():void {
                            var i: int;
                            var f: float;
                            var s: string;
                            var b: bool;
                            
                            var ia: [4]int;
                            var fa: [4]float;
                            var sa: [4]string;
                            var ba: [4]bool;
                            var c:C;
                            c := new BC();
                            var newA: A = new A(i, null);
                            f := newA.call(fa, s);
                            var err: int = err;
                        }
                    }
                """
        expect = "Undeclared Identifier: err"
        self.assertTrue(TestChecker.test(input,expect,533))
    
    
    
    
    
    
    
    # def test_redeclared_class_with_ast(self):
    #     input = Program([ClassDecl(Id("a"),[]),ClassDecl(Id("b"),[]),ClassDecl(Id("a"),[])])
    #     expect = "Redeclared Class: a"
    #     self.assertTrue(TestChecker.test(input,expect,402))
    # def test_redeclared_attribute_with_ast(self):
    #     input = Program([ClassDecl(Id("a"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType()))])])
    #     expect = "Redeclared Attribute: c"
    #     self.assertTrue(TestChecker.test(input,expect,404))    
    