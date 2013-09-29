#!/usr/bin/env python
#P4-ssbfs.py

from mrjob.job import MRJob
from collections import defaultdict
import json
from mrjob.job import JSONProtocol


class MRBFS(MRJob):
	INPUT_PROTOCOL = JSONProtocol
	"""
	def __init__(self, *args, **kwargs):
		super(MRBFS, self).__init__(*args, **kwargs)
		self.count1 = 0
		self.count2 = 0
		self.count3 = 0 
	
	"""
	def mapper(self, key, line):
		
		node_id = key 
		yield node_id, line
		
		orig_dist = line[0]
		
		if type(orig_dist) == int: # and line[1] != None:
			new_dist = 1 + orig_dist
			neighbors = line[1]
			for n in neighbors:
				yield n, new_dist
			
	def reducer(self, key, values):
	
		d1 = list(values)
		#print d1
		
		data = [d for d in d1 if type(d) == list][0]
		new_distance = [n for n in d1 if type(n) != list]
		
		#print data
		#print new_distance
		if data[0] == 'None' and new_distance:
			distance = min(new_distance)
		else:
			distance = data[0]
		
	
		neighbors = data[1]
		
			
		
		
		
		"""
		if n1:
			neighbors = n1[0]
		else:
			neighbors = str(None)
		
		d = [k for k in d1 if type(k) == int]
		d.append(data[0])
		
		df = [z for z in d if type(z) == int]
		if df:
			distance = min(df)
		else:
			distance = None
		"""
		"""
		#increment vertex counters
		if distance == 3:
			self.count3 += 1
		if distance == 2:
			self.count2 += 1
		if distance == 1:
			self.count1 +=1
			
		print 'count1: ' + str(self.count1)
		print 'count2: ' + str(self.count2)
		print 'count3: ' + str(self.count3)
		"""		

		yield key, (distance, neighbors)

	def steps(self):
   		return [self.mr(mapper= self.mapper, reducer=self.reducer)]*4

if __name__ == '__main__':
	MRBFS.run()
