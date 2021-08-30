FROM python:3.10.0rc1-alpine3.14

WORKDIR /project

# Copia as dependencias do projeto
COPY ./src/requirements.txt .

# Instala as dependencias do projeto
RUN pip install -r requirements.txt

# Copia todo o projeto
COPY ./src /project

CMD [ "python", "app.py" ]
