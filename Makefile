printMsg=printf "\033[36m\033[1m%-15s\033[0m\033[36m %-30s\033[0m\n"

.PHONY: help test
## use triple hashes ### to indicate main build targets
help:
	@awk 'BEGIN {FS = ":[^#]*? ### "} /^[a-zA-Z0-9_\-\.]+:[^#]* ### / {printf "\033[1m\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@awk 'BEGIN {FS = ":[^#]*? ## "} /^[a-zA-Z0-9_\-\.]+:[^#]* ## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
.DEFAULT_GOAL := help

SERVICE_NAME=registry

API_FOLDER=waylay_${SERVICE_NAME}_api
API_SRC=${API_FOLDER}/src
TYPES_FOLDER=waylay_${SERVICE_NAME}_types
TYPES_SRC=${TYPES_FOLDER}/src
TEST_FOLDER=test

CMD_FORMAT=ruff format
CMD_FIX=ruff check --fix
CMD_CHECK=ruff check

# disables test QA unless set to empty string
TEST_QA_PREFIX?=echo DISABLED

VENV_DIR=.venv
VENV_ACTIVATE_CMD=${VENV_DIR}/bin/activate
VENV_ACTIVATE=. ${VENV_ACTIVATE_CMD}

${VENV_ACTIVATE_CMD}:
	python3 -m venv ${VENV_DIR}
	${VENV_ACTIVATE} && make exec-dev-install

install: ${VENV_ACTIVATE_CMD}

clean:
	rm -fr ${VENV_DIR}
	rm -fr .*_cache/*

lint: install ### Run linting checks
	@${VENV_ACTIVATE} && make exec-lint

typecheck: install ### Run type checks
	@${VENV_ACTIVATE} && make exec-typecheck

code-qa: install ### perform code quality checks
	@${VENV_ACTIVATE} && make exec-code-qa

test: install ### Run unit tests
	@${VENV_ACTIVATE} && make exec-test

format: install ### Format code
	@${VENV_ACTIVATE} && make exec-format

exec-lint: ### Run linting checks
	cd ${API_FOLDER} && ${CMD_CHECK}
	@${printMsg} 'lint ${API_FOLDER}' 'OK'
	cd ${TYPES_FOLDER} && ${CMD_CHECK}
	@${printMsg} 'lint ${TYPES_FOLDER}' 'OK'
	${CMD_CHECK}
	@${printMsg} 'lint test' 'OK'

exec-typecheck: ### Run type checks
	cd ${API_SRC}/ && mypy --namespace-packages -p waylay
	@${printMsg} 'typecheck api' 'OK'
	cd ${TYPES_SRC}/ && mypy --namespace-packages -p waylay
	@${printMsg} 'typecheck types' 'OK'
	${TEST_QA_PREFIX} mypy ${TEST_FOLDER}
	@${printMsg} 'typecheck test' '${TEST_QA_PREFIX} OK'

exec-test: ### Run unit tests
	pytest ${TEST_FOLDER}

exec-format: ### Format code
	${CMD_FIX} ${API_FOLDER}
	${CMD_FORMAT} ${API_FOLDER}
	@${printMsg} 'format api' 'OK'
	${CMD_FIX} ${TYPES_FOLDER}
	${CMD_FORMAT} ${TYPES_FOLDER}
	@${printMsg} 'format types' 'OK'
	${CMD_FIX} ${TEST_FOLDER}
	${CMD_FORMAT} ${TEST_FOLDER}
	@${printMsg} 'format test' 'OK'

exec-code-qa: exec-lint exec-typecheck ### perform code quality checks

ci-code-qa: exec-code-qa ### perform ci code quality checks

exec-dev-install: _install_requirements ### Install the development environment
	pip install -e ${API_FOLDER}[dev]
	pip install -e ${TYPES_FOLDER}[dev]

ci-install: _install_requirements ### Install the environment with frozen dependencies
	pip install './${API_FOLDER}[dev]'
	pip install './${TYPES_FOLDER}[dev]'

_install_requirements:
	pip install --upgrade pip
	pip install -r requirements.txt
