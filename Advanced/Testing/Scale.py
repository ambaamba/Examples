#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     Scale.py
#

import traceback
from random import random
from pagebot import getAllContexts, getResourcesPath
from pagebot.toolbox.color import Color
from pagebot.constants import A4Rounded
from pagebot.contexts.base.babelstring import BabelString
from pagebot import getContext
from pagebot.toolbox.units import pt
from pagebot.document import Document
from pagebot.fonttoolbox.objects.font import findFont

H, W = A4Rounded
W = pt(W)
H = pt(H)

f = Color(0, 0, 0)
s = Color(1, 0, 0)

def testContexts():
    contexts = getAllContexts()

    for i, c in enumerate(contexts):
        if i in (0, 1):
            #print(c)
            try:
                testContext(c)
            except Exception as e:
                    print('Context errors', traceback.format_exc())

def testContext(context):
    doc = Document(w=W, h=H, context=context, autoPages=1)
    sq = 100
    x = 0
    y = 0 
    context.frameDuration(1)
    context.newDrawing()
    context.newPage(w=W, h=H)
    context.fill(f)
    context.stroke(s)
    context.translate(sq, sq)
    context.scale(0.1, center=(sq, 2*sq))
    p0 = (x, y)
    p1 = (x + 20*sq, y)
    context.line(p0, p1)
    context.oval(10*sq, sq, 10*sq, 5*sq)
    context.rect(x, y, pt(sq), pt(sq))
    font = findFont('Roboto-Black')
    glyphName = 'Q'
    glyph = font[glyphName]
    context.drawGlyphPath(glyph)
    path = '_export/Scale-%s.pdf' % context.name
    context.saveImage(path)

testContexts()
