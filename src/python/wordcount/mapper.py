#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# Para cada línea que nos llegue de la entrada estándar...
for line in sys.stdin:
  # Para cada elemento de una línea separado por espacios = palabra
  for word in line.split(' '):
    word = word.strip(',;.:-?¿!¡[]()"\'').lower()
    # Imprimimos la palabra, un tabulador y un 1
    print "{0}\t1".format(word)
