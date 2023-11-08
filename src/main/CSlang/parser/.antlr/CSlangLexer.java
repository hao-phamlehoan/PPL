// Generated from e:/231/PPL/Assignment/Assignment3/initial/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1

from lexererr import *

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class CSlangLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, ZERO=2, DIGIT=3, FLOATLIT=4, BOOLIT=5, STRINGLIT=6, CONST_VAR=7, 
		LP=8, RP=9, LCURB=10, RCURB=11, LSQAB=12, RSQAB=13, DOT=14, COMMA=15, 
		SEMI=16, COLON=17, ADD=18, SUBTRAC=19, MULTI=20, DIVID=21, BSLASH=22, 
		NOT=23, AND=24, OR=25, ISEQUAL=26, EQUAL=27, NOTEQUAL=28, LESSTHAN=29, 
		LESSTHANOREQ=30, GREATERTHAN=31, GREATERTHANOREQ=32, ASSIGN=33, STRINGCON=34, 
		MODUL=35, BREAK=36, CONTINUE=37, IF=38, ELSE=39, FOR=40, TRUE=41, FALSE=42, 
		INT=43, FLOAT=44, BOOL=45, STRING=46, RETURN=47, NULL=48, CLASS=49, CONSTRUCTOR=50, 
		VAR=51, SELF=52, NEW=53, VOID=54, CONST=55, FUNC=56, A_ID=57, ID=58, CMSINGLE=59, 
		CMMULTI=60, WS=61, UNCLOSE_STRING=62, ILLEGAL_ESCAPE=63, ERROR_CHAR=64;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "ZERO", "DIGIT", "FLOATLIT", "INTPART", "DECPART", "EXPPART", 
			"BOOLIT", "STRINGLIT", "CONST_VAR", "LP", "RP", "LCURB", "RCURB", "LSQAB", 
			"RSQAB", "DOT", "COMMA", "SEMI", "COLON", "ADD", "SUBTRAC", "MULTI", 
			"DIVID", "BSLASH", "NOT", "AND", "OR", "ISEQUAL", "EQUAL", "NOTEQUAL", 
			"LESSTHAN", "LESSTHANOREQ", "GREATERTHAN", "GREATERTHANOREQ", "ASSIGN", 
			"STRINGCON", "MODUL", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
			"FALSE", "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
			"CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "A_ID", 
			"ID", "CMSINGLE", "CMMULTI", "CHARINSTR", "ESC_PART", "WS", "UNCLOSE_STRING", 
			"ILLEGAL_ESCAPE", "ERROR_CHAR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'<-'", null, null, null, null, null, null, "'('", "')'", "'{'", 
			"'}'", "'['", "']'", "'.'", "','", "';'", "':'", "'+'", "'-'", "'*'", 
			"'/'", "'\\'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", "'<='", 
			"'>'", "'>='", "':='", "'^'", "'%'", "'break'", "'continue'", "'if'", 
			"'else'", "'for'", "'true'", "'false'", "'int'", "'float'", "'bool'", 
			"'string'", "'return'", "'null'", "'class'", "'constructor'", "'var'", 
			"'self'", "'new'", "'void'", "'const'", "'func'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "ZERO", "DIGIT", "FLOATLIT", "BOOLIT", "STRINGLIT", "CONST_VAR", 
			"LP", "RP", "LCURB", "RCURB", "LSQAB", "RSQAB", "DOT", "COMMA", "SEMI", 
			"COLON", "ADD", "SUBTRAC", "MULTI", "DIVID", "BSLASH", "NOT", "AND", 
			"OR", "ISEQUAL", "EQUAL", "NOTEQUAL", "LESSTHAN", "LESSTHANOREQ", "GREATERTHAN", 
			"GREATERTHANOREQ", "ASSIGN", "STRINGCON", "MODUL", "BREAK", "CONTINUE", 
			"IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", 
			"RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", 
			"CONST", "FUNC", "A_ID", "ID", "CMSINGLE", "CMMULTI", "WS", "UNCLOSE_STRING", 
			"ILLEGAL_ESCAPE", "ERROR_CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public CSlangLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "CSlang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 8:
			STRINGLIT_action((RuleContext)_localctx, actionIndex);
			break;
		case 66:
			UNCLOSE_STRING_action((RuleContext)_localctx, actionIndex);
			break;
		case 67:
			ILLEGAL_ESCAPE_action((RuleContext)_localctx, actionIndex);
			break;
		case 68:
			ERROR_CHAR_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void STRINGLIT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			self.text = self.text[1:-1]
			break;
		}
	}
	private void UNCLOSE_STRING_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:
			raise UncloseString(self.text[1:])
			break;
		}
	}
	private void ILLEGAL_ESCAPE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:
			raise IllegalEscape(self.text[1:])
			break;
		}
	}
	private void ERROR_CHAR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 3:
			raise ErrorToken(self.text)
			break;
		}
	}

	public static final String _serializedATN =
		"\u0004\u0000@\u01d1\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007"+
		"!\u0002\"\u0007\"\u0002#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007"+
		"&\u0002\'\u0007\'\u0002(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007"+
		"+\u0002,\u0007,\u0002-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u0007"+
		"0\u00021\u00071\u00022\u00072\u00023\u00073\u00024\u00074\u00025\u0007"+
		"5\u00026\u00076\u00027\u00077\u00028\u00078\u00029\u00079\u0002:\u0007"+
		":\u0002;\u0007;\u0002<\u0007<\u0002=\u0007=\u0002>\u0007>\u0002?\u0007"+
		"?\u0002@\u0007@\u0002A\u0007A\u0002B\u0007B\u0002C\u0007C\u0002D\u0007"+
		"D\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0004\u0001\u0090\b"+
		"\u0001\u000b\u0001\f\u0001\u0091\u0001\u0002\u0005\u0002\u0095\b\u0002"+
		"\n\u0002\f\u0002\u0098\t\u0002\u0001\u0002\u0001\u0002\u0005\u0002\u009c"+
		"\b\u0002\n\u0002\f\u0002\u009f\t\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0003\u0003\u00a4\b\u0003\u0001\u0003\u0003\u0003\u00a7\b\u0003\u0001"+
		"\u0004\u0001\u0004\u0003\u0004\u00ab\b\u0004\u0001\u0005\u0001\u0005\u0005"+
		"\u0005\u00af\b\u0005\n\u0005\f\u0005\u00b2\t\u0005\u0001\u0006\u0001\u0006"+
		"\u0003\u0006\u00b6\b\u0006\u0001\u0006\u0004\u0006\u00b9\b\u0006\u000b"+
		"\u0006\f\u0006\u00ba\u0001\u0007\u0001\u0007\u0003\u0007\u00bf\b\u0007"+
		"\u0001\b\u0001\b\u0005\b\u00c3\b\b\n\b\f\b\u00c6\t\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0003\t\u00cd\b\t\u0001\n\u0001\n\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f"+
		"\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015"+
		"\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0018"+
		"\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001c"+
		"\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001f"+
		"\u0001\u001f\u0001 \u0001 \u0001 \u0001!\u0001!\u0001\"\u0001\"\u0001"+
		"\"\u0001#\u0001#\u0001#\u0001$\u0001$\u0001%\u0001%\u0001&\u0001&\u0001"+
		"&\u0001&\u0001&\u0001&\u0001\'\u0001\'\u0001\'\u0001\'\u0001\'\u0001\'"+
		"\u0001\'\u0001\'\u0001\'\u0001(\u0001(\u0001(\u0001)\u0001)\u0001)\u0001"+
		")\u0001)\u0001*\u0001*\u0001*\u0001*\u0001+\u0001+\u0001+\u0001+\u0001"+
		"+\u0001,\u0001,\u0001,\u0001,\u0001,\u0001,\u0001-\u0001-\u0001-\u0001"+
		"-\u0001.\u0001.\u0001.\u0001.\u0001.\u0001.\u0001/\u0001/\u0001/\u0001"+
		"/\u0001/\u00010\u00010\u00010\u00010\u00010\u00010\u00010\u00011\u0001"+
		"1\u00011\u00011\u00011\u00011\u00011\u00012\u00012\u00012\u00012\u0001"+
		"2\u00013\u00013\u00013\u00013\u00013\u00013\u00014\u00014\u00014\u0001"+
		"4\u00014\u00014\u00014\u00014\u00014\u00014\u00014\u00014\u00015\u0001"+
		"5\u00015\u00015\u00016\u00016\u00016\u00016\u00016\u00017\u00017\u0001"+
		"7\u00017\u00018\u00018\u00018\u00018\u00018\u00019\u00019\u00019\u0001"+
		"9\u00019\u00019\u0001:\u0001:\u0001:\u0001:\u0001:\u0001;\u0001;\u0004"+
		";\u0187\b;\u000b;\f;\u0188\u0001<\u0001<\u0005<\u018d\b<\n<\f<\u0190\t"+
		"<\u0001=\u0001=\u0001=\u0001=\u0005=\u0196\b=\n=\f=\u0199\t=\u0001=\u0001"+
		"=\u0001>\u0001>\u0001>\u0001>\u0005>\u01a1\b>\n>\f>\u01a4\t>\u0001>\u0001"+
		">\u0001>\u0001>\u0001>\u0001?\u0001?\u0001?\u0003?\u01ae\b?\u0001@\u0001"+
		"@\u0001@\u0003@\u01b3\b@\u0001A\u0004A\u01b6\bA\u000bA\fA\u01b7\u0001"+
		"A\u0001A\u0001B\u0001B\u0005B\u01be\bB\nB\fB\u01c1\tB\u0001B\u0001B\u0001"+
		"C\u0001C\u0005C\u01c7\bC\nC\fC\u01ca\tC\u0001C\u0001C\u0001C\u0001D\u0001"+
		"D\u0001D\u0001\u01a2\u0000E\u0001\u0001\u0003\u0002\u0005\u0003\u0007"+
		"\u0004\t\u0000\u000b\u0000\r\u0000\u000f\u0005\u0011\u0006\u0013\u0007"+
		"\u0015\b\u0017\t\u0019\n\u001b\u000b\u001d\f\u001f\r!\u000e#\u000f%\u0010"+
		"\'\u0011)\u0012+\u0013-\u0014/\u00151\u00163\u00175\u00187\u00199\u001a"+
		";\u001b=\u001c?\u001dA\u001eC\u001fE G!I\"K#M$O%Q&S\'U(W)Y*[+],_-a.c/"+
		"e0g1i2k3m4o5q6s7u8w9y:{;}<\u007f\u0000\u0081\u0000\u0083=\u0085>\u0087"+
		"?\u0089@\u0001\u0000\u000b\u0001\u000000\u0001\u000019\u0001\u000009\u0002"+
		"\u0000EEee\u0002\u0000++--\u0004\u000009AZ__az\u0003\u0000AZ__az\u0002"+
		"\u0000\n\n\r\r\u0004\u0000\n\n\r\r\"\"\\\\\u0007\u0000\"\"\\\\bbffnnr"+
		"rtt\u0003\u0000\b\n\f\r  \u01e0\u0000\u0001\u0001\u0000\u0000\u0000\u0000"+
		"\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000"+
		"\u0007\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000"+
		"\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000"+
		"\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000"+
		"\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000"+
		"\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000"+
		"!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001"+
		"\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000"+
		"\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000"+
		"\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u00003"+
		"\u0001\u0000\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u00007\u0001\u0000"+
		"\u0000\u0000\u00009\u0001\u0000\u0000\u0000\u0000;\u0001\u0000\u0000\u0000"+
		"\u0000=\u0001\u0000\u0000\u0000\u0000?\u0001\u0000\u0000\u0000\u0000A"+
		"\u0001\u0000\u0000\u0000\u0000C\u0001\u0000\u0000\u0000\u0000E\u0001\u0000"+
		"\u0000\u0000\u0000G\u0001\u0000\u0000\u0000\u0000I\u0001\u0000\u0000\u0000"+
		"\u0000K\u0001\u0000\u0000\u0000\u0000M\u0001\u0000\u0000\u0000\u0000O"+
		"\u0001\u0000\u0000\u0000\u0000Q\u0001\u0000\u0000\u0000\u0000S\u0001\u0000"+
		"\u0000\u0000\u0000U\u0001\u0000\u0000\u0000\u0000W\u0001\u0000\u0000\u0000"+
		"\u0000Y\u0001\u0000\u0000\u0000\u0000[\u0001\u0000\u0000\u0000\u0000]"+
		"\u0001\u0000\u0000\u0000\u0000_\u0001\u0000\u0000\u0000\u0000a\u0001\u0000"+
		"\u0000\u0000\u0000c\u0001\u0000\u0000\u0000\u0000e\u0001\u0000\u0000\u0000"+
		"\u0000g\u0001\u0000\u0000\u0000\u0000i\u0001\u0000\u0000\u0000\u0000k"+
		"\u0001\u0000\u0000\u0000\u0000m\u0001\u0000\u0000\u0000\u0000o\u0001\u0000"+
		"\u0000\u0000\u0000q\u0001\u0000\u0000\u0000\u0000s\u0001\u0000\u0000\u0000"+
		"\u0000u\u0001\u0000\u0000\u0000\u0000w\u0001\u0000\u0000\u0000\u0000y"+
		"\u0001\u0000\u0000\u0000\u0000{\u0001\u0000\u0000\u0000\u0000}\u0001\u0000"+
		"\u0000\u0000\u0000\u0083\u0001\u0000\u0000\u0000\u0000\u0085\u0001\u0000"+
		"\u0000\u0000\u0000\u0087\u0001\u0000\u0000\u0000\u0000\u0089\u0001\u0000"+
		"\u0000\u0000\u0001\u008b\u0001\u0000\u0000\u0000\u0003\u008f\u0001\u0000"+
		"\u0000\u0000\u0005\u0096\u0001\u0000\u0000\u0000\u0007\u00a0\u0001\u0000"+
		"\u0000\u0000\t\u00aa\u0001\u0000\u0000\u0000\u000b\u00ac\u0001\u0000\u0000"+
		"\u0000\r\u00b3\u0001\u0000\u0000\u0000\u000f\u00be\u0001\u0000\u0000\u0000"+
		"\u0011\u00c0\u0001\u0000\u0000\u0000\u0013\u00cc\u0001\u0000\u0000\u0000"+
		"\u0015\u00ce\u0001\u0000\u0000\u0000\u0017\u00d0\u0001\u0000\u0000\u0000"+
		"\u0019\u00d2\u0001\u0000\u0000\u0000\u001b\u00d4\u0001\u0000\u0000\u0000"+
		"\u001d\u00d6\u0001\u0000\u0000\u0000\u001f\u00d8\u0001\u0000\u0000\u0000"+
		"!\u00da\u0001\u0000\u0000\u0000#\u00dc\u0001\u0000\u0000\u0000%\u00de"+
		"\u0001\u0000\u0000\u0000\'\u00e0\u0001\u0000\u0000\u0000)\u00e2\u0001"+
		"\u0000\u0000\u0000+\u00e4\u0001\u0000\u0000\u0000-\u00e6\u0001\u0000\u0000"+
		"\u0000/\u00e8\u0001\u0000\u0000\u00001\u00ea\u0001\u0000\u0000\u00003"+
		"\u00ec\u0001\u0000\u0000\u00005\u00ee\u0001\u0000\u0000\u00007\u00f1\u0001"+
		"\u0000\u0000\u00009\u00f4\u0001\u0000\u0000\u0000;\u00f7\u0001\u0000\u0000"+
		"\u0000=\u00f9\u0001\u0000\u0000\u0000?\u00fc\u0001\u0000\u0000\u0000A"+
		"\u00fe\u0001\u0000\u0000\u0000C\u0101\u0001\u0000\u0000\u0000E\u0103\u0001"+
		"\u0000\u0000\u0000G\u0106\u0001\u0000\u0000\u0000I\u0109\u0001\u0000\u0000"+
		"\u0000K\u010b\u0001\u0000\u0000\u0000M\u010d\u0001\u0000\u0000\u0000O"+
		"\u0113\u0001\u0000\u0000\u0000Q\u011c\u0001\u0000\u0000\u0000S\u011f\u0001"+
		"\u0000\u0000\u0000U\u0124\u0001\u0000\u0000\u0000W\u0128\u0001\u0000\u0000"+
		"\u0000Y\u012d\u0001\u0000\u0000\u0000[\u0133\u0001\u0000\u0000\u0000]"+
		"\u0137\u0001\u0000\u0000\u0000_\u013d\u0001\u0000\u0000\u0000a\u0142\u0001"+
		"\u0000\u0000\u0000c\u0149\u0001\u0000\u0000\u0000e\u0150\u0001\u0000\u0000"+
		"\u0000g\u0155\u0001\u0000\u0000\u0000i\u015b\u0001\u0000\u0000\u0000k"+
		"\u0167\u0001\u0000\u0000\u0000m\u016b\u0001\u0000\u0000\u0000o\u0170\u0001"+
		"\u0000\u0000\u0000q\u0174\u0001\u0000\u0000\u0000s\u0179\u0001\u0000\u0000"+
		"\u0000u\u017f\u0001\u0000\u0000\u0000w\u0184\u0001\u0000\u0000\u0000y"+
		"\u018a\u0001\u0000\u0000\u0000{\u0191\u0001\u0000\u0000\u0000}\u019c\u0001"+
		"\u0000\u0000\u0000\u007f\u01ad\u0001\u0000\u0000\u0000\u0081\u01b2\u0001"+
		"\u0000\u0000\u0000\u0083\u01b5\u0001\u0000\u0000\u0000\u0085\u01bb\u0001"+
		"\u0000\u0000\u0000\u0087\u01c4\u0001\u0000\u0000\u0000\u0089\u01ce\u0001"+
		"\u0000\u0000\u0000\u008b\u008c\u0005<\u0000\u0000\u008c\u008d\u0005-\u0000"+
		"\u0000\u008d\u0002\u0001\u0000\u0000\u0000\u008e\u0090\u00050\u0000\u0000"+
		"\u008f\u008e\u0001\u0000\u0000\u0000\u0090\u0091\u0001\u0000\u0000\u0000"+
		"\u0091\u008f\u0001\u0000\u0000\u0000\u0091\u0092\u0001\u0000\u0000\u0000"+
		"\u0092\u0004\u0001\u0000\u0000\u0000\u0093\u0095\u0007\u0000\u0000\u0000"+
		"\u0094\u0093\u0001\u0000\u0000\u0000\u0095\u0098\u0001\u0000\u0000\u0000"+
		"\u0096\u0094\u0001\u0000\u0000\u0000\u0096\u0097\u0001\u0000\u0000\u0000"+
		"\u0097\u0099\u0001\u0000\u0000\u0000\u0098\u0096\u0001\u0000\u0000\u0000"+
		"\u0099\u009d\u0007\u0001\u0000\u0000\u009a\u009c\u0007\u0002\u0000\u0000"+
		"\u009b\u009a\u0001\u0000\u0000\u0000\u009c\u009f\u0001\u0000\u0000\u0000"+
		"\u009d\u009b\u0001\u0000\u0000\u0000\u009d\u009e\u0001\u0000\u0000\u0000"+
		"\u009e\u0006\u0001\u0000\u0000\u0000\u009f\u009d\u0001\u0000\u0000\u0000"+
		"\u00a0\u00a6\u0003\t\u0004\u0000\u00a1\u00a3\u0003\u000b\u0005\u0000\u00a2"+
		"\u00a4\u0003\r\u0006\u0000\u00a3\u00a2\u0001\u0000\u0000\u0000\u00a3\u00a4"+
		"\u0001\u0000\u0000\u0000\u00a4\u00a7\u0001\u0000\u0000\u0000\u00a5\u00a7"+
		"\u0003\r\u0006\u0000\u00a6\u00a1\u0001\u0000\u0000\u0000\u00a6\u00a5\u0001"+
		"\u0000\u0000\u0000\u00a7\b\u0001\u0000\u0000\u0000\u00a8\u00ab\u0003\u0003"+
		"\u0001\u0000\u00a9\u00ab\u0003\u0005\u0002\u0000\u00aa\u00a8\u0001\u0000"+
		"\u0000\u0000\u00aa\u00a9\u0001\u0000\u0000\u0000\u00ab\n\u0001\u0000\u0000"+
		"\u0000\u00ac\u00b0\u0005.\u0000\u0000\u00ad\u00af\u0007\u0002\u0000\u0000"+
		"\u00ae\u00ad\u0001\u0000\u0000\u0000\u00af\u00b2\u0001\u0000\u0000\u0000"+
		"\u00b0\u00ae\u0001\u0000\u0000\u0000\u00b0\u00b1\u0001\u0000\u0000\u0000"+
		"\u00b1\f\u0001\u0000\u0000\u0000\u00b2\u00b0\u0001\u0000\u0000\u0000\u00b3"+
		"\u00b5\u0007\u0003\u0000\u0000\u00b4\u00b6\u0007\u0004\u0000\u0000\u00b5"+
		"\u00b4\u0001\u0000\u0000\u0000\u00b5\u00b6\u0001\u0000\u0000\u0000\u00b6"+
		"\u00b8\u0001\u0000\u0000\u0000\u00b7\u00b9\u0007\u0002\u0000\u0000\u00b8"+
		"\u00b7\u0001\u0000\u0000\u0000\u00b9\u00ba\u0001\u0000\u0000\u0000\u00ba"+
		"\u00b8\u0001\u0000\u0000\u0000\u00ba\u00bb\u0001\u0000\u0000\u0000\u00bb"+
		"\u000e\u0001\u0000\u0000\u0000\u00bc\u00bf\u0003W+\u0000\u00bd\u00bf\u0003"+
		"Y,\u0000\u00be\u00bc\u0001\u0000\u0000\u0000\u00be\u00bd\u0001\u0000\u0000"+
		"\u0000\u00bf\u0010\u0001\u0000\u0000\u0000\u00c0\u00c4\u0005\"\u0000\u0000"+
		"\u00c1\u00c3\u0003\u007f?\u0000\u00c2\u00c1\u0001\u0000\u0000\u0000\u00c3"+
		"\u00c6\u0001\u0000\u0000\u0000\u00c4\u00c2\u0001\u0000\u0000\u0000\u00c4"+
		"\u00c5\u0001\u0000\u0000\u0000\u00c5\u00c7\u0001\u0000\u0000\u0000\u00c6"+
		"\u00c4\u0001\u0000\u0000\u0000\u00c7\u00c8\u0005\"\u0000\u0000\u00c8\u00c9"+
		"\u0006\b\u0000\u0000\u00c9\u0012\u0001\u0000\u0000\u0000\u00ca\u00cd\u0003"+
		"s9\u0000\u00cb\u00cd\u0003k5\u0000\u00cc\u00ca\u0001\u0000\u0000\u0000"+
		"\u00cc\u00cb\u0001\u0000\u0000\u0000\u00cd\u0014\u0001\u0000\u0000\u0000"+
		"\u00ce\u00cf\u0005(\u0000\u0000\u00cf\u0016\u0001\u0000\u0000\u0000\u00d0"+
		"\u00d1\u0005)\u0000\u0000\u00d1\u0018\u0001\u0000\u0000\u0000\u00d2\u00d3"+
		"\u0005{\u0000\u0000\u00d3\u001a\u0001\u0000\u0000\u0000\u00d4\u00d5\u0005"+
		"}\u0000\u0000\u00d5\u001c\u0001\u0000\u0000\u0000\u00d6\u00d7\u0005[\u0000"+
		"\u0000\u00d7\u001e\u0001\u0000\u0000\u0000\u00d8\u00d9\u0005]\u0000\u0000"+
		"\u00d9 \u0001\u0000\u0000\u0000\u00da\u00db\u0005.\u0000\u0000\u00db\""+
		"\u0001\u0000\u0000\u0000\u00dc\u00dd\u0005,\u0000\u0000\u00dd$\u0001\u0000"+
		"\u0000\u0000\u00de\u00df\u0005;\u0000\u0000\u00df&\u0001\u0000\u0000\u0000"+
		"\u00e0\u00e1\u0005:\u0000\u0000\u00e1(\u0001\u0000\u0000\u0000\u00e2\u00e3"+
		"\u0005+\u0000\u0000\u00e3*\u0001\u0000\u0000\u0000\u00e4\u00e5\u0005-"+
		"\u0000\u0000\u00e5,\u0001\u0000\u0000\u0000\u00e6\u00e7\u0005*\u0000\u0000"+
		"\u00e7.\u0001\u0000\u0000\u0000\u00e8\u00e9\u0005/\u0000\u0000\u00e90"+
		"\u0001\u0000\u0000\u0000\u00ea\u00eb\u0005\\\u0000\u0000\u00eb2\u0001"+
		"\u0000\u0000\u0000\u00ec\u00ed\u0005!\u0000\u0000\u00ed4\u0001\u0000\u0000"+
		"\u0000\u00ee\u00ef\u0005&\u0000\u0000\u00ef\u00f0\u0005&\u0000\u0000\u00f0"+
		"6\u0001\u0000\u0000\u0000\u00f1\u00f2\u0005|\u0000\u0000\u00f2\u00f3\u0005"+
		"|\u0000\u0000\u00f38\u0001\u0000\u0000\u0000\u00f4\u00f5\u0005=\u0000"+
		"\u0000\u00f5\u00f6\u0005=\u0000\u0000\u00f6:\u0001\u0000\u0000\u0000\u00f7"+
		"\u00f8\u0005=\u0000\u0000\u00f8<\u0001\u0000\u0000\u0000\u00f9\u00fa\u0005"+
		"!\u0000\u0000\u00fa\u00fb\u0005=\u0000\u0000\u00fb>\u0001\u0000\u0000"+
		"\u0000\u00fc\u00fd\u0005<\u0000\u0000\u00fd@\u0001\u0000\u0000\u0000\u00fe"+
		"\u00ff\u0005<\u0000\u0000\u00ff\u0100\u0005=\u0000\u0000\u0100B\u0001"+
		"\u0000\u0000\u0000\u0101\u0102\u0005>\u0000\u0000\u0102D\u0001\u0000\u0000"+
		"\u0000\u0103\u0104\u0005>\u0000\u0000\u0104\u0105\u0005=\u0000\u0000\u0105"+
		"F\u0001\u0000\u0000\u0000\u0106\u0107\u0005:\u0000\u0000\u0107\u0108\u0005"+
		"=\u0000\u0000\u0108H\u0001\u0000\u0000\u0000\u0109\u010a\u0005^\u0000"+
		"\u0000\u010aJ\u0001\u0000\u0000\u0000\u010b\u010c\u0005%\u0000\u0000\u010c"+
		"L\u0001\u0000\u0000\u0000\u010d\u010e\u0005b\u0000\u0000\u010e\u010f\u0005"+
		"r\u0000\u0000\u010f\u0110\u0005e\u0000\u0000\u0110\u0111\u0005a\u0000"+
		"\u0000\u0111\u0112\u0005k\u0000\u0000\u0112N\u0001\u0000\u0000\u0000\u0113"+
		"\u0114\u0005c\u0000\u0000\u0114\u0115\u0005o\u0000\u0000\u0115\u0116\u0005"+
		"n\u0000\u0000\u0116\u0117\u0005t\u0000\u0000\u0117\u0118\u0005i\u0000"+
		"\u0000\u0118\u0119\u0005n\u0000\u0000\u0119\u011a\u0005u\u0000\u0000\u011a"+
		"\u011b\u0005e\u0000\u0000\u011bP\u0001\u0000\u0000\u0000\u011c\u011d\u0005"+
		"i\u0000\u0000\u011d\u011e\u0005f\u0000\u0000\u011eR\u0001\u0000\u0000"+
		"\u0000\u011f\u0120\u0005e\u0000\u0000\u0120\u0121\u0005l\u0000\u0000\u0121"+
		"\u0122\u0005s\u0000\u0000\u0122\u0123\u0005e\u0000\u0000\u0123T\u0001"+
		"\u0000\u0000\u0000\u0124\u0125\u0005f\u0000\u0000\u0125\u0126\u0005o\u0000"+
		"\u0000\u0126\u0127\u0005r\u0000\u0000\u0127V\u0001\u0000\u0000\u0000\u0128"+
		"\u0129\u0005t\u0000\u0000\u0129\u012a\u0005r\u0000\u0000\u012a\u012b\u0005"+
		"u\u0000\u0000\u012b\u012c\u0005e\u0000\u0000\u012cX\u0001\u0000\u0000"+
		"\u0000\u012d\u012e\u0005f\u0000\u0000\u012e\u012f\u0005a\u0000\u0000\u012f"+
		"\u0130\u0005l\u0000\u0000\u0130\u0131\u0005s\u0000\u0000\u0131\u0132\u0005"+
		"e\u0000\u0000\u0132Z\u0001\u0000\u0000\u0000\u0133\u0134\u0005i\u0000"+
		"\u0000\u0134\u0135\u0005n\u0000\u0000\u0135\u0136\u0005t\u0000\u0000\u0136"+
		"\\\u0001\u0000\u0000\u0000\u0137\u0138\u0005f\u0000\u0000\u0138\u0139"+
		"\u0005l\u0000\u0000\u0139\u013a\u0005o\u0000\u0000\u013a\u013b\u0005a"+
		"\u0000\u0000\u013b\u013c\u0005t\u0000\u0000\u013c^\u0001\u0000\u0000\u0000"+
		"\u013d\u013e\u0005b\u0000\u0000\u013e\u013f\u0005o\u0000\u0000\u013f\u0140"+
		"\u0005o\u0000\u0000\u0140\u0141\u0005l\u0000\u0000\u0141`\u0001\u0000"+
		"\u0000\u0000\u0142\u0143\u0005s\u0000\u0000\u0143\u0144\u0005t\u0000\u0000"+
		"\u0144\u0145\u0005r\u0000\u0000\u0145\u0146\u0005i\u0000\u0000\u0146\u0147"+
		"\u0005n\u0000\u0000\u0147\u0148\u0005g\u0000\u0000\u0148b\u0001\u0000"+
		"\u0000\u0000\u0149\u014a\u0005r\u0000\u0000\u014a\u014b\u0005e\u0000\u0000"+
		"\u014b\u014c\u0005t\u0000\u0000\u014c\u014d\u0005u\u0000\u0000\u014d\u014e"+
		"\u0005r\u0000\u0000\u014e\u014f\u0005n\u0000\u0000\u014fd\u0001\u0000"+
		"\u0000\u0000\u0150\u0151\u0005n\u0000\u0000\u0151\u0152\u0005u\u0000\u0000"+
		"\u0152\u0153\u0005l\u0000\u0000\u0153\u0154\u0005l\u0000\u0000\u0154f"+
		"\u0001\u0000\u0000\u0000\u0155\u0156\u0005c\u0000\u0000\u0156\u0157\u0005"+
		"l\u0000\u0000\u0157\u0158\u0005a\u0000\u0000\u0158\u0159\u0005s\u0000"+
		"\u0000\u0159\u015a\u0005s\u0000\u0000\u015ah\u0001\u0000\u0000\u0000\u015b"+
		"\u015c\u0005c\u0000\u0000\u015c\u015d\u0005o\u0000\u0000\u015d\u015e\u0005"+
		"n\u0000\u0000\u015e\u015f\u0005s\u0000\u0000\u015f\u0160\u0005t\u0000"+
		"\u0000\u0160\u0161\u0005r\u0000\u0000\u0161\u0162\u0005u\u0000\u0000\u0162"+
		"\u0163\u0005c\u0000\u0000\u0163\u0164\u0005t\u0000\u0000\u0164\u0165\u0005"+
		"o\u0000\u0000\u0165\u0166\u0005r\u0000\u0000\u0166j\u0001\u0000\u0000"+
		"\u0000\u0167\u0168\u0005v\u0000\u0000\u0168\u0169\u0005a\u0000\u0000\u0169"+
		"\u016a\u0005r\u0000\u0000\u016al\u0001\u0000\u0000\u0000\u016b\u016c\u0005"+
		"s\u0000\u0000\u016c\u016d\u0005e\u0000\u0000\u016d\u016e\u0005l\u0000"+
		"\u0000\u016e\u016f\u0005f\u0000\u0000\u016fn\u0001\u0000\u0000\u0000\u0170"+
		"\u0171\u0005n\u0000\u0000\u0171\u0172\u0005e\u0000\u0000\u0172\u0173\u0005"+
		"w\u0000\u0000\u0173p\u0001\u0000\u0000\u0000\u0174\u0175\u0005v\u0000"+
		"\u0000\u0175\u0176\u0005o\u0000\u0000\u0176\u0177\u0005i\u0000\u0000\u0177"+
		"\u0178\u0005d\u0000\u0000\u0178r\u0001\u0000\u0000\u0000\u0179\u017a\u0005"+
		"c\u0000\u0000\u017a\u017b\u0005o\u0000\u0000\u017b\u017c\u0005n\u0000"+
		"\u0000\u017c\u017d\u0005s\u0000\u0000\u017d\u017e\u0005t\u0000\u0000\u017e"+
		"t\u0001\u0000\u0000\u0000\u017f\u0180\u0005f\u0000\u0000\u0180\u0181\u0005"+
		"u\u0000\u0000\u0181\u0182\u0005n\u0000\u0000\u0182\u0183\u0005c\u0000"+
		"\u0000\u0183v\u0001\u0000\u0000\u0000\u0184\u0186\u0005@\u0000\u0000\u0185"+
		"\u0187\u0007\u0005\u0000\u0000\u0186\u0185\u0001\u0000\u0000\u0000\u0187"+
		"\u0188\u0001\u0000\u0000\u0000\u0188\u0186\u0001\u0000\u0000\u0000\u0188"+
		"\u0189\u0001\u0000\u0000\u0000\u0189x\u0001\u0000\u0000\u0000\u018a\u018e"+
		"\u0007\u0006\u0000\u0000\u018b\u018d\u0007\u0005\u0000\u0000\u018c\u018b"+
		"\u0001\u0000\u0000\u0000\u018d\u0190\u0001\u0000\u0000\u0000\u018e\u018c"+
		"\u0001\u0000\u0000\u0000\u018e\u018f\u0001\u0000\u0000\u0000\u018fz\u0001"+
		"\u0000\u0000\u0000\u0190\u018e\u0001\u0000\u0000\u0000\u0191\u0192\u0005"+
		"/\u0000\u0000\u0192\u0193\u0005/\u0000\u0000\u0193\u0197\u0001\u0000\u0000"+
		"\u0000\u0194\u0196\b\u0007\u0000\u0000\u0195\u0194\u0001\u0000\u0000\u0000"+
		"\u0196\u0199\u0001\u0000\u0000\u0000\u0197\u0195\u0001\u0000\u0000\u0000"+
		"\u0197\u0198\u0001\u0000\u0000\u0000\u0198\u019a\u0001\u0000\u0000\u0000"+
		"\u0199\u0197\u0001\u0000\u0000\u0000\u019a\u019b\u0006=\u0001\u0000\u019b"+
		"|\u0001\u0000\u0000\u0000\u019c\u019d\u0005/\u0000\u0000\u019d\u019e\u0005"+
		"*\u0000\u0000\u019e\u01a2\u0001\u0000\u0000\u0000\u019f\u01a1\t\u0000"+
		"\u0000\u0000\u01a0\u019f\u0001\u0000\u0000\u0000\u01a1\u01a4\u0001\u0000"+
		"\u0000\u0000\u01a2\u01a3\u0001\u0000\u0000\u0000\u01a2\u01a0\u0001\u0000"+
		"\u0000\u0000\u01a3\u01a5\u0001\u0000\u0000\u0000\u01a4\u01a2\u0001\u0000"+
		"\u0000\u0000\u01a5\u01a6\u0005*\u0000\u0000\u01a6\u01a7\u0005/\u0000\u0000"+
		"\u01a7\u01a8\u0001\u0000\u0000\u0000\u01a8\u01a9\u0006>\u0001\u0000\u01a9"+
		"~\u0001\u0000\u0000\u0000\u01aa\u01ae\b\b\u0000\u0000\u01ab\u01ac\u0005"+
		"\\\u0000\u0000\u01ac\u01ae\u0007\t\u0000\u0000\u01ad\u01aa\u0001\u0000"+
		"\u0000\u0000\u01ad\u01ab\u0001\u0000\u0000\u0000\u01ae\u0080\u0001\u0000"+
		"\u0000\u0000\u01af\u01b0\u0005\\\u0000\u0000\u01b0\u01b3\b\t\u0000\u0000"+
		"\u01b1\u01b3\u0005\\\u0000\u0000\u01b2\u01af\u0001\u0000\u0000\u0000\u01b2"+
		"\u01b1\u0001\u0000\u0000\u0000\u01b3\u0082\u0001\u0000\u0000\u0000\u01b4"+
		"\u01b6\u0007\n\u0000\u0000\u01b5\u01b4\u0001\u0000\u0000\u0000\u01b6\u01b7"+
		"\u0001\u0000\u0000\u0000\u01b7\u01b5\u0001\u0000\u0000\u0000\u01b7\u01b8"+
		"\u0001\u0000\u0000\u0000\u01b8\u01b9\u0001\u0000\u0000\u0000\u01b9\u01ba"+
		"\u0006A\u0001\u0000\u01ba\u0084\u0001\u0000\u0000\u0000\u01bb\u01bf\u0005"+
		"\"\u0000\u0000\u01bc\u01be\u0003\u007f?\u0000\u01bd\u01bc\u0001\u0000"+
		"\u0000\u0000\u01be\u01c1\u0001\u0000\u0000\u0000\u01bf\u01bd\u0001\u0000"+
		"\u0000\u0000\u01bf\u01c0\u0001\u0000\u0000\u0000\u01c0\u01c2\u0001\u0000"+
		"\u0000\u0000\u01c1\u01bf\u0001\u0000\u0000\u0000\u01c2\u01c3\u0006B\u0002"+
		"\u0000\u01c3\u0086\u0001\u0000\u0000\u0000\u01c4\u01c8\u0005\"\u0000\u0000"+
		"\u01c5\u01c7\u0003\u007f?\u0000\u01c6\u01c5\u0001\u0000\u0000\u0000\u01c7"+
		"\u01ca\u0001\u0000\u0000\u0000\u01c8\u01c6\u0001\u0000\u0000\u0000\u01c8"+
		"\u01c9\u0001\u0000\u0000\u0000\u01c9\u01cb\u0001\u0000\u0000\u0000\u01ca"+
		"\u01c8\u0001\u0000\u0000\u0000\u01cb\u01cc\u0003\u0081@\u0000\u01cc\u01cd"+
		"\u0006C\u0003\u0000\u01cd\u0088\u0001\u0000\u0000\u0000\u01ce\u01cf\t"+
		"\u0000\u0000\u0000\u01cf\u01d0\u0006D\u0004\u0000\u01d0\u008a\u0001\u0000"+
		"\u0000\u0000\u0016\u0000\u0091\u0096\u009d\u00a3\u00a6\u00aa\u00b0\u00b5"+
		"\u00ba\u00be\u00c4\u00cc\u0188\u018e\u0197\u01a2\u01ad\u01b2\u01b7\u01bf"+
		"\u01c8\u0005\u0001\b\u0000\u0006\u0000\u0000\u0001B\u0001\u0001C\u0002"+
		"\u0001D\u0003";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}