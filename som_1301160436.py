import csv
import math
import random

dataset = []
w = [[float("%.2f" % random.uniform(0,10)),float("%.2f" % random.uniform(0,10))],[float("%.2f" % random.uniform(0,10)),float("%.2f" % random.uniform(0,10))]]

# read file
with open('Tugas 2 ML Genap 2018-2019 Dataset Tanpa Label.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        # if line_count == 0:
        #     line_count += 1
        # else:
        dataset.append([float(row[0]),float(row[1])])

def eculidean_distance(w1,x1):
    hasil = 0
    for i in range(0,len(w)):
        hasil += (w1-x1)**2
    return float("%.2f" % round(hasil,2))

def new_weight():
    global w
    for i in range(0,len(w[index])):
        w[index][i] = float("%.2f" % (w[index][i] + alpha * (dataset[j][i] - w[index][i])))

    return w

distance = []
alpha = 0.5
stop = False
# print(dataset)
print('w lama : ', w)
while not stop:
    for j in range (0,len(dataset)):
        for i in range(0,len(w)):
            distance.append(eculidean_distance(w[i][0],dataset[j][0]))
        # print(j,'-',adaw)

        if (distance[0] > distance[1]):
            index = 1
        else:
            index = 0

        # w[index][0] = float("%.2f" % (w[index][0] + alpha*(dataset[j][0]-w[index][0])))
        # w[index][1] = float("%.2f" % (w[index][1] + alpha*(dataset[j][1]-w[index][1])))
        new_weight()
        del distance[:]
    alpha *= 0.5
    if (math.isclose(0.0, alpha, abs_tol=0.000000001)):
        stop = True

cluster = []
for j in range (0,len(dataset)):
    for i in range(0,len(w)):
        distance.append(eculidean_distance(w[i][0],dataset[j][0]))
    # print(j,'-',adaw)

    if (distance[0] > distance[1]):
        index = 1
    else:
        index = 0

    # w[index][0] = float("%.2f" % (w[index][0] + alpha*(dataset[j][0]-w[index][0])))
    # w[index][1] = float("%.2f" % (w[index][1] + alpha*(dataset[j][1]-w[index][1])))
    cluster.append(index)
    del distance[:]

print('w baru : ', w)
print(cluster)
#
# alpha = 0.5
# stop = False
# # print(dataset)
# del w[:]
# w = [[float("%.2f" % random.uniform(0,10)),float("%.2f" % random.uniform(0,10))],[float("%.2f" % random.uniform(0,10)),float("%.2f" % random.uniform(0,10))],[float("%.2f" % random.uniform(0,10)),float("%.2f" % random.uniform(0,10))]]
# print('w lama : ', w)
# while not stop:
#     for j in range (0,len(dataset)):
#         for i in range(0,len(w)):
#             distance.append(eculidean_distance(w[i][0],dataset[j][0]))
#         # print(j,'-',adaw)
#         # distance[1]<distance[0]<distance[2]
#         if (distance[0] < distance[1] and distance[0] < distance[2]):
#             index = 0
#         elif (distance[1] < distance[0] and distance[1] < distance[2]):
#             index = 1
#         elif (distance[2] < distance[0] and distance[2] < distance[1]):
#             index = 2
#         # w[index][0] = float("%.2f" % (w[index][0] + alpha*(dataset[j][0]-w[index][0])))
#         # w[index][1] = float("%.2f" % (w[index][1] + alpha*(dataset[j][1]-w[index][1])))
#         new_weight()
#         del distance[:]
#     alpha *= 0.5
#     if (math.isclose(0.0, alpha, abs_tol=0.000000001)):
#         stop = True
#
#
# del cluster[:]
# for j in range (0,len(dataset)):
#     for i in range(0,len(w)):
#         distance.append(eculidean_distance(w[i][0],dataset[j][0]))
#     # print(j,'-',adaw)
#
#     if (distance[0] < distance[1] and distance[0] < distance[2]):
#         index = 0
#     elif (distance[1] < distance[0] and distance[1] < distance[2]):
#         index = 1
#     elif (distance[2] < distance[0] and distance[2] < distance[1]):
#         index = 2
#
#     # w[index][0] = float("%.2f" % (w[index][0] + alpha*(dataset[j][0]-w[index][0])))
#     # w[index][1] = float("%.2f" % (w[index][1] + alpha*(dataset[j][1]-w[index][1])))
#     cluster.append(index)
#     del distance[:]
#
# print('w baru : ', w)
# print(cluster)
#
# alpha = 0.5
# stop = False
# # print(dataset)
# del w[:]
# w = [[float("%.2f" % random.uniform(0,10)),float("%.2f" % random.uniform(0,10))],[float("%.2f" % random.uniform(0,10)),float("%.2f" % random.uniform(0,10))],[float("%.2f" % random.uniform(0,10)),float("%.2f" % random.uniform(0,10))],[float("%.2f" % random.uniform(0,10)),float("%.2f" % random.uniform(0,10))]]
# print('w lama : ', w)
# while not stop:
#     for j in range (0,len(dataset)):
#         for i in range(0,len(w)):
#             distance.append(eculidean_distance(w[i][0],dataset[j][0]))
#         # print(j,'-',adaw)
#         # distance[0]<distance[1]<distance[2]<distance[3]
#         if (distance[0] < distance[1] and distance[0] < distance[2] and distance[0] < distance[3]):
#             index = 0
#         elif (distance[1] < distance[0] and distance[1] < distance[2] and distance[1] < distance[3]):
#             index = 1
#         elif (distance[2] < distance[0] and distance[2] < distance[1] and distance[2] < distance[3]):
#             index = 2
#         elif (distance[3] < distance[0] and distance[3] < distance[1] and distance[3] < distance[2]):
#             index = 3
#         # w[index][0] = float("%.2f" % (w[index][0] + alpha*(dataset[j][0]-w[index][0])))
#         # w[index][1] = float("%.2f" % (w[index][1] + alpha*(dataset[j][1]-w[index][1])))
#         new_weight()
#         del distance[:]
#     alpha *= 0.5
#     if (math.isclose(0.0, alpha, abs_tol=0.000000001)):
#         stop = True
#
#
# del cluster[:]
# for j in range (0,len(dataset)):
#     for i in range(0,len(w)):
#         distance.append(eculidean_distance(w[i][0],dataset[j][0]))
#     # print(j,'-',adaw)
#
#     if (distance[0] < distance[1] and distance[0] < distance[2] and distance[0] < distance[3]):
#         index = 0
#     elif (distance[1] < distance[0] and distance[1] < distance[2] and distance[1] < distance[3]):
#         index = 1
#     elif (distance[2] < distance[0] and distance[2] < distance[1] and distance[2] < distance[3]):
#         index = 2
#     elif (distance[3] < distance[0] and distance[3] < distance[1] and distance[3] < distance[2]):
#         index = 3
#
#     # w[index][0] = float("%.2f" % (w[index][0] + alpha*(dataset[j][0]-w[index][0])))
#     # w[index][1] = float("%.2f" % (w[index][1] + alpha*(dataset[j][1]-w[index][1])))
#     cluster.append(index)
#     del distance[:]
#
# print('w baru : ', w)
# print(cluster)