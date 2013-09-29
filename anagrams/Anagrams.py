#!/usr/bin/env python
#P3.py

from mrjob.job import MRJob
from collections import defaultdict

class MRAnagrams(MRJob):
	def mapper(self, _, line):
		for word in line.split(' '):
			sorted_word = sorted(word)
			yield sorted_word, word
	
	def reducer(self, sls, values):	
		l = list(values)
		pair = [l, len(l)]
		yield sls, pair
		 
if __name__ == '__main__':
	MRAnagrams.run()
