import sys

def tree(acts,words):
    btree = []
    openidx = []
    wid = 0

    previous_act = 'N'

    size_tree = 0
    max_size_tree = len(words)


    nts=[]
    skip=[]
    
    
    for act in acts:
        if act[0] == 'S' and act[1] == 'H':
            if len(words) != 0:
                btree.append(words[0])
                del words[0]
                
                wid += 1
            previous_act = 'S'
            size_tree += 1

        elif (act[0] == 'S' and act[1] == 'L') or act[0] == 'I':
            if len(nts)==0 and act[0] == 'S':
                #print(act)
                new_act="IN(IN:"
                aux=act.split(':')[1]
                #print(aux)
                for c in range(len(aux)):
                    new_act+=aux[c]

                act=new_act
                #print(act)
                #exit(0)
                
            action=act.split('(')[0]
            name=act[3:-1]
            if len(nts)==0 or (nts[-1]=='IN' and action=='SL') or (nts[-1]=='SL' and action=='IN'):
                
            
                btree.append("["+name.split('#')[0])
                openidx.append(len(btree)-2)
                previous_act = 'N'
                nts.append(act.split('(')[0])
                
            else:
                
                #print(words)
                #print(nts)
                
                skip.append(name)
                #print(skip)

            #print('NT',nts,skip)
        else:#REDUCE
            action=act.split('(')[0]
            name=act[3:-1]
            #print('RE',nts)
            if name not in skip:
                btree.append("]")
                last_nt=nts.pop()

                previous_act = 'R'
            #else:
            #    exit(0)

        #print(nts)
    '''
    if len(openidx)>0:
        tope = len(openidx)
        for i in range(tope):
            tmp = " ".join(btree[openidx[-1]:])+")"
            btree = btree[:openidx[-1]]
            btree.append(tmp)
            openidx = openidx[:-1]

    if len(btree)>1:
        print('(TOP', end='')
        for i in range(len(btree)):
                print(btree[i], end='')
        print(')')  
    else:
        print(btree[0])
    '''
    print(' '.join(btree))



if __name__ == "__main__":

        words = []
        text = []
        for line in open(sys.argv[2]):
                line=line.strip()
                if line !=  "":
                        ws = line.split("\t")
                        for i in range(len(ws)):
                                if ws[i]=='ROOT':
                                        continue
                                words.append(ws[i])
                        text.append(words)
                        words = []

        allactions = []
        actions = []

        sent = 0
        for line in open(sys.argv[1]):
            line=line.strip()
            if line != "":
                trans = line.split("\t")
                num_shift = 0
                num_nt = 0
                num_reduce = 0
                for i in range(len(trans)):
                                actions.append(trans[i])
                                if trans[i][0] == 'S' and trans[i][1] == 'H': num_shift=num_shift+1
                                #if trans[i][0] == 'N': num_nt=num_nt+1
                                #if trans[i][0] == 'R': num_reduce=num_reduce+1

                if len(text[sent])!=num_shift:
                                print('FALLO: ',sent,len(text[sent]),num_shift)
                                print(text[sent])
                                print(actions)
                                exit(0)

                allactions.append(actions)
                actions=[]
                sent = sent + 1

        for i in range(len(text)):
                tree(allactions[i], text[i]);
        #exit(0)
        
        
