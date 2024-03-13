# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./api /code/api

# 
CMD ["uvicorn", "api.main:api", "--reload","--host", "0.0.0.0", "--port", "3000"]