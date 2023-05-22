import copy
import generator
# Reserved Words(Keywords)
reserved_words = {
    "INT", "MAIN", "VOID", "BREAK",
    "DO", "ELSE", "IF", "WHILE",
    "RETURN", "READ", "WRITE",
}
# INT NUM and ID
type_specification=[
    'INT_NUM', 'ID'
]
# Special Symbols
special_symbols=[
    "LBRACE", "RBRACE", "LSQUARE", "RSQUARE",
    "LPAR", "RPAR", "SEMI", "PLUS", 
    "MINUS", "MUL_OP", "DIV_OP", "AND_OP",
    "OR_OP", "NOT_OP", "ASSIGN", "LT",
    "GT", "SHL_OP", "SHR_OP", "EQ",
    "NOTEQ", "LTEQ", "GTEQ", "ANDAND",
    "OROR", "COMMA"
]


def generate_first_set():
    global FIRST
    global production_group
    end_symbol={'class':'T','type':'$'}
    # first, initialize all NT's First as its beginning Ts, if its beginning is NT, just ignore it
    for non_terminal in left_group:
        if non_terminal not in FIRST:
            FIRST[non_terminal] = []
        productions = [production for production in production_group if production.left == non_terminal]
        if len(productions)==0:
            print("ERROR! an NT doesn't contain any productions")
            return
        else:
            for production in productions:
                right=production.right
                # print(right)
                if right==[end_symbol] and end_symbol not in FIRST[non_terminal]:
                    FIRST[non_terminal].append(end_symbol)
                elif right[0]['class'] == 'T' and right[0] not in FIRST[non_terminal]:
                    FIRST[non_terminal].append(right[0])

    # then, set an changed_flag, do while (changed) loop
    changed_flag = True
    while changed_flag == True:
        # print("!!!")
        changed_flag = False
        # for all the NT|xxx productions:
        for production in production_group:
            # print("x",production)
            # recording the current position of RHS, will increase till the end of the production
            pos = 0
            left = production.left
            # initialized as false every time when the loop begin, only turned true when current element is/contain empty
            contain_empty = True
            # keep adding NT's first into other NT which has it as its RHS first production
            while pos < len(production.right) and contain_empty:
                # print(pos)
                contain_empty = False
                # non-terminal case
                if production.right[pos]['class'] == 'NT':
                    for first in FIRST[production.right[pos]['type']]:
                        
                        if first['class'] == 'T' and first not in FIRST[left]:
                            # print(left,":",first['type'])
                            FIRST[left].append(first)
                            changed_flag = True
                        # if NT1 | NT2 xxx, and NT2 contains $, take xxx into consideration as its First sets
                        if first==end_symbol:
                            # print(left,first,pos,len(production.right))
                            contain_empty = True
                # terminal case
                else:
                    if production.right[pos] not in FIRST[left]:
                        # print("!!!!!!")
                        FIRST[left].append(production.right[pos])
                    if production.right[pos] == end_symbol:
                        contain_empty = True
                pos = pos+1
    
    # when no change in one loop, stop.

    return

class PRODUCTION():
    def __init__(self, left, right, position=0, terminals=None):
        self.left=left
        self.right=right
        self.position=position # actually, it is from 1 - ...
        self.terminals=terminals # the terminal symbols, core attribute of LR(1)
    # get next production item (@+=1)
    def Next(self):
        return PRODUCTION(self.left,
                          self.right,
                          self.position + 1,
                          self.terminals)
    # convert to string
    def to_string(self):
        result=self.left+'->'
        position=1
        for data in self.right:
            if position==self.position: # at @ pos, mark @
                result += '@'
            result += data['type']+' '
            position += 1
        if position == self.position: # e.g., x->xxxx@
            result += '@'
        result += ',['
        if self.terminals!=None:
            # print("!")
            if len(self.terminals)>0:
                for item in sorted(self.terminals):
                    result += '\''+item+'\''+','
                result= result[:-1]
        result += ']'
        return result
class STATE():
    def __init__(self,name):
        self.name=name
        self.productions=[]
        self.string=[]
    def to_string(self):
        for Production in self.productions:
            if Production.to_string() not in self.string:
                self.string.append(Production.to_string())
        return "\n".join(sorted(self.string))
    # get the current state's item set, return a list of current nodes on each productions
    # noticing that the item can be both T and NT, depending on what's next in the production position
    def get_item(self):
        result=[]
        for production in self.productions:
            expression = production.right
            position = production.position
            if position < len(expression) + 1:
                node = expression[position - 1]
                if node not in result:
                    result.append(node)
        return result
