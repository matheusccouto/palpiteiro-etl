# :soccer: Palpiteiro ETL
Points prediction for the fantasy soccer app.

![aws](https://img.shields.io/badge/Amazon_AWS-FF9900?logo=amazonaws&logoColor=white)
![gcp](https://img.shields.io/badge/Google_Cloud-4285F4?logo=google-cloud&logoColor=white)
![python](https://img.shields.io/badge/Python-FFD43B?logo=python&logoColor=blue)

[![Deploy](https://github.com/matheusccouto/palpiteiro-etl/actions/workflows/deploy.yml/badge.svg)](https://github.com/matheusccouto/palpiteiro-etl/actions/workflows/deploy.yml)

## ETLs
ETLs are AWS step functions that reads the API, saves raw data in a S3 bucket and loads into GCP Big Query.
![overview](diagrams/overview.png)

### Cartola Players
Players data from Cartola API comes in a nested JSON. It is stored as it is in S3, flatten into a CSV, which is also stored and finally loaded into google big query.
![state-machine-cartola-players](diagrams/state-machine-cartola-players.png)

### Cartola Scouts
Players scouts data from Cartola API comes in a nested JSON. It is stored as it is in S3, flatten into a CSV, which is also stored and finally loaded into google big query.
![state-machine-cartola-scouts](diagrams/state-machine-cartola-scouts.png)

### Cartola Matches
Matches data from Cartola API comes in a nested JSON. It is stored as it is in S3, flatten into a CSV, which is also stored and finally loaded into google big query.
![state-machine-cartola-matches](diagrams/state-machine-cartola-matches.png)

### FiveThirtyEight SPI
Soccer Power Index data from FiveThirtyEight API already comes in CSV, so it just need to be stored as it is in S3 and loaded into Google Big Query.
![state-machine-fivethirtyeight-spi](diagrams/state-machine-fivethirtyeight-spi.png)

### Odds
Odds data from The Odds API comes in a nested JSON. It is stored as it is in S3, flatten into a CSV, which is also stored and finally loaded into google big query.
![state-machine-odds](diagrams/state-machine-odds.png)