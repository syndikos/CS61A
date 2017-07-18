def multiplication_table(rows, cols):
    """A ROWS x COLS multiplication table where row x, column y
    (element [x][y]) contains xy. Example:
    >>> multiplication table(4, 3)
    [[0, 0, 0], [0, 1, 2], [0, 2, 4], [0, 3, 6]]
    """
    return [ [ row * col for col in range(cols) ] 
            for row in range(rows) ]

def triangle(rows):
    """A ROWSxROWS lower-triangular array
    containing "*"s.
    >>> triangle(4)
    [[’*’], [’*’, ’*’], [’*’, ’*’, ’*’], [’*’, ’*’, ’*’, ’*’]]
    """
    return [ [ "*" for c in range(k+1) ] for k in range(rows) ]

def numbered_triangle(rows):
    """A ROWSxROWS lower-triangular array whose elements
    are integers, starting at 0 going left-to-right,
    up-to-down.
    >>> numbered triangle(3)
    [ [ 0 ], [ 1, 2 ], [ 3, 4, 5 ] ]"""
    # def first_row()
    pass

# def count_leaves(tree):
#     """The number of leaf nodes in TREE."""
def make_tree(label, kids = []):
    """A (sub)tree with given LABEL at its root, whose children
    are KIDS."""
    return (label, kids)

def label(tree):
    """The label on TREE."""
    return tree[0]

def branches(tree):
    """The children of TREE (each a tree)."""
    return tree[1]

def is_leaf(tree):
    """True if TREE is a leaf node."""
    return len(branches(tree)) == 0

def count_leaves(tree):
    """The number of leaf nodes in TREE."""
    if is_leaf(tree):
        return 1
    else:
        return sum(map(count_leaves, branches(tree)))

def value(expr):
    """Return the value of the expression represented by the
    expression tree expr
    >>> value(make tree("*", [ make tree("+", [make tree(3), make tree(4)]),
    ... make tree("-", [make tree(9), make tree(6)]))
    36
    """
    from operator import add, sub, mul, truediv
    operator_pair = {'+':add, '-':sub, '*':mul, '/':truediv}
    if is_leaf(expr):
        return label(expr)
    # elif label(expr) == '+':
    #     return value(branches(expr)[0]) + value(branches(expr)[1])
    # elif label
    else:
        for operator in ('+', '-', '*', '/'):
            if label(expr) == operator:
                return operator_pair[operator](value(branches(expr)[0]),\
             value(branches(expr)[1]))

