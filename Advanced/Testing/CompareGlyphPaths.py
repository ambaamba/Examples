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
#     CompareContexts.py
#

import traceback
from random import random
from pagebot import getAllContexts, getResourcesPath
from pagebot.toolbox.color import Color
from pagebot.constants import A4Rounded
from pagebot.strings.babelstring import BabelString
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
    print('All contexts: %s' % contexts)

    for i, c in enumerate(contexts):
        if i in (0, 1):
            #print(c)
            try:
                testContext(c)
            except Exception as e:
                    print('Context errors', traceback.format_exc())

def getRandom():
    x = (W - 100) * random()
    y = (H - 100) * random()
    return x, y

def testContext(context):

    doc = Document(w=W, h=H, context=context, autoPages=1)

    sq = 100
    x = 0
    y =  4*sq
    context.frameDuration(1)
    context.newDrawing()
    context.newPage(w=W, h=H)
    context.fill(f)

    font = findFont('Roboto-Black')
    glyphName = 'Q'
    glyph = font[glyphName]
    #context.translate(2*sq, sq)
    #context.scale(0.1)
    context.drawGlyphPath(glyph)


    path = '_export/GlyphPath-%s.pdf' % context.name
    context.saveImage(path)

testContexts()