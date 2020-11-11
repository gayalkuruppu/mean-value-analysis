# Mean Value Analysis
Evaluates performance of chaining and aggregator patterns for some use cases(Pass Through, CPU bound, DB and DB with caching)

MVA is a recursive algorithm to find the expected waiting times, queue lengths of a  closed queueing network. In our implementation, we use K servers with M/M/1 queues and altogether N requests(concurrency) in the system. 

MVA assumes exponentially distributed inter-interval and exponentially distributed service times (aka markovian assumptions).

## How to use the code

### Modeling the System Thoughput and Latency

#### General MVA is implemented in mva_multipleSystems.py script. You can run the code by,

tip: set number of scenarios to 1 as in data_single_scenario for a single closed system.

`python mva_multipleSystems.py < data/data_single_scenario`


#### Compare several scenarios of closed systems using MVA is implemented in mva_multipleSystems.py script. You can run the code by,

`python mva_multipleSystems.py < data/<relavent data file>`

data file has the following structure

- first line is the systems which you want to compare (S)
- seccond line is the maximum concurrency in the system (N)
- next S blocks of lines depicts the characteristics related to each S scenarios (each different closed system).
    - first line has the service rates of the i<sup>th</sup> closed system(ith scenario) where (1 < i <= K). Let's say we have K servers in the system.
    - second line of the i<sup>th</sup> block represents the additional overheads in the server (set to 0's for no additional overhead)
    - next K lines in the i<sup>th</sup> block are the routing probabilities. m<sup>th</sup> column in j<sup>th</sup> row (1 < j <= K) in these these K lines shows the routing probability of k<sup>th</sup> server to mth server
