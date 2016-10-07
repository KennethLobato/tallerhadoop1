#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json

# Para cada tweet que nos llegue de la entrada estándar...
for line in sys.stdin:
  tweet = json.loads(line)
  # Es un tweet normal?
  if 'text' in tweet:
    for word in tweet['text'].split(' '):
      word = word.encode('utf8')
      word = word.strip(',;.:-?¿!¡[]()"\'').lower()
      print word, "\t", tweet['user']['screen_name']
