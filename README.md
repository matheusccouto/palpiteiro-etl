# :soccer: Palpiteiro ETL
Points prediction for the fantasy soccer app.

![aws](https://img.shields.io/badge/Amazon_AWS-FF9900?logo=amazonaws&logoColor=white)
![gcp](https://img.shields.io/badge/Google_Cloud-4285F4?logo=google-cloud&logoColor=white)
![python](https://img.shields.io/badge/Python-FFD43B?logo=python&logoColor=blue)

[![Deploy](https://github.com/matheusccouto/palpiteiro-etl/actions/workflows/deploy.yml/badge.svg)](https://github.com/matheusccouto/palpiteiro-etl/actions/workflows/deploy.yml)

## ETLs
ETLs are AWS step functions that reads the API, saves raw data in a S3 bucket and loads into GCP Big Query.
![overview](diagrams/overview.png)
