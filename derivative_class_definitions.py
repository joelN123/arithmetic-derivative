"""
Class and associated methods for creating arithmetic derivative graph.
"""

from sympy.ntheory import factorint


class ArithmeticDerivativeGraph():
	""" This class defines a graph representing the arithmetic derivative."""
	def __init__(self,
				 node_set = {(1, "1 = root")},
				 edge_set = set(),
				 iterations = 100,
				 max_value = 10**18
				 ):
					self.node_set = node_set
					self.edge_set = edge_set
					# Both iterations and max value are safety values that
					# should be large enough that they are not reached.
					self.iterations = iterations
					self.max_value = max_value


	def _arithmetic_derivative(self, x):
		"""Return arithmetic derivative by using prime decomposition.
		Input should be positive integer or zero.
		Output is positive integer or zero, so this function can be used repeatedly.
		"""
		if x == 0: return 0 #  Zero maps to zero.
		canonical_representation = factorint(x)
		#  Canon_rep of 1 is empty list. 1 should map to zero.
		if not canonical_representation: return 0
		update_ratio = sum(power/prime for prime, power in canonical_representation.items())
		output = x*update_ratio
		# This should be integer already, only using round for typecasting.
		return round(output)


	def repeat_derivative(self, x):
		"""Add new edges to the graph of derivatives, starting from the seed.
		Input x is the seed number, should be integer > 1.
		Output is triggered by safety parameters. In normal use, return None.
		"""
		if x < 2: return "invalid seed number"
		time = 0
		x_new = self._arithmetic_derivative(x)
		v = (str(x), str(x_new))

		while v not in self.edge_set:
			if any([power>prime for prime, power in factorint(x).items()]):
				self.node_set.add((str(x), str(x)+" = diverge"))
				return None
			else:
				self.edge_set.add(v)

			if v[1] == "1": return None
			if x_new > self.max_value: return "exceeded max value?!"
			time += 1
			if time >= self.iterations: return "still going at end of iterations"

			x = x_new
			x_new = self._arithmetic_derivative(x_new)
			v = (str(x), str(x_new))

		return None
