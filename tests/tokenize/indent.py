#!/usr/bin/env python

from codetalker import pgm
from codetalker.pgm.tokens import STRING, ID, NUMBER, WHITE, NEWLINE, INDENT, DEDENT
from codetalker.pgm.special import star, plus, _or
from codetalker.pgm.grammar import ParseError

def start(rule):
    rule | 'what'

def SMALL(token):
    token | 'hello'

grammar = pgm.Grammar(start=start, tokens=[SMALL, WHITE, NEWLINE], indent=True)

def test_indent():
    tokens = grammar.get_tokens('hello\n  hello')
    assert len(tokens) == 5
    assert tokens[2][0] == INDENT

def test_dedent():
    tokens = grammar.get_tokens('hello\n hello\nhello')
    assert len(tokens) == 8
    assert tokens[6][0] == DEDENT


# vim: et sw=4 sts=4
