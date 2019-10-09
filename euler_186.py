number=5079
p=1

def generator(end):
    values=[]
    for i in range (1,end):
        if i >= 1 and i <=55:
            values.append((100003 - (i*200003) + 300007*(i**(3))) % 1000000)
        else:
            values.append((values[i-24]+values[i-55]) % 1000000)
    return values

    
if __name__ == "__main__":
    abon_base=[]
    for abon in range(1000000):
        abon_base.append([abon])
    print(f'Clients db generated with {len(abon_base)} rows')
    miscalled_values=0
    exit_trigger=False
    iter_num=2
    while exit_trigger!=True:
        #get line
        print(f'iteration:{iter_num-1}')
        line = (iter_num //2 +1)
        caller_id = generator(iter_num).pop()
        print(f'Caller ID:{caller_id}')
        called_id = generator(iter_num+1).pop()
        print(f'Called ID:{called_id}')
        if called_id == caller_id:
            miscalled_values+=1
            print('Misscall detected!')
        #process of friendship
        print(f'Trying to extend abon_base[caller_id] {abon_base[caller_id]} with abon_base[called_id] {abon_base[called_id]}')
        abon_base[caller_id].extend(abon_base[called_id])
        print(f'Trying to extend abon_base[caller_id] {abon_base[called_id]} with abon_base[called_id] {abon_base[caller_id]}')
        abon_base[called_id].extend(abon_base[caller_id])
        print(f'Result{abon_base[caller_id]}')
        print(f'Result{abon_base[caller_id]}')
        prime_minister_friends_share=len(set(abon_base[number]))/10000
        print(f'prime_minister_friends_share {prime_minister_friends_share}')
        iter_num+=1
        if prime_minister_friends_share>=0.0005:
            exit_trigger=True
        else:
            pass








        
        
    