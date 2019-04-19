import csv
import math
import random
import matplotlib.pyplot as plt

dataset = []

# read file
with open('Tugas 2 ML Genap 2018-2019 Dataset Tanpa Label.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        dataset.append([float(row[0]),float(row[1])])

def neuron(x):
    w = []
    for i in range(0,x):
        w.append([float("%.2f" % random.uniform(0, 10)), float("%.2f" % random.uniform(0, 10))])

    return w

def euclidean(weight,input):
    dist = 0
    for i in range(0,len(weight)):
        dist += (weight[i]-input[i])**2
    return float("%.2f" % round(dist,2))

def new_weight(w,alpha,x):
    for i in range(0,len(w)):
        w[i] = float("%.2f" % (w[i] + alpha * (x[i] - w[i])))

    return w

def find_index(i,distance):
    return distance.index(min(distance))


def som(z):
    distance = []
    w = neuron(z)
    alpha = 0.5
    stop = False
    print('w lama : ', w)

    while not stop:
        for j in range(0, len(dataset)):
            for i in range(0, len(w)):
                distance.append(euclidean(w[i], dataset[j]))

            index = find_index(len(w),distance)

            new_weight(w[index], alpha, dataset[j])
            del distance[:]

        alpha *= 0.5
        if (math.isclose(0.0, alpha, abs_tol=0.000000001)):
            stop = True

    cluster = []
    jum = 0
    for j in range(0, len(dataset)):
        for i in range(0, len(w)):
            distance.append(euclidean(w[i], dataset[j]))

        index = find_index(len(w), distance)

        cluster.append(index)
        jum += distance[index]
        del distance[:]

    print('w baru : ', w)
    print(cluster)
    print(math.floor(jum))
    return jum

def main():
    wss = []
    clus = []
    i = 2
    while i <= 10:
        wss.append(som(i))
        clus.append(i)
        i += 1
    plt.plot(clus,wss)
    plt.show()

if __name__ == '__main__':
    main()