class DFA(object):
    def __init__(self):
        self.state=[]
        self.edge=[]
    def add_state(self, Ix):
        self.state.append(Ix)
    def add_edge(self, Ia, t, Ib):
        self.edge.append((Ia,t,Ib))
def scan_grammar(grammar):
    global production_group
    global terminal_symbol_group
    global left_group
    global start_production
    # initialization: 
    # 1. add root node 'S' at left set (optional, just for better understanding)
    # 2. the terminal group should at least contain a # symbol respresenting the terminal of the whole program
    # 3. the start production, meaning the true beginning situation of the program, S->@program is essiential
    left_group.append('S')
    terminal_symbol_group.append({'class':'T', 'type': '#'})
    start_production = PRODUCTION('S',[{'class': 'NT', 'type': 'program'}],1, terminals=['#'])
    # print("!!!!",StartProduction.to_string())
    # ProductionGroup.append(StartProduction)
    left_group=[x.split('\n')[0] for x in grammar]
    for block in grammar:
        lines=block.split('\n')
        left=lines[0]
        expressions=[x.strip(' ')[1:] for x in lines[1:-1]]
        # print("left")
        for expression in expressions:
            right=[]
            items=expression.strip(' ').split(' ')
            for item in items:
                # print(item)
                data={}
                # if item == '':
                #     print("!")
                #     print(item)

                if item == "'$'":
                    # print("!!!!!")
                    data = {'class': 'T', 'type': '$'}
                elif item in special_symbols:# Special Symbols
                    data ={'class':'T','name': item, 'type': item}
                elif item in type_specification:# INT NUM and ID 
                    data ={'class':'T','name': item, 'type': item}
                elif item in reserved_words:# Reserved Words(Keywords)
                    # print("!!!")
                    data ={'class':'T','name': item, 'type': item}
                    # print(data)
                else:# non-terminal cases
                    data ={'class':'NT','type':item}
                right.append(data)
                if not data in terminal_symbol_group and data['class']!='NT':
                    terminal_symbol_group.append(data)
            production_group.append(PRODUCTION(left, right, terminals=['#']))
            # print("!!!",PRODUCTION(left, right, terminals=['#']).to_string())
    return
def add_dot_to_productions(production):
    result=[]
    # empty case, only one dot situation
    if len(production.right)==1 and production.right[0]['type']== '$':
        result.append(PRODUCTION(production.left, production.right, 1))
    # otherwise, at least 2
    else:
        # for every dot situation
        temp=[PRODUCTION(production.left, production.right, i + 1)
              for i in range(len(production.right) + 1)]
        for item in temp:
            result.append(item)
    return result
def generate_doted_productions():
    global doted_production_group
    print(len(production_group))
    for P in production_group:
        # print("!!!!",P.to_string())
        for item in add_dot_to_productions(P):
            doted_production_group.append(item)
            
def find_production(NT):
    result=[]
    for Production in doted_production_group:
        if Production.left==NT:
            result.append(Production)
    return result

# expand a production, return a set of all the new derived productions
# e.g.: X|@xxxx
def expand_a_production(production):
        data=[]
        right = production.right
        position = production.position
        terminal = production.terminals
        def get_first_set(node):
            if node['class'] == 'NT':
                return FIRST[next['type']]
            else:
                # if is a terminal, its first set is only itself
                return [{'class':'T','type':next['type']}]
                # return GetFirstSet(next['type'])
        if position < len(right) + 1 and right[position - 1]['class'] == 'NT':
            first=[]
            # flag means such production from current position can be all eps, 
            # meaning that its own terminal set should be included in the first set
            flag=True
            for i in range(position, len(right)):
                next=right[i]
                firstset=copy.deepcopy(get_first_set(next))
                eps={'class':'T','type':'$'}
                if eps in firstset:
                    firstset.remove(eps)
                    for item in firstset:
                        if not item in first:
                            first.append(item)
                else:
                    for item in firstset:
                        if not item in first:
                            first.append(item)
                    flag =False
                    break
            if flag:
                for item in terminal:
                    if not item in first:
                        first.append({'class':'T','type':item})
            # find productions (doted) with current NT as LHS
            productions = find_production(right[position - 1]['type'])
            # only expand production in x|@xxx case
            for item in productions:
                if item.position == 1:
                    temp = copy.deepcopy(item)
                    temp.terminals =[item['type'] for item in first]
                    data.append(temp)
        return data


