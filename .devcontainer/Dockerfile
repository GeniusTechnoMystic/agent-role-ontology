FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN apt-get update \
    && apt-get install -y --no-install-recommends git ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && python -m venv /opt/venv

COPY requirements-dev.txt /tmp/requirements-dev.txt
RUN pip install --no-cache-dir -r /tmp/requirements-dev.txt \
    && pip check \
    && rm /tmp/requirements-dev.txt

RUN useradd --create-home --uid 1000 --shell /bin/bash sandbox \
    && mkdir -p /workspaces/agent-role-ontology \
    && chown sandbox:sandbox /workspaces/agent-role-ontology

USER sandbox
WORKDIR /workspaces/agent-role-ontology
CMD ["sleep", "infinity"]
