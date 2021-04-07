FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

RUN pip install --upgrade pip

# Install Python dependencies from requirements.txt & development.txt if it exists
COPY requirements.txt requirements.txt* /usr/src/app/
RUN if [ -f "requirements.txt" ]; then pip install --no-cache-dir -r requirements.txt && rm requirements.txt; fi

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

COPY . /usr/src/app/