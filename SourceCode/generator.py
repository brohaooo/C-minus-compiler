# 这只能硬编码吧，好像没啥用
# from parser_lr1 import production_group

# register ref: https://blog.csdn.net/wbwwf8685/article/details/53762908
register_map = ["$t0","$t1","$t2","$t3","$t4","$t5",
                "$t6","$t7","$t7","$t8","$t9"]

register_occupancy = {"$t0":True,"$t1":True,"$t2":True,"$t3":True,"$t4":True,"$t5":True,
                "$t6":True,"$t7":True,"$t7":True,"$t8":True,"$t9":True}


ID_address_map = {}
FP = 268468224
SP = 268468224
CURRENT_LABEL_ID = 0
CURRENT_ID_ADDRESS = FP;



def production_case(production_string,reduction_list):

    if production_string == "S->program ,['#']":
        program_val = reduction_list[0]['NT_vals']
        return S__to__program(program_val)
    
    elif production_string == "program->external_declarations statement_list ,['#']":
        external_declarations_val = reduction_list[0]['NT_vals']
        statement_list_val = reduction_list[1]['NT_vals']
        return program__to__external_declarations_statement_list(external_declarations_val,statement_list_val)
    

    elif production_string == "external_declarations->declaration external_declarations ,['#']":
        declaration_val = reduction_list[0]['NT_vals']
        external_declarations_val = reduction_list[1]['NT_vals']
        return external_declarations__to__declaration_external_declarations(declaration_val,external_declarations_val)
    

    elif production_string == "external_declarations->$ ,['#']":
        return external_declarations__to__empty()
    
    
    elif production_string == "statement_list->statement statement_list ,['#']":
        statement_val = reduction_list[0]['NT_vals']
        statement_list_val = reduction_list[1]['NT_vals']
        return statement_list__to__statement_statement_list(statement_val,statement_list_val)
    

    elif production_string == "statement_list->$ ,['#']":
        return statement_list__to__empty()
    

    elif production_string == "operator_1->MUL_OP ,['#']":
        return operator_1__to__MUL_OP()
    

    elif production_string == "operator_1->DIV_OP ,['#']":
        return operator_1__to__DIV_OP()
    

    elif production_string == "operator_2->PLUS ,['#']":
        return operator_2__to__PLUS()
    

    elif production_string == "operator_2->MINUS ,['#']":
        return operator_2__to__MINUS()
    

    elif production_string == "operator_3->SHL_OP ,['#']":
        return operator_3__to__SHL_OP()
    

    elif production_string == "operator_3->SHR_OP ,['#']":
        return operator_3__to__SHR_OP()
    

    elif production_string == "operator_4->LT ,['#']":
        return operator_4__to__LT()
    

    elif production_string == "operator_4->GT ,['#']":
        return operator_4__to__GT()
    

    elif production_string == "operator_4->LTEQ ,['#']":
        return operator_4__to__LTEQ()
    

    elif production_string == "operator_4->GTEQ ,['#']":
        return operator_4__to__GTEQ()
    

    elif production_string == "operator_4->EQ ,['#']":
        return operator_4__to__EQ()
    

    elif production_string == "operator_4->NOTEQ ,['#']":
        return operator_4__to__NOTEQ()
    

    elif production_string == "operator_5->AND_OP ,['#']":
        return operator_5__to__AND_OP()
    

    elif production_string == "operator_5->OR_OP ,['#']":
        return operator_5__to__OR_OP()
    

    elif production_string == "operator_6->ANDAND ,['#']":
        return operator_6__to__ANDAND()
    

    elif production_string == "operator_6->OROR ,['#']":
        return operator_6__to__OROR()
    

    elif production_string == "primary_expression->ID ,['#']":
        ID = reduction_list[0]
        return primary_expression__to__ID(ID)
    

    elif production_string == "primary_expression->INT_NUM ,['#']":
        INT_NUM = reduction_list[0]
        return primary_expression__to__INT_NUM(INT_NUM)
    

    elif production_string == "primary_expression->LPAR expression RPAR ,['#']":
        expression_vals = reduction_list[1]['NT_vals']
        return primary_expression__to__LPAR_expression_RPAR(expression_vals)
    

    elif production_string == "primary_expression->ID LSQUARE primary_expression RSQUARE ,['#']":
        ID = reduction_list[0]
        primary_expression_vals = reduction_list[2]['NT_vals']
        return primary_expression__to__ID_LSQUARE_primary_expression_RSQUARE(ID,primary_expression_vals)
    

    elif production_string == "expression->logic_expression ,['#']":
        logic_expression_vals = reduction_list[0]['NT_vals']
        return expression__to__logic_expression(logic_expression_vals)
    

    elif production_string == "logic_expression->logic_expression operator_6 bit_expression ,['#']":
        logic_expression_vals = reduction_list[0]['NT_vals']
        bit_expression_vals = reduction_list[2]['NT_vals']
        operator_6_vals = reduction_list[1]['NT_vals']
        return logic_expression__to__logic_expression_operator_6_bit_expression(logic_expression_vals,bit_expression_vals,operator_6_vals)
    

    elif production_string == "logic_expression->bit_expression ,['#']":
        bit_expression_vals = reduction_list[0]['NT_vals']
        return logic_expression__to__bit_expression(bit_expression_vals)
    
    
    elif production_string == "bit_expression->bit_expression operator_5 cmp_expression ,['#']":
        bit_expression_vals = reduction_list[0]['NT_vals']
        cmp_expression_vals = reduction_list[2]['NT_vals']
        operator_5_vals = reduction_list[1]['NT_vals']
        return bit_expression__to__bit_expression_operator_5_cmp_expression(bit_expression_vals,cmp_expression_vals,operator_5_vals)
    

    elif production_string == "bit_expression->NOT_OP cmp_expression ,['#']":
        cmp_expression_vals = reduction_list[1]['NT_vals']
        return bit_expression__to__NOT_OP_cmp_expression(cmp_expression_vals)
    

    elif production_string == "bit_expression->cmp_expression ,['#']":
        cmp_expression_vals = reduction_list[0]['NT_vals']
        return bit_expression__to__cmp_expression(cmp_expression_vals)
    

    elif production_string == "cmp_expression->cmp_expression operator_4 shi_expression ,['#']":
        cmp_expression_vals = reduction_list[0]['NT_vals']
        shi_expression_vals = reduction_list[2]['NT_vals']
        operator_4_vals = reduction_list[1]['NT_vals']
        return cmp_expression__to__cmp_expression_operator_4_shi_expression(cmp_expression_vals,shi_expression_vals,operator_4_vals)
    

    elif production_string == "cmp_expression->shi_expression ,['#']":
        shi_expression_vals = reduction_list[0]['NT_vals']
        return cmp_expression__to__shi_expression(shi_expression_vals)
    

    elif production_string == "shi_expression->shi_expression operator_3 add_expression ,['#']":
        shi_expression_vals = reduction_list[0]['NT_vals']
        add_expression_vals = reduction_list[2]['NT_vals']
        operator_3_vals = reduction_list[1]['NT_vals']
        return shi_expression__to__shi_expression_operator_3_add_expression(shi_expression_vals,add_expression_vals,operator_3_vals)
    

    elif production_string == "shi_expression->add_expression ,['#']":
        add_expression_vals = reduction_list[0]['NT_vals']
        return shi_expression__to__add_expression(add_expression_vals)
    

    elif production_string == "add_expression->add_expression operator_2 mul_expression ,['#']":
        add_expression_vals = reduction_list[0]['NT_vals']
        mul_expression_vals = reduction_list[2]['NT_vals']
        operator_2_vals = reduction_list[1]['NT_vals']
        return add_expression__to__add_expression_operator_2_mul_expression(add_expression_vals,mul_expression_vals,operator_2_vals)
    

    elif production_string == "add_expression->MINUS mul_expression ,['#']":
        mul_expression_vals = reduction_list[1]['NT_vals']
        return add_expression__to__MINUS_mul_expression(mul_expression_vals)
    

    elif production_string == "add_expression->mul_expression ,['#']":
        mul_expression_vals = reduction_list[0]['NT_vals']
        return add_expression__to__mul_expression(mul_expression_vals)
    

    elif production_string == "mul_expression->mul_expression operator_1 primary_expression ,['#']":
        mul_expression_vals = reduction_list[0]['NT_vals']
        primary_expression_vals = reduction_list[2]['NT_vals']
        operator_1_vals = reduction_list[1]['NT_vals']
        return mul_expression__to__mul_expression_operator_1_primary_expression(mul_expression_vals,primary_expression_vals,operator_1_vals)
    

    elif production_string == "mul_expression->primary_expression ,['#']":
        primary_expression_vals = reduction_list[0]['NT_vals']
        return mul_expression__to__primary_expression(primary_expression_vals)
    

    elif production_string == "assignment_operator->ASSIGN ,['#']":
        return assignment_operator__to__ASSIGN()
    

    elif production_string == "assignment_statement->ID assignment_operator expression SEMI ,['#']":
        ID = reduction_list[0]
        expression_val = reduction_list[2]['NT_vals']
        return assignment_statement__to__ID_assignment_operator_expression_SEMI(ID,expression_val)
    

    elif production_string == "assignment_statement->ID LSQUARE expression RSQUARE assignment_operator expression SEMI ,['#']":
        ID = reduction_list[0]
        index_expression_val = reduction_list[2]['NT_vals']
        expression_val = reduction_list[5]['NT_vals']
        return assignment_statement__to__ID_LSQUARE_expression_RSQUARE_assignment_operator_expression_SEMI(ID,index_expression_val,expression_val)
    

    elif production_string == "type_specifier->INT ,['#']":
        return type_specifier__to__INT()
    

    elif production_string == "declaration_assign->ASSIGN expression ,['#']":
        expression_val = reduction_list[1]['NT_vals']
        return declaration_assign__to__ASSIGN_expression(expression_val)
    

    elif production_string == "declaration_assign->$ ,['#']":
        return declaration_assign__to__empty()
    

    elif production_string == "declaration_init->ID declaration_assign ,['#']":
        ID = reduction_list[0]
        declaration_assign_val = reduction_list[1]['NT_vals']
        return declaration_init__to__ID_declaration_assign(ID,declaration_assign_val)
    

    elif production_string == "declaration_init->ID LSQUARE INT_NUM RSQUARE ,['#']":
        ID = reduction_list[0]
        INT_NUM = reduction_list[2]
        return declaration_init__to__ID_LSQUARE_INT_NUM_RSQUARE(ID,INT_NUM)
    

    elif production_string == "declaration_init_list->COMMA declaration_init declaration_init_list ,['#']":
        # print("!!!!!!")
        declaration_init_val = reduction_list[1]['NT_vals']
        declaration_init_list_val = reduction_list[2]['NT_vals']
        return declaration_init_list__to__COMMA_declaration_init_declaration_init_list(declaration_init_val,declaration_init_list_val)
    

    elif production_string == "declaration_init_list->$ ,['#']":
        # print("!!!!!!")
        return declaration_init_list__to__empty()
    

    elif production_string == "declaration->type_specifier declaration_init declaration_init_list SEMI ,['#']":
        declaration_init_val = reduction_list[1]['NT_vals']
        # print(reduction_list)
        declaration_init_list_val = reduction_list[2]['NT_vals']
        return declaration__to__type_specifier_declaration_init_declaration_init_list_SEMI(declaration_init_val,declaration_init_list_val)
    

    elif production_string == "statement->assignment_statement ,['#']":
        assignment_statement_val = reduction_list[0]['NT_vals']
        return statement__to__assignment_statement(assignment_statement_val)
    

    elif production_string == "statement->jump_statement ,['#']":
        jump_statement_val = reduction_list[0]['NT_vals']
        return statement__to__jump_statement(jump_statement_val)
    

    elif production_string == "statement->if_statement ,['#']":
        if_statement_val = reduction_list[0]['NT_vals']
        return statement__to__if_statement(if_statement_val)
    

    elif production_string == "statement->iteration_statement ,['#']":
        iteration_statement_val = reduction_list[0]['NT_vals']
        return statement__to__iteration_statement(iteration_statement_val)
    

    elif production_string == "statement->LBRACE statement_list RBRACE ,['#']":
        statement_list_val = reduction_list[1]['NT_vals']
        return statement__to__LBRACE_statement_list_RBRACE(statement_list_val)
    

    elif production_string == "statement->read_statement ,['#']":
        read_statement_val = reduction_list[0]['NT_vals']
        return statement__to__read_statement(read_statement_val)
    

    elif production_string == "statement->write_statement ,['#']":
        write_statement_val = reduction_list[0]['NT_vals']
        return statement__to__write_statement(write_statement_val)



    elif production_string == "statement->return_statement ,['#']":
        return_statement_val = reduction_list[0]['NT_vals']
        return statement__to__return_statement(return_statement_val)
    

    elif production_string == "single_statement->assignment_statement ,['#']":
        assignment_statement_val = reduction_list[0]['NT_vals']
        return single_statement__to__assignment_statement(assignment_statement_val)
    

    elif production_string == "single_statement->jump_statement ,['#']":
        jump_statement_val = reduction_list[0]['NT_vals']
        return single_statement__to__jump_statement(jump_statement_val)
    

    elif production_string == "single_statement->read_statement ,['#']":
        read_statement_val = reduction_list[0]['NT_vals']
        return single_statement__to__read_statement(read_statement_val)
    

    elif production_string == "single_statement->write_statement ,['#']":
        write_statement_val = reduction_list[0]['NT_vals']
        return single_statement__to__write_statement(write_statement_val)
    

    elif production_string == "single_statement->return_statement ,['#']":
        return_statement_val = reduction_list[0]['NT_vals']
        return single_statement__to__return_statement(return_statement_val)
    

    elif production_string == "single_statement->LBRACE statement_list RBRACE ,['#']":
        statement_list_val = reduction_list[1]['NT_vals']
        return single_statement__to__LBRACE_statement_list_RBRACE(statement_list_val)
    

    elif production_string == "read_statement->READ LPAR ID RPAR SEMI ,['#']":
        ID = reduction_list[2]
        return read_statement__to__READ_LPAR_ID_RPAR_SEMI(ID)
    

    elif production_string == "write_statement->WRITE LPAR expression RPAR SEMI ,['#']":
        expression = reduction_list[2]['NT_vals']
        return write_statement__to__WRITE_LPAR_expression_RPAR_SEMI(expression)
    

    elif production_string == "jump_statement->BREAK SEMI ,['#']":
        return jump_statement__to__BREAK_SEMI()
    

    elif production_string == "return_statement->RETURN SEMI ,['#']":
        return return_statement__to__RETURN_SEMI()
    

    elif production_string == "if_statement->IF LPAR expression RPAR single_statement ELSE single_statement ,['#']":
        expression_val = reduction_list[2]['NT_vals']
        single_statement_1_val = reduction_list[4]['NT_vals']
        single_statement_2_val = reduction_list[6]['NT_vals']
        return if_statement__to__IF_LPAR_expression_RPAR_single_statement_ELSE_single_statement(expression_val,single_statement_1_val,
                                                                                     single_statement_2_val)
    

    elif production_string == "if_statement->IF LPAR expression RPAR single_statement ,['#']":
        expression_val = reduction_list[2]['NT_vals']
        single_statement_val = reduction_list[4]['NT_vals']
        return if_statement__to__IF_LPAR_expression_RPAR_single_statement(expression_val,single_statement_val)
    

    elif production_string == "iteration_statement->WHILE LPAR expression RPAR statement ,['#']":
        expression_val = reduction_list[2]['NT_vals']
        statement_val = reduction_list[4]['NT_vals']
        return iteration_statement__to__WHILE_LPAR_expression_RPAR_statement(expression_val,statement_val)
    

    elif production_string == "iteration_statement->DO statement WHILE LPAR expression RPAR SEMI ,['#']":
        statement_val = reduction_list[1]['NT_vals']
        expression_val = reduction_list[4]['NT_vals']
        return iteration_statement__to__DO_statement_WHILE_LPAR_expression_RPAR_SEMI(statement_val,expression_val)
    

    else:
        print("ERROR!unknown production")


