FROM postgres:16

# Set default environment variables
ENV POSTGRES_USER=pizarrauser
ENV POSTGRES_PASSWORD=pizarrapass
ENV POSTGRES_DB=pizarradb

# Copy initialization scripts
COPY postgres/init.sql /docker-entrypoint-initdb.d/

# Ensure proper permissions
RUN chmod a+r /docker-entrypoint-initdb.d/*


