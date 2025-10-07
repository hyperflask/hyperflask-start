FROM nikolaik/python-nodejs:python3.13-nodejs24 AS build

ADD . /app
WORKDIR /app
RUN uv sync && npm install
RUN uv run hyperflask build
RUN mkdir -p _site
RUN uv export --frozen --no-hashes > requirements.txt

FROM python:3.13-slim

RUN apt update && apt install -y git
ADD . /app
WORKDIR /app

RUN --mount=type=bind,from=build,source=/app/requirements.txt,target=/tmp/requirements.txt \
    pip install -r /tmp/requirements.txt

COPY --from=build /app/app/assets.json /app/app/assets.json
COPY --from=build /app/public /app/public
COPY --from=build /app/_site /app/_site

VOLUME ["/app/database", "/app/_site"]
EXPOSE 5000
EXPOSE 5500

ENTRYPOINT ["hyperflask"]
CMD ["run", "--init-db", "--host", "0.0.0.0"]