# generate content for every reduction
def generator(production,reduction_list):
    NT = production.left
    
    mips_code = ""
    # print(production.to_string())
    # if("cmp_expression->shi_expression ,['#']"==production.to_string()):
    #     print("yes")
    production_string =  production.to_string()
    NT_values = production_case(production_string,reduction_list)

    # NT_values ={'val_type':1,'val':'2'}
    # NT_values = operator_1__to__MUL_OP()
    NT_item = {'class': 'NT', 'type': NT, 'NT_vals':NT_values}

    return NT_item






# find the ID
def find_ID(ID_name):
    try:
        return ID_address_map[ID_name]
    except:
        print("ERROR!ID used before declear! ID:",ID_name)  
        return -999

# print(find_ID('xxx'))

# record the ID
def record_ID(ID_name):
    global CURRENT_ID_ADDRESS
    address = CURRENT_ID_ADDRESS
    CURRENT_ID_ADDRESS += 4
    ID_address_map[ID_name] = address
    return address

# record the ID[length]
def record_ID_list(ID_name,length):
    global CURRENT_ID_ADDRESS
    address = CURRENT_ID_ADDRESS
    CURRENT_ID_ADDRESS += 4
    ID_address_map[ID_name] = address
    i = 1
    while i < int(length):
        CURRENT_ID_ADDRESS += 4
        i+=1
    return address

