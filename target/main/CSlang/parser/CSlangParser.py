# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u0217\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\3\2\6\2x\n\2\r\2\16\2y\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\u0083\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5")
        buf.write("\5\u008f\n\5\3\6\3\6\3\6\5\6\u0094\n\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00a2\n\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\5\b\u00ab\n\b\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\5\f\u00c3\n\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\5\r\u00ca\n\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\5\20\u00d8\n\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u00e0\n\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\5\21\u00e7\n\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00f7\n\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0100\n\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\27\5\27\u0109\n\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0115")
        buf.write("\n\30\3\30\3\30\3\30\3\30\3\30\5\30\u011c\n\30\3\31\3")
        buf.write("\31\3\31\5\31\u0121\n\31\3\31\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u0128\n\31\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\5\37\u0143\n\37\3 \3 \3")
        buf.write(" \3 \3 \5 \u014a\n \3!\3!\3!\3!\3!\3!\7!\u0152\n!\f!\16")
        buf.write("!\u0155\13!\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u015d\n\"\f\"")
        buf.write("\16\"\u0160\13\"\3#\3#\3#\3#\3#\3#\7#\u0168\n#\f#\16#")
        buf.write("\u016b\13#\3$\3$\3$\5$\u0170\n$\3%\3%\3%\5%\u0175\n%\3")
        buf.write("&\3&\3&\3&\3&\3&\5&\u017d\n&\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u018c\n\'\f\'\16\'\u018f")
        buf.write("\13\'\3(\3(\3(\5(\u0194\n(\3(\3(\3(\3(\5(\u019a\n(\3(")
        buf.write("\3(\3(\3(\3(\3(\5(\u01a2\n(\3)\3)\3)\3)\3)\3)\3)\5)\u01ab")
        buf.write("\n)\3*\3*\3*\3*\3*\3*\5*\u01b3\n*\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3,\3,\5,\u01bf\n,\3-\3-\3-\3-\3-\3-\3-\5-\u01c8\n")
        buf.write("-\3.\3.\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\60\5\60\u01d5")
        buf.write("\n\60\3\61\3\61\3\61\3\61\5\61\u01db\n\61\3\62\3\62\5")
        buf.write("\62\u01df\n\62\3\63\3\63\3\63\3\63\3\63\5\63\u01e6\n\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u01ef\n\64\3")
        buf.write("\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\5\66\u01fa")
        buf.write("\n\66\3\67\3\67\3\67\3\67\3\67\5\67\u0201\n\67\38\38\3")
        buf.write("8\38\58\u0207\n8\39\39\39\39\59\u020d\n9\3:\3:\3:\3:\5")
        buf.write(":\u0213\n:\3;\3;\3;\2\6@BDL<\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnprt\2\t\3\2;<\4\2\34\34\36\"\3\2\32\33\3\2\24")
        buf.write("\25\4\2\26\30%%\3\2-\60\3\2\4\5\2\u0223\2w\3\2\2\2\4}")
        buf.write("\3\2\2\2\6\u0086\3\2\2\2\b\u008e\3\2\2\2\n\u0093\3\2\2")
        buf.write("\2\f\u00a1\3\2\2\2\16\u00aa\3\2\2\2\20\u00ac\3\2\2\2\22")
        buf.write("\u00b0\3\2\2\2\24\u00b9\3\2\2\2\26\u00c2\3\2\2\2\30\u00c9")
        buf.write("\3\2\2\2\32\u00cb\3\2\2\2\34\u00cf\3\2\2\2\36\u00d7\3")
        buf.write("\2\2\2 \u00e6\3\2\2\2\"\u00e8\3\2\2\2$\u00f6\3\2\2\2&")
        buf.write("\u00ff\3\2\2\2(\u0101\3\2\2\2*\u0103\3\2\2\2,\u0105\3")
        buf.write("\2\2\2.\u011b\3\2\2\2\60\u011d\3\2\2\2\62\u0129\3\2\2")
        buf.write("\2\64\u012b\3\2\2\2\66\u0133\3\2\2\28\u0137\3\2\2\2:\u0139")
        buf.write("\3\2\2\2<\u0142\3\2\2\2>\u0149\3\2\2\2@\u014b\3\2\2\2")
        buf.write("B\u0156\3\2\2\2D\u0161\3\2\2\2F\u016f\3\2\2\2H\u0174\3")
        buf.write("\2\2\2J\u017c\3\2\2\2L\u017e\3\2\2\2N\u01a1\3\2\2\2P\u01aa")
        buf.write("\3\2\2\2R\u01b2\3\2\2\2T\u01b4\3\2\2\2V\u01be\3\2\2\2")
        buf.write("X\u01c7\3\2\2\2Z\u01c9\3\2\2\2\\\u01ce\3\2\2\2^\u01d4")
        buf.write("\3\2\2\2`\u01da\3\2\2\2b\u01de\3\2\2\2d\u01e5\3\2\2\2")
        buf.write("f\u01ee\3\2\2\2h\u01f0\3\2\2\2j\u01f9\3\2\2\2l\u0200\3")
        buf.write("\2\2\2n\u0206\3\2\2\2p\u020c\3\2\2\2r\u0212\3\2\2\2t\u0214")
        buf.write("\3\2\2\2vx\5\4\3\2wv\3\2\2\2xy\3\2\2\2yw\3\2\2\2yz\3\2")
        buf.write("\2\2z{\3\2\2\2{|\7\2\2\3|\3\3\2\2\2}~\7\63\2\2~\u0082")
        buf.write("\7<\2\2\177\u0080\7\3\2\2\u0080\u0083\7<\2\2\u0081\u0083")
        buf.write("\3\2\2\2\u0082\177\3\2\2\2\u0082\u0081\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\u0085\5\6\4\2\u0085\5\3\2\2\2\u0086\u0087")
        buf.write("\7\f\2\2\u0087\u0088\5\b\5\2\u0088\u0089\7\r\2\2\u0089")
        buf.write("\7\3\2\2\2\u008a\u008b\5\n\6\2\u008b\u008c\5\b\5\2\u008c")
        buf.write("\u008f\3\2\2\2\u008d\u008f\3\2\2\2\u008e\u008a\3\2\2\2")
        buf.write("\u008e\u008d\3\2\2\2\u008f\t\3\2\2\2\u0090\u0094\5\f\7")
        buf.write("\2\u0091\u0094\5\24\13\2\u0092\u0094\5\22\n\2\u0093\u0090")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0092\3\2\2\2\u0094")
        buf.write("\13\3\2\2\2\u0095\u0096\7\t\2\2\u0096\u0097\5^\60\2\u0097")
        buf.write("\u0098\7\23\2\2\u0098\u0099\5V,\2\u0099\u009a\7\22\2\2")
        buf.write("\u009a\u00a2\3\2\2\2\u009b\u009c\7\t\2\2\u009c\u009d\t")
        buf.write("\2\2\2\u009d\u009e\5\16\b\2\u009e\u009f\5<\37\2\u009f")
        buf.write("\u00a0\7\22\2\2\u00a0\u00a2\3\2\2\2\u00a1\u0095\3\2\2")
        buf.write("\2\u00a1\u009b\3\2\2\2\u00a2\r\3\2\2\2\u00a3\u00a4\7\21")
        buf.write("\2\2\u00a4\u00a5\t\2\2\2\u00a5\u00a6\5\16\b\2\u00a6\u00a7")
        buf.write("\5<\37\2\u00a7\u00a8\7\21\2\2\u00a8\u00ab\3\2\2\2\u00a9")
        buf.write("\u00ab\5\20\t\2\u00aa\u00a3\3\2\2\2\u00aa\u00a9\3\2\2")
        buf.write("\2\u00ab\17\3\2\2\2\u00ac\u00ad\7\23\2\2\u00ad\u00ae\5")
        buf.write("V,\2\u00ae\u00af\7\35\2\2\u00af\21\3\2\2\2\u00b0\u00b1")
        buf.write("\7:\2\2\u00b1\u00b2\t\2\2\2\u00b2\u00b3\7\n\2\2\u00b3")
        buf.write("\u00b4\5\26\f\2\u00b4\u00b5\7\13\2\2\u00b5\u00b6\7\23")
        buf.write("\2\2\u00b6\u00b7\5X-\2\u00b7\u00b8\5\34\17\2\u00b8\23")
        buf.write("\3\2\2\2\u00b9\u00ba\7:\2\2\u00ba\u00bb\7\64\2\2\u00bb")
        buf.write("\u00bc\7\n\2\2\u00bc\u00bd\5\26\f\2\u00bd\u00be\7\13\2")
        buf.write("\2\u00be\u00bf\5\34\17\2\u00bf\25\3\2\2\2\u00c0\u00c3")
        buf.write("\5\30\r\2\u00c1\u00c3\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c3\27\3\2\2\2\u00c4\u00c5\5\32\16\2")
        buf.write("\u00c5\u00c6\7\21\2\2\u00c6\u00c7\5\30\r\2\u00c7\u00ca")
        buf.write("\3\2\2\2\u00c8\u00ca\5\32\16\2\u00c9\u00c4\3\2\2\2\u00c9")
        buf.write("\u00c8\3\2\2\2\u00ca\31\3\2\2\2\u00cb\u00cc\5`\61\2\u00cc")
        buf.write("\u00cd\7\23\2\2\u00cd\u00ce\5V,\2\u00ce\33\3\2\2\2\u00cf")
        buf.write("\u00d0\7\f\2\2\u00d0\u00d1\5\36\20\2\u00d1\u00d2\7\r\2")
        buf.write("\2\u00d2\35\3\2\2\2\u00d3\u00d4\5 \21\2\u00d4\u00d5\5")
        buf.write("\36\20\2\u00d5\u00d8\3\2\2\2\u00d6\u00d8\3\2\2\2\u00d7")
        buf.write("\u00d3\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\37\3\2\2\2\u00d9")
        buf.write("\u00e0\5$\23\2\u00da\u00e0\5\"\22\2\u00db\u00e0\5*\26")
        buf.write("\2\u00dc\u00e0\5(\25\2\u00dd\u00e0\5,\27\2\u00de\u00e0")
        buf.write("\5.\30\2\u00df\u00d9\3\2\2\2\u00df\u00da\3\2\2\2\u00df")
        buf.write("\u00db\3\2\2\2\u00df\u00dc\3\2\2\2\u00df\u00dd\3\2\2\2")
        buf.write("\u00df\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\7")
        buf.write("\22\2\2\u00e2\u00e7\3\2\2\2\u00e3\u00e7\5\60\31\2\u00e4")
        buf.write("\u00e7\5\64\33\2\u00e5\u00e7\5\34\17\2\u00e6\u00df\3\2")
        buf.write("\2\2\u00e6\u00e3\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5")
        buf.write("\3\2\2\2\u00e7!\3\2\2\2\u00e8\u00e9\5J&\2\u00e9\u00ea")
        buf.write("\7#\2\2\u00ea\u00eb\5<\37\2\u00eb#\3\2\2\2\u00ec\u00ed")
        buf.write("\7\t\2\2\u00ed\u00ee\5`\61\2\u00ee\u00ef\7\23\2\2\u00ef")
        buf.write("\u00f0\5V,\2\u00f0\u00f7\3\2\2\2\u00f1\u00f2\7\t\2\2\u00f2")
        buf.write("\u00f3\7<\2\2\u00f3\u00f4\5&\24\2\u00f4\u00f5\5<\37\2")
        buf.write("\u00f5\u00f7\3\2\2\2\u00f6\u00ec\3\2\2\2\u00f6\u00f1\3")
        buf.write("\2\2\2\u00f7%\3\2\2\2\u00f8\u00f9\7\21\2\2\u00f9\u00fa")
        buf.write("\7<\2\2\u00fa\u00fb\5&\24\2\u00fb\u00fc\5<\37\2\u00fc")
        buf.write("\u00fd\7\21\2\2\u00fd\u0100\3\2\2\2\u00fe\u0100\5\20\t")
        buf.write("\2\u00ff\u00f8\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100\'\3\2")
        buf.write("\2\2\u0101\u0102\7\'\2\2\u0102)\3\2\2\2\u0103\u0104\7")
        buf.write("&\2\2\u0104+\3\2\2\2\u0105\u0108\7\61\2\2\u0106\u0109")
        buf.write("\5<\37\2\u0107\u0109\3\2\2\2\u0108\u0106\3\2\2\2\u0108")
        buf.write("\u0107\3\2\2\2\u0109-\3\2\2\2\u010a\u010b\5J&\2\u010b")
        buf.write("\u010c\7\20\2\2\u010c\u010d\7<\2\2\u010d\u010e\7\n\2\2")
        buf.write("\u010e\u010f\5b\62\2\u010f\u0110\7\13\2\2\u0110\u011c")
        buf.write("\3\2\2\2\u0111\u0112\7<\2\2\u0112\u0115\7\20\2\2\u0113")
        buf.write("\u0115\3\2\2\2\u0114\u0111\3\2\2\2\u0114\u0113\3\2\2\2")
        buf.write("\u0115\u0116\3\2\2\2\u0116\u0117\7;\2\2\u0117\u0118\7")
        buf.write("\n\2\2\u0118\u0119\5b\62\2\u0119\u011a\7\13\2\2\u011a")
        buf.write("\u011c\3\2\2\2\u011b\u010a\3\2\2\2\u011b\u0114\3\2\2\2")
        buf.write("\u011c/\3\2\2\2\u011d\u0120\7(\2\2\u011e\u0121\5\62\32")
        buf.write("\2\u011f\u0121\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u011f")
        buf.write("\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123\5<\37\2\u0123")
        buf.write("\u0127\5\34\17\2\u0124\u0125\7)\2\2\u0125\u0128\5\34\17")
        buf.write("\2\u0126\u0128\3\2\2\2\u0127\u0124\3\2\2\2\u0127\u0126")
        buf.write("\3\2\2\2\u0128\61\3\2\2\2\u0129\u012a\5\34\17\2\u012a")
        buf.write("\63\3\2\2\2\u012b\u012c\7*\2\2\u012c\u012d\5\66\34\2\u012d")
        buf.write("\u012e\7\22\2\2\u012e\u012f\58\35\2\u012f\u0130\7\22\2")
        buf.write("\2\u0130\u0131\5:\36\2\u0131\u0132\5\34\17\2\u0132\65")
        buf.write("\3\2\2\2\u0133\u0134\5J&\2\u0134\u0135\7#\2\2\u0135\u0136")
        buf.write("\5<\37\2\u0136\67\3\2\2\2\u0137\u0138\5<\37\2\u01389\3")
        buf.write("\2\2\2\u0139\u013a\5J&\2\u013a\u013b\7#\2\2\u013b\u013c")
        buf.write("\5<\37\2\u013c;\3\2\2\2\u013d\u013e\5> \2\u013e\u013f")
        buf.write("\7$\2\2\u013f\u0140\5> \2\u0140\u0143\3\2\2\2\u0141\u0143")
        buf.write("\5> \2\u0142\u013d\3\2\2\2\u0142\u0141\3\2\2\2\u0143=")
        buf.write("\3\2\2\2\u0144\u0145\5@!\2\u0145\u0146\t\3\2\2\u0146\u0147")
        buf.write("\5@!\2\u0147\u014a\3\2\2\2\u0148\u014a\5@!\2\u0149\u0144")
        buf.write("\3\2\2\2\u0149\u0148\3\2\2\2\u014a?\3\2\2\2\u014b\u014c")
        buf.write("\b!\1\2\u014c\u014d\5B\"\2\u014d\u0153\3\2\2\2\u014e\u014f")
        buf.write("\f\4\2\2\u014f\u0150\t\4\2\2\u0150\u0152\5B\"\2\u0151")
        buf.write("\u014e\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2")
        buf.write("\u0153\u0154\3\2\2\2\u0154A\3\2\2\2\u0155\u0153\3\2\2")
        buf.write("\2\u0156\u0157\b\"\1\2\u0157\u0158\5D#\2\u0158\u015e\3")
        buf.write("\2\2\2\u0159\u015a\f\4\2\2\u015a\u015b\t\5\2\2\u015b\u015d")
        buf.write("\5D#\2\u015c\u0159\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c")
        buf.write("\3\2\2\2\u015e\u015f\3\2\2\2\u015fC\3\2\2\2\u0160\u015e")
        buf.write("\3\2\2\2\u0161\u0162\b#\1\2\u0162\u0163\5F$\2\u0163\u0169")
        buf.write("\3\2\2\2\u0164\u0165\f\4\2\2\u0165\u0166\t\6\2\2\u0166")
        buf.write("\u0168\5F$\2\u0167\u0164\3\2\2\2\u0168\u016b\3\2\2\2\u0169")
        buf.write("\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016aE\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u016d\7\31\2\2\u016d\u0170\5F$\2")
        buf.write("\u016e\u0170\5H%\2\u016f\u016c\3\2\2\2\u016f\u016e\3\2")
        buf.write("\2\2\u0170G\3\2\2\2\u0171\u0172\7\25\2\2\u0172\u0175\5")
        buf.write("H%\2\u0173\u0175\5J&\2\u0174\u0171\3\2\2\2\u0174\u0173")
        buf.write("\3\2\2\2\u0175I\3\2\2\2\u0176\u0177\5L\'\2\u0177\u0178")
        buf.write("\7\16\2\2\u0178\u0179\5<\37\2\u0179\u017a\7\17\2\2\u017a")
        buf.write("\u017d\3\2\2\2\u017b\u017d\5L\'\2\u017c\u0176\3\2\2\2")
        buf.write("\u017c\u017b\3\2\2\2\u017dK\3\2\2\2\u017e\u017f\b\'\1")
        buf.write("\2\u017f\u0180\5N(\2\u0180\u018d\3\2\2\2\u0181\u0182\f")
        buf.write("\5\2\2\u0182\u0183\7\20\2\2\u0183\u018c\7<\2\2\u0184\u0185")
        buf.write("\f\4\2\2\u0185\u0186\7\20\2\2\u0186\u0187\7<\2\2\u0187")
        buf.write("\u0188\7\n\2\2\u0188\u0189\5b\62\2\u0189\u018a\7\13\2")
        buf.write("\2\u018a\u018c\3\2\2\2\u018b\u0181\3\2\2\2\u018b\u0184")
        buf.write("\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u018b\3\2\2\2\u018d")
        buf.write("\u018e\3\2\2\2\u018eM\3\2\2\2\u018f\u018d\3\2\2\2\u0190")
        buf.write("\u0191\7<\2\2\u0191\u0194\7\20\2\2\u0192\u0194\3\2\2\2")
        buf.write("\u0193\u0190\3\2\2\2\u0193\u0192\3\2\2\2\u0194\u0195\3")
        buf.write("\2\2\2\u0195\u01a2\7;\2\2\u0196\u0197\7<\2\2\u0197\u019a")
        buf.write("\7\20\2\2\u0198\u019a\3\2\2\2\u0199\u0196\3\2\2\2\u0199")
        buf.write("\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019c\7;\2\2")
        buf.write("\u019c\u019d\7\n\2\2\u019d\u019e\5b\62\2\u019e\u019f\7")
        buf.write("\13\2\2\u019f\u01a2\3\2\2\2\u01a0\u01a2\5P)\2\u01a1\u0193")
        buf.write("\3\2\2\2\u01a1\u0199\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2")
        buf.write("O\3\2\2\2\u01a3\u01a4\7\67\2\2\u01a4\u01a5\7<\2\2\u01a5")
        buf.write("\u01a6\7\n\2\2\u01a6\u01a7\5b\62\2\u01a7\u01a8\7\13\2")
        buf.write("\2\u01a8\u01ab\3\2\2\2\u01a9\u01ab\5R*\2\u01aa\u01a3\3")
        buf.write("\2\2\2\u01aa\u01a9\3\2\2\2\u01abQ\3\2\2\2\u01ac\u01b3")
        buf.write("\5T+\2\u01ad\u01b3\7<\2\2\u01ae\u01b3\7;\2\2\u01af\u01b3")
        buf.write("\5f\64\2\u01b0\u01b3\7\66\2\2\u01b1\u01b3\7\62\2\2\u01b2")
        buf.write("\u01ac\3\2\2\2\u01b2\u01ad\3\2\2\2\u01b2\u01ae\3\2\2\2")
        buf.write("\u01b2\u01af\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b1\3")
        buf.write("\2\2\2\u01b3S\3\2\2\2\u01b4\u01b5\7\n\2\2\u01b5\u01b6")
        buf.write("\5<\37\2\u01b6\u01b7\7\13\2\2\u01b7U\3\2\2\2\u01b8\u01bf")
        buf.write("\7-\2\2\u01b9\u01bf\7.\2\2\u01ba\u01bf\7/\2\2\u01bb\u01bf")
        buf.write("\7\60\2\2\u01bc\u01bf\5Z.\2\u01bd\u01bf\7<\2\2\u01be\u01b8")
        buf.write("\3\2\2\2\u01be\u01b9\3\2\2\2\u01be\u01ba\3\2\2\2\u01be")
        buf.write("\u01bb\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2")
        buf.write("\u01bfW\3\2\2\2\u01c0\u01c8\7-\2\2\u01c1\u01c8\7.\2\2")
        buf.write("\u01c2\u01c8\7/\2\2\u01c3\u01c8\7\60\2\2\u01c4\u01c8\5")
        buf.write("Z.\2\u01c5\u01c8\7<\2\2\u01c6\u01c8\78\2\2\u01c7\u01c0")
        buf.write("\3\2\2\2\u01c7\u01c1\3\2\2\2\u01c7\u01c2\3\2\2\2\u01c7")
        buf.write("\u01c3\3\2\2\2\u01c7\u01c4\3\2\2\2\u01c7\u01c5\3\2\2\2")
        buf.write("\u01c7\u01c6\3\2\2\2\u01c8Y\3\2\2\2\u01c9\u01ca\7\16\2")
        buf.write("\2\u01ca\u01cb\7\5\2\2\u01cb\u01cc\7\17\2\2\u01cc\u01cd")
        buf.write("\5\\/\2\u01cd[\3\2\2\2\u01ce\u01cf\t\7\2\2\u01cf]\3\2")
        buf.write("\2\2\u01d0\u01d1\t\2\2\2\u01d1\u01d2\7\21\2\2\u01d2\u01d5")
        buf.write("\5^\60\2\u01d3\u01d5\t\2\2\2\u01d4\u01d0\3\2\2\2\u01d4")
        buf.write("\u01d3\3\2\2\2\u01d5_\3\2\2\2\u01d6\u01d7\7<\2\2\u01d7")
        buf.write("\u01d8\7\21\2\2\u01d8\u01db\5`\61\2\u01d9\u01db\7<\2\2")
        buf.write("\u01da\u01d6\3\2\2\2\u01da\u01d9\3\2\2\2\u01dba\3\2\2")
        buf.write("\2\u01dc\u01df\5d\63\2\u01dd\u01df\3\2\2\2\u01de\u01dc")
        buf.write("\3\2\2\2\u01de\u01dd\3\2\2\2\u01dfc\3\2\2\2\u01e0\u01e1")
        buf.write("\5<\37\2\u01e1\u01e2\7\21\2\2\u01e2\u01e3\5d\63\2\u01e3")
        buf.write("\u01e6\3\2\2\2\u01e4\u01e6\5<\37\2\u01e5\u01e0\3\2\2\2")
        buf.write("\u01e5\u01e4\3\2\2\2\u01e6e\3\2\2\2\u01e7\u01ef\5h\65")
        buf.write("\2\u01e8\u01ef\5t;\2\u01e9\u01ef\7\6\2\2\u01ea\u01ef\7")
        buf.write("\7\2\2\u01eb\u01ef\7\b\2\2\u01ec\u01ef\7\62\2\2\u01ed")
        buf.write("\u01ef\7<\2\2\u01ee\u01e7\3\2\2\2\u01ee\u01e8\3\2\2\2")
        buf.write("\u01ee\u01e9\3\2\2\2\u01ee\u01ea\3\2\2\2\u01ee\u01eb\3")
        buf.write("\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ed\3\2\2\2\u01efg")
        buf.write("\3\2\2\2\u01f0\u01f1\7\16\2\2\u01f1\u01f2\5j\66\2\u01f2")
        buf.write("\u01f3\7\17\2\2\u01f3i\3\2\2\2\u01f4\u01f5\5f\64\2\u01f5")
        buf.write("\u01f6\7\21\2\2\u01f6\u01f7\5j\66\2\u01f7\u01fa\3\2\2")
        buf.write("\2\u01f8\u01fa\5f\64\2\u01f9\u01f4\3\2\2\2\u01f9\u01f8")
        buf.write("\3\2\2\2\u01fak\3\2\2\2\u01fb\u01fc\5t;\2\u01fc\u01fd")
        buf.write("\7\21\2\2\u01fd\u01fe\5l\67\2\u01fe\u0201\3\2\2\2\u01ff")
        buf.write("\u0201\5t;\2\u0200\u01fb\3\2\2\2\u0200\u01ff\3\2\2\2\u0201")
        buf.write("m\3\2\2\2\u0202\u0203\7\6\2\2\u0203\u0204\7\21\2\2\u0204")
        buf.write("\u0207\5n8\2\u0205\u0207\7\6\2\2\u0206\u0202\3\2\2\2\u0206")
        buf.write("\u0205\3\2\2\2\u0207o\3\2\2\2\u0208\u0209\7\7\2\2\u0209")
        buf.write("\u020a\7\21\2\2\u020a\u020d\5p9\2\u020b\u020d\7\7\2\2")
        buf.write("\u020c\u0208\3\2\2\2\u020c\u020b\3\2\2\2\u020dq\3\2\2")
        buf.write("\2\u020e\u020f\7\b\2\2\u020f\u0210\7\21\2\2\u0210\u0213")
        buf.write("\5r:\2\u0211\u0213\7\b\2\2\u0212\u020e\3\2\2\2\u0212\u0211")
        buf.write("\3\2\2\2\u0213s\3\2\2\2\u0214\u0215\t\b\2\2\u0215u\3\2")
        buf.write("\2\2/y\u0082\u008e\u0093\u00a1\u00aa\u00c2\u00c9\u00d7")
        buf.write("\u00df\u00e6\u00f6\u00ff\u0108\u0114\u011b\u0120\u0127")
        buf.write("\u0142\u0149\u0153\u015e\u0169\u016f\u0174\u017c\u018b")
        buf.write("\u018d\u0193\u0199\u01a1\u01aa\u01b2\u01be\u01c7\u01d4")
        buf.write("\u01da\u01de\u01e5\u01ee\u01f9\u0200\u0206\u020c\u0212")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "'.'", "','", "';'", "':'", 
                     "'+'", "'-'", "'*'", "'/'", "'\\'", "'!'", "'&&'", 
                     "'||'", "'=='", "'='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "':='", "'^'", "'%'", "'break'", "'continue'", 
                     "'if'", "'else'", "'for'", "'true'", "'false'", "'int'", 
                     "'float'", "'bool'", "'string'", "'return'", "'null'", 
                     "'class'", "'constructor'", "'var'", "'self'", "'new'", 
                     "'void'", "'const'", "'func'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ZERO", "DIGIT", "FLOATLIT", 
                      "BOOLIT", "STRINGLIT", "CONST_VAR", "LP", "RP", "LCURB", 
                      "RCURB", "LSQAB", "RSQAB", "DOT", "COMMA", "SEMI", 
                      "COLON", "ADD", "SUBTRAC", "MULTI", "DIVID", "BSLASH", 
                      "NOT", "AND", "OR", "ISEQUAL", "EQUAL", "NOTEQUAL", 
                      "LESSTHAN", "LESSTHANOREQ", "GREATERTHAN", "GREATERTHANOREQ", 
                      "ASSIGN", "STRINGCON", "MODUL", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", 
                      "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
                      "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "A_ID", 
                      "ID", "CMSINGLE", "CMMULTI", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_dcl = 1
    RULE_class_body = 2
    RULE_decls = 3
    RULE_decl = 4
    RULE_att_decl = 5
    RULE_recursion_att = 6
    RULE_vari_decl = 7
    RULE_method_decl = 8
    RULE_constructor_decl = 9
    RULE_paramlist = 10
    RULE_paramprime = 11
    RULE_param = 12
    RULE_block_stmt = 13
    RULE_stmtlist = 14
    RULE_stmt = 15
    RULE_asm_stmt = 16
    RULE_var_stmt = 17
    RULE_recursion_vari = 18
    RULE_continue_stmt = 19
    RULE_break_stmt = 20
    RULE_return_stmt = 21
    RULE_call_stmt = 22
    RULE_if_stmt = 23
    RULE_preblock_stmt = 24
    RULE_for_stmt = 25
    RULE_init_stmt = 26
    RULE_condition_expr = 27
    RULE_post_stmt = 28
    RULE_expr = 29
    RULE_expr1 = 30
    RULE_expr2 = 31
    RULE_expr3 = 32
    RULE_expr4 = 33
    RULE_expr5 = 34
    RULE_expr6 = 35
    RULE_expr7 = 36
    RULE_expr8 = 37
    RULE_expr9 = 38
    RULE_expr10 = 39
    RULE_expr11 = 40
    RULE_subexpr = 41
    RULE_data_type_decl = 42
    RULE_data_type = 43
    RULE_array_type = 44
    RULE_array_data_type_decl = 45
    RULE_super_idlist = 46
    RULE_idlist = 47
    RULE_empty_exprlist = 48
    RULE_exprprime = 49
    RULE_lit = 50
    RULE_arraylit = 51
    RULE_array_decl = 52
    RULE_array_int = 53
    RULE_array_float = 54
    RULE_array_bool = 55
    RULE_array_string = 56
    RULE_intlit = 57

    ruleNames =  [ "program", "class_dcl", "class_body", "decls", "decl", 
                   "att_decl", "recursion_att", "vari_decl", "method_decl", 
                   "constructor_decl", "paramlist", "paramprime", "param", 
                   "block_stmt", "stmtlist", "stmt", "asm_stmt", "var_stmt", 
                   "recursion_vari", "continue_stmt", "break_stmt", "return_stmt", 
                   "call_stmt", "if_stmt", "preblock_stmt", "for_stmt", 
                   "init_stmt", "condition_expr", "post_stmt", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "expr8", "expr9", "expr10", "expr11", "subexpr", "data_type_decl", 
                   "data_type", "array_type", "array_data_type_decl", "super_idlist", 
                   "idlist", "empty_exprlist", "exprprime", "lit", "arraylit", 
                   "array_decl", "array_int", "array_float", "array_bool", 
                   "array_string", "intlit" ]

    EOF = Token.EOF
    T__0=1
    ZERO=2
    DIGIT=3
    FLOATLIT=4
    BOOLIT=5
    STRINGLIT=6
    CONST_VAR=7
    LP=8
    RP=9
    LCURB=10
    RCURB=11
    LSQAB=12
    RSQAB=13
    DOT=14
    COMMA=15
    SEMI=16
    COLON=17
    ADD=18
    SUBTRAC=19
    MULTI=20
    DIVID=21
    BSLASH=22
    NOT=23
    AND=24
    OR=25
    ISEQUAL=26
    EQUAL=27
    NOTEQUAL=28
    LESSTHAN=29
    LESSTHANOREQ=30
    GREATERTHAN=31
    GREATERTHANOREQ=32
    ASSIGN=33
    STRINGCON=34
    MODUL=35
    BREAK=36
    CONTINUE=37
    IF=38
    ELSE=39
    FOR=40
    TRUE=41
    FALSE=42
    INT=43
    FLOAT=44
    BOOL=45
    STRING=46
    RETURN=47
    NULL=48
    CLASS=49
    CONSTRUCTOR=50
    VAR=51
    SELF=52
    NEW=53
    VOID=54
    CONST=55
    FUNC=56
    A_ID=57
    ID=58
    CMSINGLE=59
    CMMULTI=60
    WS=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    ERROR_CHAR=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def class_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Class_dclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Class_dclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 116
                self.class_dcl()
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSlangParser.CLASS):
                    break

            self.state = 121
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

        def class_body(self):
            return self.getTypedRuleContext(CSlangParser.Class_bodyContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_dcl" ):
                return visitor.visitClass_dcl(self)
            else:
                return visitor.visitChildren(self)




    def class_dcl(self):

        localctx = CSlangParser.Class_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(CSlangParser.CLASS)
            self.state = 124
            self.match(CSlangParser.ID)
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.T__0]:
                self.state = 125
                self.match(CSlangParser.T__0)
                self.state = 126
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.LCURB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 130
            self.class_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCURB(self):
            return self.getToken(CSlangParser.LCURB, 0)

        def decls(self):
            return self.getTypedRuleContext(CSlangParser.DeclsContext,0)


        def RCURB(self):
            return self.getToken(CSlangParser.RCURB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_class_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = CSlangParser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(CSlangParser.LCURB)
            self.state = 133
            self.decls()
            self.state = 134
            self.match(CSlangParser.RCURB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(CSlangParser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(CSlangParser.DeclsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = CSlangParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decls)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CONST_VAR, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.decl()
                self.state = 137
                self.decls()
                pass
            elif token in [CSlangParser.RCURB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def att_decl(self):
            return self.getTypedRuleContext(CSlangParser.Att_declContext,0)


        def constructor_decl(self):
            return self.getTypedRuleContext(CSlangParser.Constructor_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(CSlangParser.Method_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = CSlangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decl)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.att_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.constructor_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Att_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST_VAR(self):
            return self.getToken(CSlangParser.CONST_VAR, 0)

        def super_idlist(self):
            return self.getTypedRuleContext(CSlangParser.Super_idlistContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def data_type_decl(self):
            return self.getTypedRuleContext(CSlangParser.Data_type_declContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def recursion_att(self):
            return self.getTypedRuleContext(CSlangParser.Recursion_attContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def A_ID(self):
            return self.getToken(CSlangParser.A_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_att_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtt_decl" ):
                return visitor.visitAtt_decl(self)
            else:
                return visitor.visitChildren(self)




    def att_decl(self):

        localctx = CSlangParser.Att_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_att_decl)
        self._la = 0 # Token type
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(CSlangParser.CONST_VAR)
                self.state = 148
                self.super_idlist()
                self.state = 149
                self.match(CSlangParser.COLON)
                self.state = 150
                self.data_type_decl()
                self.state = 151
                self.match(CSlangParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.match(CSlangParser.CONST_VAR)
                self.state = 154
                _la = self._input.LA(1)
                if not(_la==CSlangParser.A_ID or _la==CSlangParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 155
                self.recursion_att()
                self.state = 156
                self.expr()
                self.state = 157
                self.match(CSlangParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Recursion_attContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def recursion_att(self):
            return self.getTypedRuleContext(CSlangParser.Recursion_attContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def A_ID(self):
            return self.getToken(CSlangParser.A_ID, 0)

        def vari_decl(self):
            return self.getTypedRuleContext(CSlangParser.Vari_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_recursion_att

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecursion_att" ):
                return visitor.visitRecursion_att(self)
            else:
                return visitor.visitChildren(self)




    def recursion_att(self):

        localctx = CSlangParser.Recursion_attContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_recursion_att)
        self._la = 0 # Token type
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(CSlangParser.COMMA)
                self.state = 162
                _la = self._input.LA(1)
                if not(_la==CSlangParser.A_ID or _la==CSlangParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 163
                self.recursion_att()
                self.state = 164
                self.expr()
                self.state = 165
                self.match(CSlangParser.COMMA)
                pass
            elif token in [CSlangParser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.vari_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def data_type_decl(self):
            return self.getTypedRuleContext(CSlangParser.Data_type_declContext,0)


        def EQUAL(self):
            return self.getToken(CSlangParser.EQUAL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_vari_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decl" ):
                return visitor.visitVari_decl(self)
            else:
                return visitor.visitChildren(self)




    def vari_decl(self):

        localctx = CSlangParser.Vari_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vari_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(CSlangParser.COLON)
            self.state = 171
            self.data_type_decl()
            self.state = 172
            self.match(CSlangParser.EQUAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(CSlangParser.ParamlistContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(CSlangParser.Data_typeContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def A_ID(self):
            return self.getToken(CSlangParser.A_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = CSlangParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(CSlangParser.FUNC)
            self.state = 175
            _la = self._input.LA(1)
            if not(_la==CSlangParser.A_ID or _la==CSlangParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 176
            self.match(CSlangParser.LP)
            self.state = 177
            self.paramlist()
            self.state = 178
            self.match(CSlangParser.RP)
            self.state = 179
            self.match(CSlangParser.COLON)
            self.state = 180
            self.data_type()
            self.state = 181
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def CONSTRUCTOR(self):
            return self.getToken(CSlangParser.CONSTRUCTOR, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(CSlangParser.ParamlistContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constructor_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_decl" ):
                return visitor.visitConstructor_decl(self)
            else:
                return visitor.visitChildren(self)




    def constructor_decl(self):

        localctx = CSlangParser.Constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(CSlangParser.FUNC)
            self.state = 184
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 185
            self.match(CSlangParser.LP)
            self.state = 186
            self.paramlist()
            self.state = 187
            self.match(CSlangParser.RP)
            self.state = 188
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(CSlangParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = CSlangParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramlist)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.paramprime()
                pass
            elif token in [CSlangParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(CSlangParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def paramprime(self):
            return self.getTypedRuleContext(CSlangParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = CSlangParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paramprime)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.param()
                self.state = 195
                self.match(CSlangParser.COMMA)
                self.state = 196
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(CSlangParser.IdlistContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def data_type_decl(self):
            return self.getTypedRuleContext(CSlangParser.Data_type_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = CSlangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.idlist()
            self.state = 202
            self.match(CSlangParser.COLON)
            self.state = 203
            self.data_type_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCURB(self):
            return self.getToken(CSlangParser.LCURB, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(CSlangParser.StmtlistContext,0)


        def RCURB(self):
            return self.getToken(CSlangParser.RCURB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = CSlangParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(CSlangParser.LCURB)
            self.state = 206
            self.stmtlist()
            self.state = 207
            self.match(CSlangParser.RCURB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(CSlangParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(CSlangParser.StmtlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = CSlangParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmtlist)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ZERO, CSlangParser.DIGIT, CSlangParser.FLOATLIT, CSlangParser.BOOLIT, CSlangParser.STRINGLIT, CSlangParser.CONST_VAR, CSlangParser.LP, CSlangParser.LCURB, CSlangParser.LSQAB, CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.RETURN, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.A_ID, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.stmt()
                self.state = 210
                self.stmtlist()
                pass
            elif token in [CSlangParser.RCURB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def var_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Var_stmtContext,0)


        def asm_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Asm_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Return_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Call_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(CSlangParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(CSlangParser.For_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmt)
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ZERO, CSlangParser.DIGIT, CSlangParser.FLOATLIT, CSlangParser.BOOLIT, CSlangParser.STRINGLIT, CSlangParser.CONST_VAR, CSlangParser.LP, CSlangParser.LSQAB, CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.RETURN, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.A_ID, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 215
                    self.var_stmt()
                    pass

                elif la_ == 2:
                    self.state = 216
                    self.asm_stmt()
                    pass

                elif la_ == 3:
                    self.state = 217
                    self.break_stmt()
                    pass

                elif la_ == 4:
                    self.state = 218
                    self.continue_stmt()
                    pass

                elif la_ == 5:
                    self.state = 219
                    self.return_stmt()
                    pass

                elif la_ == 6:
                    self.state = 220
                    self.call_stmt()
                    pass


                self.state = 223
                self.match(CSlangParser.SEMI)
                pass
            elif token in [CSlangParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.if_stmt()
                pass
            elif token in [CSlangParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 226
                self.for_stmt()
                pass
            elif token in [CSlangParser.LCURB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 227
                self.block_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asm_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_asm_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsm_stmt" ):
                return visitor.visitAsm_stmt(self)
            else:
                return visitor.visitChildren(self)




    def asm_stmt(self):

        localctx = CSlangParser.Asm_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_asm_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.expr7()
            self.state = 231
            self.match(CSlangParser.ASSIGN)
            self.state = 232
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST_VAR(self):
            return self.getToken(CSlangParser.CONST_VAR, 0)

        def idlist(self):
            return self.getTypedRuleContext(CSlangParser.IdlistContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def data_type_decl(self):
            return self.getTypedRuleContext(CSlangParser.Data_type_declContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def recursion_vari(self):
            return self.getTypedRuleContext(CSlangParser.Recursion_variContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_var_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_stmt" ):
                return visitor.visitVar_stmt(self)
            else:
                return visitor.visitChildren(self)




    def var_stmt(self):

        localctx = CSlangParser.Var_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_var_stmt)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(CSlangParser.CONST_VAR)
                self.state = 235
                self.idlist()
                self.state = 236
                self.match(CSlangParser.COLON)
                self.state = 237
                self.data_type_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(CSlangParser.CONST_VAR)
                self.state = 240
                self.match(CSlangParser.ID)
                self.state = 241
                self.recursion_vari()
                self.state = 242
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Recursion_variContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def recursion_vari(self):
            return self.getTypedRuleContext(CSlangParser.Recursion_variContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def vari_decl(self):
            return self.getTypedRuleContext(CSlangParser.Vari_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_recursion_vari

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecursion_vari" ):
                return visitor.visitRecursion_vari(self)
            else:
                return visitor.visitChildren(self)




    def recursion_vari(self):

        localctx = CSlangParser.Recursion_variContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_recursion_vari)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(CSlangParser.COMMA)
                self.state = 247
                self.match(CSlangParser.ID)
                self.state = 248
                self.recursion_vari()
                self.state = 249
                self.expr()
                self.state = 250
                self.match(CSlangParser.COMMA)
                pass
            elif token in [CSlangParser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.vari_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = CSlangParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(CSlangParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = CSlangParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(CSlangParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = CSlangParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(CSlangParser.RETURN)
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ZERO, CSlangParser.DIGIT, CSlangParser.FLOATLIT, CSlangParser.BOOLIT, CSlangParser.STRINGLIT, CSlangParser.LP, CSlangParser.LSQAB, CSlangParser.SUBTRAC, CSlangParser.NOT, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.A_ID, CSlangParser.ID]:
                self.state = 260
                self.expr()
                pass
            elif token in [CSlangParser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def empty_exprlist(self):
            return self.getTypedRuleContext(CSlangParser.Empty_exprlistContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def A_ID(self):
            return self.getToken(CSlangParser.A_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = CSlangParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_call_stmt)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.expr7()
                self.state = 265
                self.match(CSlangParser.DOT)
                self.state = 266
                self.match(CSlangParser.ID)
                self.state = 267
                self.match(CSlangParser.LP)
                self.state = 268
                self.empty_exprlist()
                self.state = 269
                self.match(CSlangParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.ID]:
                    self.state = 271
                    self.match(CSlangParser.ID)
                    self.state = 272
                    self.match(CSlangParser.DOT)
                    pass
                elif token in [CSlangParser.A_ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 276
                self.match(CSlangParser.A_ID)
                self.state = 277
                self.match(CSlangParser.LP)
                self.state = 278
                self.empty_exprlist()
                self.state = 279
                self.match(CSlangParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Block_stmtContext,i)


        def preblock_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Preblock_stmtContext,0)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = CSlangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(CSlangParser.IF)
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LCURB]:
                self.state = 284
                self.preblock_stmt()
                pass
            elif token in [CSlangParser.ZERO, CSlangParser.DIGIT, CSlangParser.FLOATLIT, CSlangParser.BOOLIT, CSlangParser.STRINGLIT, CSlangParser.LP, CSlangParser.LSQAB, CSlangParser.SUBTRAC, CSlangParser.NOT, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.A_ID, CSlangParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 288
            self.expr()
            self.state = 289
            self.block_stmt()
            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ELSE]:
                self.state = 290
                self.match(CSlangParser.ELSE)
                self.state = 291
                self.block_stmt()
                pass
            elif token in [CSlangParser.ZERO, CSlangParser.DIGIT, CSlangParser.FLOATLIT, CSlangParser.BOOLIT, CSlangParser.STRINGLIT, CSlangParser.CONST_VAR, CSlangParser.LP, CSlangParser.LCURB, CSlangParser.RCURB, CSlangParser.LSQAB, CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.RETURN, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.A_ID, CSlangParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Preblock_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_preblock_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreblock_stmt" ):
                return visitor.visitPreblock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def preblock_stmt(self):

        localctx = CSlangParser.Preblock_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_preblock_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def init_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Init_stmtContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.SEMI)
            else:
                return self.getToken(CSlangParser.SEMI, i)

        def condition_expr(self):
            return self.getTypedRuleContext(CSlangParser.Condition_exprContext,0)


        def post_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Post_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = CSlangParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(CSlangParser.FOR)
            self.state = 298
            self.init_stmt()
            self.state = 299
            self.match(CSlangParser.SEMI)
            self.state = 300
            self.condition_expr()
            self.state = 301
            self.match(CSlangParser.SEMI)
            self.state = 302
            self.post_stmt()
            self.state = 303
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_init_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_stmt" ):
                return visitor.visitInit_stmt(self)
            else:
                return visitor.visitChildren(self)




    def init_stmt(self):

        localctx = CSlangParser.Init_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_init_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.expr7()
            self.state = 306
            self.match(CSlangParser.ASSIGN)
            self.state = 307
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_condition_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_expr" ):
                return visitor.visitCondition_expr(self)
            else:
                return visitor.visitChildren(self)




    def condition_expr(self):

        localctx = CSlangParser.Condition_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_condition_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Post_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_post_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPost_stmt" ):
                return visitor.visitPost_stmt(self)
            else:
                return visitor.visitChildren(self)




    def post_stmt(self):

        localctx = CSlangParser.Post_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_post_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.expr7()
            self.state = 312
            self.match(CSlangParser.ASSIGN)
            self.state = 313
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr1Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr1Context,i)


        def STRINGCON(self):
            return self.getToken(CSlangParser.STRINGCON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CSlangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.expr1()
                self.state = 316
                self.match(CSlangParser.STRINGCON)
                self.state = 317
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr2Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr2Context,i)


        def ISEQUAL(self):
            return self.getToken(CSlangParser.ISEQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(CSlangParser.NOTEQUAL, 0)

        def LESSTHAN(self):
            return self.getToken(CSlangParser.LESSTHAN, 0)

        def LESSTHANOREQ(self):
            return self.getToken(CSlangParser.LESSTHANOREQ, 0)

        def GREATERTHAN(self):
            return self.getToken(CSlangParser.GREATERTHAN, 0)

        def GREATERTHANOREQ(self):
            return self.getToken(CSlangParser.GREATERTHANOREQ, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = CSlangParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.expr2(0)
                self.state = 323
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.ISEQUAL) | (1 << CSlangParser.NOTEQUAL) | (1 << CSlangParser.LESSTHAN) | (1 << CSlangParser.LESSTHANOREQ) | (1 << CSlangParser.GREATERTHAN) | (1 << CSlangParser.GREATERTHANOREQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 324
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(CSlangParser.Expr2Context,0)


        def AND(self):
            return self.getToken(CSlangParser.AND, 0)

        def OR(self):
            return self.getToken(CSlangParser.OR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 337
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 332
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 333
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND or _la==CSlangParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 334
                    self.expr3(0) 
                self.state = 339
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(CSlangParser.ADD, 0)

        def SUBTRAC(self):
            return self.getToken(CSlangParser.SUBTRAC, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 348
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 343
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 344
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD or _la==CSlangParser.SUBTRAC):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 345
                    self.expr4(0) 
                self.state = 350
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def MULTI(self):
            return self.getToken(CSlangParser.MULTI, 0)

        def DIVID(self):
            return self.getToken(CSlangParser.DIVID, 0)

        def BSLASH(self):
            return self.getToken(CSlangParser.BSLASH, 0)

        def MODUL(self):
            return self.getToken(CSlangParser.MODUL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 359
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 354
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 355
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MULTI) | (1 << CSlangParser.DIVID) | (1 << CSlangParser.BSLASH) | (1 << CSlangParser.MODUL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 356
                    self.expr5() 
                self.state = 361
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(CSlangParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = CSlangParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr5)
        try:
            self.state = 365
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(CSlangParser.NOT)
                self.state = 363
                self.expr5()
                pass
            elif token in [CSlangParser.ZERO, CSlangParser.DIGIT, CSlangParser.FLOATLIT, CSlangParser.BOOLIT, CSlangParser.STRINGLIT, CSlangParser.LP, CSlangParser.LSQAB, CSlangParser.SUBTRAC, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.A_ID, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBTRAC(self):
            return self.getToken(CSlangParser.SUBTRAC, 0)

        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = CSlangParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr6)
        try:
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUBTRAC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.match(CSlangParser.SUBTRAC)
                self.state = 368
                self.expr6()
                pass
            elif token in [CSlangParser.ZERO, CSlangParser.DIGIT, CSlangParser.FLOATLIT, CSlangParser.BOOLIT, CSlangParser.STRINGLIT, CSlangParser.LP, CSlangParser.LSQAB, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.A_ID, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def LSQAB(self):
            return self.getToken(CSlangParser.LSQAB, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RSQAB(self):
            return self.getToken(CSlangParser.RSQAB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = CSlangParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr7)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.expr8(0)
                self.state = 373
                self.match(CSlangParser.LSQAB)
                self.state = 374
                self.expr()
                self.state = 375
                self.match(CSlangParser.RSQAB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.expr8(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(CSlangParser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def empty_exprlist(self):
            return self.getTypedRuleContext(CSlangParser.Empty_exprlistContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 395
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 393
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 383
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 384
                        self.match(CSlangParser.DOT)
                        self.state = 385
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 386
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 387
                        self.match(CSlangParser.DOT)
                        self.state = 388
                        self.match(CSlangParser.ID)
                        self.state = 389
                        self.match(CSlangParser.LP)
                        self.state = 390
                        self.empty_exprlist()
                        self.state = 391
                        self.match(CSlangParser.RP)
                        pass

             
                self.state = 397
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def A_ID(self):
            return self.getToken(CSlangParser.A_ID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def empty_exprlist(self):
            return self.getTypedRuleContext(CSlangParser.Empty_exprlistContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def expr10(self):
            return self.getTypedRuleContext(CSlangParser.Expr10Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = CSlangParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr9)
        try:
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.ID]:
                    self.state = 398
                    self.match(CSlangParser.ID)
                    self.state = 399
                    self.match(CSlangParser.DOT)
                    pass
                elif token in [CSlangParser.A_ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 403
                self.match(CSlangParser.A_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.ID]:
                    self.state = 404
                    self.match(CSlangParser.ID)
                    self.state = 405
                    self.match(CSlangParser.DOT)
                    pass
                elif token in [CSlangParser.A_ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 409
                self.match(CSlangParser.A_ID)
                self.state = 410
                self.match(CSlangParser.LP)
                self.state = 411
                self.empty_exprlist()
                self.state = 412
                self.match(CSlangParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def empty_exprlist(self):
            return self.getTypedRuleContext(CSlangParser.Empty_exprlistContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def expr11(self):
            return self.getTypedRuleContext(CSlangParser.Expr11Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = CSlangParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr10)
        try:
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.match(CSlangParser.NEW)
                self.state = 418
                self.match(CSlangParser.ID)
                self.state = 419
                self.match(CSlangParser.LP)
                self.state = 420
                self.empty_exprlist()
                self.state = 421
                self.match(CSlangParser.RP)
                pass
            elif token in [CSlangParser.ZERO, CSlangParser.DIGIT, CSlangParser.FLOATLIT, CSlangParser.BOOLIT, CSlangParser.STRINGLIT, CSlangParser.LP, CSlangParser.LSQAB, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.A_ID, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.expr11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subexpr(self):
            return self.getTypedRuleContext(CSlangParser.SubexprContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def A_ID(self):
            return self.getToken(CSlangParser.A_ID, 0)

        def lit(self):
            return self.getTypedRuleContext(CSlangParser.LitContext,0)


        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = CSlangParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr11)
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.subexpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.match(CSlangParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 428
                self.match(CSlangParser.A_ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 429
                self.lit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 430
                self.match(CSlangParser.SELF)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 431
                self.match(CSlangParser.NULL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_subexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = CSlangParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(CSlangParser.LP)
            self.state = 435
            self.expr()
            self.state = 436
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_type_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def array_type(self):
            return self.getTypedRuleContext(CSlangParser.Array_typeContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_data_type_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type_decl" ):
                return visitor.visitData_type_decl(self)
            else:
                return visitor.visitChildren(self)




    def data_type_decl(self):

        localctx = CSlangParser.Data_type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_data_type_decl)
        try:
            self.state = 444
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.match(CSlangParser.INT)
                pass
            elif token in [CSlangParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.match(CSlangParser.FLOAT)
                pass
            elif token in [CSlangParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 440
                self.match(CSlangParser.BOOL)
                pass
            elif token in [CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 441
                self.match(CSlangParser.STRING)
                pass
            elif token in [CSlangParser.LSQAB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 442
                self.array_type()
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 443
                self.match(CSlangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def array_type(self):
            return self.getTypedRuleContext(CSlangParser.Array_typeContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = CSlangParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_data_type)
        try:
            self.state = 453
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.match(CSlangParser.INT)
                pass
            elif token in [CSlangParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.match(CSlangParser.FLOAT)
                pass
            elif token in [CSlangParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 448
                self.match(CSlangParser.BOOL)
                pass
            elif token in [CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 449
                self.match(CSlangParser.STRING)
                pass
            elif token in [CSlangParser.LSQAB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 450
                self.array_type()
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 451
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 452
                self.match(CSlangParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQAB(self):
            return self.getToken(CSlangParser.LSQAB, 0)

        def DIGIT(self):
            return self.getToken(CSlangParser.DIGIT, 0)

        def RSQAB(self):
            return self.getToken(CSlangParser.RSQAB, 0)

        def array_data_type_decl(self):
            return self.getTypedRuleContext(CSlangParser.Array_data_type_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = CSlangParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(CSlangParser.LSQAB)
            self.state = 456
            self.match(CSlangParser.DIGIT)
            self.state = 457
            self.match(CSlangParser.RSQAB)
            self.state = 458
            self.array_data_type_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_data_type_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_array_data_type_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_data_type_decl" ):
                return visitor.visitArray_data_type_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_data_type_decl(self):

        localctx = CSlangParser.Array_data_type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_array_data_type_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.INT) | (1 << CSlangParser.FLOAT) | (1 << CSlangParser.BOOL) | (1 << CSlangParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Super_idlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def super_idlist(self):
            return self.getTypedRuleContext(CSlangParser.Super_idlistContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def A_ID(self):
            return self.getToken(CSlangParser.A_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_super_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuper_idlist" ):
                return visitor.visitSuper_idlist(self)
            else:
                return visitor.visitChildren(self)




    def super_idlist(self):

        localctx = CSlangParser.Super_idlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_super_idlist)
        self._la = 0 # Token type
        try:
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                _la = self._input.LA(1)
                if not(_la==CSlangParser.A_ID or _la==CSlangParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 463
                self.match(CSlangParser.COMMA)
                self.state = 464
                self.super_idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                _la = self._input.LA(1)
                if not(_la==CSlangParser.A_ID or _la==CSlangParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(CSlangParser.IdlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = CSlangParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_idlist)
        try:
            self.state = 472
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                self.match(CSlangParser.ID)
                self.state = 469
                self.match(CSlangParser.COMMA)
                self.state = 470
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 471
                self.match(CSlangParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Empty_exprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprprime(self):
            return self.getTypedRuleContext(CSlangParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_empty_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmpty_exprlist" ):
                return visitor.visitEmpty_exprlist(self)
            else:
                return visitor.visitChildren(self)




    def empty_exprlist(self):

        localctx = CSlangParser.Empty_exprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_empty_exprlist)
        try:
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ZERO, CSlangParser.DIGIT, CSlangParser.FLOATLIT, CSlangParser.BOOLIT, CSlangParser.STRINGLIT, CSlangParser.LP, CSlangParser.LSQAB, CSlangParser.SUBTRAC, CSlangParser.NOT, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.A_ID, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.exprprime()
                pass
            elif token in [CSlangParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def exprprime(self):
            return self.getTypedRuleContext(CSlangParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprprime" ):
                return visitor.visitExprprime(self)
            else:
                return visitor.visitChildren(self)




    def exprprime(self):

        localctx = CSlangParser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_exprprime)
        try:
            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.expr()
                self.state = 479
                self.match(CSlangParser.COMMA)
                self.state = 480
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arraylit(self):
            return self.getTypedRuleContext(CSlangParser.ArraylitContext,0)


        def intlit(self):
            return self.getTypedRuleContext(CSlangParser.IntlitContext,0)


        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def BOOLIT(self):
            return self.getToken(CSlangParser.BOOLIT, 0)

        def STRINGLIT(self):
            return self.getToken(CSlangParser.STRINGLIT, 0)

        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit" ):
                return visitor.visitLit(self)
            else:
                return visitor.visitChildren(self)




    def lit(self):

        localctx = CSlangParser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_lit)
        try:
            self.state = 492
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LSQAB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.arraylit()
                pass
            elif token in [CSlangParser.ZERO, CSlangParser.DIGIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 486
                self.intlit()
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 487
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.BOOLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 488
                self.match(CSlangParser.BOOLIT)
                pass
            elif token in [CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 489
                self.match(CSlangParser.STRINGLIT)
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 490
                self.match(CSlangParser.NULL)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 491
                self.match(CSlangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQAB(self):
            return self.getToken(CSlangParser.LSQAB, 0)

        def array_decl(self):
            return self.getTypedRuleContext(CSlangParser.Array_declContext,0)


        def RSQAB(self):
            return self.getToken(CSlangParser.RSQAB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = CSlangParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(CSlangParser.LSQAB)
            self.state = 495
            self.array_decl()
            self.state = 496
            self.match(CSlangParser.RSQAB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit(self):
            return self.getTypedRuleContext(CSlangParser.LitContext,0)


        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def array_decl(self):
            return self.getTypedRuleContext(CSlangParser.Array_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = CSlangParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_array_decl)
        try:
            self.state = 503
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.lit()
                self.state = 499
                self.match(CSlangParser.COMMA)
                self.state = 500
                self.array_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.lit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_intContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intlit(self):
            return self.getTypedRuleContext(CSlangParser.IntlitContext,0)


        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def array_int(self):
            return self.getTypedRuleContext(CSlangParser.Array_intContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_array_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_int" ):
                return visitor.visitArray_int(self)
            else:
                return visitor.visitChildren(self)




    def array_int(self):

        localctx = CSlangParser.Array_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_array_int)
        try:
            self.state = 510
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.intlit()
                self.state = 506
                self.match(CSlangParser.COMMA)
                self.state = 507
                self.array_int()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self.intlit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_floatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def array_float(self):
            return self.getTypedRuleContext(CSlangParser.Array_floatContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_array_float

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_float" ):
                return visitor.visitArray_float(self)
            else:
                return visitor.visitChildren(self)




    def array_float(self):

        localctx = CSlangParser.Array_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_array_float)
        try:
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 512
                self.match(CSlangParser.FLOATLIT)
                self.state = 513
                self.match(CSlangParser.COMMA)
                self.state = 514
                self.array_float()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.match(CSlangParser.FLOATLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_boolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLIT(self):
            return self.getToken(CSlangParser.BOOLIT, 0)

        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def array_bool(self):
            return self.getTypedRuleContext(CSlangParser.Array_boolContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_array_bool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_bool" ):
                return visitor.visitArray_bool(self)
            else:
                return visitor.visitChildren(self)




    def array_bool(self):

        localctx = CSlangParser.Array_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_array_bool)
        try:
            self.state = 522
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.match(CSlangParser.BOOLIT)
                self.state = 519
                self.match(CSlangParser.COMMA)
                self.state = 520
                self.array_bool()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 521
                self.match(CSlangParser.BOOLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLIT(self):
            return self.getToken(CSlangParser.STRINGLIT, 0)

        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def array_string(self):
            return self.getTypedRuleContext(CSlangParser.Array_stringContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_array_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_string" ):
                return visitor.visitArray_string(self)
            else:
                return visitor.visitChildren(self)




    def array_string(self):

        localctx = CSlangParser.Array_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_array_string)
        try:
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.match(CSlangParser.STRINGLIT)
                self.state = 525
                self.match(CSlangParser.COMMA)
                self.state = 526
                self.array_string()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.match(CSlangParser.STRINGLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZERO(self):
            return self.getToken(CSlangParser.ZERO, 0)

        def DIGIT(self):
            return self.getToken(CSlangParser.DIGIT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_intlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntlit" ):
                return visitor.visitIntlit(self)
            else:
                return visitor.visitChildren(self)




    def intlit(self):

        localctx = CSlangParser.IntlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_intlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ZERO or _la==CSlangParser.DIGIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[31] = self.expr2_sempred
        self._predicates[32] = self.expr3_sempred
        self._predicates[33] = self.expr4_sempred
        self._predicates[37] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




