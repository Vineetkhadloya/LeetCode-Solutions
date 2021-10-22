import sys

batch_size = 5
transfer_limit = 3
fraud_window_size = 5

transactions = []
op = []

transactions = ['deposit,1,200','transfer,1,2,200','deposit,2,200','transfer,2,1,200','transfer,1,3,100','transfer,1,2,100','transfer,3,2,100']
invovled = []

for i in range(0,len(transactions),batch_size):
    customer_transactions = {}
    flag_dict = {}
    batch = transactions[i:i+batch_size]
    #print(batch)
    for i in range(len(batch)):
        transaction_type = batch[i].split(',')

        if(transaction_type[0] == "deposit"):
            invovled.append([transaction_type[1]])
            if(transaction_type[1] not in customer_transactions.keys()):
                flag_dict[transaction_type[1]] = False
                customer_transactions[transaction_type[1]] = int(transaction_type[2])
            else:
                customer_transactions[transaction_type[1]] += int(transaction_type[2])

        elif transaction_type[0] == "withdraw":
            invovled.append([transaction_type[1]])
            if(transaction_type[1] not in customer_transactions.keys()):
                flag_dict[transaction_type[1]] = False
                customer_transactions[transaction_type[1]] = -1*int(transaction_type[2])
            else:
                customer_transactions[transaction_type[1]] -= int(transaction_type[2])
        else:
            invovled.append([transaction_type[1],transaction_type[2]])

            if(transaction_type[1] not in customer_transactions.keys()):
                flag_dict[transaction_type[1]] = False
                customer_transactions[transaction_type[1]] = -1*int(transaction_type[3])
            else:
                customer_transactions[transaction_type[1]] -= int(transaction_type[3])

            if(transaction_type[2] not in customer_transactions.keys()):
                flag_dict[transaction_type[2]] = False
                customer_transactions[transaction_type[2]] = int(transaction_type[3])
            else:
                customer_transactions[transaction_type[2]] += int(transaction_type[3])

    for key,value in customer_transactions.items():
        print(str(key)+","+str(value))

    print("")
    v = []
    flag = 0
    for i in invovled[max(0,len(invovled)-fraud_window_size):len(invovled)]:
        for j in i:
            v.append(j)
    #print(v)
    for i in v:
        if(v.count(i)>transfer_limit):
            flag_dict[i] = True
            flag = 1
    if flag == 0:
        print("EMPTY")
    else:
        x = ""
        for k,v in flag_dict.items():
            if v == True:
                x = x + str(k)+ " " 
        print(x)
    print("")
    