# get the closure of a set of productions (adding equal deriviative states onto it)
def get_closure(productions):
    # the result contains 
    # 1. the original productions we want to expand
    # cache is used to remember those productions which already contains
    cache=[p.to_string() for p in productions]
    result=[p for p in productions]
    procession=[p for p in productions]
    # 2. the new added productions in beginning phrase
    while len(procession)>0:
        production=procession.pop()
        data=expand_a_production(production)
        for item in data:
            if item.to_string() not in cache:
                result.append(item)
                cache.append(item.to_string())
                procession.append(item)
    return result

# get a new reachable set of productions from state I through input item(both T and NT)
def get_reachable_go_states(I,item):
    params=[]
    for production in I.productions:
        expression=production.right
        position=production.position
        if position<len(expression)+1:
            node=expression[position-1]
            # ignore expression = $ case (optional, because adding x|$@ is meaningless in DFA)
            if node['type']=='$' and len(expression)==1:
                continue
            if node==item and production.Next() not in params:
                params.append(production.Next())
    return get_closure(params)

# merge serveral productions according to their LHS & RHS & position,
# meaning that the terminal symbol sets are merged
def merge_productions(productions):
    # table record <production_string-terminal> pair
    # reversed record <production_string-production> pair
    result=[]
    table={}
    reversed={}
    for p in productions:
        # copy the production(ignore terminals)
        temp=PRODUCTION(p.left,p.right,p.position)
        terminals = p.terminals
        if not temp.to_string() in table.keys():
            # table record <production_string-terminal> pair
            table[temp.to_string()]=terminals
            # reversed record <production_string-production> pair
            reversed[temp.to_string()]=temp
        else:
            for t in terminals:
                table[temp.to_string()].append(t)
    for key in table.keys():
        temp=reversed[key]
        temp.terminals=table[key]
        result.append(temp)
    return result

def generate_DFA():
    global DFA    
    # <state_name-state_string> pair, used to check elements in such state
    state_table={}
    # Tranfer=[]
    # counting from 0 to ...
    current_state_number=0
    # state list, used to get the state
    states=[]
    # records current un-finished states, if goes to 0, the state set is complete
    processing_state_stack=[]
    # generate the initial state 0
    I=STATE('I'+str(current_state_number))
    I.productions=get_closure([start_production])
    state_table[I.name]=I.to_string()
    processing_state_stack.append(I)
    DFA.add_state(I)
    states.append(I)
    current_state_number+=1
    # while there is still some state unfinished:
    while len(processing_state_stack)>0:
        # select one state to find all of its goto states
        I=processing_state_stack.pop(0)
        # noticing that the item can be both T and NT, depending on what's next in the production position
        items=I.get_item()
        # iterate through all its items to get all of its pointing states
        for item in items:
            temp=STATE('I'+str(current_state_number))
            # generate such item's reaching state with all of the possible reaching productions
            temp.productions = merge_productions(get_reachable_go_states(I, item))
            string=temp.to_string()
            if string=='':
                continue
            # and if such state doesn't exist in the stateTable, add it into the table
            if string not in state_table.values():
                states.append(temp)
                state_table[temp.name] = string
                DFA.add_state(temp)
                DFA.add_edge(I, item, temp)
                # Tranfer.append((I.name,item['type'],temp.name))
                processing_state_stack.append(temp)
                current_state_number += 1
            # and if such state does exist, add its edges from current state through current item
            else:
                for state in states:
                    if state_table[state.name] == string:
                        DFA.add_edge(I, item, state)
                        # Tranfer.append((I.name, item['type'], state.name))
                        break
    return
# find which state does this state go to through target element
def search_goto_state(I,target):
    for tuple in DFA.edge:
        From, item, To = tuple
        if (From,item)==(I,target):
            return To
    return
