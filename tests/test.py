from tabulate import tabulate
table = [['a1', 'b1'], ['a2', 'b2']]
colspan = {(0, 0): 2}
rowspan = {(0, 1): 2}

print(tabulate(table, colspan, rowspan))