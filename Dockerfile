# Použijme oficiální Python 3.11 slim image
FROM python:3.11-slim

# Nastavení prostředí
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Nastav pracovní adresář
WORKDIR /app

# Zkopíruj requirements.txt a nainstaluj závislosti
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Zkopíruj celý projekt do kontejneru
COPY . /app/

# Spusť collectstatic (pokud používáš whitenoise a máš nastaven STATIC_ROOT)
RUN python manage.py collectstatic --noinput

# Definuj příkaz, který se spustí při startu kontejneru
CMD ["gunicorn", "jacketHM.wsgi:application", "--bind", "0.0.0.0:8000"]
