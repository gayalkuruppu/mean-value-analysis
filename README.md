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

- first line is the systems which you want to compare (S). If you are not comparing multiple systems just pass 1.
- seccond line is the maximum concurrency in the system (N)
- next S blocks of lines depicts the characteristics related to each S scenarios (each different closed system).
    - first line has the service rates of the i<sup>th</sup> closed system(ith scenario) where (1 < i <= K). Let's say we have K servers in the system.
    - second line of the i<sup>th</sup> block represents the additional overheads in the server (set to 0's for no additional overhead)
    - next K lines in the i<sup>th</sup> block are the routing probabilities. m<sup>th</sup> column in j<sup>th</sup> row (1 < j <= K) in these these K lines shows the routing probability of k<sup>th</sup> server to mth server

#### Example 1
![Screenshot from 2022-04-21 22-58-27](https://user-images.githubusercontent.com/46120162/164517298-4fc4cb83-074d-4c0e-8ba5-d489640e6ff3.png)

- Input for the above example would be,

1\
100\
s1, s2, s3\
0, 0, 0\
0, 1, 0\
0.5, 0, 0.5\
0, 1, 0

- Explanation - first line is 1 because we're not comparing multiple systems but only have one system. Second line we have the maximum concurrent users (=100). Next are the service rates of each servers. Overheads are set to zero for each server. routing probabilities are given as shown in the only diagram.

## For Windows

To run the code in windows, you just need to run the `mva_multipleSystems.py` and enter the required input data in the terminal according to the above structure. You can run like this even with Ubuntu and MacOS.
