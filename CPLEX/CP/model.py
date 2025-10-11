from docplex.cp.model import CpoModel, context
import argparse
import os
import resource
context.solver.local.execfile = "/home/AP/cplex/cpoptimizer/bin/x86-64_linux/cpoptimizer"

cabw_bounds = {
    "A-pores_1.mtx.rnd": (3, 8),
    "B-ibm32.mtx.rnd": (5, 9),
    "C-bcspwr01.mtx.rnd": (8, 17),
    "D-bcsstk01.mtx.rnd": (4, 9),
    "E-bcspwr02.mtx.rnd": (11, 22),
    "F-curtis54.mtx.rnd": (6, 13),
    "G-will57.mtx.rnd": (6, 14),
    "H-impcol_b.mtx.rnd": (4, 8),
    "I-ash85.mtx.rnd": (10, 27),
    "J-nos4.mtx.rnd": (16, 40),
    "K-dwt__234.mtx.rnd": (23, 58),
    "L-bcspwr03.mtx.rnd": (20, 39),
    "M-bcsstk06.mtx.rnd": (14, 72),
    "N-bcsstk07.mtx.rnd": (14, 72),
    "O-impcol_d.mtx.rnd": (46, 173),
    "P-can__445.mtx.rnd": (39, 120),
    "Q-494_bus.mtx.rnd": (110, 246),
    "R-dwt__503.mtx.rnd": (23, 71),
    "S-sherman4.mtx.rnd": (128, 272),
    "T-dwt__592.mtx.rnd": (52, 150),
    "U-662_bus.mtx.rnd": (110, 220),
    "V-nos6.mtx.rnd": (163, 337),
    "W-685_bus.mtx.rnd": (68, 136),
    "X-can__715.mtx.rnd": (56, 142)
}
# Khởi tạo parser
parser = argparse.ArgumentParser(
    description='Giải bài toán cyclicantibandwidth trên đồ thị.'
)

# Thêm tham số dòng lệnh
parser.add_argument(
    'input_file',
    type=str,
    help='Đường dẫn đến tệp đầu vào chứa dữ liệu đồ thị (.mtx.rnd).'
)

# Lấy các tham số từ dòng lệnh
args = parser.parse_args()

# Lấy tên file từ đường dẫn
file_name = os.path.basename(args.input_file)
with open(args.input_file, 'r') as file:
    lines = file.readlines()

size_info = lines[1].strip().split()
num_vertices = int(size_info[0])
LB, UB = cabw_bounds[file_name] 
edges = set()
for line in lines[2:]:
    row, col = map(int, line.strip().split())
    edges.add((row, col))
#edges = [...]     

# ---------------------------
# Create model
# ---------------------------   
mdl = CpoModel()

# Decision variables
labels = mdl.integer_var_list(num_vertices, min=1, max=num_vertices, name="labels")

# Variable b (objective)
b = mdl.integer_var(min=LB, max=UB, name="b")

# ---------------------------
# degree of vertices
# ---------------------------
vertex_degree = [0] * num_vertices
for e in edges:
    vertex_degree[e[0]-1] += 1
    vertex_degree[e[1]-1] += 1

# Vertex with maximum degree
max_degree_vertex = vertex_degree.index(max(vertex_degree))

# Constraint cyclic antibandwidth
for e in edges:
    i = e[0]-1
    j = e[1]-1
    temp = mdl.abs(labels[i] - labels[j])
    mdl.add_constraint(b <= mdl.min(temp, num_vertices - temp))

# Constraint: labels allDifferent
mdl.add_constraint(mdl.all_diff(labels))

# Symmetry breaking
mdl.add_constraint(labels[max_degree_vertex] <= num_vertices // 2)

# ---------------------------
# Objective
# ---------------------------
mdl.maximize(b)

# ---------------------------
# Solve model
# ---------------------------
solution = mdl.solve(TimeLimit=1800, LogVerbosity='Quiet', Workers=8, MemoryLimit=30000)


if solution:
    print("Value Cyclic-Antibandwidth =", solution.get_objective_value())
    print("Labels:", [solution.get_value(lbl) for lbl in labels])
    print("Solve time (s):", solution.get_solve_time())
    usage = resource.getrusage(resource.RUSAGE_SELF)
    print("Memory usage (MB):", usage.ru_maxrss / 1024)  
else:
    print("No solution found")

