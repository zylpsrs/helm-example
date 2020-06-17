IMAGE_VERSION ?= latest
#REPO_URL_PREFIX ?= registry.ocp.zyl.io/
REPO_URL_PREFIX ?= registry.cn-hangzhou.aliyuncs.com/zylpsrs/example/

HELLO_IMAGE ?= $(REPO_URL_PREFIX)hello:$(IMAGE_VERSION)
GREETER_IMAGE ?= $(REPO_URL_PREFIX)greeter:$(IMAGE_VERSION)

BUILDAH_FORMAT ?= oci

build-hello:
	buildah bud --format $(BUILDAH_FORMAT) --tls-verify=false --layers \
		--pull=false -f hello/Dockerfile -t $(HELLO_IMAGE) hello

build-greeter:
	buildah bud --format $(BUILDAH_FORMAT) --tls-verify=false --layers \
		--pull=false -f greeter/Dockerfile -t $(GREETER_IMAGE) greeter

build:
	make build-hello
	make build-greeter

push:
	buildah push --tls-verify=false $(HELLO_IMAGE) docker://$(HELLO_IMAGE)
	buildah push --tls-verify=false $(GREETER_IMAGE) docker://$(GREETER_IMAGE)

all:
	make build
	make push