def generate_table():
    # ACTION has T*states entries
    global ACTION
    # GOTO has NT*states entries
    global GOTO
    global state_index_table
    global terminal_index_table
    global nonterminal_index_table
    global Reduce
    global Shift
    production_string_group = copy.deepcopy(production_group)
    # print(production_string_group[0].to_string())
    # production_string_group[0].position=0
    # [production_string] list, used for indexing
    production_string_group=[p.to_string() for p in production_string_group]
    states=DFA.state
    edges=DFA.edge
    # <state-numberID>pair, just for reference
    state_index_table = {states[i].name:i for i in range(len(states))}
    # <terminal_symbol-numberID>pair, just for reference
    terminal_index_table = {terminal_symbol_group[i]["type"]:i for i in range(len(terminal_symbol_group))}
    # <non_terminal_symbol-numberID>pair, just for reference
    nonterminal_index_table = {left_group[i]:i for i in range(len(left_group))}
    ACTION=[["" for x in range(len(terminal_symbol_group))] for y in range(len(states))]
    GOTO=[["" for x in range(len(left_group))] for y in range(len(states))]
    # end prodction is S-> program@, derived from start production
    end_production = copy.deepcopy(start_production)
    end_production.position += 1
    # check for each state
    # x--row(state number), y--column(input number)
    for state in states:
        x = state_index_table[state.name]
        lable_group=[p.to_string() for p in state.productions]
        # first check the # case
        if end_production.to_string() in lable_group:
            y = terminal_index_table["#"]
            ACTION[x][y] = 'acc'
            continue
        # then check all the possible N & NT nodes and fill their position in the table
        for production in state.productions:
            expression = production.right
            position = production.position
            if position < len(expression) + 1:
                # node can be either T or NT, find its corresponding y
                # here firstly deal with T case only
                node = expression[position - 1]
                if node['class'] == 'T':
                    y = terminal_index_table[node["type"]]
                    # get To state quickly via checking edges
                    To = search_goto_state(state, node)
                    # no-$ case, where terminal sign is useless
                    if node['type'] != '$':
                        index='s'+To.name[1:]
                        # shift-reduce detection: happen when such entry already has an ACTION
                        if ACTION[x][y] != "" and ACTION[x][y] != index:
                            print("{}shift-reduce conflict detected".format(state.name))
                            print(index, end='->')
                            print(ACTION[x][y])
                            print(state.to_string())
                            print('-------------')
                        ACTION[x][y] = index
                        temp = copy.deepcopy(production)
                        temp.position = 0
                        temp.terminals = ('#')
                        Shift[index] = temp
                    # $ case, meaning that a rule is now complete, key attribute for LR(1) where we need to look at terminals
                    else:
                        # only current production's terminals can be recognized as reduce action
                        for i in range(len(production.terminals)):
                            y = terminal_index_table[production.terminals[i]]
                            temp = copy.deepcopy(production)
                            temp.position = 0
                            temp.terminals = ('#')
                            index = 'r' + str(production_string_group.index(temp.to_string()))
                            # shift-reduce detection: happen when such entry already has an ACTION
                            if ACTION[x][y] != "" and ACTION[x][y] != index:
                                print("{}shift-reduce conflict detected".format(state.name))
                                print(index, end='->')
                                print(ACTION[x][y])
                                print(state.to_string())
                                print(temp.to_string())
                                print('-------------')
                            ACTION[x][y] = index
                            # save the reduce reference production
                            Reduce[index] = temp
            # ending case, also meaning that a rule is now complete, key attribute for LR(1) where we need to look at terminals
            # same as the $ case
            elif position == len(expression) + 1:
                for i in range(len(production.terminals)):
                    y = terminal_index_table[production.terminals[i]]
                    temp=copy.deepcopy(production)
                    temp.position=0
                    temp.terminals=('#')
                    index= 'r'+str(production_string_group.index(temp.to_string()))
                    if ACTION[x][y]!="" and ACTION[x][y]!=index:
                        print("{}shift-reduce conflict detected".format(state.name))
                        print(index,end='->')
                        print(ACTION[x][y])
                        print(state.to_string())
                        print(temp.to_string())
                        print('-------------')
                    ACTION[x][y] =index
                    # save the reduce reference production
                    Reduce[index] = temp
    # now deal with all the NT edges, since no longer need terminal checking,
    # we can just iterate through all NT edges and add them into the GOTO table
    for tuple in edges:
        From,item,To=tuple
        if item['class']=='NT':
            x= state_index_table[From.name]
            y= nonterminal_index_table[item['type']]
            if GOTO[x][y] != "" and GOTO[x][y] != To.name:
                print(To.name,end='->')
                print(GOTO[x][y])
                print('-------------')
            GOTO[x][y]=To.name
    return
