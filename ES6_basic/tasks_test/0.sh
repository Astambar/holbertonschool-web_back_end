#!/bin/bash

# Capture the output of the script
output=$(node 0-main.js)

# Test taskFirst
expected_taskFirst="I prefer const when I can."
if [[ "$output" == *"$expected_taskFirst"* ]]; then
    echo "taskFirst test passed"
else
    echo "taskFirst test failed"
fi

# Test taskNext
expected_taskNext="But sometimes let is okay"
if [[ "$output" == *"$expected_taskNext"* ]]; then
    echo "taskNext test passed"
else
    echo "taskNext test failed"
fi
