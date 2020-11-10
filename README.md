# Mean Value Analysis
Evaluates performance of chaining and aggregator patterns for some use cases(Pass Through, CPU bound, DB and DB with caching)

MVA is a recursive algorithm to find the expected waiting times, queue lengths of a  closed queueing network. In our implementation, we use K servers with M/M/1 queues and altogether N requests(concurrency) in the system. 

MVA assumes exponentially distributed inter-interval and exponentially distributed service times (aka markovian assumptions).

## How to use the code

### General MVA is implemented in xxx.py script. You can run the code by,

`python mva_multipleSystems.py < data/<relavent data file>`

(will be added soon)

### Compare several scenarios of closed systems using MVA is implemented in mva_multipleSystems.py script. You can run the code by,

`python mva_multipleSystems.py < data/<relavent data file>`

data file has the following structure

- first line is the number of servers in the network (K)
- seccond line is the maximum concurrency in the system (N)
- next K blocks of lines depicts the characteristics related to K servers.
    - first line of the ith block (1 < i <= K) represents the additional overheads in the server (set to 0's for no additional overhead)
    - next K lines in the ith block are the routing probabilities. mth column in jth row (1 < j <= K) in these these K lines shows the routing probability of kth server to mth server