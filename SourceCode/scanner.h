#pragma once
#include <stdio.h>
#include <iostream>
#include <string>
#include <ctype.h>
#include <list>
#include <fstream>

typedef enum 
{
	// Keywords
    INT, MAIN, VOID, BREAK,
    DO, ELSE, IF, WHILE,
    RETURN, READ, WRITE,
    // Special Symbols 
    LBRACE, RBRACE, LSQUARE, RSQUARE,
    LPAR, RPAR, SEMI, PLUS, 
    MINUS, MUL_OP, DIV_OP, AND_OP,
    OR_OP, NOT_OP, ASSIGN, LT,
    GT, SHL_OP, SHR_OP, EQ,
    NOTEQ, LTEQ, GTEQ, ANDAND,
    OROR, COMMA,
    // INT_NUM & ID
    INT_NUM, ID,
    // two token I defined
    _EOF,UNKNOWN

} TOKEN;


class Scanner {
    private:
        // file-reading stream
        std::ifstream src;
        // temporary buffer for current token, will refresh when current token is recognized
        std::string buffer;
        // if a token is satisfied in the buffer and it might suit longer tokens, use these
        // two data to store the current token in case not fitting longer tokens
        int sub_token_length;
        TOKEN sub_token;
        // temporary error buffer, help store a continuous unknown string
        std::string error_buffer;
        // result list, stores all the tokens in order
        std::list<std::pair<TOKEN,std::string>> result;
        // when get_next_char() reaches eof, turn this flag as true.
        bool EOF_flag;
        // open the input file via ifstream 'src'
        void open_file(const char* path);
        // get the next char 
        char get_next_char();
        // unget the next char 
        void unget_next_char();
        // peek the next char
        char peek_next_char();
        std::pair<TOKEN,std::string> get_next_token();
    public:
        Scanner(const char* path);
        ~Scanner();
        void lexical_analysis();
        void print_output();
        void save_output_to_file(const char *file_name);
};