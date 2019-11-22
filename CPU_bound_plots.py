import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 14})

path = '/home/gayal/Documents/mlith_project1/'
prime_check_chain = 'prime-chain - prime-chain.csv'
prime_check_agg = 'prime-aggregator.csv'
save_to = 'plots/prime'    # change the destination between plots and plotsAgg
data = pd.read_csv(path+prime_check_chain)   # change the data csv according to agg or chain you want
prime = [521, 7919, 10007, 100003, 1000003, 10000019]


for s in range(0, 121, 24):
    plt.figure()
    # switch between plot title wrt to the use case
    # plt.title('Prime number - {} (Aggregator pattern)'.format(prime[s//24]))
    plt.title('Prime number - {} (Chaining pattern)'.format(prime[s//24]))
    plt.xlabel('Concurrency')
    plt.ylabel('TPS (per second)')
    plt.plot(data['Users'].iloc[s:s+8], data['Throughput'].iloc[s:s+8], label='One Service', marker='o')
    plt.plot(data['Users'].iloc[s+8:s+16], data['Throughput'].iloc[s+8:s+16], label='Two Services', marker='o')
    plt.plot(data['Users'].iloc[s+16:s+24], data['Throughput'].iloc[s+16:s+24], label='Three Services', marker='o')
    plt.legend()
    plt.savefig(path+save_to+'/TPS_plot'+str(s//24), bbox_inches='tight')

for s in range(0, 121, 24):
    plt.figure()
    # switch between plot title wrt to the use case
    # plt.title('Prime number - {} (Aggregator pattern)'.format(prime[s//24]))
    plt.title('Prime number - {} (Chaining pattern)'.format(prime[s//24]))
    plt.xlabel('Concurrency')
    plt.ylabel('Average Latency (ms)')
    plt.plot(data['Users'].iloc[s:s+8], data['Avg_Latency'].iloc[s:s+8], label='One Service', marker='o')
    plt.plot(data['Users'].iloc[s+8:s+16], data['Avg_Latency'].iloc[s+8:s+16], label='Two Services', marker='o')
    plt.plot(data['Users'].iloc[s+16:s+24], data['Avg_Latency'].iloc[s+16:s+24], label='Three Services', marker='o')
    plt.legend()
    plt.savefig(path+save_to+'/Latency_plot'+str(s//24), bbox_inches='tight')
