#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Write Upside-Down
Translate English into Upside-Down Unicode
"""

Xlate = {

	'a':'ɐ', 'b':'q', 'c':'ɔ', 'd':'p', 'e':'ə',
	'f':'ɟ', 'g':'ɓ', 'h':'ɥ', 'i':'!', 'j':'ɾ',
	'k':'ʞ', 'l':'l', 'm':'ɯ', 'n':'u', 'o':'o',
	'p':'p', 'q':'q', 'r':'ɹ', 's':'s', 't':'ʇ',
	'u':'n', 'v':'ʌ', 'w':'ʍ', 'x':'x', 'y':'ʎ',
	'z':'z',

	'A':'∀', 'B':'B', 'C':'Ↄ', 'D':'◖', 'E':'Ǝ',
	'F':'Ⅎ', 'G':'⅁', 'H':'H', 'I':'I', 'J':'ſ',
	'K':'K', 'L':'⅂', 'M':'W', 'N':'ᴎ', 'O':'O',
	'P':'Ԁ', 'Q':'Ό', 'R':'ᴚ', 'S':'S', 'T':'⊥',
	'U':'∩', 'V':'ᴧ', 'W':'M', 'X':'X', 'Y':'⅄',
	'Z':'Z',

	'0':'0', '1':'1', '2':'0', '3':'Ɛ', '4':'ᔭ',
	'5':'5', '6':'9', '7':'Ɫ', '8':'8', '9':'0',

	'_':'¯', "'":',', ',':"'", '\\':'/', '/':'\\',
	'!':'¡', '?':'¿',
}

import sys

line = sys.stdin.readline()
while line:
	line = line.strip("\r\n")
	xline = ''.join([Xlate[c] if c in Xlate else c for c in line[::-1]])
	print xline
	line = sys.stdin.readline()

