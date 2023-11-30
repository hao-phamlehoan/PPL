// MSSV 2013093

grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: class_dcl+ EOF ;

// class
class_dcl: CLASS ID ('<-' ID | )  class_body;
class_body: LCURB decls RCURB;

decls: decl decls | ;
decl: att_decl | constructor_decl | method_decl;

// attribute
att_decl: (CONST_VAR super_idlist COLON data_type_decl SEMI)
				| (CONST_VAR (ID | A_ID) recursion_att expr SEMI);

recursion_att: COMMA (ID | A_ID) recursion_att expr COMMA | vari_decl;
vari_decl: COLON data_type_decl EQUAL;

// method
method_decl: FUNC (ID | A_ID) LP paramlist RP COLON data_type block_stmt;

// contruction
constructor_decl: FUNC CONSTRUCTOR LP paramlist RP block_stmt;

paramlist: paramprime | ;
paramprime: param COMMA paramprime | param ;
param: idlist COLON data_type_decl;

// statement
block_stmt: LCURB stmtlist RCURB;
stmtlist: stmt stmtlist | ;
stmt: ( var_stmt | asm_stmt | break_stmt | continue_stmt | return_stmt | call_stmt) SEMI
			| if_stmt 
			| for_stmt
			| block_stmt;

asm_stmt: expr7 ASSIGN expr;

var_stmt: (CONST_VAR idlist COLON data_type_decl) 
				| (CONST_VAR ID recursion_vari expr);

recursion_vari: COMMA ID recursion_vari expr COMMA | vari_decl;

continue_stmt: CONTINUE;

break_stmt: BREAK	;

return_stmt: RETURN ( expr | );

call_stmt: expr7 DOT ID LP empty_exprlist RP
										| (ID DOT | ) A_ID LP empty_exprlist RP;

if_stmt: IF (preblock_stmt | ) expr block_stmt (ELSE block_stmt | );
preblock_stmt: block_stmt;

for_stmt: FOR init_stmt SEMI condition_expr SEMI post_stmt block_stmt;

// For element
init_stmt: expr7 ASSIGN expr;
condition_expr: expr;
post_stmt: expr7 ASSIGN expr;


// Expressions
expr: expr1 STRINGCON expr1 | expr1;
expr1: expr2 (ISEQUAL | NOTEQUAL | LESSTHAN | LESSTHANOREQ | GREATERTHAN | GREATERTHANOREQ) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUBTRAC) expr4 | expr4;
expr4: expr4 (MULTI | DIVID | BSLASH | MODUL) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUBTRAC expr6 | expr7;
expr7: expr8 LSQAB expr RSQAB | expr8; //index operator
expr8: expr8 DOT ID | expr8 DOT ID LP empty_exprlist RP | expr9; //mem access
expr9: (ID DOT| ) A_ID | (ID DOT | ) A_ID LP empty_exprlist RP | expr10;
expr10: NEW ID LP empty_exprlist RP | expr11;
expr11: subexpr | ID | A_ID | lit | SELF | NULL;
subexpr: LP expr RP;

// Type
data_type_decl: INT | FLOAT | BOOL | STRING | array_type | ID ;
data_type: INT | FLOAT | BOOL | STRING | array_type | ID | VOID;

//Array type
array_type: LSQAB DIGIT RSQAB array_data_type_decl;
array_data_type_decl: INT | FLOAT | BOOL | STRING;

// utilities
super_idlist: (ID | A_ID) COMMA super_idlist | (ID | A_ID);
idlist: ID COMMA idlist | ID;

empty_exprlist: exprprime | ;
exprprime: expr COMMA exprprime | expr;

lit: arraylit | intlit | FLOATLIT | BOOLIT | STRINGLIT | NULL | ID;

arraylit: LSQAB array_decl RSQAB;
array_decl: lit COMMA array_decl | lit;
// array_decl: array_int | array_float | array_bool | array_string;
// array type
array_int: intlit COMMA array_int | intlit;
array_float: FLOATLIT COMMA array_float | FLOATLIT;
array_bool: BOOLIT COMMA array_bool | BOOLIT;
array_string: STRINGLIT COMMA array_string | STRINGLIT;

intlit: ZERO | DIGIT ;

//Literals
ZERO: '0'+;
DIGIT: [0]*[1-9][0-9]*;

FLOATLIT: INTPART (DECPART EXPPART? | EXPPART);
fragment INTPART: ZERO | DIGIT;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: [eE][-+]?[0-9]+;

BOOLIT: TRUE | FALSE;

STRINGLIT: '"' CHARINSTR* '"' {self.text = self.text[1:-1]};

CONST_VAR: CONST | VAR;

// Separators
LP: '('; RP: ')'; // Left and right parentheses ( )
LCURB: '{'; RCURB: '}'; // Left and right curly brackets: { }
LSQAB: '['; RSQAB: ']'; // Left and right square brackets: [ ]
DOT: '.'; // .
COMMA: ','; // ,
SEMI: ';'; // ;
COLON: ':'; // :

// Operators
ADD: '+'; 			SUBTRAC: '-'; 	MULTI: '*'; 				DIVID: '/'; 			BSLASH: '\\'; 
NOT: '!'; 			AND: '&&'; 			OR: '||'; 					ISEQUAL: '=='; 		EQUAL: '=';
NOTEQUAL: '!='; LESSTHAN: '<'; 	LESSTHANOREQ: '<='; GREATERTHAN: '>'; GREATERTHANOREQ: '>=';
ASSIGN: ':='; 	STRINGCON: '^';									 		MODUL: '%'; 			

// Keywords
BREAK: 'break';		CONTINUE: 'continue';	IF: 'if'; 		ELSE: 'else'; 	FOR: 'for';
TRUE: 'true'; 		FALSE: 'false'; 			INT: 'int'; 	FLOAT: 'float'; BOOL: 'bool';
STRING: 'string'; RETURN: 'return'; 		NULL: 'null'; CLASS: 'class'; CONSTRUCTOR: 'constructor';
VAR: 'var'; 			SELF: 'self';					NEW: 'new'; 	VOID: 'void';		CONST: 'const'; 			
FUNC: 'func';

// Identifiers

A_ID: '@'[0-9a-zA-Z_]+;

ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Program comment
CMSINGLE: '//' ~[\r\n]* -> skip;
CMMULTI: '/*' .*? '*/' -> skip;

fragment CHARINSTR: ~[\n\r"\\] | '\\' [btnfr"\\];
fragment ESC_PART: '\\' ~[btnfr"\\] | '\\';

WS : [ \t\b\f\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' CHARINSTR*  {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: '"' CHARINSTR* ESC_PART {raise IllegalEscape(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};