# print(record_ID('xxx'))
# print(record_ID('xx1x'))
# print(find_ID('xx1x'))



# register allocation
def use_a_register():
    for reg in register_map:
        if register_occupancy[reg] == True:
            register_occupancy[reg] = False
            return reg
    print("ERROR!used up all the tmp registers")  
    return "$X"
# for i in range(0,10):
#     print(use_a_register())
# free one register
def free_a_register(reg):
    if reg in register_map:
        register_occupancy[reg] = True
    else:
        print("ERROR!unknown register:", reg)
    return

# free_a_register("$t0")

# free all registers
def free_all_registers():
    for reg in register_map:
        register_occupancy[reg] = True
    return

# free_all_registers()
# for i in range(0,10):
#     print(use_a_register())



# create a label 
def new_label():
    global CURRENT_LABEL_ID
    CURRENT_LABEL_ID+=1
    return ("$L" + str(CURRENT_LABEL_ID))


# add a label
def mips_label(target_label):
    return (target_label+":") + "\n"

# memory allocation (e.g., reduce 4 bytes of SP)
# length: 1 --> 4 byte
def mips_allocate_memory(length):
    mips_code = "addi $sp, $sp, -"
    mips_code = mips_code + str(length*4) + "\n"
    return mips_code


# free memory
def mips_free_memory(length):
    mips_code = "addi $sp, $sp, "
    mips_code = mips_code + str(length*4) + "\n"
    return mips_code


# low-level mips word generation
def mips_load_word(target_reg,pos_reg,shift):
    mips_code = "lw " + target_reg + "," + str(shift) + "(" + pos_reg + ")" + "\n"
    return mips_code

def mips_store_word(from_reg,pos_reg,shift):
    mips_code = "sw " + from_reg + "," + str(shift) + "(" +  pos_reg + ")" + "\n"
    return mips_code

def mips_load_immediate(reg_number,immediate_val):
    mips_code = "li " + reg_number + "," +  str(immediate_val) + "\n"
    return mips_code

def mips_add(out_reg,in_reg1,in_reg2):
    mips_code = "add " + out_reg + "," + in_reg1 + "," + in_reg2 + "\n"
    return mips_code

def mips_subtract(out_reg,in_reg1,in_reg2):
    mips_code = "sub " + out_reg + "," + in_reg1 + "," + in_reg2 + "\n"
    return mips_code

def mips_mul(out_reg,in_reg1,in_reg2):
    mips_code = "mul " + out_reg + "," + in_reg1 + "," + in_reg2 + "\n"
    return mips_code

def mips_mult(in_reg1,in_reg2):
    mips_code = "mult " + in_reg1 + "," + in_reg2 + "\n"
    return mips_code

def mips_move_from_hi(out_reg):
    mips_code = "mfhi " + out_reg + "\n"
    return mips_code

def mips_move_from_lo(out_reg):
    mips_code = "mflo " + out_reg + "\n"
    return mips_code

def mips_div(in_reg1,in_reg2):
    mips_code = "div " + in_reg1 + "," + in_reg2 + "\n"
    return mips_code


def mips_and(out_reg,in_reg1,in_reg2):
    mips_code = "and " + out_reg + "," + in_reg1 + "," + in_reg2 + "\n"
    return mips_code

def mips_andi(out_reg,in_reg1,immediate_val):
    mips_code = "andi " + out_reg + "," + in_reg1 + "," + str(immediate_val) + "\n"
    return mips_code

def mips_or(out_reg,in_reg1,in_reg2):
    mips_code = "or " + out_reg + "," + in_reg1 + "," + in_reg2 + "\n"
    return mips_code

def mips_xor(out_reg,in_reg1,in_reg2):
    mips_code = "xor " + out_reg + "," + in_reg1 + "," + in_reg2 + "\n"
    return mips_code

def mips_xori(out_reg,in_reg1,immediate_val):
    mips_code = "xori " + out_reg + "," + in_reg1 + "," + str(immediate_val) + "\n"
    return mips_code

def mips_and_immediate(out_reg,in_reg1,immediate_val):
    mips_code = "andi " + out_reg + "," + in_reg1 + "," + str(immediate_val) + "\n"
    return mips_code

def mips_shift_left_logical(out_reg,in_reg1,immediate_val):
    mips_code = "sll " + out_reg + "," + in_reg1 + "," + str(immediate_val) + "\n"
    return mips_code

def mips_shift_left_logical_variable(out_reg,in_reg1,in_reg2):
    mips_code = "sllv " + out_reg + "," + in_reg1 + "," + in_reg2 + "\n"
    return mips_code

def mips_shift_right_logical(out_reg,in_reg1,immediate_val):
    mips_code = "srl " + out_reg + "," + in_reg1 + "," + str(immediate_val) + "\n"
    return mips_code



# def mips_shift_left_arithmetic(out_reg,in_reg1,in_reg2):
#     mips_code = "sla " + out_reg + "," + in_reg1 + "," + in_reg2 + "\n"
#     return mips_code

def mips_shift_right_arithmetic(out_reg,in_reg1,immediate_val):
    mips_code = "sra " + out_reg + "," + in_reg1 + "," + str(immediate_val) + "\n"
    return mips_code

def mips_shift_right_arithmetic_variable(out_reg,in_reg1,in_reg2):
    mips_code = "srav " + out_reg + "," + in_reg1 + "," + in_reg2 + "\n"
    return mips_code




