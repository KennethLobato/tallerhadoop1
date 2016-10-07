#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# Variables para comprobar la clave que estamos tratando y su cuenta
lastWord = None
lastUsers = []

# Para cada línea que nos llegue de la entrada estándar...
for line in sys.stdin:
  # Comprobamos que es una palabra-tabulador-user
  data_mapped = line.strip().split("\t")
  if len(data_mapped) != 2:
    # No tiene el formato esperado, pasamos de esta línea
    continue
  word, user = data_mapped
  # Estamos con una nueva palabra?
  if lastWord and lastWord != word:
    # Sí, imprimimos el total de la anterior
    lastUsers = list(set(lastUsers))
    print lastWord, "\t", lastUsers
    lastUsers = []
  lastWord = word
  lastUsers.append(user)

# La última palabra queda sin imprimir
if lastWord:
  print lastWord, "\t", lastUsers

