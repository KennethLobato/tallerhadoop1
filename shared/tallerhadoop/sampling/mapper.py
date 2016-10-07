#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json

count = 0

# Para cada tweet que nos llegue de la entrada estándar...
for line in sys.stdin:
  tweet = json.loads(line)
  # Es un tweet normal?
  if 'text' in tweet:
    count += 1
  # Es el décimo tweet?
  if count > 9:
    print line
    count = 0
