import random
goods=['zeszyt','ksiazka 1','ksiazka 2','ksiazka 3','olowek','dlugopis','zeszyt 2', 'zeszyt 3','gumka']
days=['poniedzialek','wtorek','sroda','czwartek','piatek','sobota']
day=0
number_of_sale=1
for i in range(1,51):
    
    if day>5:
        day=0

    all_sales=[i,days[day]]
    
    if days[day] == 'sobota':
        amount_of_sales=random.randrange(12,30,1)
    else:
        amount_of_sales=random.randrange(12,55,1)
    print('Ilosc sprzedazy w dniu',i,'=',amount_of_sales)
    
    for q in range(1,amount_of_sales+1):
        sale=[number_of_sale,i,days[day]]
        amount_of_goods=random.randrange(1,6,1)
        print('Ilosc towarow w sprzedazy',number_of_sale,'=',amount_of_goods)
        for a in range(0,amount_of_goods):
            temp=random.randrange(0,len(goods)-1,1)
            sale.append(goods[temp])

        number_of_sale+=1
        print(sale)
    day+=1


