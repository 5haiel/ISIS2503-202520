set -e
python manage.py migrate --noinput
python manage.py collectstatic --noinput
# threads
exec gunicorn provesi.wsgi:application \
  --bind 0.0.0.0:${PORT:-8080} \
  --workers ${WORKERS:-3} \
  --threads ${THREADS:-2} \
  --timeout ${TIMEOUT:-60}