# PASO1 utilizamos una imagen base de python
FROM python:3.12-slim

# PASO2
WORKDIR /app

# PASO3: copiamos el requirements.txt 
COPY requirements.txt /app

# PASO4 instalar las dependencias
RUN pip install -r requirements.txt

# PASO5 copiamos los archivos del proyecto al contenedor
COPY . /app

# PASO6: ejecutamos la aplicacion
CMD ["python", "app.py"]