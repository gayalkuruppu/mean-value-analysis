import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# matplotlib.rcParams.update({'font.size': 22})


def lmbda(x):  # used to get lambda(m-1)
    total = 0
    for t in range(no_of_services):
        total += p_ratios[t] * ET[t][x]
    return (x + 1) / total


throughput = []
concurrency = 500

serviceRates = [50000, 14300, 21000]
no_of_services = len(serviceRates)  # number of servers
serverNames = ['JMeter Client', 'Pass-through Service', 'Backend Service', 'Total']
overheads = [0, 0, 0]   # overheads in seconds
# routingProb[i][j] = routing probability from i th server to j th server
routingProb = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]     # how to convert the routing Prob matrix into p_ratios
# p_ratios = [0.25, 0.5, 0.25]
p_ratios = [1/3, 1/3, 1/3]

p = 1/no_of_services
ET = np.zeros((no_of_services, concurrency))     # concurrency * no_of_servers 2d list
lm = np.arange(1, concurrency+1)        # nodes axis 1d list elements are concurrency from 1 to concurrency
EN = np.zeros((no_of_services, concurrency))     # concurrency * no_of_servers 2d list

for i in range(no_of_services):
    serverNames[i] = serverNames[i]+' (Service Rate = {} requests/sec)'.format(serviceRates[i])

for i in range(no_of_services):
    ET[i][0] = 1000*((1/serviceRates[i]) + overheads[i])    # expected time in milli seconds

# plt.figure(figsize=(16, 10))
plt.figure()
plt.title('Response Time Vs Concurrency')
plt.xlabel('Concurrency(N)')
plt.ylabel('Response Time (ms)')


for n in range(1, concurrency):
    for s in range(no_of_services):
        ET[s][n] = (1 + p_ratios[s]*lmbda(n-1)*ET[s][n-1])*ET[s][0]

for n in range(1, concurrency):
    for s in range(no_of_services):
        EN[s][n] = ET[s][n]*lmbda(n)*p_ratios[s]

ER = np.sum(ET, axis=0)  # Response Time in milli seconds
'''
  E[s][n]
E[R]
for n in range(1, concurrency):
    for s in range(no_of_services):
        ET[s][n] = (1 + p_ratios[s]*lmbda(n-1)*ET[s][n-1])*ET[s][0]


'''


X = 1000*lm/ER  # Throughput req/sec
throughput.append(X)

for s in range(1, no_of_services):
    plt.plot(lm, ET[s], label=serverNames[s])

plt.plot(lm, ER, label='Total Response Time')
plt.legend()
# plt.legend(prop={'size': 22})
plt.savefig('/home/gayal/Documents/queueingTheoryModels/test02/Response Time')

plt.figure()
plt.title('Overall Throughput Vs Concurrency')
plt.xlabel('Concurrency(N)')
plt.ylabel('Overall Throughput (requests/second)')
plt.plot(lm, X)
plt.savefig('/home/gayal/Documents/queueingTheoryModels/test02/Throughput')


plt.figure()
plt.title('Expected No of Requests Vs Concurrency')
plt.xlabel('Concurrency(N)')
plt.ylabel('Expected No of Requests (requests)')

for s in range(1, no_of_services):
    plt.plot(lm, EN[s], label=serverNames[s])

plt.legend()
# plt.legend(prop={'size': 22})
plt.savefig('/home/gayal/Documents/queueingTheoryModels/test02/No_of_requests')
plt.show()
