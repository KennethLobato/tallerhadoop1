#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json

# Para cada tweet que nos llegue de la entrada estándar...
for line in sys.stdin:
  tweet = json.loads(line)
  # Es un tweet normal?
  if 'text' in tweet:
    length = len(tweet['text'])
    user = tweet['user']['screen_name'].encode('utf8')
    print "{0}\t{1}".format(user, length)

