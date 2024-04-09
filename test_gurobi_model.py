import gurobipy as gp
import numpy as np
from gurobipy import GRB

try:
    m = gp.Model("distributedCare")

    #Variables
    x = m.addVar(vtype=GRB.BINARY, name="x")
    y = m.addVar(vtype=GRB.BINARY, name="y")
    z = m.addVar(vtype=GRB.BINARY, name="z")

    #Objective
    m.setObjective(x+y+2*z, GRB.MAXIMIZE)

    #Constraints
    m.addConstr(x+2*y+3*z <= 4, "c0")
    m.addConstr(x+y<=1, "c1")

    #Optimize
    m.optimize()

    for v in m.getVars():
        print(f'{v.VarName:10s} {v.X}')

    print(f'Obj: {m.ObjVal}')
    print("Hilvi er kul")

except gp.GurobiError as e:
    print(f'Error code {e.errno}: {e}')

except AttributeError as e:
    print(f'Encountered an attribute error: {e}')


