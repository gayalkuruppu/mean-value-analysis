import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 14})

path = '/home/gayal/Documents/mlith_project1/'
db_cache_agg = 'DB-caching-aggregator.csv'
db_cache_chain = 'db-cache-chain - db-cache-chain.csv'
save_to = 'plotsAgg/DB-cache'   # change the destination between plots and plotsAgg
data = pd.read_csv(path+db_cache_agg)   # change the data csv according to agg or chain you want


for s in range(0, 1, 24):
    plt.figure()
    plt.title('DB cache - Aggregator pattern')
    # plt.title('DB cache - Chaining pattern')  # switch between plot title wrt to the use case
    plt.xlabel('Concurrency')
    plt.ylabel('TPS (per second)')
    plt.plot(data['Users'].iloc[s:s+8], data['Throughput'].iloc[s:s+8], label='One Service', marker='o')
    plt.plot(data['Users'].iloc[s+8:s+16], data['Throughput'].iloc[s+8:s+16], label='Two Services', marker='o')
    # plt.plot(data['Users'].iloc[s+16:s+24], data['Throughput'].iloc[s+16:s+24], label='Three Services', marker='o')
    #
    # this is used only in chaining pattern where we have data for 3 services case. otherwise leave this line commented
    #
    plt.legend()
    plt.savefig(path+save_to+'/TPS_plot'+str(s//24), bbox_inches='tight')

for s in range(0, 1, 24):
    plt.figure()
    plt.title('DB cache - Aggregator pattern')
    # plt.title('DB cache - Chaining pattern')  # switch between plot title wrt to the use case
    plt.xlabel('Concurrency')
    plt.ylabel('Average Latency (ms)')
    plt.plot(data['Users'].iloc[s:s+8], data['Avg_Latency'].iloc[s:s+8], label='One Service', marker='o')
    plt.plot(data['Users'].iloc[s+8:s+16], data['Avg_Latency'].iloc[s+8:s+16], label='Two Services', marker='o')
    # plt.plot(data['Users'].iloc[s+16:s+24], data['Avg_Latency'].iloc[s+16:s+24], label='Three Services', marker='o')
    plt.legend()
    plt.savefig(path+save_to+'/Latency_plot'+str(s//24), bbox_inches='tight')
