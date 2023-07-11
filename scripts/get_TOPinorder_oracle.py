import sys
import types


def is_next_open_bracket(line, start_idx):
    for char in line[(start_idx + 1):]:
        if char == '[':
            return True
        elif char == ']':
            return False
    raise IndexError('Bracket possibly not balanced, open bracket not followed by closed bracket')    

def get_between_brackets(line, start_idx):
    output = []
    for char in line[(start_idx + 1):]:
        if char == ']':
            break
        assert not(char == '[')
        output.append(char)    
    return ''.join(output)


def get_nonterminal(line, start_idx):
    assert line[start_idx] == '[' # make sure it's an open bracket
    output = []
    for char in line[(start_idx + 1):]:
        if char == ' ':
            break
        assert not(char == '[') and not(char == ']')
        output.append(char)
    return ''.join(output)

def get_word(line, start_idx):
    #assert line[start_idx] == '(' # make sure it's an open bracket
    output = []
    for char in line[(start_idx + 1):]:
        if char == ']':
            break
        if char == ' ':
            continue
        #assert not(char == '(') and not(char == ')')
        output.append(char)
    return ''.join(output)

def get_actions(line):
    output_actions = []
    line_strip = line.rstrip()
    i = 0
    max_idx = (len(line_strip) - 1)
    curr_NTs = []
    while i <= max_idx:
        #assert line_strip[i] == '[' or line_strip[i] == ']'
        #print('inicio',line_strip[i])
        if line_strip[i] == '[':
            #if is_next_open_bracket(line_strip, i): # open non-terminal
                curr_NT = get_nonterminal(line_strip, i)
                curr_NTs.append(curr_NT)
                if curr_NT[0] == 'I':
                    output_actions.append('IN(' + curr_NT + ')')
                else:
                    output_actions.append('SL(' + curr_NT + ')')
                #output_actions.append('NT(' + curr_NT + ')')
                i += 1  
                while line_strip[i] != ' ': # get the next open bracket, which may be a terminal or another non-terminal
                    i += 1
                i += 1
                #print(line_strip[i],curr_NT)
        elif line_strip[i] != '[' and line_strip[i] != ']': # it's a terminal symbol
                #word = get_word(line_strip, i)
                #if word == ".." or word == ",,":
                #    output_actions.append('SHIFT('+word+')')
                #else:
                output_actions.append('SHIFT')

                #output_actions.append('SHIFT')
                while line_strip[i] != ' ':
                    i += 1
                i += 1
                #while line_strip[i] == ' '_strip[i] != '[':
                #    i += 1
        elif line_strip[i] == ']':
             output_actions.append('RE')
             curr_NT=curr_NTs.pop()
             #output_actions.append('RE('+ curr_NT + ')') 
             if i == max_idx:
                 break
             i += 1
             while line_strip[i] == ' ':
                 i += 1
             
             #while line_strip[i] != ']' and line_strip[i] != '[':
             #    i += 1
        #exit(0)
    assert i == max_idx  
    return output_actions

def construct(actions, trees):
    while len(actions) > 0:
        act = actions[0]
        actions = actions[1:]
        if (act[0] == 'S' and act[1] == 'L') or act[0] == 'I':
            tree = [act]
            actions, tree = construct(actions,tree)
            trees.append(tree)
        elif act[0] == 'S' and act[1] == 'H':
            trees.append(act)
        elif act[0] == 'R':
            break;
        else:
            assert False
    return actions, trees

def get_actions2(trees, actions):
    if type(trees[1]) == list: #types.ListType:
        actions = get_actions2(trees[1], actions)
    else:
        actions.append(trees[1])

    assert type(trees[0]) == str  #types.StringType
    #print(trees[0][2])
    if trees[0][3] == 'I':
        actions.append("IN"+trees[0][2:])
    else:
        actions.append("SL"+trees[0][2:])
        
    for item in trees[2:]:
        if type(item) == list: #types.ListType:
            actions = get_actions2(item, actions)
        else:
            actions.append(item)
    #actions.append("RE"+trees[0][2:])
    actions.append("RE")
    return actions	

def main():
    #if len(sys.argv) != 4:
    #    raise NotImplementedError('Program only takes three arguments:  en|ch train file and dev file (for vocabulary mapping purposes)')
    #assert sys.argv[1] == "ch" or sys.argv[1] == "en"

    #train_file = open(sys.argv[2], 'r')
    #lines = train_file.readlines()
    #train_file.close()
    dev_file = open(sys.argv[1], 'r')
    dev_lines = dev_file.readlines()
    dev_file.close()
    #words_list = get_dictionary.get_dict(lines) 
    line_ctr = 0
    # get the oracle for the train file
    for line in dev_lines:
        line_ctr += 1
        # assert that the parenthesis are balanced
        if line.count('[') != line.count(']'):
            raise NotImplementedError('Unbalanced number of parenthesis in line ' + str(line_ctr)) 
        # first line: the bracketed tree itself itself 
        #print('# ' + line.rstrip()) #Ponemos ! para que coincida con lo que envio LIU
        #tags, tokens, lowercase = get_tags_tokens_lowercase(line)
        #assert len(tags) == len(tokens)
        #assert len(tokens) == len(lowercase)
        #print(' '.join(tags))
        #print(' '.join(tokens))
        #print(' '.join(lowercase))
        #unkified = unkify(tokens, words_list, sys.argv[1])    
        #print(' '.join(unkified))
        output_actions = get_actions(line)
        _, trees = construct(output_actions, [])

        output_actions2 = get_actions2(trees[0], [])
        #print('\t'.join(output_actions))
        for action in output_actions2:
            print(action, end='\t')
        print('TERM')
        #print('')
    

if __name__ == "__main__":
    main()
