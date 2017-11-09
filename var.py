# /usr/bin/env python
#  -*- coding: utf-8 -*-
import pickle
city = {}
rage = ['198012.tsv','198112.tsv','198212.tsv','198312.tsv','198412.tsv','198512.tsv','198612.tsv','198712.tsv','198812.tsv','198912.tsv',
        '199012.tsv','199112.tsv','199212.tsv','199312.tsv','199412.tsv','199512.tsv','199612.tsv','199712.tsv','199812.tsv','199912.tsv',
        '200012.tsv','200112.tsv','200212.tsv','200312.tsv','200412.tsv','200512.tsv','200612.tsv','200712.tsv','200812.tsv','200912.tsv',
        '201012.tsv','201112.tsv','201312.tsv','201412.tsv','201512.tsv','201612.tsv']
for i in rage:
  with open(i) as f:
      cfile = f.read()
      clst = cfile.split("\n")
      for r in clst:
        if not r == '':
          l = r.split()
          city[l[2]] = l[3]
pickle_file = open('cityid_data.pkl', 'wb')
pickle.dump(city, pickle_file)
pickle_file.close()