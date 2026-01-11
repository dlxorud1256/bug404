FROM python:3.14-slim

RUN apt-get update && apt-get install -y \
    wget curl gnupg unzip git locales \
    chromium \
    chromium-driver \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN localedef -f UTF-8 -i ko_KR ko_KR.UTF-8
ENV LC_ALL=ko_KR.UTF-8
ENV LANG=ko_KR.UTF-8
ENV PYTHONIOENCODING=utf-8

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
CMD ["pytest", "tests/e2e", "-s", "--alluredir=allure-results"]