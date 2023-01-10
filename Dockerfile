FROM python:3.11-alpine
RUN apk update && \
apk add --no-cache --virtual build-deps gcc python3-dev musl-dev && \
apk add postgresql-dev
ENV APP_DIR="/opt/dim"
ENV RECORDS_DIR="/opt/dim/tests/dummy_files"
RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR
RUN python -m venv $APP_DIR/venv
ENV PATH="$APP_DIR:$PATH"
COPY --chown=1001:1001 . .
RUN pip install -r requirements.txt
USER 1001
ENV PATH="/usr/app/venv/bin:$PATH"
CMD ["pytest"]