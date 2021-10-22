import math

pricelist = ["item1: 100","item2: 200"]
logs = ["sell 12, item2, 2",
        "supply 0, item1, 2",
        "discount 16, 10, 40",
        "supply 20, item2, 1",
        "sell 5, item1, 1",
        "sell 10, item1, 2",
        "supply 2, item2, 3",
        "sell 25, item2, 2",
        ]

logs = sorted(logs, key=lambda s: int(((s.split(', ')[0]).split(' ',1)[1])) )
print(logs)

inventory = {}
income = 0
discount_start = 0
discount_end = 0
discount_percent = 0

price_dict = {}
for i in pricelist:
    item_price = i.split(": ")
    price_dict[item_price[0]] = int(item_price[1])

print(price_dict)

for tran in logs:
    print("Tran = ",tran)
    data = tran.split(", ")
    op_n_time = data[0].split(" ")
    op = op_n_time[0]
    time = int(op_n_time[1])
    tran_quantity = int(data[2])

    # SUPPLY
    if(op == "supply"):
        inventory.update({data[1]:inventory.get(data[1],0)+tran_quantity})
    # SELL
    elif(op == "sell"):
        if(inventory.get(data[1]) < tran_quantity):
            continue

        inventory.update({data[1]:inventory.get(data[1],0)-tran_quantity})
        
        if(time>= discount_start and time < discount_end) :
            income += math.ceil(int(price_dict[data[1]]) * (100 - discount_percent)/100)*tran_quantity
        else:
            income += int(price_dict[data[1]])*tran_quantity
    #DISCOUNT
    else:
        discount_start = int(op_n_time[1])
        discount_end = discount_start + int(data[1])
        discount_percent = int(data[2])

print(income)
