# GitHub Actions Demonstration Workflows

This repo contains source code to demonstrate how to set various GitHub Actions workflows to monitor code coming into production.

Our [Python CI workflow](./.github/workflows/python_checks.yml) runs `ruff` and `pytest` in two parallel jobs to evaluate our code quality and prevent breaking changes.

Our [Docker CD workflow](./.github/workflows/docker_build.yml) builds and ships a Docker image based on the latest code in `main` when changes are merged.