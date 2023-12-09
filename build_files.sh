# build_files.sh
apt-get update
apt-get install -y libpq-dev  # Install libpq-dev to get pg_config
pip install -r requirements.txt
python3 manage.py collectstatic --noinput
