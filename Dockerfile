FROM python:3.11-alpine
RUN apk update && \
apk add --no-cache --virtual build-deps gcc python3-dev musl-dev && \
apk add postgresql-dev
ENV APP_DIR="/opt/dim"
ENV RECORDS_DIR="/opt/dim/records"
RUN mkdir -p $APP_DIR $RECORDS_DIR
WORKDIR $APP_DIR
RUN python -m venv $APP_DIR/venv
ENV PATH="$APP_DIR:$PATH"
COPY . .
RUN chown -R 1001:1001 .
RUN pip install -r requirements.txt
USER 1001
ENV PATH="/usr/app/venv/bin:$PATH"
CMD ["python", "main.py"]