FROM --platform=$BUILDPLATFORM python:3.10-alpine
EXPOSE 8000
WORKDIR /app

# Install dependencies
RUN apk update && apk add \
    gcc \
    musl-dev \
    bash \
    mariadb-dev \
    mariadb-connector-c-dev \ 
    python3-dev \
    nodejs \
    npm \
    && rm -rf /var/cache/apk/*

# Install cnpm with China registry
RUN npm install -g cnpm --registry=https://registry.npmmirror.com

# Copy package files
COPY package*.json ./

# Install dependencies using cnpm
RUN cnpm install

# Install Python dependencies
COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

RUN cnpm run build && \
    rm -rf Docker && \
    rm -f db.sqlite3

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"] 