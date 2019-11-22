import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 14})

path = '/home/gayal/Documents/mlith_project1/'
db_agg = 'DB-aggregator.csv'
db_chain = 'db-chain - db-chain.csv'
save_to = 'plots/DB'       # change the destination between plots and plotsAgg
data = pd.read_csv(path+db_chain)   # change the data csv according to agg or chain you want


for s in range(0, 1, 24):
    plt.figure()
    # switch between plot title wrt to the use case
    # plt.title('DB - Aggregator pattern')
    plt.title('DB - Chaining pattern')
    plt.xlabel('Concurrency')
    plt.ylabel('TPS (per second)')
    plt.plot(data['Users'].iloc[s:s+8], data['Throughput'].iloc[s:s+8], label='One Service', marker='o')
    plt.plot(data['Users'].iloc[s+8:s+16], data['Throughput'].iloc[s+8:s+16], label='Two Services', marker='o')
    plt.legend()
    plt.savefig(path+save_to+'/TPS_plot'+str(s//24), bbox_inches='tight')

for s in range(0, 1, 24):
    plt.figure()
    # switch between plot title wrt to the use case
    # plt.title('DB - Aggregator pattern')
    plt.title('DB - Chaining pattern')
    plt.xlabel('Concurrency')
    plt.ylabel('Average Latency (ms)')
    plt.plot(data['Users'].iloc[s:s+8], data['Avg_Latency'].iloc[s:s+8], label='One Service', marker='o')
    plt.plot(data['Users'].iloc[s+8:s+16], data['Avg_Latency'].iloc[s+8:s+16], label='Two Services', marker='o')
    plt.legend()
    plt.savefig(path+save_to+'/Latency_plot'+str(s//24), bbox_inches='tight')
