FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pytest
RUN python src/main.py -f "examples/ex1.txt"