#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition
SUBSTITUTE = 'Spanish'
INQUISITION_BEGINNING = inquisition.SPANISH.index(SUBSTITUTE)
INQUISITION_ENDDING = INQUISITION_BEGINNING + len(SUBSTITUTE)
FIRST = inquisition.SPANISH[0:INQUISITION_BEGINNING]
SECOND = inquisition.SPANISH[INQUISITION_ENDDING:]
FLEMISH = FIRST + "Flemish" + SECOND
print FLEMISH
