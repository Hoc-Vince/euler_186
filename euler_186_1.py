number=000000
p=1

    
if __name__ == "__main__":
    values=[]
    for i in range (1,10000000):
        if i >= 1 and i <=55:
            values.append((100003 - (i*200003) + 300007*(i**(3))) % 1000000)
        else:
            values.append((values[i-25]+values[i-56]) % 1000000)
    print(f'Telecom db generated with {len(values)} rows')
    abon_base=[]
    for abon in range(1000000):
        abon_base.append([abon])
    print(f'Clients db generated with {len(abon_base)} rows')
    miscalled_values=0
    exit_trigger=False
    iter_num=0
    while exit_trigger!=True:
        #get line
        line = (iter_num //2 +1)
        #print(f'row:{line}')
        caller_id = values[iter_num]
        #print(f'DB Cell:{iter_num+1} Caller ID:{caller_id}')
        called_id = values[iter_num+1]
        #print(f'DB Cell:{iter_num+2} Called ID:{called_id}')
        if called_id == caller_id:
            miscalled_values+=1
            print('Misscall detected!')
        else:
            #process of friendship
            #print(f'Trying to extend abon_base[caller_id] {abon_base[caller_id]} with abon_base[called_id] {abon_base[called_id]}')
            abon_base[caller_id].extend(abon_base[called_id])
            abon_base[caller_id]=list(set(abon_base[caller_id]))
            #print(f'Trying to extend abon_base[caller_id] {abon_base[called_id]} with abon_base[called_id] {abon_base[caller_id]}')
            abon_base[called_id].extend(abon_base[caller_id])
            abon_base[called_id]=list(set(abon_base[called_id]))
            #print(f'Result{abon_base[caller_id]}')
            #print(f'Result{abon_base[caller_id]}')
            prime_minister_friends_share=len(set(abon_base[number]))/1000000
            #print(f'prime_minister_friends_share {prime_minister_friends_share}')
        iter_num+=2
        if prime_minister_friends_share>=(p/100):
            exit_trigger=True
            result = iter_num/2-miscalled_values
        elif iter_num == 10000000:
            exit_trigger=True
        else:
            if iter_num % 1000 == 0:
                print(f'Percent completed={iter_num/1000000}')
                print(f'prime_minister_friends_share {prime_minister_friends_share}')
    print(f'Result:{result}')
            
       








        
        
    