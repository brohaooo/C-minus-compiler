# C-minus-compiler
a compiler generate MIPS code for C language, final project of CSC4180

## What is it
A compiler which takes C source codes as input and generate MIPS codes as output.

1. scanner (implemented by c++)
2. parser (implemented by python)
3. code generator (implemented by python, embedded in parser's reduction process)

## about scanner

It reads a file and output a token list stored in intermediate_tokens.txt.

## about parser

It is based on LR(1) parsing, meaning that it will generate an LR(1) parsing table to fulfill its job.
The reason that I use python in this part is that actually I referred an LR(1) project and adapted from it: https://github.com/LiuChangFreeman/C--Compiler
which is written in python. (also, writing in C++ is not easy)

## How to use
The dockerfile is given, illustrated the required environment (c++, python3.7),
you can compile it either in windows (run run_compiler.bat) or in linux (run Makefile)
then use the command
  ./run_compiler.bat \$testfile
  or
  ./run_compiler.sh \$testfile
to see the result. The result MIPS codes are also store in the output.txt file.

## some issues
This c-compiler is extremely inefficient because it will store all the temporary values (during expression calculation process) on the stack
instead of using registers. But it works fine and gets rid of the register-allocation problem (e.g., run out of registers in exp+(exp+(exp+...))) case)
To do that, I manually set up \$FP and \$SP at the beginning of the MIPS program.

## final score:
106/110 (96 + 10 bonus, failed one test case)
