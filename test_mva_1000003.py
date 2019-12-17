import numpy as np
import matplotlib.pyplot as plt
import os
import stat
import matplotlib
import pandas as pd
matplotlib.rcParams.update({'font.size': 14})

path = '/Users/Gayal/PycharmProjects/mean-value-analysis/'
csv = '5_CPU_Orchestration.csv'
save_to = 'Analysis/Plotting/plots/5_CPU_Orchestration/'
data = pd.read_csv(path+csv)


def lmbda(x):  # we use to get lambda(m-1)
    total = 0
    for t in range(no_of_services):
        total += p_ratios[t] * ET[t][x]
    return (x + 1) / total


def find_arrival_rate_ratios(prob_rout_matrix):
    """"
    routingProb[i][j] = routing probability from i th server to j th server

    :param prob_rout_matrix: array of routing probabilities. dimension (#servers)x(#servers)
    :return: the arrival rate/ summation of all arrival rates, for each server as
    an array
    """
    size = len(prob_rout_matrix)
    identity_matrix = np.identity(size)
    transpose = np.transpose(prob_rout_matrix)
    mat = transpose - identity_matrix
    mat[size-1] = [1]*size
    q = np.array([0]*(size-1)+[1])
    x = np.linalg.solve(mat, q)
    return x


mode = os.fstat(0).st_mode
if stat.S_ISREG(mode):
    # print("stdin is redirected")
    throughput = []
    responseTime = []
    no_of_requests = []
    no_of_systems = int(input())
    concurrency_max = int(input())
    throughput_max = 0

    for t in range(no_of_systems):
        serviceRates = list(map(int, input().split(',')))
        overheads = list(map(float, input().split(',')))
        routingProb = []
        for i in range(len(serviceRates)):
            routingProb.append(list(map(float, input().split(','))))
        p_ratios = find_arrival_rate_ratios(routingProb)
        no_of_services = len(serviceRates)
        p = 1 / no_of_services
        ET = np.zeros((no_of_services, concurrency_max))
        EN = np.zeros((no_of_services, concurrency_max))
        lm = np.arange(1, concurrency_max + 1)

        for s in range(no_of_services):
            ET[s][0] = ((1 / serviceRates[s]) + overheads[s])  # expected time in milli seconds

        for n in range(1, concurrency_max):
            for s in range(no_of_services):
                ET[s][n] = (1 + p_ratios[s] * lmbda(n - 1) * ET[s][n - 1]) * ET[s][0]

        for n in range(1, concurrency_max):
            for s in range(no_of_services):
                EN[s][n] = ET[s][n] * lmbda(n) * p_ratios[s]

        ER = np.sum(ET, axis=0)  # Response Time
        X = lm / ER  # Throughput
        if throughput_max <= max(X):
            throughput_max = max(X)
        throughput.append(X)
        responseTime.append(ER)
        no_of_requests.append(EN)

    plt.figure()
    plt.subplot(1, 2, 1)
    # plt.title('Throughput Vs Concurrency')
    plt.xlabel('Concurrency(N)')
    plt.ylabel('Throughput (requests/second)')
    plt.ylim(ymin=0, ymax=throughput_max*1.1)
    for s in range(no_of_systems):
        plt.plot(lm, throughput[s], label='{} service(s)'.format(s + 1))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 3))
    plt.legend()
    # plt.tight_layout()

    s = 96
    plt.subplot(1, 2, 2)
    plt.xlabel('Concurrency(N)')
    plt.ylabel('Throughput (requests/second)')
    plt.ylim(ymin=0, ymax=throughput_max*1.1)
    plt.plot(data['Users'].iloc[s:s + 8], data['Throughput'].iloc[s:s + 8], label='1 Service(s)', marker='o')
    plt.plot(data['Users'].iloc[s + 8:s + 16], data['Throughput'].iloc[s + 8:s + 16], label='2 Service(s)', marker='o')
    plt.plot(data['Users'].iloc[s + 16:s + 24], data['Throughput'].iloc[s + 16:s + 24], label='3 Service(s)',
             marker='o')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 3))
    plt.legend()
    plt.tight_layout()

    plt.figure()
    plt.subplot(1, 2, 1)
    # plt.title('Response Time Vs Concurrency')
    plt.xlabel('Concurrency(N)')
    plt.ylabel('Average Response Time (ms)')
    for s in range(no_of_systems):
        plt.plot(lm, 1000*responseTime[s], label='{} service(s)'.format(s + 1))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 3))
    plt.legend()

    s = 96
    plt.subplot(1, 2, 2)
    plt.xlabel('Concurrency(N)')
    plt.ylabel('Average Response Time (ms)')
    plt.plot(data['Users'].iloc[s:s + 8], data['Avg_Latency'].iloc[s:s + 8], label='1 Service(s)', marker='o')
    plt.plot(data['Users'].iloc[s + 8:s + 16], data['Avg_Latency'].iloc[s + 8:s + 16], label='2 Service(s)', marker='o')
    plt.plot(data['Users'].iloc[s + 16:s + 24], data['Avg_Latency'].iloc[s + 16:s + 24], label='3 Service(s)',
             marker='o')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 3))
    plt.legend()
    plt.tight_layout()
    plt.show()

else:
    # print("stdin is terminal")
    throughput = []
    responseTime = []
    no_of_requests = []
    no_of_systems = int(input('Enter the number of scenarios(systems) you want to analyze : '))
    concurrency_max = int(input('Enter the maximum concurrency : '))

    for t in range(no_of_systems):
        serviceRates = list(map(int, input('Enter the service rates separated by commas : ').split(',')))
        overheads = list(map(float, input('Enter the service time overheads separated by commas : ').split(',')))
        routingProb = []
        for i in range(len(serviceRates)):
            routingProb.append(list(map(float, input('Routing probabilities from server {} to all servers '
                                                 '(separated by commas) : '.format(i+1)).split(','))))
        p_ratios = find_arrival_rate_ratios(routingProb)
        no_of_services = len(serviceRates)
        p = 1 / no_of_services
        ET = np.zeros((no_of_services, concurrency_max))
        EN = np.zeros((no_of_services, concurrency_max))
        lm = np.arange(1, concurrency_max+1)

        for s in range(no_of_services):
            ET[s][0] = 1000*((1/serviceRates[s]) + overheads[s])    # expected time in milli seconds

        for n in range(1, concurrency_max):
            for s in range(no_of_services):
                ET[s][n] = (1 + p_ratios[s] * lmbda(n - 1) * ET[s][n - 1]) * ET[s][0]

        for n in range(1, concurrency_max):
            for s in range(no_of_services):
                EN[s][n] = ET[s][n] * lmbda(n) * p_ratios[s]

        ER = np.sum(ET, axis=0)  # Response Time
        X = lm/ER  # Throughput
        throughput.append(X)
        responseTime.append(ER)
        no_of_requests.append(EN)

    plt.figure()
    plt.title('Throughput Vs Concurrency')
    plt.xlabel('Concurrency(N)')
    plt.ylabel('Throughput (requests/second)')
    for s in range(no_of_systems):
        plt.plot(lm, throughput[s], label='system {}'.format(s+1))

    plt.figure()
    plt.title('Response Time Vs Concurrency')
    plt.xlabel('Concurrency(N)')
    plt.ylabel('Response Time (seconds)')
    for s in range(no_of_systems):
        plt.plot(lm, responseTime[s], label='system {}'.format(s+1))
    plt.show()