# def generate_table():
#     # ACTION has T*states entries
#     global ACTION
#     # GOTO has NT*states entries
#     global GOTO
#     global state_index_table
#     global terminal_index_table
#     global nonterminal_index_table
#     global Reduce
#     global Shift
#     production_string_group = copy.deepcopy(production_group)
#     # print(production_string_group[0].to_string())
#     # production_string_group[0].position=0
#     # [production_string] list, used for indexing
#     production_string_group=[p.to_string() for p in production_string_group]
#     states=DFA.state
#     edges=DFA.edge
#     # <state-numberID>pair, just for reference
#     state_index_table = {states[i].name:i for i in range(len(states))}
#     # <terminal_symbol-numberID>pair, just for reference
#     terminal_index_table = {terminal_symbol_group[i]["type"]:i for i in range(len(terminal_symbol_group))}
#     # <non_terminal_symbol-numberID>pair, just for reference
#     nonterminal_index_table = {left_group[i]:i for i in range(len(left_group))}
#     ACTION=[["" for x in range(len(terminal_symbol_group))] for y in range(len(states))]
#     GOTO=[["" for x in range(len(left_group))] for y in range(len(states))]
#     # end prodction is S-> program@, derived from start production
#     end_production = copy.deepcopy(start_production)
#     end_production.position += 1
#     # check for each state
#     # x--row(state number), y--column(input number)
#     for state in states:
#         x = state_index_table[state.name]
#         lable_group=[p.to_string() for p in state.productions]
#         # first check the # case
#         if end_production.to_string() in lable_group:
#             y = terminal_index_table["#"]
#             ACTION[x][y] = 'acc'
#             continue
#         # then check all the possible N & NT nodes and fill their position in the table
#         for production in state.productions:
#             expression = production.right
#             position = production.position
#             if position < len(expression) + 1:
#                 # node can be either T or NT, find its corresponding y
#                 # here firstly deal with T case only
#                 node = expression[position - 1]
#                 if node['class'] == 'T':
#                     y = terminal_index_table[node["type"]]
#                     # get To state quickly via checking edges
#                     To = search_goto_state(state, node)
#                     # no-$ case, where terminal sign is useless
#                     if node['type'] != '$':
#                         index='s'+To.name[1:]
#                         ACTION[x][y] = index
#                         temp = copy.deepcopy(production)
#                         temp.position = 0
#                         temp.terminals = ('#')
#                         Shift[index] = temp
#                     # $ case, meaning that a rule is now complete, key attribute for LR(1) where we need to look at terminals
#                     else:
#                         # only current production's terminals can be recognized as reduce action
#                         for i in range(len(production.terminals)):
#                             y = terminal_index_table[production.terminals[i]]
#                             temp = copy.deepcopy(production)
#                             temp.position = 0
#                             temp.terminals = ('#')
#                             index = 'r' + str(production_string_group.index(temp.to_string()))
#                             ACTION[x][y] = index
#                             # save the reduce reference production
#                             Reduce[index] = temp
#             # ending case, also meaning that a rule is now complete, key attribute for LR(1) where we need to look at terminals
#             # same as the $ case
#             elif position == len(expression) + 1:
#                 for i in range(len(production.terminals)):
#                     y = terminal_index_table[production.terminals[i]]
#                     temp=copy.deepcopy(production)
#                     temp.position=0
#                     temp.terminals=('#')
#                     index= 'r'+str(production_string_group.index(temp.to_string()))
#                     ACTION[x][y] =index
#                     # save the reduce reference production
#                     Reduce[index] = temp
#     # now deal with all the NT edges, since no longer need terminal checking,
#     # we can just iterate through all NT edges and add them into the GOTO table
#     for tuple in edges:
#         From,item,To=tuple
#         if item['class']=='NT':
#             x= state_index_table[From.name]
#             y= nonterminal_index_table[item['type']]
#             GOTO[x][y]=To.name
#     return

