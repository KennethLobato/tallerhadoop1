#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
import re

regex = 'RT*'
pattern = re.compile(regex)

# Para cada tweet que nos llegue de la entrada estándar...
for line in sys.stdin:
  tweet = json.loads(line)
  # Es un tweet normal?
  if 'text' in tweet:
    # Comple el patron?
    if pattern.match(tweet['text']):
      print line
