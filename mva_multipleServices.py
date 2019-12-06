import numpy as np
import matplotlib.pyplot as plt


def lmbda(x):  # we use to get lambda(m-1)
    total = 0
    for t in range(k):
        total += p * ET[x][t]
    return (x + 1) / total


def find_arrival_rate_ratios(prob_rout_matrix):
    """"
    routingProb[i][j] = routing probability from i th server to j th server

    :param prob_rout_matrix: array of routing probabilities. dimension (#servers)x(#servers)
    :return: the arrival rate/ summation of all arrival rates, for each server as
    an array
    """
    identity_matrix = np.identity(3)
    transpose = np.transpose(prob_rout_matrix)
    mat = transpose - identity_matrix
    mat[2] = [1, 1, 1]
    q = np.array([0, 0, 1])
    x = np.linalg.solve(mat, q)
    return x


while True:
    m = input('Press "q" to exit or Enter the concurrency : ')
    if m == 'q':
        break
    else:
        m = int(m)
    serviceRates = list(map(int, input('Enter the service rates seperated by commas : ').split(',')))
    overheads = list(map(float, input('Enter the service time overheads seperated by commas : ').split(',')))
    # routingProb = list(map(float, input('Enter the service time overheads seperated by commas : ').split(',')))

    k = len(serviceRates)  # number of servers
    p = 1/k
    ET = np.zeros((m, k))
    lm = np.arange(1, m+1)

    for i in range(k):
        ET[0][i] = (1/serviceRates[i]) + overheads[i]

    for i in range(1, m):
        for j in range(k):
            ET[i][j] = (1 + p*lmbda(i-1)*ET[i-1][j])*ET[0][j]

    ER = np.sum(ET, axis=1)  # Response Time
    X = lm/ER  # Throughput

    plt.figure()
    plt.title('Throughput Vs Concurrency')
    plt.xlabel('Concurrency(N)')
    plt.ylabel('Throughput (requests/second)')
    plt.plot(lm, X)

    plt.figure()
    plt.title('Response Time Vs Concurrency')
    plt.xlabel('Concurrency(N)')
    plt.ylabel('Response Time (seconds)')
    plt.plot(lm, ER)
    plt.show()

    print(ET[0])
