# arithmetic-derivative
create a graph representing the arithmetic derivative from a set of seed values.

To create the graph, run ``` python3 main.py ```

For the network visualization, I used [graphviz](https://www.graphviz.org/) and the python module also called [graphviz](https://www.graphviz.org/).

For the prime decomposition, I used [factorint](https://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.factor_.factorint) from sympy.ntheory. It looks like a powerful function, which can switch between several algorithms depending on the input value.

# More detail

The [arithmetic derivative](https://en.wikipedia.org/wiki/Arithmetic_derivative) is a map from the positive integers to itself. It has some similar properties to the usual kind of derivative.

Since the input and output of the arithmetic derivative are both positive integers, it is possible to do repeated arithmetic differentiation on some initial integer.

In this code, repeated arithmetic differentiation is performed on a set of initial integer values (default is up to 100).

In the created graph, nodes are integers and arrows between nodes denote arithmetic differentiation. For example, there is an arrow from 26 to 15 because the arithmetic derivative of 26 is 15.

# Example graph


# Possible outcomes of repeated differentiation


