FROM python

WORKDIR /restApi

COPY . /restApi

COPY requirement.txt .

RUN pip install -r requirement.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
