#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# Variables para comprobar la clave que estamos tratando y su cuenta
lastWord = None
lastCount = 0

# Para cada línea que nos llegue de la entrada estándar...
for line in sys.stdin:
  # Comprobamos que es una palabra-tabulador-valor
  data_mapped = line.strip().split("\t")
  if len(data_mapped) != 2:
    # No tiene el formato esperado, pasamos de esta línea
    continue
  word, count = data_mapped
  # Estamos con una nueva palabra?
  if lastWord and lastWord != word:
    # Sí, imprimimos el total de la anterior
    print lastWord, "\t", lastCount
    lastCount = 0
  lastWord = word
  lastCount += int(count)

# La última palabra queda sin imprimir
if lastWord:
  print lastWord, "\t", lastCount