def mips_add_immediate(out_reg,in_reg1,immediate_val):
    mips_code = "addi " + out_reg + "," + in_reg1 + "," + str(immediate_val) + "\n"
    return mips_code

def mips_syscall():
    mips_code = "syscall" + "\n"
    return mips_code



def mips_branch_on_equal(in_reg1,in_reg2,target_label):
    mips_code = "beq " + in_reg1 + "," + in_reg2 + "," + target_label + "\n"
    return mips_code

def mips_branch_on_not_equal(in_reg1,in_reg2,target_label):
    mips_code = "bne " + in_reg1 + "," + in_reg2 + "," + target_label  + "\n"
    return mips_code

def mips_branch(target_label):
    mips_code = "b " + target_label + "\n"
    return mips_code

def mips_set_on_less_than(out_reg,in_reg1,in_reg2):
    mips_code = "slt " + out_reg + "," + in_reg1 + "," + in_reg2 + "\n"
    return mips_code

def mips_set_on_less_than_unsigned(out_reg,in_reg1,in_reg2):
    mips_code = "sltu " + out_reg + "," + in_reg1 + "," + in_reg2 + "\n"
    return mips_code

def mips_set_on_less_than_immediate_unsigned(out_reg,in_reg1,immediate_val):
    mips_code = "sltiu " + out_reg + "," + in_reg1 + "," + str(immediate_val) + "\n"
    return mips_code

def mips_jump(target_address):
    mips_code = "j " + str(target_address) + "\n"
    return mips_code







# !!! 
# the generated mips codes are stored and merged and passed through the AST tree
# when passed to the program, it's over, and output the whole codes

# code_block: ["mips code1","mips code2","label1",...]

# pass codes as NT {code_block:xxx}, output all mips codes
def S__to__program(program_val):
    mips_codes = program_val['mips_codes']
    # print(mips_codes)
    
    return {'val_type':'S','mips_codes': mips_codes}
# pass codes as NT {code_block:xxx}
def program__to__external_declarations_statement_list(external_declarations_val,statement_list_val):
    mips_codes = mips_load_immediate("$sp",SP)
    mips_codes += mips_load_immediate("$ra",FP)
    mips_codes += (external_declarations_val['mips_codes']+statement_list_val['mips_codes']) 
    mips_codes += "end_block:\n"
    print("---------mips_codes:---------")
    print(mips_codes)

    
    fh = open('output.txt', 'w', encoding='utf-8')
    fh.write(mips_codes)
    fh.close()

    return {'val_type':'program', 'mips_codes': mips_codes }
# pass codes as NT {code_block:xxx}
def external_declarations__to__declaration_external_declarations(declaration_val,external_declarations_val):
    return {'val_type':'declaration', 'mips_codes': (declaration_val['mips_codes']+external_declarations_val['mips_codes']) }
# pass codes as NT {code_block:empty}
def external_declarations__to__empty():
    return {'val_type':'declaration', 'mips_codes': "" }
# pass codes as NT {code_block:xxx}
def statement_list__to__statement_statement_list(statement_val,statement_list_val):
    return {'val_type':'statement', 'mips_codes': (statement_val['mips_codes']+statement_list_val['mips_codes']) }
# pass codes as NT {code_block:empty}
def statement_list__to__empty():
    return {'val_type':'statement', 'mips_codes': "" }


# return NT {op_sign:*}
def operator_1__to__MUL_OP():
    return {'op_sign':'*'}
# return NT {op_sign:/}
def operator_1__to__DIV_OP():
    return {'op_sign':'/'}
# return NT {op_sign:+}
def operator_2__to__PLUS():
    return {'op_sign':'+'}
# return NT {op_sign:-}
def operator_2__to__MINUS():
    return {'op_sign':'-'}
# return NT {op_sign:<<}
def operator_3__to__SHL_OP():
    return {'op_sign':'<<'}
# return NT {op_sign:>>}
def operator_3__to__SHR_OP():
    return {'op_sign':'>>'}
# return NT {op_sign:<}
def operator_4__to__LT():
    return {'op_sign':'<'}
# return NT {op_sign:>}
def operator_4__to__GT():
    return {'op_sign':'>'}
# return NT {op_sign:<=}
def operator_4__to__LTEQ():
    return {'op_sign':'<='}
# return NT {op_sign:>=}
def operator_4__to__GTEQ():
    return {'op_sign':'>='}
# return NT {op_sign:==}
def operator_4__to__EQ():
    return {'op_sign':'=='}
# return NT {op_sign:!=}
def operator_4__to__NOTEQ():
    return {'op_sign':'!='}
# return NT {op_sign:&}
def operator_5__to__AND_OP():
    return {'op_sign':'&'}
# return NT {op_sign:|}
def operator_5__to__OR_OP():
    return {'op_sign':'|'}
# return NT {op_sign:&&}
def operator_6__to__ANDAND():
    return {'op_sign':'&&'}
# return NT {op_sign:||}
def operator_6__to__OROR():
    return {'op_sign':'||'}

## IDEA: don't load the expression until it is excecuted right now, otherwise might run out of register
## e.g.: exp + (exp + (exp + ...))
## so primary expression won't be loaded until it is used in expressions with op

## also, all the expression are saved in memory (or immediate value) instead of register
## so, for expressions receive 'tmp_val_in_stack' elements, it will free the address after using the element

## another thing is that 'tmp_val_in_stack' also take FP as its reference initial position, SP only indicate
## the current outermost address used here (actually useless)


# return NT {val_type:tmp_val_in_stack, mips_codes: the mips codes generated here}
# 我太懒了，全部存 stack 里算了
def primary_expression__to__ID(ID):
    mips_codes = ""
    address =  find_ID(ID['val'])
    reg1 = use_a_register()
    mips_codes += mips_load_word(reg1,"$zero",address)
    mips_codes += mips_allocate_memory(1)
    mips_codes += mips_store_word(reg1,"$sp",0)
    free_a_register(reg1)
    return {'val_type':'tmp_val_in_stack','mips_codes':mips_codes}
# return NT {val_type:tmp_val_in_stack, mips_codes: the mips codes generated here}
# 我太懒了，全部存 stack 里算了
def primary_expression__to__INT_NUM(INT_NUM):
    mips_codes = ""
    reg1 = use_a_register()
    mips_codes += mips_load_immediate(reg1,INT_NUM['val'])
    mips_codes += mips_allocate_memory(1)
    mips_codes += mips_store_word(reg1,"$sp",0)
    free_a_register(reg1)
    return {'val_type':'tmp_val_in_stack','mips_codes':mips_codes}
# return NT {val_type:tmp_val_in_stack, val:its_address_in_memory}/{val_type:INT_NUM, val:its_val}
# /{val_type:ID, val:its_address_in_memory, ID_name:ID_name(might be useless)}
# it won't free tmp_val_in_stack since such val is only passed but not used yet
def primary_expression__to__LPAR_expression_RPAR(expression_vals):
    return expression_vals
