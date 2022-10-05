codespaces: pip serverless
	pip install -r requirements-bigquery.txt
	pip install -r requirements-kaggle.txt
	pip install -r requirements-pandas.txt
	pip install -r requirements-requests.txt
pip:
	pip install --upgrade pip wheel
diagrams: pip
	sudo apt install graphviz -y
	pip install diagrams
serverless:
	npm install -g serverless@3
	npm install --save-dev serverless-step-functions
layer_bigquery.zip: pip
	mkdir python
	pip install \
		--platform manylinux2014_x86_64 \
		--implementation cp \
		--python 3.9 \
		--only-binary=:all: \
		--target python \
		-r requirements-bigquery.txt
	zip -r layer_bigquery.zip python/
	rm -r python
layer_kaggle.zip: pip
	mkdir python
	pip install --target python -r requirements-kaggle.txt
	zip -r layer_kaggle.zip python/
	rm -r python
layer_pandas.zip: pip
	mkdir python
	pip install \
		--platform manylinux2014_x86_64 \
		--implementation cp \
		--python 3.9 \
		--only-binary=:all: \
		--target python \
		-r requirements-pandas.txt
	zip -r layer_pandas.zip python/
	rm -r python
layer_requests.zip: pip
	mkdir python
	pip install \
		--platform manylinux2014_x86_64 \
		--implementation cp \
		--python 3.9 \
		--only-binary=:all: \
		--target python \
		-r requirements-requests.txt
	zip -r layer_requests.zip python/
	rm -r python
layers: layer_bigquery.zip layer_kaggle.zip layer_kaggle.zip layer_pandas.zip layer_requests.zip