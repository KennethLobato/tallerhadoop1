#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json

# Inicializamos diccionario de valencias
sent_file = open('/root/tallerhadoop/sentiment/AFINN-111.txt')
scores = {}
for line in sent_file:
  term, score  = line.split("\t")
  scores[term] = int(score)
print "Llega aquí"

# Para cada tweet que nos llegue de la entrada estándar...
for line in sys.stdin:
  tweet = json.loads(line)
  # Es un tweet normal?
  if 'text' in tweet:
    user = tweet['user']['screen_name'].encode('utf8')
    for word in tweet['text'].split(' '):
      word = word.encode('utf8')
      word = word.strip(',;.:-?¿!¡[]()"\'').lower()
      if word in scores:
        print "{0}\t{1}".format(user, scores[word])
