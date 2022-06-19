FROM python:3.10 as deps
WORKDIR /app
ADD pyproject.toml requirements.txt requirements-prod.txt setup.cfg ./
RUN mkdir -p /deps && pip wheel --wheel-dir /deps -r requirements.txt -r requirements-prod.txt

FROM python:3.10
WORKDIR /app
COPY --from=deps /deps /deps
ADD pyproject.toml requirements.txt requirements-prod.txt setup.cfg ./
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/81b1373f17855a4dc21156cfe1694c31d7d1792e/wait-for-it.sh scripts/wait-for-it.sh
RUN pip install --no-cache --find-links=/deps -r requirements.txt -r requirements-prod.txt
COPY . ./
RUN chmod 755 scripts/*.sh
USER 1000

ENTRYPOINT ["scripts/docker-entrypoint.sh"]
CMD ["uwsgi", "--http", "0.0.0.0:8000", "--module", "gentry.wsgi", "--master", "--workers", "3", "--enable-threads", "--disable-logging"]
