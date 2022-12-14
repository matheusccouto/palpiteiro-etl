# :soccer: Palpiteiro ETL
ETL pipelines for fantasy soccer data.

[![Deploy](https://github.com/matheusccouto/palpiteiro-etl/actions/workflows/deploy.yml/badge.svg)](https://github.com/matheusccouto/palpiteiro-etl/actions/workflows/deploy.yml)
[![codecov](https://codecov.io/gh/matheusccouto/palpiteiro-etl/branch/main/graph/badge.svg?token=YIQQ0Bbnh6)](https://codecov.io/gh/matheusccouto/palpiteiro-etl)

## Architecture
ETLs are AWS step functions that reads the API, saves raw data in a S3 bucket and loads into GCP Big Query.

![aws](https://img.shields.io/badge/Amazon_AWS-FF9900?logo=amazonaws&logoColor=white)
![gcp](https://img.shields.io/badge/Google_Cloud-4285F4?logo=google-cloud&logoColor=white)
![python](https://img.shields.io/badge/Python-FFD43B?logo=python&logoColor=blue)
![architecture](diagrams/architecture.png)
