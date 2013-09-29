#!/usr/bin/env python
#P5.py

from mrjob.job import MRJob
import random
import numpy as np

class MRMonteCarlo(MRJob):
	def __init__(self, *args, **kwargs):
		super(MRMonteCarlo, self).__init__(*args, **kwargs)
		self.num_sum = 0
		self.denom_sum = 0
	def mapper(self, key, line):
		if False:
			yield
		
		seed = int(line.split()[0])
		random = np.random.RandomState(seed)
		
		x = random.uniform(0,1,1000)
		y = random.uniform(0,1,1000)
		
		yofx = np.sqrt(1.0-x**2)
		
		self.num_sum += sum(y <= yofx)
		self.denom_sum += 1000
	
	def mapper_final(self):
		yield 'numerator', self.num_sum
		yield 'denominator', self.denom_sum
		
	def reducer(self, key, values):
		yield key, list(values)
		
if __name__ == '__main__':
	MRMonteCarlo.run()