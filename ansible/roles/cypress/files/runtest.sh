#!/bin/bash
set -e

# Usage: ./runtest.sh my_test.cy.js

TEST_FILE=${1:-"hello_world.cy.js"}  # default test if no argument

# Path to your Cypress tests on the host
HOST_TESTS_PATH="/actions-runner/files/cypress"

docker run --rm \
  -v "${HOST_TESTS_PATH}:/e2e" \
  -w /e2e \
  cypress/included:latest \
  npx cypress run --spec "${TEST_FILE}"
