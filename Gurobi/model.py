from gurobipy import Model, GRB
import time
import threading
import argparse
#import psutil
#from memory_profiler import memory_usage
import math
#from func_timeout import func_timeout, FunctionTimedOut

DATA_DIR = "./graph/harwell_boeing"

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



def calculate_label_differences(labels, edges):
    label_differences = []
    n = len(labels)
    for edge in edges:
        v1, v2 = edge
        label_difference = abs(labels[v1 - 1] - labels[v2 - 1])
        cyclic_difference = min(label_difference, n - label_difference)
        label_differences.append(cyclic_difference)
    return label_differences

def build_model(vertices, edges, k, time_limit=1800):
    
    n = len(vertices)
    model = Model("Antibandwidth")
    model.setParam('TimeLimit', time_limit)

    x = model.addVars(vertices, vertices, vtype=GRB.BINARY, name="x")

    # Ràng buộc 1: Mỗi đỉnh được gán đúng một nhãn
    for i in vertices:
        model.addConstr(sum(x[i, l] for l in vertices) == 1, name=f"VERTICES_{i}")

    # Ràng buộc 2: Mỗi nhãn được gán đúng một đỉnh
    for l in vertices:
        model.addConstr(sum(x[i, l] for i in vertices) == 1, name=f"LABELS_{l}")

    # Ràng buộc OBJ-k: Không được gán nhãn quá gần nhau cho các đỉnh kề nhau
    for (i, j) in edges:
        for l2 in range(1, n - k + 1):
            model.addConstr(
                sum(x[i, l] for l in range(l2, l2 + k + 1)) + 
                sum(x[j, l] for l in range(l2, l2 + k + 1)) <= 1, 
                name=f"NO_CLOSE_LABELS_{i}_{j}_{l2}"
            )
        # Nối 2 đầu chu trình   
        for l2 in range(n - k + 1, n + 1):            
            model.addConstr(
            sum(x[i, ((l - 1) % n) + 1] for l in range(l2, l2 + k + 1)) +
            sum(x[j, ((l - 1) % n) + 1] for l in range(l2, l2 + k + 1)) <= 1,
            name=f"NO_CLOSE_LABELS_CYCLIC_{i}_{j}_{l2}"
        )

    # Ràng buộc phá vỡ đối xứng
    degree = {i: 0 for i in vertices}
    for (i, j) in edges:
        degree[i] += 1
        degree[j] += 1
    max_degree_vertex = max(degree, key=degree.get)
    for l in range((n // 2) + 1, n + 1):
        model.addConstr(x[max_degree_vertex, l] == 0, name=f"SYMMETRY_BREAK_{max_degree_vertex}_{l}")

    return model

def solve_cyclicantibandwidth(vertices, edges, UB, LB):
    k = LB + 1
    labels = [None] * len(vertices)
    while True:
        if k >= UB:
            break
        
        model = build_model(vertices, edges, k)
        model.setParam('OutputFlag', 0)
        model.optimize()

        if model.Status != GRB.OPTIMAL:
            print(f"(w = {k + 1}) Not found solution with CAB = {k + 1}.")
            print(f"Final result: CAB = {k}, Labels = {labels}")
            break

        var_values = model.getAttr('X', model.getVars())
        for i in range(len(vertices)):
            for l in range(len(vertices)):
                if var_values[i * len(vertices) + l] > 0.5:
                    labels[i] = l + 1
                    break

        print(f"(w = {k + 1}) Value Cyclicantibandwidth: {k + 1}")
        print("Lables:", labels)

        label_differences = calculate_label_differences(labels, edges)
        if any(element < k + 1 for element in label_differences):
            print(f"(w = {k + 1}) Uncorrect Cyclicantibandwidth")
        else:
            print(f"(w = {k + 1}) Correct Cyclicantibandwidth")
        k += 1
    return k, labels


def solve_cab_dfs(vertices, edges, UB, LB):
    k = (UB + LB) // 2
    best = 1
    left = LB
    right = UB
    labels = [None] * len(vertices)
    while left <= right:      
        build_start_time = time.time()
        model = build_model(vertices, edges, k)
        model.setParam('OutputFlag', 0)
        build_end_time = time.time()
        print(f"(k = {k+1}) Build time: {build_end_time - build_start_time} seconds")
        solve_start_time = time.time()
        model.optimize()
        solve_end_time = time.time()
        print(f"(k = {k+1}) Solve time: {solve_end_time - solve_start_time} seconds")

        if model.Status != GRB.OPTIMAL:
            print(f"(k = {k+1}) Not found solution with CAB = {k + 1}.")
            right = k - 1
            k = (left + right) // 2
            continue

        var_values = model.getAttr('X', model.getVars())
        for i in range(len(vertices)):
            for l in range(len(vertices)):
                if var_values[i * len(vertices) + l] > 0.5:
                    labels[i] = l + 1
                    break

        print(f"(k = {k+1}) Value Cyclicantibandwidth: {k+1}")
        print(f"(k = {k+1}) Lables:", labels)

        label_differences = calculate_label_differences(labels, edges)
        if any(element < k + 1 for element in label_differences):
            print(f"(k = {k+1}) Uncorrect Cyclicantibandwidth")
        else:
            print(f"(k = {k+1}) Correct Cyclicantibandwidth")
        best = k + 1
        best_labels = labels
        left = k + 1
        k = (left + right) // 2
    model = build_model(vertices, edges, best)
    model.setParam('OutputFlag', 0)
    model.optimize()
    if model.Status != GRB.OPTIMAL:
        print(f"Final result: CAB = {best}")
        print(f"Labels = {labels}")
    else:
        print("Solver error!")
    return best, labels

def read_file(file_name):
    edges = set()
    file_path = f"{DATA_DIR}/{file_name}"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    size_info = lines[1].strip().split()
    num_vertices = int(size_info[0])
    LB, UB = cabw_bounds[file_name]

    for line in lines[2:]:
        row, col = map(int, line.strip().split())
        edges.add((row, col))
    
    return num_vertices, list(edges), UB, LB

def main():
    real_time_start = time.time()
    parser = argparse.ArgumentParser(description='Giải bài toán cyclicantibandwidth trên đồ thị.')
    parser.add_argument('input_file', type=str, help='Đường dẫn đến tệp đầu vào chứa dữ liệu đồ thị (.mtx.rnd).')
    args = parser.parse_args()

    num_vertices, edges, UB, LB = read_file(args.input_file)
    #num_vertices, edges = read_mtx_rnd_file(args.input_file)

    vertices = list(range(1, num_vertices + 1))

    solve_cyclicantibandwidth(vertices, edges, UB, LB)
    real_time_end = time.time()
    print(f"Real time: {real_time_end - real_time_start} seconds")
if __name__ == "__main__":
    main()