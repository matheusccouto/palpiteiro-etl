build:
	pip install --upgrade pip wheel
	pip install pytest pylint black boto3
	pip install -r requirements-bigquery.txt
	pip install -r requirements-kaggle.txt
	pip install -r requirements-pandas.txt
	pip install -r requirements-requests.txt