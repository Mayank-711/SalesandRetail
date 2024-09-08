set -o errexit
pip install -r SalesandRetail/requirements.txt
python SalesandRetail/manage.py collectstatic --no-input
python SalesandRetail/manage.py migrate