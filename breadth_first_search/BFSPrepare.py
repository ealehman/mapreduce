#!/usr/bin/env python
#P4-prepare.py


from mrjob.job import MRJob
from collections import defaultdict
import json
from mrjob.protocol import JSONProtocol, RawProtocol


class MRPrepare(MRJob):
	INPUT_PROTOCOL = RawProtocol
	OUTPUT_PROTOCOL = JSONProtocol
	
	#parse line
	def transform_input(self,heroes,comic):
		yield comic, heroes
		
	#for each hero, output list of other heroes in same comic
	def transform_output(self,_,values):

		herolist = list(values)
		for h in herolist:
			rest = [n for n in herolist if n!= h]
			yield h, rest
	
	#add distance values
	def set_distance(self,key,values):

		h1 = list(values)
		heroes = h1[0]

		yield key, ('None', heroes)
	
	def mapper(self,key,line):
		yield key, line
	
	def reducer(self,key,values):
		#make connections unique
		connections = set(values)
		
		#get rid of isolated vertices if connected to other sets of connections
		for c in connections:
			if len(connections) > 1 and c == 'None':
				connections.remove(c)
			
		yield key, connections
		
	def steps(self):
   		return [self.mr(mapper= self.transform_input, reducer=self.transform_output),
   		self.mr(mapper=self.mapper, reducer = self.set_distance)]
   		       
if __name__ == '__main__':
	MRPrepare.run()
