#!/bin/bash

./scanner $1 intermediate_tokens.txt
python3.7 parser_lr1.py