# return NT {'val_type':'tmp_val_in_stack','mips_codes':mips_codes}
# where tmp
def primary_expression__to__ID_LSQUARE_primary_expression_RSQUARE(ID,primary_expression_vals):
    # ID[xxx], this is ID's start address
    ID_address =  find_ID(ID['val']) 
    mips_codes = primary_expression_vals['mips_codes']
    new_mips_codes = ""
    # ID[exp], exp is now already calculated and is in the stack as tmp value
    if primary_expression_vals['val_type'] == 'tmp_val_in_stack':
        # get the tmp value
        reg1 = use_a_register()
        # reg2 = 4
        reg2 = use_a_register()
        new_mips_codes += mips_load_immediate(reg2,4)
        # reg1 = index
        new_mips_codes += mips_load_word(reg1,"$sp",0)
        # reg1 = 4*reg1
        new_mips_codes += mips_mul(reg1,reg1,reg2)
        # reg1 = reg1 + ID's start address = ID[exp]'s address
        new_mips_codes += mips_add_immediate(reg1,reg1,ID_address)
        # free the tmp_value
        new_mips_codes += mips_free_memory(1)
        # push new stack element, to store 
        new_mips_codes += mips_allocate_memory(1)
        # now reg1 = ID[exp]'s true value
        new_mips_codes += mips_load_word(reg1,reg1,0)
        # store ID[exp]'s vals at current SP's pos, actually form a new exp in old SP pos
        new_mips_codes += mips_store_word(reg1,"$sp",0)
        # free registers
        free_a_register(reg1)
        free_a_register(reg2)
        mips_codes = mips_codes + new_mips_codes
        return {'val_type':'tmp_val_in_stack', 'mips_codes':mips_codes }
    else:
        print("ERROR!!!Unknown primary expression type:",primary_expression_vals['val_type'])
        return
# just pass the expression's values
def expression__to__logic_expression(logic_expression_vals):
    return logic_expression_vals
## OP type example:
# if it is logic_expression OP(&&,||) bit_expression, do the following:
# 1. load 2 expression(load from ID address/ pass by tmp exp address/ pass by INT_VAL) into register, 
#    free address if possible by adding SP (0/4/8)
# 2. execute OP, store to a reg
# 3. put the answer into memory (at current SP pos), reduce SP by 4
# pass its value, return NT {val_type:tmp_val_in_stack, val:its_address_in_memory}
def logic_expression__to__logic_expression_operator_6_bit_expression(logic_expression_vals,bit_expression_vals,operator_6_vals):
    mips_codes = logic_expression_vals['mips_codes']+bit_expression_vals['mips_codes']
    new_mips_codes = ""
    
    
    # load second exp first, then the first one
    # exp should all be tmp values on stack, check if it is correct
    if bit_expression_vals['val_type'] != 'tmp_val_in_stack':
        print("ERROR!!!Unknown bit expression type:",bit_expression_vals['val_type'])
        return
    if logic_expression_vals['val_type'] != 'tmp_val_in_stack':
        print("ERROR!!!Unknown logic expression type:",logic_expression_vals['val_type'])
        return
    
    # --load bit_expression
    reg1 = use_a_register()
    new_mips_codes += mips_load_word(reg1,"$sp",0)
    # free the tmp_value
    new_mips_codes += mips_free_memory(1)
    # --load logic_expression
    reg2 = use_a_register()
    new_mips_codes += mips_load_word(reg2,"$sp",0)
    # free the tmp_value
    new_mips_codes += mips_free_memory(1)
    

    # do OP
    if operator_6_vals['op_sign'] == '&&':
        new_label1 = new_label()
        new_label2 = new_label()
        new_mips_codes += mips_branch_on_equal(reg2,"$zero",new_label1)
        new_mips_codes += mips_branch_on_equal(reg1,"$zero",new_label1)
        new_mips_codes += mips_load_immediate(reg1,1)
        new_mips_codes += mips_branch(new_label2)
        new_mips_codes += mips_label(new_label1)
        new_mips_codes += mips_load_immediate(reg1,0)
        new_mips_codes += mips_label(new_label2)

    elif operator_6_vals['op_sign'] == '||':
        new_label1 = new_label()
        new_label2 = new_label()
        new_label3 = new_label()
        new_mips_codes += mips_branch_on_not_equal(reg2,"$zero",new_label1)
        new_mips_codes += mips_branch_on_equal(reg1,"$zero",new_label2)
        new_mips_codes += mips_label(new_label1)
        new_mips_codes += mips_load_immediate(reg1,1)
        new_mips_codes += mips_branch(new_label3)
        new_mips_codes += mips_label(new_label2)
        new_mips_codes += mips_load_immediate(reg1,0)
        new_mips_codes += mips_label(new_label3)
        


    else:
        print("ERROR!!!Unknown op type:",operator_6_vals['op_sign'])
    

    # store as tmp_val_in_stack
    new_mips_codes += mips_allocate_memory(1)
    new_mips_codes += mips_store_word(reg1,"$sp",0)


    free_a_register(reg1)
    free_a_register(reg2)
    mips_codes += new_mips_codes
    
    return {'val_type':'tmp_val_in_stack', 'mips_codes':mips_codes }
# if it is one single expression, pass its values
def logic_expression__to__bit_expression(bit_expression_vals):
    return bit_expression_vals
# OP type
def bit_expression__to__bit_expression_operator_5_cmp_expression(bit_expression_vals,cmp_expression_vals,operator_5_vals):
    mips_codes = bit_expression_vals['mips_codes']+cmp_expression_vals['mips_codes']
    new_mips_codes = ""
    
    
    # load second exp first, then the first one
    # exp should all be tmp values on stack, check if it is correct
    if cmp_expression_vals['val_type'] != 'tmp_val_in_stack':
        print("ERROR!!!Unknown cmp expression type:",cmp_expression_vals['val_type'])
        return
    if bit_expression_vals['val_type'] != 'tmp_val_in_stack':
        print("ERROR!!!Unknown bit expression type:",bit_expression_vals['val_type'])
        return
    
    
    # --load cmp_expression
    reg1 = use_a_register()
    new_mips_codes += mips_load_word(reg1,"$sp",0)
    # free the tmp_value
    new_mips_codes += mips_free_memory(1)
    # --load bit_expression
    reg2 = use_a_register()
    new_mips_codes += mips_load_word(reg2,"$sp",0)
    # free the tmp_value
    new_mips_codes += mips_free_memory(1)
    

    # do OP
    if operator_5_vals['op_sign'] == '&':
        new_mips_codes += mips_and(reg1,reg1,reg2)
       
    elif operator_5_vals['op_sign'] == '|':
        new_mips_codes += mips_or(reg1,reg1,reg2)
        
    else:
        print("ERROR!!!Unknown op type:",operator_5_vals['op_sign'])
    # new_mips_codes += mips_add(reg1,reg1,reg2)
    

    # store as tmp_val_in_stack
    new_mips_codes += mips_allocate_memory(1)
    new_mips_codes += mips_store_word(reg1,"$sp",0)


    free_a_register(reg1)
    free_a_register(reg2)
    mips_codes += new_mips_codes
    
    return {'val_type':'tmp_val_in_stack', 'mips_codes':mips_codes }
# similar to A OP B: load, free, exe, push & store
def bit_expression__to__NOT_OP_cmp_expression(cmp_expression_vals):
    mips_codes = cmp_expression_vals['mips_codes']
    new_mips_codes = ""
    reg1 = use_a_register()
    new_mips_codes += mips_load_word(reg1,"$sp",0)
    new_mips_codes += mips_free_memory(1)
    new_mips_codes += mips_set_on_less_than_immediate_unsigned(reg1,reg1,1)
    new_mips_codes += mips_andi(reg1,reg1,"0x00ff")
    new_mips_codes += mips_allocate_memory(1)
    new_mips_codes += mips_store_word(reg1,"$sp",0)
    mips_codes += new_mips_codes
    free_a_register(reg1)
    return {'val_type':'tmp_val_in_stack', 'mips_codes':mips_codes }
    
# pass values
def bit_expression__to__cmp_expression(cmp_expression_vals):
    return cmp_expression_vals
