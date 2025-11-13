import os
from gurobipy import Model, GRB
import time
import threading
import argparse
#import psutil
#from memory_profiler import memory_usage
import math
#from func_timeout import func_timeout, FunctionTimedOut



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
    "X-can__715.mtx.rnd": (56, 142),

    "3dmesh_2_2_3.txt": (2, 4),
    "3dmesh_2_2_168.txt": (2, 334),
    "3dmesh_2_2_335.txt": (2, 668),
    "3dmesh_2_2_500.txt": (2, 998),
    "3dmesh_3_3_3.txt": (2, 9),
    "3dmesh_3_3_135.txt": (2, 603),
    "3dmesh_3_3_270.txt": (2, 1211),
    "3dmesh_3_3_400.txt": (2, 1796),
    "3dmesh_4_4_5.txt": (2, 32),
    "3dmesh_4_4_68.txt": (2, 536),
    "3dmesh_4_4_137.txt": (2, 1088),
    "3dmesh_4_4_200.txt": (2, 1592),
    "3dmesh_5_5_7.txt": (2, 74),
    "3dmesh_5_5_35.txt": (2, 424),
    "3dmesh_5_5_70.txt": (2, 862),
    "3dmesh_5_5_100.txt": (2, 1237),
    "3dmesh_6_6_8.txt": (2, 125),
    "3dmesh_6_6_36.txt": (2, 629),
    "3dmesh_6_6_72.txt": (2, 1277),
    "3dmesh_6_6_100.txt": (2, 1781),

    "hypercube_4_16.txt": (2, 4),
    "hypercube_5_32.txt": (5, 9),
    "hypercube_6_64.txt": (10, 19),
    "hypercube_7_128.txt": (21, 41),
    "hypercube_8_256.txt": (43, 85),
    "hypercube_9_512.txt": (89, 178),
    "hypercube_10_1024.txt": (182, 364),

    "double_star_15_5.txt" :(2,3),
    "double_star_15_7.txt" :(2,4),
    "double_star_15_10.txt" :(2,5),
    "double_star_15_12.txt" :(2,6),
    "double_star_30_20.txt" :(2,10),
    "double_star_30_25.txt" :(2,13),
    "double_star_35_20.txt" :(2,10),
    "double_star_35_25.txt" :(2,13),
    "double_star_40_20.txt":( 2,10),
    "double_star_40_25.txt" :(2,13),
    "double_star_40_30.txt":( 2,15),
    "double_star_50_20.txt" :(2,10),
    "double_star_50_25.txt":( 2,13),
    "double_star_50_30.txt" :(2,15),
    "double_star_100_20.txt" :(2,10),
    "double_star_100_25.txt":( 2,13),
    "double_star_100_30.txt" :(2,15),
    "double_star_150_20.txt" :(2,10),
    "double_star_150_25.txt":( 2,13),
    "double_star_150_30.txt":( 2,15),

    "caterpillar_5_4.txt":(2, 20),
    "caterpillar_5_5.txt":(2, 25),
    "caterpillar_5_6.txt":(2, 30),
    "caterpillar_5_7.txt":(2, 35),
    "caterpillar_9_4.txt":(2,36),
    "caterpillar_9_5.txt":(2,45),
    "caterpillar_9_6.txt":(2,54),
    "caterpillar_9_7.txt":(2,63),
    "caterpillar_10_4.txt":(2,40),
    "caterpillar_10_5.txt":(2,50),
    "caterpillar_10_6.txt":(2,60),
    "caterpillar_10_7.txt":(2,70),
    "caterpillar_15_4.txt":(2,60),
    "caterpillar_15_5.txt":(2,75),
    "caterpillar_15_6.txt":(2,90),
    "caterpillar_15_7.txt":(2,105),
    "caterpillar_20_4.txt":(2,80),
    "caterpillar_20_5.txt":(2,100),
    "caterpillar_20_6.txt":(2,120),
    "caterpillar_20_7.txt":(2,140),
    "caterpillar_20_10.txt":(2,200),
    "caterpillar_20_15.txt":(2,300),
    "caterpillar_20_20.txt":(2,400),
    "caterpillar_20_25.txt":(2,500),
    "caterpillar_25_10.txt":(2,250),
    "caterpillar_25_15.txt":(2,375),
    "caterpillar_25_20.txt":(2,500),
    "caterpillar_25_25.txt":(2,625),
    "caterpillar_30_10.txt":(2,300),
    "caterpillar_30_15.txt":(2,450),
    "caterpillar_30_20.txt":(2,600),
    "caterpillar_30_25.txt":(2,750),
    "caterpillar_35_10.txt":(2,350),
    "caterpillar_35_15.txt":(2,525),
    "caterpillar_35_20.txt":(2,700),
    "caterpillar_35_25.txt":(2,875),
    "caterpillar_40_10.txt":(2,400),
    "caterpillar_40_15.txt":(2,600),
    "caterpillar_40_20.txt":(2,80),
    "caterpillar_40_25.txt":(2,1000),

    

    "cbt_30.txt" : (2,30),
    "cbt_31.txt" : (2,31),
    "cbt_32.txt" : (2,32),
    "cbt_33.txt" : (2,33),
    "cbt_34.txt" : (2,34),
    "cbt_35.txt" : (2,35),
    "cbt_45.txt" : (2,45),
    "cbt_46.txt" : (2,46),
    "cbt_47.txt" : (2,47),
    "cbt_48.txt" : (2,48),
    "cbt_49.txt" : (2,49),
    "cbt_50.txt" : (2,50),
    "cbt_500.txt" : (2,500),
    "cbt_510.txt" : (2,510),
    "cbt_550.txt" : (2,550),
    "cbt_600.txt" : (2,600),
    "cbt_620.txt" : (2,620),
    "cbt_630.txt" : (2,630),
    "cbt_640.txt" : (2,640),
    "cbt_730.txt" : (2,730),
    "cbt_790.txt" : (2,790),
    "cbt_880.txt" : (2,880),
    "cbt_910.txt" : (2,910),
    "cbt_950.txt" : (2,950),

    "p1_100_200" : (2, 100),
    "p2_100_200" : (2, 100),
    "p3_100_200" : (2, 100),
    "p4_100_200" : (2, 100),
    "p5_100_200" : (2, 100),
    "p6_100_200" : (2, 100),
    "p7_100_200" : (2, 100),
    "p8_100_200" : (2, 100),
    "p9_100_200" : (2, 100),
    "p10_100_200" : (2, 100),
    "p11_100_600" : (2, 100),
    "p12_100_600" : (2, 100),
    "p13_100_600" : (2, 100),
    "p14_100_600" : (2, 100),
    "p15_100_600" : (2, 100),
    "p16_100_600" : (2, 100),
    "p17_100_600" : (2, 100),
    "p18_100_600" : (2, 100),
    "p19_100_600" : (2, 100),
    "p20_100_600" : (2, 100),
    "p21_200_400" : (2, 200),
    "p22_200_400" : (2, 200),
    "p23_200_400" : (2, 200),
    "p24_200_400" : (2, 200),
    "p25_200_400" : (2, 200),
    "p26_200_400" : (2, 200),
    "p27_200_400" : (2, 200),
    "p28_200_400" : (2, 200),
    "p29_200_400" : (2, 200),
    "p30_200_400" : (2, 200),
    "p31_200_2000" : (2, 200),
    "p32_200_2000" : (2, 200),
    "p33_200_2000" : (2, 200),
    "p34_200_2000" : (2, 200),
    "p35_200_2000" : (2, 200),
    "p36_200_2000" : (2, 200),
    "p37_200_2000" : (2, 200),
    "p38_200_2000" : (2, 200),
    "p39_200_2000" : (2, 200),
    "p40_200_2000" : (2, 200),
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
    file_path = f"{file_name}"
    with open(file_path, 'r') as file:
        lines = file.readlines()
    file_name = os.path.basename(file_path)
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