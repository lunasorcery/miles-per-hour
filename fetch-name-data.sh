#!/bin/bash
curl -O https://www.ssa.gov/oact/babynames/names.zip
unzip names.zip -d names
rm -f names.zip
