printMsg=printf "\033[36m\033[1m%-15s\033[0m\033[36m %-30s\033[0m\n"

.PHONY: help test
## use triple hashes ### to indicate main build targets
help:
	@awk 'BEGIN {FS = ":[^#]*? ### "} /^[a-zA-Z0-9_\-\.]+:[^#]* ### / {printf "\033[1m\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@awk 'BEGIN {FS = ":[^#]*? ## "} /^[a-zA-Z0-9_\-\.]+:[^#]* ## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
.DEFAULT_GOAL := help

SERVICE_NAME=registry

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

lint: install ### Run linting checks
	@${VENV_ACTIVATE} && make exec-lint

codestyle: install ### Run codestyle checks
	@${VENV_ACTIVATE} && make exec-codestyle

typecheck: install ### Run type checks
	@${VENV_ACTIVATE} && make exec-typecheck

docstyle: install ### Run docstyle checks
	@${VENV_ACTIVATE} && make exec-docstyle

code-qa: install ### perform code quality checks
	@${VENV_ACTIVATE} && make exec-code-qa

test: install ### Run unit tests
	@${VENV_ACTIVATE} && make exec-test

format: install ### Format code
	@${VENV_ACTIVATE} && make exec-format


exec-lint: ### Run linting checks
	cd waylay_${SERVICE_NAME}_api && pylint --errors-only src/
	@${printMsg} 'lint waylay_${SERVICE_NAME}_api' 'OK'
	cd waylay_${SERVICE_NAME}_types && pylint --errors-only src/
	@${printMsg} 'lint waylay_${SERVICE_NAME}_types' 'OK'
	pylint --errors-only test/
	@${printMsg} 'lint test' 'OK'

exec-codestyle: ### Run codestyle checks
	pycodestyle waylay_${SERVICE_NAME}_api/src/
	@${printMsg} 'codestyle waylay_${SERVICE_NAME}_api' 'OK'
	pycodestyle waylay_${SERVICE_NAME}_types/src/
	@${printMsg} 'codestyle waylay_${SERVICE_NAME}_types' 'OK'
	pycodestyle test/
	@${printMsg} 'codestyle test' 'OK'

exec-typecheck: ### Run type checks
	cd waylay_${SERVICE_NAME}_api/src/ && mypy --namespace-packages -p waylay
	@${printMsg} 'typecheck api package' 'OK'
	cd waylay_${SERVICE_NAME}_types/src/ && mypy --namespace-packages -p waylay
	@${printMsg} 'typecheck types package' 'OK'
	${TEST_QA_PREFIX} mypy test
	@${printMsg} 'typecheck test package' '${TEST_QA_PREFIX} OK'

exec-docstyle: ### Run docstyle checks
	pydocstyle waylay_${SERVICE_NAME}_api/src/
	@${printMsg} 'pydocstyle waylay_${SERVICE_NAME}_types' 'OK'
	pydocstyle waylay_${SERVICE_NAME}_types/src/
	@${printMsg} 'pydocstyle waylay_${SERVICE_NAME}_types' 'OK'
	${TEST_QA_PREFIX} pydocstyle test/
	@${printMsg} 'pydocstyle test' '${TEST_QA_PREFIX} OK'

exec-test: ### Run unit tests
	pytest test/

exec-format: ### Format code
	pip install autopep8
	autopep8 waylay_${SERVICE_NAME}_api/src
	@${printMsg} 'format waylay_${SERVICE_NAME}_api' 'OK'
	autopep8 waylay_${SERVICE_NAME}_types/src
	@${printMsg} 'format waylay_${SERVICE_NAME}_types' 'OK'
	autopep8 test
	@${printMsg} 'format test package' 'OK'

exec-code-qa: exec-codestyle exec-docstyle exec-lint exec-typecheck ### perform code quality checks

ci-code-qa: exec-code-qa ### perform ci code quality checks

exec-dev-install: _install_requirements ### Install the development environment
	pip install -e waylay_${SERVICE_NAME}_api[dev]
	pip install -e waylay_${SERVICE_NAME}_types[dev]

ci-install: _install_requirements ### Install the environment with frozen dependencies
	pip install './waylay_${SERVICE_NAME}_api[dev]'
	pip install './waylay_${SERVICE_NAME}_types[dev]'

_install_requirements:
	pip install --upgrade pip
	pip install -r test-requirements.txt
	pip install -r requirements.txt
