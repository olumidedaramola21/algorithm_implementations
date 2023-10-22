import graphviz

dot = graphviz.Digraph()
dot.node("program", shape="box3d", width="1", height="0.7")
dot.edge("inputs", "program")
dot.edge("program", "results")

dot.view()
