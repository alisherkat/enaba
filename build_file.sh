# build_files.sh

pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic 