# do syntax analyse
def syntax_analyse(tokens):
    print("step    "," next token    "," state    "," ACTION & GOTO    ")
    step=0
    def find_state_by_name(name):
        for state in DFA.state:
            if state.name==name:
                return state
    end_symbol={'class': 'T', 'type': '#','val':'#'}
    # getting operator in a list
    op_stack=[]
    state_stack=[DFA.state[0]]
    while True:
        reduction_list = []
        current_state=state_stack[-1]
        if len(tokens)==0:
            token = end_symbol
        else:
            token = tokens[0]
        output_token = token['type']
        if token == end_symbol:
            output_token = "EOF"
        token={'class':token['class'],'type':token['type'],'val':token['val']}
        x = state_index_table[current_state.name]
        y = terminal_index_table[token['type']]
        action=ACTION[x][y]
        if action=='':
            ##### print("step:",str(step),"next token:",output_token,"stack:",op_stack_column,"action:","x"," ","")
            print("not matching rule is found, error!")
            break
        if action=='acc':
            step+=1
            op_stack_column = " ".join([x['type'] for x in op_stack])
            ##### print("step:",str(step),"next token:",output_token,"stack:",op_stack_column,"action:",action," ","")
            ##### print("accept!")
            break
        elif action[0]=='s':
            next_state=find_state_by_name('I'+action[1:])
            state_stack.append(next_state)
            Temp =tokens.pop(0)
            Temp= {'class': Temp['class'], 'type': Temp['type'],'val':token['val']}
            op_stack.append(Temp)
            step += 1
            op_stack_column = " ".join([x['type'] for x in op_stack])
            ##### print("step:",str(step),"next token:",output_token,"stack:",op_stack_column,"action:",action," ","")
        elif action[0]=='r':
            production=Reduce[action]
            print("reduction rule: ", production.to_string())
            cnt=len(production.right)
            # if is a x|$ rule, we directly add the LHS NT token and the LHS state because now we don't need to remove a '$' at real (no need to remove 1 element)
            # because actually nothing should be removed
            if cnt==1 and production.right[0]['type'] == '$':
                NT_item = generator.generator(production,reduction_list)
                des = {'class': 'NT', 'type': production.left}
                current_state = state_stack[-1]
                state_stack.append(search_goto_state(current_state, des))
                op_stack.append(NT_item)
                # print("!!!")
                continue
            
            # first copy the production elements into a temporary list
            for i in range(cnt):
                reduction_list.append(op_stack[-cnt+i])
            # print(reduction_list)

            # remove the op_stack and state_stack's RHS element
            for i in range(cnt):
                    item=production.right[cnt-i-1]
                    back = op_stack[-1]
                    if item['class'] != back['class'] and item['type'] != back['type']:
                        print("error")
                        print(item['type'],back['type'])
                    else:
                        op_stack.pop(-1)
                        state_stack.pop(-1)
            # then, according to current state and the LHS of the reducing production, goto a new state.
            current_state = state_stack[-1]

            # generate new NT----------------------------------------------------
            NT=production.left
            # generate mips codes and NT's passing values
            
            NT_values ={'a':1,'b':'2'}

            NT_item = generator.generator(production,reduction_list)
            

            x = state_index_table[current_state.name]
            y = nonterminal_index_table[NT]
            next_state=find_state_by_name(GOTO[x][y])
            state_stack.append(next_state)
            op_stack.append(NT_item)
            # op_stack.append({'class': 'NT', 'type': NT, 'val':NT_values})
            step += 1
            op_stack_column = " ".join([x['type'] for x in op_stack])
            ##### print("step:",str(step),"next token:",output_token,"stack:",op_stack_column,"action:",action,",",next_state.name)
    return


production_group=[]
doted_production_group=[]
terminal_symbol_group=[]
left_group=[]
state_index_table={}
terminal_index_table={}
nonterminal_index_table={}
Reduce={}
Shift={}
start_production=None
ACTION=[]
GOTO=[]
DFA=DFA()
FIRST={}
FOLLOW={}

mips_codes=[]

if __name__=='__main__':
    # first read the grammar we defined, generate LHS set, production set and terminal set
    grammars=open("grammar.txt").read().split('\n\n')
    scan_grammar(grammars)
    # with production sets, expand it into a larger doted production(items)set.
    generate_doted_productions()
    # generate first set
    generate_first_set()
    keys = sorted(FIRST)
    # generate DFA by creating closures
    generate_DFA()
    # generate the table with the help of DFA
    generate_table()
    # load token list from scanner
    tokens = []
    _tokens= open("intermediate_tokens.txt").read().split('\n')
    for token_val in _tokens:
        if token_val != '':
            [token,val] = token_val.split(' | ')

            # print("!",token,val)
            tokens.append({'class': 'T', 'type': token, 'val': val })
    # finally, make syntactic analyse
    syntax_analyse(tokens)
    print("syntax analyse complete")

    # for production in production_group:
    #     print(production.to_string())

    # for line in mips_codes:
    #     print(line)
