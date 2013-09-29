#!/usr/bin/env python
#P2a_test.py

from mrjob.job import MRJob
import math

class MrTrapIntegration(MRJob):
	def mapper(self, _, line):
		for x in line.split():
			x = float(x)
			yield 1, (math.sqrt(1-(x/100001.0)**2) + math.sqrt(1-((x+1)/100001.0)**2))*(1/100001.0)/2

	def reducer(self, _, values):
		yield 1, sum(values)

if __name__ == '__main__':
	MrTrapIntegration.run()
