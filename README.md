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
