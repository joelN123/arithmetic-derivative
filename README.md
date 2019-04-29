# arithmetic-derivative
create a graph representing the arithmetic derivative from a set of seed values.

To create the graph, run ``` python3 main.py ```

For the network visualization, I used [graphviz](https://www.graphviz.org/) and the python module also called [graphviz](https://www.graphviz.org/).

For the prime decomposition, I used [factorint](https://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.factor_.factorint) from sympy.ntheory. It looks like a powerful function, which can switch between several algorithms depending on the input value.

## More detail

The [arithmetic derivative](https://en.wikipedia.org/wiki/Arithmetic_derivative) is a map from the positive integers to itself. It has some similar properties to the usual kind of derivative.

Since the input and output of the arithmetic derivative are both positive integers, it is possible to do repeated arithmetic differentiation on some initial integer. For example, let's say we start with 77. The derivative of 77 is 18. And the derivative of 18 is 21. And the derivative of 21 is 10. And so on. So, three iterations of repeated differentiation on an initial value of 77 would look like 77 -> 18 -> 21 -> 10.

In this code, repeated arithmetic differentiation is performed on a set of initial integer values (default is up to 100).

In the created graph, nodes are integers and arrows between nodes denote arithmetic differentiation. For example, there is an arrow from 26 to 15 because the arithmetic derivative of 26 is 15.

## Example graph

![nice example repeated derivative](https://github.com/joelN123/arithmetic-derivative/blob/master/nice_example_repeated_derivative.png)

## Possible outcomes of repeated differentiation

Looking at the example graph, there's a lot going on. But, essentially there are three cases for where the derivative ends up

#### Firstly :

At 1. The arithmetic derivative of 1 is 0, and arithmetic derivative of 0 is 0. So, once 1 is reached, the journey ends. For this reason, I've written 'root' for node 1.

p.s. prime numbers always have derivative equal to 1 - convince yourself.

#### Secondly :

For some values, their derivative is equal to themselves (for example 4). In these cases, no new nodes are reached, and the code can stop computing arithmetic derivative.

p.s. the values p^p (for p prime) always lead to this kind of loop - convince yourself.

#### Thirdly :

Divergence. In some cases, values can get very high before coming back down to 1. However, there are some nodes (labelled 'diverge'), that will continue to get larger and larger (monotonically) and never get smaller. For these nodes, the code will stop taking derivatives and label as 'diverge'.

p.s. an integer that contains at least one prime power p^n with n>p will always diverge - convince yourself.

#### Other cases ?

There may be other cases... For example, a loop of length longer than one. Or a non-looping path that does not hit 1, and does not hit any of the divergent numbers mentioned in case three above. However, with using only a small number of initial integer values, I did not find any of these other possible cases.
