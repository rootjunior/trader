FROM python:3.9.15-bullseye

ARG ENVIRON

WORKDIR /code

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY /services/api/requirements.txt /code/api/requirements.txt
COPY /services/api/dev-requirements.txt /code/api/dev-requirements.txt

RUN if [ "$ENVIRON" = "dev" ]; then \
    pip install --no-cache-dir --upgrade -r /code/api/dev-requirements.txt; \
    else \
    pip install --no-cache-dir --upgrade -r /code/api/requirements.txt; \
    fi

COPY /services/api/ /code/api
COPY /scripts/ /code/scripts/

WORKDIR /code/api

EXPOSE 8000

CMD ["python3", "."]
