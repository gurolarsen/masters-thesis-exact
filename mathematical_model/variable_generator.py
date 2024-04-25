import gurobipy as gp
from data_generation.data import *
#from data_generation import set_generator
#from data_generation import set_functions
from data_generation.set_generator import *
from data_generation.set_functions import *


def initialize_arc_flow_variables(model):
    #TODO: Må se om vi skal håndtere depoet på et vis (hvis i eller j er 0)
    count = 0
    x_ijed = {}
    for d in DAYS:
        for e in EMPLOYEES_ON_DAY[d]:
            for i in ACTIVITIES_DEPOT:
                for j in setOFJ_iActDepo_jActDepo[d][e][i]:
                    x_ijed[i, j, e, d] = model.addVar(vtype=gp.GRB.BINARY, name=f'x_{i}_{j}_{e}_{d}')
                    count += 1
    return x_ijed


def initialize_patient_home_variables(model):
    h_p = {}
    for p in PATIENTS:
        h_p[p] = model.addVar(vtype=gp.GRB.BINARY, name=f'h_{p}')
    return h_p

def initalize_activity_home_variables(model):
    delta_i = {}
    for i in ACTIVITIES:
        delta_i[i] = model.addVar(vtype=gp.GRB.BINARY, name=f'delta_{i}')
    return delta_i

def initialize_pattern_variables(model):
    y_bc = {}
    for b in TREATMENTS:
        for c in PATTERNS_FOR_TREATMENT[b]:
            y_bc[b, c] = model.addVar(vtype=gp.GRB.BINARY, name=f'y_{b}_{c}')
    return y_bc

def initialize_start_time_variables(model):
    s_i = {}
    for i in ACTIVITIES:
        s_i[i] = model.addVar(vtype=gp.GRB.INTEGER, ub=1440, name=f's_{i}')
    return s_i

def initialize_heaviness_variables(model):
    h_d = {}
    for d in DAYS:
        h_d[d] = model.addVar(vtype=gp.GRB.INTEGER, name=f'h_{d}')
    return h_d

def initalize_highest_heaviness_variables(model):
    h_over_dg = {}
    for d in DAYS:
        for g in PROFESSION_GROUPS:
            h_over_dg[d, g] = model.addVar(vtype=gp.GRB.INTEGER, name=f'h_over_{d}_{g}')
    return h_over_dg

def initalize_lowest_heaviness_variables(model):
    h_under_dg = {}
    for d in DAYS:
        for g in PROFESSION_GROUPS:
            h_under_dg[d, g] = model.addVar(vtype=gp.GRB.INTEGER, name=f'h_under_{d}_{g}')
    return h_under_dg

def initalize_highest_avg_heaviness_variables(model):
    h_avg_over_g = {}
    for g in PROFESSION_GROUPS:
        h_avg_over_g[g] = model.addVar(vtype=gp.GRB.INTEGER, name=f'h_avg_over_{g}')
    return h_avg_over_g

def initalize_lowest_avg_heaviness_variables(model):
    h_avg_under_g = {}
    for g in PROFESSION_GROUPS:
        h_avg_under_g[g] = model.addVar(vtype=gp.GRB.INTEGER, name=f'h_avg_under_{g}')
    return h_avg_under_g


def initialize_preferred_speciality_variables(model):
    z_i = {}
    for i in ACTIVITIES_WITH_PREFERRED_SPECIALITY:
        z_i[i] = model.addVar(vtype=gp.GRB.BINARY, ub=1440, name=f's_{i}')
    return z_i
#TESTING
#test_model = gp.Model("testModel")
#x = initialize_arc_flow_variables(test_model)
#print("Number of arcs generated: ", len(x.keys()))


#y = initialize_pattern_variables(test_model)
#print("y",y)
#h = initialize_patient_home_variables(test_model)
#print(h)
#delta = initalize_activity_home_variables(test_model)
#print("delta",delta)
#s = initialize_start_time_variables(test_model)
#print(s)
#heaviness = initialize_heaviness_variables(test_model)
#print(heaviness)
#heaviness_over = initalize_highest_heaviness_variables(test_model)
#print(heaviness_over)