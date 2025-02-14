APP_NAME=iris

run-local:
	python -m $(APP_NAME)

PHONY: build publish

build:
	docker build --platform linux/amd64 --platform linux/arm64/v8 -t docker.yesidlopez.de/$(APP_NAME):$(VERSION) .

publish: build
publish:
	docker push docker.yesidlopez.de/$(APP_NAME):$(VERSION)

PHONY: update-image-version release publish-with-chart

update-image-version:
	sed -i '' 's/tag: ".*"/tag: "$(VERSION)"/' ./chart/values.yaml

publish-with-chart: publish update-image-version

# Local
deps:
	poetry install

.PHONY: clean-pycache
clean-pycache: ## Clean up pycache files
	find . -name '.mypy_cache' -exec rm -rf {} +
	find . -name '.ruff_cache' -exec rm -rf {} +
	find . -name '.pytest_cache' -exec rm -rf {} +
	find . -name '__pycache__' -exec rm -rf {} +
