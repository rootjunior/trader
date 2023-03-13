#!/usr/bin/env bash

cd env
for file in *.example
  do cp "$file" "${file/.example/}"
done
