---
title: Terraform
date: 2016-01-08 15:04:23
category: code-as-infrastructure
tags: []

layout: page
---

HashiCorp Terraform enables you to safely and predictably create, change, and improve infrastructure. It is an open source tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.

## Installation

### macOS

```bash
brew install terraform
```

## Usage

Create a `.env` file with your desired environment variables, that could include the aws credentials, etc.

Example:

```
AWS_ACCESS_KEY_ID=********************
AWS_SECRET_ACCESS_KEY=****************************************
AWS_DEFAULT_REGION=ap-southeast-2

TF_VAR_app_name=example_app
TF_VAR_app_version=1.0.0
TF_VAR_app_env=development
```

### Create Makefile

```
init:
	docker run --rm --env-file=$(shell pwd)/.env --volume=$(shell pwd)/:/src --workdir=/src hashicorp/terraform:light init -force-copy
.PHONY: init

validate:
	docker run --rm --env-file=$(shell pwd)/.env --volume=$(shell pwd)/:/src --workdir=/src hashicorp/terraform:light validate
.PHONY: validate

plan:
	docker run --rm --env-file=$(shell pwd)/.env --volume=$(shell pwd)/:/src --workdir=/src hashicorp/terraform:light plan -input=false
.PHONY: plan

refresh:
	docker run --rm --env-file=$(shell pwd)/.env --volume=$(shell pwd)/:/src --workdir=/src hashicorp/terraform:light refresh -input=false
.PHONY: refresh

apply:
	docker run --rm --env-file $(shell pwd)/.env --volume $(shell pwd)/:/src --workdir /src hashicorp/terraform:light apply -input=false -auto-approve
.PHONY: apply

destroy:
	docker run --rm --env-file=$(shell pwd)/.env --volume=$(shell pwd)/:/src --workdir=/src hashicorp/terraform:light destroy -input=false -auto-approve
.PHONY: destroy

```