# OP type
def cmp_expression__to__cmp_expression_operator_4_shi_expression(cmp_expression_vals,shi_expression_vals,operator_4_vals):
    new_mips_codes = ""
    mips_codes = cmp_expression_vals['mips_codes']+shi_expression_vals['mips_codes']
    # load second exp first, then the first one
    # exp should all be tmp values on stack, check if it is correct
    if shi_expression_vals['val_type'] != 'tmp_val_in_stack':
        print("ERROR!!!Unknown shi expression type:",shi_expression_vals['val_type'])
        return
    if cmp_expression_vals['val_type'] != 'tmp_val_in_stack':
        print("ERROR!!!Unknown cmp expression type:",cmp_expression_vals['val_type'])
        return
    
    
    # --load shi_expression = reg2
    reg2 = use_a_register()
    new_mips_codes += mips_load_word(reg2,"$sp",0)
    # free the tmp_value
    new_mips_codes += mips_free_memory(1)
    # --load cmp_expression = reg1
    reg1 = use_a_register()
    new_mips_codes += mips_load_word(reg1,"$sp",0)
    # free the tmp_value
    new_mips_codes += mips_free_memory(1)
    

    # do OP
    if operator_4_vals['op_sign'] == '<':
        new_mips_codes += mips_set_on_less_than(reg1,reg1,reg2)
       
    elif operator_4_vals['op_sign'] == '>':
        new_mips_codes += mips_set_on_less_than(reg1,reg2,reg1)
    
    elif operator_4_vals['op_sign'] == '<=':
        new_mips_codes += mips_set_on_less_than(reg1,reg2,reg1)
        new_mips_codes += mips_xori(reg1,reg1,"0x1")
        new_mips_codes += mips_andi(reg1,reg1,"0x00ff")
    elif operator_4_vals['op_sign'] == '>=':
        new_mips_codes += mips_set_on_less_than(reg1,reg1,reg2)
        new_mips_codes += mips_xori(reg1,reg1,"0x1")
        new_mips_codes += mips_andi(reg1,reg1,"0x00ff")
    elif operator_4_vals['op_sign'] == '==':
        new_mips_codes += mips_xor(reg1,reg1,reg2)
        new_mips_codes += mips_set_on_less_than_immediate_unsigned(reg1,reg1,1)
        new_mips_codes += mips_andi(reg1,reg1,"0x00ff")

    elif operator_4_vals['op_sign'] == '!=':
        new_mips_codes += mips_xor(reg1,reg1,reg2)
        new_mips_codes += mips_set_on_less_than_unsigned(reg1,"$zero",reg1)
        new_mips_codes += mips_andi(reg1,reg1,"0x00ff")
        
    else:
        print("ERROR!!!Unknown op type:",operator_4_vals['op_sign'])
    # new_mips_codes += mips_add(reg1,reg1,reg2)
    

    # store as tmp_val_in_stack
    new_mips_codes += mips_allocate_memory(1)
    new_mips_codes += mips_store_word(reg1,"$sp",0)


    free_a_register(reg1)
    free_a_register(reg2)



    mips_codes += new_mips_codes
    return {'val_type':'tmp_val_in_stack', 'mips_codes':mips_codes }
# pass values
def cmp_expression__to__shi_expression(shi_expression_vals):
    return shi_expression_vals
# OP type
def shi_expression__to__shi_expression_operator_3_add_expression(shi_expression_vals,add_expression_vals,operator_3_vals):
    new_mips_codes = ""
    mips_codes = shi_expression_vals['mips_codes']+add_expression_vals['mips_codes']
    # load second exp first, then the first one
    # exp should all be tmp values on stack, check if it is correct
    if add_expression_vals['val_type'] != 'tmp_val_in_stack':
        print("ERROR!!!Unknown add expression type:",add_expression_vals['val_type'])
        return
    if shi_expression_vals['val_type'] != 'tmp_val_in_stack':
        print("ERROR!!!Unknown shi expression type1:",shi_expression_vals['val_type'])
        return
    
    
    # --load cmp_expression
    reg2 = use_a_register()
    new_mips_codes += mips_load_word(reg2,"$sp",0)
    # free the tmp_value
    new_mips_codes += mips_free_memory(1)
    # --load bit_expression
    reg1 = use_a_register()
    new_mips_codes += mips_load_word(reg1,"$sp",0)
    # free the tmp_value
    new_mips_codes += mips_free_memory(1)
    

    # do OP
    if operator_3_vals['op_sign'] == '<<':
        new_mips_codes += mips_shift_left_logical_variable(reg1,reg1,reg2)
       
    elif operator_3_vals['op_sign'] == '>>':
        new_mips_codes += mips_shift_right_arithmetic_variable(reg1,reg1,reg2)
        
    else:
        print("ERROR!!!Unknown op type:",operator_3_vals['op_sign'])
    # new_mips_codes += mips_add(reg1,reg1,reg2)
    

    # store as tmp_val_in_stack
    new_mips_codes += mips_allocate_memory(1)
    new_mips_codes += mips_store_word(reg1,"$sp",0)


    free_a_register(reg1)
    free_a_register(reg2)



    mips_codes += new_mips_codes
    return {'val_type':'tmp_val_in_stack', 'mips_codes':mips_codes }
# pass values
def shi_expression__to__add_expression(add_expression_vals):
    return add_expression_vals
# OP type
def add_expression__to__add_expression_operator_2_mul_expression(add_expression_vals,mul_expression_vals,operator_2_vals):
    new_mips_codes = ""
    mips_codes = add_expression_vals['mips_codes']+mul_expression_vals['mips_codes']
    # load second exp first, then the first one
    # exp should all be tmp values on stack, check if it is correct
    if add_expression_vals['val_type'] != 'tmp_val_in_stack':
        print("ERROR!!!Unknown add expression type:",add_expression_vals['val_type'])
        return
    if mul_expression_vals['val_type'] != 'tmp_val_in_stack':
        print("ERROR!!!Unknown mul expression type:",mul_expression_vals['val_type'])
        return
    
    
    # --load cmp_expression
    reg2 = use_a_register()
    new_mips_codes += mips_load_word(reg2,"$sp",0)
    # free the tmp_value
    new_mips_codes += mips_free_memory(1)
    # --load bit_expression
    reg1 = use_a_register()
    new_mips_codes += mips_load_word(reg1,"$sp",0)
    # free the tmp_value
    new_mips_codes += mips_free_memory(1)
    

    # do OP
    if operator_2_vals['op_sign'] == '+':
        new_mips_codes += mips_add(reg1,reg1,reg2)
       
    elif operator_2_vals['op_sign'] == '-':
        new_mips_codes += mips_subtract(reg1,reg1,reg2)
        
    else:
        print("ERROR!!!Unknown op type:",operator_2_vals['op_sign'])
    # new_mips_codes += mips_add(reg1,reg1,reg2)
    

    # store as tmp_val_in_stack
    new_mips_codes += mips_allocate_memory(1)
    new_mips_codes += mips_store_word(reg1,"$sp",0)


    free_a_register(reg1)
    free_a_register(reg2)



    mips_codes += new_mips_codes
    return {'val_type':'tmp_val_in_stack', 'mips_codes':mips_codes }
# similar to A OP B: load, free, exe, push & store
def add_expression__to__MINUS_mul_expression(mul_expression_vals):
    mips_codes = mul_expression_vals['mips_codes']
    new_mips_codes = ""
    reg1 = use_a_register()
    new_mips_codes += mips_load_word(reg1,"$sp",0)
    new_mips_codes += mips_free_memory(1)
    new_mips_codes += mips_subtract(reg1,"$zero",reg1)
    new_mips_codes += mips_allocate_memory(1)
    new_mips_codes += mips_store_word(reg1,"$sp",0)
    mips_codes += new_mips_codes
    free_a_register(reg1)
    return {'val_type':'tmp_val_in_stack', 'mips_codes':mips_codes }
