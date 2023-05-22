#include <stdio.h>
#include <iostream>
#include <string>
#include <ctype.h>
#include <list>
#include <fstream>
#include "scanner.h"


std::string token_to_string(TOKEN t) {
	const char* LexicalTypeStr[] = {
    "INT", "MAIN", "VOID", "BREAK",
    "DO", "ELSE", "IF", "WHILE",
    "RETURN", "READ", "WRITE",
    "LBRACE", "RBRACE", "LSQUARE", "RSQUARE",
    "LPAR", "RPAR", "SEMI", "PLUS", 
    "MINUS", "MUL_OP", "DIV_OP", "AND_OP",
    "OR_OP", "NOT_OP", "ASSIGN", "LT",
    "GT", "SHL_OP", "SHR_OP", "EQ",
    "NOTEQ", "LTEQ", "GTEQ", "ANDAND",
    "OROR", "COMMA",
    "INT_NUM", "ID", "_EOF", "UNKNOWN"
	};
	std::string res;
	res = LexicalTypeStr[t];
	return res;
}


Scanner::Scanner(const char* path){
    EOF_flag = false;
    buffer = "";
    error_buffer = "";
    open_file(path);
    printf("lexical scanner initialized successfully\n");
}

Scanner::~Scanner(){
    if(src.is_open()){
        src.close();
    }
}

void Scanner::print_output(){
    std::list<std::pair<TOKEN,std::string>>::iterator iter;
    std::string t;
    std::string value;
    for(iter = result.begin(); iter != result.end(); iter++){
        t = token_to_string(iter->first);
        value = iter->second;
        printf("Token: %8s , \t val: %5s\n",t.c_str(),value.c_str());
    }
}

void Scanner::save_output_to_file(const char *file_name){
    std::ofstream fout;
	fout.open(file_name);
    if (!fout.is_open()) {
		std::cerr << "file " << file_name << " open error" << std::endl;
		return;
	}
    std::list<std::pair<TOKEN,std::string>>::iterator iter;
    std::string t;
    std::string value;
    for(iter = result.begin(); iter != result.end(); iter++){
        t = token_to_string(iter->first);
        value = iter->second;
        fout<<t.c_str()<< " | " <<value <<std::endl;
    }
    fout.close();
}

void Scanner::open_file(const char* path){
    src.open(path);
    if(!src.is_open()){
        std::cerr << "file " << path << " open error" << std::endl;
		exit(-1);
    }
}

char Scanner::get_next_char(){
    char c;
    c = src.get();
    if(src.eof()){
        EOF_flag = true;
    }
    return c;

}

void Scanner::unget_next_char(){
    src.unget();
}


char Scanner::peek_next_char(){
    char c;
    c = src.peek();
    if(src.eof()){
        EOF_flag = true;
        return ' ';
    }
    return c;
}


