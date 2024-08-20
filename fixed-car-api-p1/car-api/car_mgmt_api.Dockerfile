FROM python:3.10 as car-mgmt-api


WORKDIR /var/www/html/car_mgmt_api

# Copy dependencies
COPY . ./

# Install requirements
RUN pip install -r requirements.txt

# Run application
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--reload"]
