codespaces: pip
	pip install -r requirements-bigquery.txt
	pip install -r requirements-kaggle.txt
	pip install -r requirements-pandas.txt
	pip install -r requirements-requests.txt
upgrade-pip: pip
	pip install --upgrade pip wheel
bigquery-layer: layer_bigquery.zip
	mkdir python
	pip install -r requirements-bigquery.txt --target python
	zip -r layer_bigquery.zip python/
	rm -r python
kaggle-layer: layer_kaggle.zip
	mkdir python
	pip install -r requirements-kaggle.txt --target python
	zip -r layer_kaggle.zip python/
	rm -r python
pandas-layer: layer_pandas.zip
	mkdir python
	pip install -r requirements-pandas.txt --target python
	zip -r layer_pandas.zip python/
	rm -r python
requests-layer: layer_requests.zip
	mkdir python
	pip install -r requirements-requests.txt --target python
	zip -r layer_requests.zip python/
	rm -r python
layers: layer_bigquery.zip layer_kaggle.zip layer_kaggle.zip layer_pandas.zip layer_requests.zip