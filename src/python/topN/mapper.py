#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json

n = 5
top = []
lengths = [0 for x in range(n)]

# Para cada tweet que nos llegue de la entrada estándar...
for line in sys.stdin:
  tweet = json.loads(line)
  # Es un tweet normal?
  if 'text' in tweet:
    length = len(tweet['text'])
    # Gana a alguno de los n primeros en longitud?
    for index in range(len(lengths)):
      if length > lengths[index]:
        # Sí, lo metemos en las listas y eliminamos por abajo
        lengths.insert(index, length)
        top.insert(index, tweet)
        del lengths[n:]
        del top[n:]
        break

# Al acabar, damos nuestro top-N
for tweet in top:
  print json.dumps(tweet, ensure_ascii=False).encode('utf8')
