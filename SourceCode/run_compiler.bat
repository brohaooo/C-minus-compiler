g++ -o scanner scanner.cpp

.\scanner.exe TestCases_compiler\test5.c1 intermediate_tokens.txt
python parser_lr1.py