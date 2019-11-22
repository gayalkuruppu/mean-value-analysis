import numpy as np
import matplotlib.pyplot as plt


def lmbda(x):  # we use to get lambda(m-1)
    total = 0
    for t in range(k):
        total += p * ET[x][t]
    return (x + 1) / total


throughput = []
u = 0

while True:
    m = input('Press "q" to exit or Enter the concurrency : ')
    if m == 'q':
        break
    else:
        m = int(m)
    serviceRates = list(map(int, input('Enter the service rates separated by commas : ').split(',')))
    overheads = list(map(float, input('Enter the service time overheads separated by commas : ').split(',')))
    # routingProb = list(map(float, input('Enter the service time overheads separated by commas : ').split(',')))

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
    throughput.append(X)

    # plt.figure()
    # plt.title('Throughput Vs Concurrency')
    # plt.xlabel('Concurrency(N)')
    # plt.ylabel('Throughput (requests/second)')
    # plt.plot(lm, X)
    # plt.plot(lm, throughput[u])
    u += 1
    # plt.figure()
    # plt.title('Response Time Vs Concurrency')
    # plt.xlabel('Concurrency(N)')
    # plt.ylabel('Response Time (seconds)')
    # plt.plot(lm, ER)
    # plt.show()
    #
    # print(ET[0])

plt.figure()
plt.title('Throughput Vs Concurrency for prime 10000019')
plt.xlabel('Concurrency(N)')
plt.ylabel('Throughput (requests/second)')
for y in range(u):
    plt.plot(lm, throughput[y], label=str(y+1)+'service(s)')

plt.legend()
plt.show()

