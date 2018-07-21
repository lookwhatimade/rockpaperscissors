# Use the lastest python version
FROM python:latest

# set /app as your working directory
WORKDIR /app

# copy everything from your local directory to the app
COPY . /app

ENV NAME rockpaperscissors

# use python3 to run your rock paper scissors app
CMD [ "python3", "./rockpaperscissors.py" ]