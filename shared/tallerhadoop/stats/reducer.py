#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# Variables para comprobar la clave que estamos tratando y su cuenta
lastUser = None
lastLengths = []

# Para cada línea que nos llegue de la entrada estándar...
for line in sys.stdin:
  # Comprobamos que es una user-tabulador-valor
  data_mapped = line.strip().split("\t")
  if len(data_mapped) != 2:
    # No tiene el formato esperado, pasamos de esta línea
    continue
  user, length = data_mapped
  # Estamos con un nuevo user?
  if lastUser and lastUser != user:
    # Sí, imprimimos estadísticas del anterior
    print lastUser, "\t", sum(lastLengths)/len(lastLengths), "\t", min(lastLengths), "\t", max(lastLengths)
    lastLengths = []
  lastUser = user
  lastLengths.append(int(length))

# El último user se queda sin imprimir
if lastUser:
  print lastUser, "\t", sum(lastLengths)/len(lastLengths), "\t", min(lastLengths), "\t", max(lastLengths)
