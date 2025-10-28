FROM python:3.12.1-slim-bookworm

RUN pip install uv

# Copy the 'uv' and 'uvx' executables from the latest uv image into /bin/ in this image
# 'uv' is a fast Python package installer and environment manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /machine_learning_bootcamp/05-deployment/2024/code

ENV PATH="/machine_learning_bootcamp/05-deployment/2024/code/.venv/bin:$PATH"

COPY ".python-version" "pyproject.toml" "uv.lock" "./"
RUN uv sync --locked

COPY "predict.py" "model.bin" "./"

EXPOSE 9696

ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]