# pass values
def add_expression__to__mul_expression(mul_expression_vals):
    return mul_expression_vals
# OP type
def mul_expression__to__mul_expression_operator_1_primary_expression(mul_expression_vals,primary_expression_vals,operator_1_vals):
    new_mips_codes = ""
    mips_codes = mul_expression_vals['mips_codes']+primary_expression_vals['mips_codes']
    # load second exp first, then the first one
    # exp should all be tmp values on stack, check if it is correct
    if mul_expression_vals['val_type'] != 'tmp_val_in_stack':
        print("ERROR!!!Unknown mul expression type:",mul_expression_vals['val_type'])
        return
    if primary_expression_vals['val_type'] != 'tmp_val_in_stack':
        print("ERROR!!!Unknown primary expression type:",primary_expression_vals['val_type'])
        return
    
    
    # --load cmp_expression
    reg2 = use_a_register()
    new_mips_codes += mips_load_word(reg2,"$sp",0)
    # free the tmp_value
    new_mips_codes += mips_free_memory(1)
    # --load bit_expression
    reg1 = use_a_register()
    new_mips_codes += mips_load_word(reg1,"$sp",0)
    # free the tmp_value
    new_mips_codes += mips_free_memory(1)
    

    # do OP
    if operator_1_vals['op_sign'] == '*':
        new_mips_codes += mips_mul(reg1,reg1,reg2)
       
    elif operator_1_vals['op_sign'] == '/':
        # no x/0 check here, add it later...
        new_mips_codes += mips_div(reg1,reg2)
        new_mips_codes += mips_move_from_lo(reg1)
    else:
        print("ERROR!!!Unknown op type:",operator_1_vals['op_sign'])
    # new_mips_codes += mips_add(reg1,reg1,reg2)
    

    # store as tmp_val_in_stack
    new_mips_codes += mips_allocate_memory(1)
    new_mips_codes += mips_store_word(reg1,"$sp",0)


    free_a_register(reg1)
    free_a_register(reg2)




    mips_codes += new_mips_codes
    return {'val_type':'tmp_val_in_stack', 'mips_codes':mips_codes }
# pass values
def mul_expression__to__primary_expression(primary_expression_vals):
    return primary_expression_vals
# return NT {op_sign:=}
def assignment_operator__to__ASSIGN():
    return {'op_sign':'='}
# # return NT {op_sign:+=}
# def assignment_operator__to__PLUS_ASSIGN():
#     return
# # return NT {op_sign:-=}
# def assignment_operator__to__MINUS_ASSIGN():
#     return
# # return NT {op_sign:*=}
# def assignment_operator__to__MUL_OP_ASSIGN():
#     return
# # return NT {op_sign:/=}
# def assignment_operator__to__DIV_OP_ASSIGN():
#     return



# 1. load expression from ID/tmp address/immediate INT
#    increase SP by 0/4/0 (free address)
# 2. load ID address, store in a reg
# 3. store (SW) to target ID
def assignment_statement__to__ID_assignment_operator_expression_SEMI(ID,expression_val):
    mips_codes = expression_val['mips_codes']
    new_mips_codes = ""
    address =  find_ID(ID['val'])
    reg1 = use_a_register()
    new_mips_codes += mips_load_word(reg1,"$sp",0)
    new_mips_codes += mips_free_memory(1)
    new_mips_codes += mips_store_word(reg1,"$zero",address)

    
    mips_codes += new_mips_codes
    free_a_register(reg1)
    return {'val_type':'tmp_val_in_stack', 'mips_codes':mips_codes }
    
    
# 1. load expression from ID/tmp address/immediate INT
#    increase SP by 0/4/0 (free address)
# 2. load ID address, store in a reg; and load shift amount of ID[xxx] as a immediate value 'shift'
# 3. store (SW) to target ID[xxx] address: ID address + shift amount
# 4. increase SP by 0(exp is INT or ID)/4(exp is tmp_val)
def assignment_statement__to__ID_LSQUARE_expression_RSQUARE_assignment_operator_expression_SEMI(ID,index_expression_val,expression_val):
    mips_codes = index_expression_val['mips_codes'] + expression_val['mips_codes']
    new_mips_codes = ""

    # reg1 = ID[x]'s address, reg2 = exp's value
    reg2 = use_a_register()
    new_mips_codes += mips_load_word(reg2,"$sp",0)
    new_mips_codes += mips_free_memory(1)

    ID_address =  find_ID(ID['val'])
    if expression_val['val_type'] == 'tmp_val_in_stack':
        # get the tmp value
        reg1 = use_a_register()
        # reg3 = 4
        reg3 = use_a_register()
        new_mips_codes += mips_load_immediate(reg3,4)
        # reg1 = index
        new_mips_codes += mips_load_word(reg1,"$sp",0)
        # free the tmp_value
        new_mips_codes += mips_free_memory(1)
        # reg1 = 4*reg1
        new_mips_codes += mips_mul(reg1,reg1,reg3)
        # reg1 = reg1 + ID's start address = ID[exp]'s address
        new_mips_codes += mips_add_immediate(reg1,reg1,ID_address)
        
        # free register 2
        
        free_a_register(reg3)
        # return {'val_type':'tmp_val_in_stack', 'mips_codes':mips_codes }
    else:
        print("ERROR!!!Unknown expression type:",index_expression_val['val_type'])

    # # reg1 = ID[x]'s address
    # reg2 = use_a_register()
    # new_mips_codes += mips_load_word(reg2,"$sp",0)
    # new_mips_codes += mips_free_memory(1)
    new_mips_codes += mips_store_word(reg2,reg1,0)

    
    mips_codes += new_mips_codes
    free_a_register(reg1)
    free_a_register(reg2)
    return {'val_type':'statement', 'mips_codes':mips_codes }
# return NT {type_specifier:'INT'}
def type_specifier__to__INT():
    return {'type_specifier':'INT'}
# return NT {initialization:true, 
# val_type:tmp_val_in_stack, val:its_address_in_memory / 
# val_type:ID, val:its_address_in_memory / 
# val_type:INT_NUM, val:its_val }
def declaration_assign__to__ASSIGN_expression(expression_val):
    expression_val['initialization'] = True
    return expression_val
# return NT {initialization:false}
def declaration_assign__to__empty():
    return {'initialization':False,'mips_codes':""}
# 算了，既然只有INT，这一步直接生成变量吧
# return NT {val_type:declaration, val:its_address_in_memory }
def declaration_init__to__ID_declaration_assign(ID,declaration_assign_val):
    mips_codes = declaration_assign_val['mips_codes']
    new_mips_codes = ""
    if declaration_assign_val['initialization'] == False:
        ID_address = record_ID(ID['val'])
        new_mips_codes += mips_store_word("$zero","$zero",ID_address)
    else:
        ID_address = record_ID(ID['val'])
        reg1 = use_a_register()
        new_mips_codes += mips_load_word(reg1,"$sp",0)
        new_mips_codes += mips_free_memory(1)
        new_mips_codes += mips_store_word(reg1,"$zero",ID_address)

        free_a_register(reg1)


    mips_codes = mips_codes + new_mips_codes
    return {'val_type':'declaration', 'mips_codes':mips_codes }
# 同上
# return NT {val_type:tmp_val_in_stack, val:its_address_in_memory }
def declaration_init__to__ID_LSQUARE_INT_NUM_RSQUARE(ID,INT_NUM):
    mips_codes = ""
    new_mips_codes = ""
    ID_address = record_ID_list(ID['val'],INT_NUM['val'])
    # 我记得一般c++不会对数组初始化

    mips_codes = mips_codes + new_mips_codes
    return {'val_type':'declaration', 'mips_codes':mips_codes }