std::pair<TOKEN,std::string> Scanner::get_next_token(){
    //get the first char (auto skip blank space,\n,\t)
    std::pair<TOKEN,std::string> ans;
    char c = get_next_char();
    while((c==' '||c=='\n'||c=='\t')&&EOF_flag==false){
        c = get_next_char();
    }
    if(EOF_flag){
        ans.first = TOKEN(_EOF);
        ans.second = "X";
        printf("reach EOF, stop scanning\n");
        return ans;
    }
    buffer += c;
    // single token case (they are unique, no further token based on them)
    switch (c)
    {
        case '{':
            ans.first = TOKEN(LBRACE);
            ans.second = buffer;
            return ans;
            break;
        case '}':
            ans.first = TOKEN(RBRACE);
            ans.second = buffer;
            return ans;
            break;
        case '[':
            ans.first = TOKEN(LSQUARE);
            ans.second = buffer;
            return ans;
            break;
        case ']':
            ans.first = TOKEN(RSQUARE);
            ans.second = buffer;
            return ans;
            break;
        case '(':
            ans.first = TOKEN(LPAR);
            ans.second = buffer;
            return ans;
            break;
        case ')':
            ans.first = TOKEN(RPAR);
            ans.second = buffer;
            return ans;
            break;
        case ';':
            ans.first = TOKEN(SEMI);
            ans.second = buffer;
            return ans;
            break;
        case '+':
            ans.first = TOKEN(PLUS);
            ans.second = buffer;
            return ans;
            break;
        case '-':
            ans.first = TOKEN(MINUS);
            ans.second = buffer;
            return ans;
            break;
        case '*':
            ans.first = TOKEN(MUL_OP);
            ans.second = buffer;
            return ans;
            break;
        case '/':
            ans.first = TOKEN(DIV_OP);
            ans.second = buffer;
            return ans;
            break;
        case ',':
            ans.first = TOKEN(COMMA);
            ans.second = buffer;
            return ans;
            break; 
        default:
            break;
    }

    // multiple token case (e.g. &,&&)
    switch (buffer[0])
    {
        case '&':
            c = get_next_char();
            buffer += c;
            if(buffer[1]=='&'){
                ans.first = TOKEN(ANDAND);
                ans.second = buffer;
                return ans;
            }
            unget_next_char();
            buffer = buffer.substr(0,buffer.length()-1);
            ans.first = TOKEN(AND_OP);
            ans.second = buffer;
            return ans;
            break;
        case '|':
            c = get_next_char();
            buffer += c;
            if(buffer[1]=='|'){
                ans.first = TOKEN(OROR);
                ans.second = buffer;
                return ans;
            }
            unget_next_char();
            buffer = buffer.substr(0,buffer.length()-1);
            ans.first = TOKEN(OR_OP);
            ans.second = buffer;
            return ans;
            break;
        case '!':
            c = get_next_char();
            buffer += c;
            if(buffer[1]=='='){
                ans.first = TOKEN(NOTEQ);
                ans.second = buffer;
                return ans;
            }
            unget_next_char();
            buffer = buffer.substr(0,buffer.length()-1);
            ans.first = TOKEN(NOT_OP);
            ans.second = buffer;
            return ans;
            break;
        case '=':
            c = get_next_char();
            buffer += c;
            if(buffer[1]=='='){
                ans.first = TOKEN(EQ);
                ans.second = buffer;
                return ans;
            }
            unget_next_char();
            buffer = buffer.substr(0,buffer.length()-1);
            ans.first = TOKEN(ASSIGN);
            ans.second = buffer;
            return ans;
            break;
        case '<':
            c = get_next_char();
            buffer += c;
            if(buffer[1]=='='){
                ans.first = TOKEN(LTEQ);
                ans.second = buffer;
                return ans;
            }
            else if(buffer[1]=='<'){
                ans.first = TOKEN(SHL_OP);
                ans.second = buffer;
                return ans;
            }
            unget_next_char();
            buffer = buffer.substr(0,buffer.length()-1);
            ans.first = TOKEN(LT);
            ans.second = buffer;
            return ans;
            break;
        case '>':
            c = get_next_char();
            buffer += c;
            if(buffer[1]=='='){
                ans.first = TOKEN(GTEQ);
                ans.second = buffer;
                return ans;
            }
            else if(buffer[1]=='>'){
                ans.first = TOKEN(SHR_OP);
                ans.second = buffer;
                return ans;
            }
            unget_next_char();
            buffer = buffer.substr(0,buffer.length()-1);
            ans.first = TOKEN(GT);
            ans.second = buffer;
            return ans;
            break;      
        default:
            break;
    }

    //INT_NUM case:
    if(isdigit(buffer[0])){
        c = get_next_char();
        while(isdigit(c)&&EOF_flag==false){
            buffer += c;
            c = get_next_char();
        }
        unget_next_char();
        ans.first = TOKEN(INT_NUM);
        ans.second = buffer;
        return ans;
    }

    //ID case:
    else if(isalpha(buffer[0])){
        c = get_next_char();
        while((isdigit(c)||isalpha(c)||c=='_')&&EOF_flag==false){
            buffer += c;
            c = get_next_char();
        }
        unget_next_char();
        //ID sub cases: check reserved words
        if(buffer=="int"){
            ans.first = TOKEN(INT);
            ans.second = buffer;
            return ans;
        }
        else if(buffer=="main"){
            ans.first = TOKEN(MAIN);
            ans.second = buffer;
            return ans;
        }
        else if(buffer=="void"){
            ans.first = TOKEN(VOID);
            ans.second = buffer;
            return ans;
        }
        else if(buffer=="break"){
            ans.first = TOKEN(BREAK);
            ans.second = buffer;
            return ans;
        }
        else if(buffer=="do"){
            ans.first = TOKEN(DO);
            ans.second = buffer;
            return ans;
        }
        else if(buffer=="else"){
            ans.first = TOKEN(ELSE);
            ans.second = buffer;
            return ans;
        }
        else if(buffer=="if"){
            ans.first = TOKEN(IF);
            ans.second = buffer;
            return ans;
        }
        else if(buffer=="while"){
            ans.first = TOKEN(WHILE);
            ans.second = buffer;
            return ans;
        }
        else if(buffer=="return"){
            ans.first = TOKEN(RETURN);
            ans.second = buffer;
            return ans;
        }
        else if(buffer=="scanf"){
            ans.first = TOKEN(READ);
            ans.second = buffer;
            return ans;
        }
        else if(buffer=="printf"){
            ans.first = TOKEN(WRITE);
            ans.second = buffer;
            return ans;
        }
        else{
            ans.first = TOKEN(ID);
            ans.second = buffer;
            return ans;
        }
        
    }

    //error case:
    else{
        ans.first = TOKEN(UNKNOWN);
        ans.second = buffer;
        return ans;
        printf("UNKNOWN TOKEN\n");
    }
    
}


void Scanner::lexical_analysis(){
    while(EOF_flag==false){
        std::pair<TOKEN,std::string> t = get_next_token();
        // TOKEN t = get_next_token();
        if(t.first != _EOF){
            result.push_back(t);
        }
        buffer = "";
        error_buffer = "";
    }
    printf("lexical analysis complete\n");
}




int main(int argc, char const *argv[]){
    printf("hello\n");
    Scanner *S = new Scanner(argv[1]);
    S->lexical_analysis();
    S->print_output();
    S->save_output_to_file(argv[2]);
    return 0;
}


