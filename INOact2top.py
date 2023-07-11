import sys

def tree(acts,words):
    btree = []
    openidx = []
    wid = 0

    previous_act = 'N'

    size_tree = 0
    max_size_tree = len(words)

    for act in acts:
        if act[0] == 'S' and act[1]=='H':
            if len(words) != 0:
                btree.append(words[0])
                del words[0]
                
                wid += 1
            previous_act = 'S'
            size_tree += 1

        elif (act[0] == 'S' and act[1] == 'L') or act[0] == 'I':
            btree.insert(-1,"["+act[3:-1])
            openidx.append(len(btree)-2)
            previous_act = 'N'
        else:#REDUCE

            if len(openidx)>0:
                tmp = " ".join(btree[openidx[-1]:])+" ]"
                btree = btree[:openidx[-1]]
                btree.append(tmp)
                openidx = openidx[:-1]
            previous_act = 'R'


    if len(openidx)>0:
        tope = len(openidx)
        for i in range(tope):
            tmp = " ".join(btree[openidx[-1]:])+" ]"
            btree = btree[:openidx[-1]]
            btree.append(tmp)
            openidx = openidx[:-1]

    if len(btree)>1:
        print('[IN:GET_EVENT', end='')
        for i in range(len(btree)):
                print(btree[i], end='')
        print(' ]')  
    else:
        print(btree[0])




if __name__ == "__main__":


    text = []
    words = []
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

    #print(text[0])
    #print(allpos[0])
    #exit(0)

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

    #print(allactions[0])
    #print(text[0])
    #print(len(allactions),len(text))
    #exit(0)    

    for i in range(len(text)):
        tree(allactions[i], text[i]);
        #exit(0)
        
        
