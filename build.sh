set -o errexit
pip install -r requirements.txt
pip install --upgrade pip
pip install --force-reinstall -U setuptools
python
import django
exit()
python manage.py collectstatic --no-input
python manage.py migrate