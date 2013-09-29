#!/usr/bin/env python
#P2b.py


from mrjob.job import MRJob
import math

class MRTrapIntegration(MRJob):
	def __init__(self, *args, **kwargs):
		super(MRTrapIntegration, self).__init__(*args, **kwargs)
		self.localsum = 0
	def mapper(self, _, line):
		if False:
			yield
		
		for x in line.split():
			x = float(x)
			self.localsum += (math.sqrt(1-(x/100001.0)**2) + math.sqrt(1-((x+1)/100001.0)**2))*(1/100001.0)/2
	
	def mapper_final(self):
		yield 1, self.localsum

	def reducer(self, _, values):
		yield 1, sum(values)

if __name__ == '__main__':
	MRTrapIntegration.run()
