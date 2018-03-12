FROM python:2.7.14-alpine3.7

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 0
# ENV DJANGO_SETTINGS_MODULE project.settings.docker

# copy app
ADD . /Bitcoin_Exchange_Rates
RUN mkdir /Bitcoin_Exchange_Rates/logs
WORKDIR /Bitcoin_Exchange_Rates
# RUN ls -l

# install pip packages
RUN ./bash_scripts/install.sh

# app runs on 8000 port
EXPOSE 8000

# run app
ENTRYPOINT ["sh", "./bash_scripts/start.sh"]
