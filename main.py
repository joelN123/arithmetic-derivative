"""
Main file for creating and rendering arithmetic derivative graph.
"""

from derivative_class_definitions import ArithmeticDerivativeGraph
from graphviz import Digraph
import random


if __name__ == "__main__":
    interval = (2,101)
    filename = "repeated_derivative"
    maths_graph = ArithmeticDerivativeGraph()

    print("Running repeated derivative on each seed value in interval {}, {}".format(*interval))

    for initial_value in range(*interval):
        error_message = maths_graph.repeat_derivative(initial_value)
        if error_message is not None:
            print(error_message)
            break

    print("Finished maths graph, now rendering graphviz")

    visual_graph = Digraph(name=filename, engine='twopi', graph_attr={'overlap': 'false'})
    visual_graph.edges(maths_graph.edge_set)
    for item in maths_graph.node_set:
        visual_graph.node(str(item[0]), str(item[1]))
    visual_graph.attr(root='1')
    file_location = visual_graph.render(filename=filename, cleanup=True, format="pdf")

    print("Finished rendering graphvis as : {}".format(file_location))