# pass the list of declaration:
# NT {[NT1,NT2,...]}  
def declaration_init_list__to__COMMA_declaration_init_declaration_init_list(declaration_init_val,declaration_init_list_val):
    mips_codes = declaration_init_val['mips_codes']+declaration_init_list_val['mips_codes']
    return {'val_type':'declaration', 'mips_codes':mips_codes }
# pass empty: NT {[]}
def declaration_init_list__to__empty():
    # print("!!!!!!!!!!!")
    mips_codes = ""  
    return {'val_type':'declaration', 'mips_codes':mips_codes }
# just merge all the mips codes
def declaration__to__type_specifier_declaration_init_declaration_init_list_SEMI(declaration_init_val,declaration_init_list_val):
    mips_codes = declaration_init_val['mips_codes']+declaration_init_list_val['mips_codes']
    return{'val_type':'declaration', 'mips_codes':mips_codes }
# pass codes as NT {code_block:xxx}
def statement__to__assignment_statement(assignment_statement_val):
    return assignment_statement_val
# pass codes as NT {code_block:xxx}
def statement__to__jump_statement(jump_statement_val):
    return jump_statement_val
# pass codes as NT {code_block:xxx}
def statement__to__if_statement(if_statement_val):
    return if_statement_val
# pass codes as NT {code_block:xxx}
def statement__to__iteration_statement(iteration_statement_val):
    return iteration_statement_val
# pass codes as NT {code_block:xxx}
def statement__to__LBRACE_statement_list_RBRACE(statement_list_val):
    return statement_list_val
# pass codes as NT {code_block:xxx}
def statement__to__read_statement(read_statement_val):
    return read_statement_val
# pass codes as NT {code_block:xxx}
def statement__to__write_statement(write_statement_val):
    return write_statement_val
# pass codes as NT {code_block:xxx}
def statement__to__return_statement(return_statement_val):
    return return_statement_val
# pass codes as NT {code_block:xxx}
def single_statement__to__assignment_statement(assignment_statement_val):
    return assignment_statement_val
# pass codes as NT {code_block:xxx}
def single_statement__to__jump_statement(jump_statement_val):
    return jump_statement_val
# pass codes as NT {code_block:xxx}
def single_statement__to__read_statement(read_statement_val):
    return read_statement_val
# pass codes as NT {code_block:xxx}
def single_statement__to__write_statement(write_statement_val):
    return write_statement_val
# pass codes as NT {code_block:xxx}
def single_statement__to__return_statement(return_statement_val):
    return return_statement_val
# pass codes as NT {code_block:xxx}
def single_statement__to__LBRACE_statement_list_RBRACE(statement_list_val):
    return statement_list_val

# use syscall's read_int
# li 12 to $v0, syscall, store word from $v0 to ID's address
def read_statement__to__READ_LPAR_ID_RPAR_SEMI(ID):
    mips_codes = ""  
    ID_address = find_ID(ID['val'])
    # reg1 = use_a_register()
    mips_codes += mips_load_immediate("$v0",5)
    mips_codes += mips_syscall()
    mips_codes += mips_store_word("$v0","$zero",ID_address)



    # free_a_register(reg1)

    return {'val_type':'statement', 'mips_codes':mips_codes }
# li 11 to $v0, load word from $a0 to ID's address, syscall
# free the expression if it is a tmp_val
def write_statement__to__WRITE_LPAR_expression_RPAR_SEMI(expression):
    mips_codes = expression['mips_codes'] 


    mips_codes += mips_load_immediate("$v0",1)
    mips_codes += mips_load_word("$a0","$sp",0)
    mips_codes += mips_free_memory(1)

    mips_codes += mips_syscall()



    return {'val_type':'statement', 'mips_codes':mips_codes }

# pass NT {break} ummmmm.... in this assignment, no break case
def jump_statement__to__BREAK_SEMI():
    print("ERROR!not implement 'break' yet")
    mips_codes = ""
    return {'val_type':'statement', 'mips_codes':mips_codes }
# pass NT {return} ummmmm.... in this assignment, return is useless
def return_statement__to__RETURN_SEMI():
    mips_codes = "j end_block\n"
    return {'val_type':'statement', 'mips_codes':mips_codes }

# generate 3 block of codes:
# if_check_block | if_block(and then jump to the end) | else_block(might not exist), return NT {code_block_type:if_else,code_block:xxx}
# also, free tmp_val of its expression at if_check_block place  (!!!)
def if_statement__to__IF_LPAR_expression_RPAR_single_statement_ELSE_single_statement(expression_val,single_statement_1_val,
                                                                                     single_statement_2_val):
    mips_codes = ""
    mips_codes += expression_val['mips_codes']
    new_label1 = new_label()
    new_label2 = new_label()
    reg1 = use_a_register()
    mips_codes += mips_load_word(reg1,"$sp",0)
    mips_codes += mips_free_memory(1)
    mips_codes += mips_branch_on_equal(reg1,"$zero",new_label1)
    free_a_register(reg1)
    mips_codes += single_statement_1_val['mips_codes']
    mips_codes += mips_branch(new_label2)
    mips_codes += mips_label(new_label1)
    mips_codes += single_statement_2_val['mips_codes']
    mips_codes += mips_label(new_label2)

    

    return {'val_type':'statement', 'mips_codes':mips_codes }
def if_statement__to__IF_LPAR_expression_RPAR_single_statement(expression_val,single_statement_val):
    mips_codes = ""
    mips_codes += expression_val['mips_codes']
    new_label1 = new_label()
    reg1 = use_a_register()
    mips_codes += mips_load_word(reg1,"$sp",0)
    mips_codes += mips_free_memory(1)
    mips_codes += mips_branch_on_equal(reg1,"$zero",new_label1)
    free_a_register(reg1)
    mips_codes += single_statement_val['mips_codes']
    mips_codes += mips_label(new_label1)


    return {'val_type':'statement', 'mips_codes':mips_codes }
# generate 3 block of codes:
# jump_2_while_check | exe_block | while_check(jump back to exe_block or continue)
# also, free tmp_val of its expression at while_check place (!!!)
def iteration_statement__to__WHILE_LPAR_expression_RPAR_statement(expression_val,statement_val):
    mips_codes = ""
    new_label1 = new_label()
    new_label2 = new_label()
    reg1 = use_a_register()

    mips_codes += mips_branch(new_label2)

    mips_codes += mips_label(new_label1)
    mips_codes += statement_val['mips_codes']

    mips_codes += mips_label(new_label2)
    mips_codes += expression_val['mips_codes']
    mips_codes += mips_load_word(reg1,"$sp",0)
    mips_codes += mips_free_memory(1)
    mips_codes += mips_branch_on_not_equal(reg1,"$zero",new_label1)
    free_a_register(reg1)

    return {'val_type':'statement', 'mips_codes':mips_codes }
    
    
# generate 2 block of codes:
# exe_block | while_check(jump back to exe_block or continue)
# also, free tmp_val of its expression at while_check place  (!!!)
def iteration_statement__to__DO_statement_WHILE_LPAR_expression_RPAR_SEMI(statement_val,expression_val):
    mips_codes = ""


    new_label1 = new_label()
    reg1 = use_a_register()


    mips_codes += mips_label(new_label1)
    mips_codes += statement_val['mips_codes']

    mips_codes += expression_val['mips_codes']
    mips_codes += mips_load_word(reg1,"$sp",0)
    mips_codes += mips_free_memory(1)
    mips_codes += mips_branch_on_not_equal(reg1,"$zero",new_label1)
    free_a_register(reg1)

    return {'val_type':'statement', 'mips_codes':mips_codes }













