FROM python:3.9.2

ENV PYTHONUNBUFFERED 1

RUN mkdir /workspace
WORKDIR /workspace

RUN pip install --upgrade pip==21.0.1

# Install Python dependencies from requirements.txt & development.txt if it exists
COPY requirements.txt requirements.txt* /workspace/
RUN if [ -f "requirements.txt" ]; then pip install --no-cache-dir -r requirements.txt && rm requirements.txt; fi

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*