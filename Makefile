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

lint: ### Run linting checks
	cd waylay_${SERVICE_NAME}_api && pylint --errors-only src/
	@${printMsg} 'lint ${SERVICE_NAME} api package' 'OK'
	cd waylay_${SERVICE_NAME}_types && pylint --errors-only src/
	@${printMsg} 'lint ${SERVICE_NAME} types package' 'OK'
	pylint --errors-only test/
	@${printMsg} 'lint ${SERVICE_NAME} test package OK'

codestyle: ### Run codestyle checks
	pycodestyle waylay_${SERVICE_NAME}_api/src/
	@${printMsg} 'codestyle ${SERVICE_NAME} api package' 'OK'
	pycodestyle waylay_${SERVICE_NAME}_types/src/
	@${printMsg} 'codestyle ${SERVICE_NAME} types package' 'OK'
	pycodestyle test/
	@${printMsg} 'codestyle ${SERVICE_NAME} test package' 'OK'

typecheck: ### Run type checks
	cd waylay_${SERVICE_NAME}_api/src/ && mypy --namespace-packages -p waylay
	@${printMsg} 'typecheck api package OK'
	cd waylay_${SERVICE_NAME}_types/src/ && mypy --namespace-packages -p waylay
	@${printMsg} 'typecheck types package OK'
	${TEST_QA_PREFIX} mypy test
	@${printMsg} 'typecheck test package' '${TEST_QA_PREFIX} OK'

docstyle: ### Run docstyle checks
	pydocstyle waylay_${SERVICE_NAME}_api/src/
	@${printMsg} 'pydocstyle ${SERVICE_NAME} api package' 'OK'
	pydocstyle waylay_${SERVICE_NAME}_types/src/
	@${printMsg} 'pydocstyle ${SERVICE_NAME} types package' 'OK'
	${TEST_QA_PREFIX} pydocstyle test/
	@${printMsg} 'pydocstyle ${SERVICE_SUBMODULE} test package' '${TEST_QA_PREFIX} OK'

code-qa: codestyle docstyle lint typecheck ### perform code quality checks

ci-code-qa: code-qa ### perform ci code quality checks

dev-install: _install_requirements ### Install the development environment
	pip install -e waylay_${SERVICE_NAME}_api[dev]
	pip install -e waylay_${SERVICE_NAME}_types[dev]

ci-install: _install_requirements ### Install the environment with frozen dependencies
	pip install './waylay_${SERVICE_NAME}_api[dev]'
	pip install './waylay_${SERVICE_NAME}_types[dev]'

_install_requirements:
	pip install --upgrade pip
	pip install -r test-requirements.txt
	pip install -r requirements.txt


test: ### Run unit tests
	pytest test/

format: ### Format code
	pip install autopep8
	autopep8 waylay_${SERVICE_NAME}_api/src
	@${printMsg} 'formatted ${SERVICE_NAME} api package'
	autopep8 waylay_${SERVICE_NAME}_types/src
	@${printMsg} 'formatted ${SERVICE_NAME} types package'
	autopep8 test
	@${printMsg} 'formatted ${SERVICE_NAME} test package'
