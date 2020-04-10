
DOCKER ?= docker
HELM ?= helm

PKG_NAME := test/trivia
PKG_VERSION := 1.0.0


.PHONY = all devel prod clean

all: devel prod

devel:
	$(DOCKER) build -t ${PKG_NAME}-backend:dev \
	-f docker/Dockerfile.backend . \
	--no-cache
	$(DOCKER) build -t ${PKG_NAME}-frontend:dev \
	-f docker/Dockerfile.frontend . \
	--no-cache
	$(HELM) install --name trivia-devel \
					--namespace trivia-devel \
					--set backend.image.repository="${PKG_NAME}-backend" \
					--set backend.image.tag="dev" \
					--set frontend.image.repository="${PKG_NAME}-frontend" \
					--set frontend.image.tag="dev" \
					--set autoScale.enabled=false \
					./date-trivia

prod:
	$(DOCKER) build -t ${PKG_NAME}-backend:${PKG_VERSION} \
					-f docker/Dockerfile.backend . \
					--no-cache
	$(DOCKER) build -t ${PKG_NAME}-frontend:${PKG_VERSION} \
					-f docker/Dockerfile.frontend . \
					--no-cache
	$(HELM) install --name trivia \
					--namespace trivia \
					--set backend.image.repository="${PKG_NAME}-backend" \
					--set backend.image.tag="${PKG_VERSION}" \
					--set frontend.image.repository="${PKG_NAME}-frontend" \
					--set frontend.image.tag="${PKG_VERSION}" \
					--set autoScale.enabled=true \
					./date-trivia

clean:
	@-$(HELM) delete --purge trivia-devel
	@-$(HELM) delete --purge trivia
	@-$(DOCKER) rmi -f ${PKG_NAME}-backend:dev
	@-$(DOCKER) rmi -f ${PKG_NAME}-frontend:dev
	@-$(DOCKER) rmi -f ${PKG_NAME}-backend:${PKG_VERSION}
	@-$(DOCKER) rmi -f ${PKG_NAME}-frontend:${PKG_VERSION}
