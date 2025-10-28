FROM agrigorev/zoomcamp-model:2025

RUN pip install uv

WORKDIR /machine_learning_bootcamp/05-deployment/2025/code

ENV PATH="/machine_learning_bootcamp/05-deployment/2025/code/.venv/bin:$PATH"

COPY ".python-version" "pyproject.toml" "uv.lock" "./"
RUN uv sync --locked

COPY "fastapi_model.py" "./"

EXPOSE 9696

ENTRYPOINT ["uvicorn", "fastapi_model:app", "--host", "0.0.0.0", "--port", "9696"]