PROJECT_NAME = video_markup
TEST_FOLDER_NAME = tests
PYTHON_VERSION = 3.12

test-ci: ##@Test Run tests with pytest and coverage in CI
	pytest ./$(TEST_FOLDER_NAME) --junitxml=./junit.xml --cov=./$(PROJECT_NAME) --cov-report=xml

lint-ci: ruff-ci mypy-ci ##@Linting Run all linters in CI

ruff-ci: ##@Linting Run ruff
	ruff check ./$(PROJECT_NAME)

mypy-ci: ##@Linting Run mypy
	mypy --config-file ./pyproject.toml ./$(PROJECT_NAME)

develop: clean_dev ##@Develop Create virtualenv
	python$(PYTHON_VERSION) -m venv .venv
	.venv/bin/pip install -U pip poetry
	.venv/bin/poetry config virtualenvs.create false
	.venv/bin/poetry install
	.venv/bin/pre-commit install

local: ##@Develop Run dev containers for test
	docker compose -f docker-compose.dev.yaml up --force-recreate --renew-anon-volumes --build

local_down: ##@Develop Stop dev containers with delete volumes
	docker compose -f docker-compose.dev.yaml down -v


alembic_init: ##@Database Run alembic init for async
	.venv/bin/alembic init -t async ./$(PROJECT_NAME)/adapters/database/migrations

clean_dev: ##@Develop Remove virtualenv
	rm -rf .venv
