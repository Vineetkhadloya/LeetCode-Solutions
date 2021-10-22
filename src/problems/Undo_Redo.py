
undo = []
redo = []

def write(word):
    undo.append(word)

def redo_op():
    undo.append(redo[-1])
    redo.pop()

def undo_op():
    redo.append(undo[-1])
    undo.pop()

def read():
    print(undo)

def QUERY(Q):
 
    # Stores total count
    # of queries
    N = len(Q)
 
    # Traverse all the query
    for i in range(N):
        if(Q[i] == "UNDO"):
            undo_op()
        elif(Q[i] == "REDO"):
            redo_op()
        elif(Q[i] == "READ"):
            read()
        else:
            write(Q[i][6])
 
# Driver Code
Q = ["WRITE A", "WRITE B", "WRITE C",
     "UNDO", "READ", "REDO", "READ"]
QUERY(Q)