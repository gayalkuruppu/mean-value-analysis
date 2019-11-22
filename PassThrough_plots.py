import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 14})


path = '/home/gayal/Documents/mlith_project1/'
pass_through_chain = 'msg-chain - msg-chain.csv'
save_to = 'plots/pass-through'     # no aggregator tests were run for pass through use case just the chaining pattern
size = [50, 400, 1024]
data = pd.read_csv(path+pass_through_chain)


for s in range(0, 49, 24):
    plt.figure()
    plt.title('Message Size - {} Bytes'.format(size[s//24]))
    plt.xlabel('Concurrency')
    plt.ylabel('TPS (per second)')
    plt.plot(data['Users'].iloc[s:s+8], data['Throughput'].iloc[s:s+8], label='One Service', marker='o')
    plt.plot(data['Users'].iloc[s+8:s+16], data['Throughput'].iloc[s+8:s+16], label='Two Services', marker='o')
    plt.plot(data['Users'].iloc[s+16:s+24], data['Throughput'].iloc[s+16:s+24], label='Three Services', marker='o')
    plt.legend()
    plt.savefig(path+save_to+'/TPS_plot'+str(s//24), bbox_inches='tight')

for s in range(0, 49, 24):
    plt.figure()
    plt.title('Message Size - {} Bytes'.format(size[s//24]))
    plt.xlabel('Concurrency')
    plt.ylabel('Average Latency (ms)')
    plt.plot(data['Users'].iloc[s:s+8], data['Avg_Latency'].iloc[s:s+8], label='One Service', marker='o')
    plt.plot(data['Users'].iloc[s+8:s+16], data['Avg_Latency'].iloc[s+8:s+16], label='Two Services', marker='o')
    plt.plot(data['Users'].iloc[s+16:s+24], data['Avg_Latency'].iloc[s+16:s+24], label='Three Services', marker='o')
    plt.legend()
    plt.savefig(path+save_to+'/Latency_plot'+str(s//24), bbox_inches='tight')
