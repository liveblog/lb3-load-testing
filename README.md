# Load testing for Liveblog3

## Installation

```
sudo pip install virtualenv
make install
```

## Usage

```
make test HOST=http://liveblogdevel.dev.superdesk.org BLOG=55fa9e3de95d73002ef2931b CLIENTS=1000 HATCH=250 REQUESTS=1000
```

and grap the results in a csv format in `results/`

## Options

Parameters | Description | Default value
-----------|-------------|--------------
`HOST` | lb host instance to test | http://liveblogdevel.dev.superdesk.org
`BLOG` | blog id to test | 55fa9e3de95d73002ef2931b
`CLIENTS` | number of clients to simulate | 1000
`HATCH` | number of clients that will spawn per second | 250
`REQUESTS` | number of requests to reach before stopping the test | 1000

## Example of results
### In stdout
```
Name        # reqs      # fails     Avg     Min     Max  |  Median   req/s
--------------------------------------------------------------------------------------
GET posts/    4645   118(2.48%)    9578     747  137318  |    3600   24.40
GET updates/  4793   112(2.28%)    8706     517  145435  |    2900   38.10
--------------------------------------------------------------------------------------
Total         9438   230(2.44%)                                      62.50

Percentage of the requests completed within given times
Name         # reqs    50%    66%    75%    80%    90%    95%    98%    99%   100%
--------------------------------------------------------------------------------------
GET posts/     4645   3600   6100   8300  11000  24000  46000  75000  89000 137318
GET updates/   4793   2900   5500   7700  11000  23000  40000  65000  85000 145435
--------------------------------------------------------------------------------------
```
### In csv

```
enpoint,median_response_time,num_requests
"updates/ GET",2900,4793
"posts/ GET",3600,4645
```
