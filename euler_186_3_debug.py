from time import perf_counter


number=000000
p=1
abon_base_init = 1000000
pm_index=None

if __name__ == "__main__":
    values=[]
    print(f'Telecom db generation started')
    for i in range (1,10000000):
        if i >= 1 and i <=55:
            values.append((100003 - (i*200003) + 300007*(i**(3))) % 1000000)
        else:
            values.append((values[i-25]+values[i-56]) % 1000000)
    print(f'Telecom db generated with {len(values)} rows')
    miscalled_values=0
    exit_trigger=False
    iter_num=0
    friends_db=[]
    while exit_trigger!=True:
        #get line
        start_0 = perf_counter()
        line = (iter_num //2 +1)
        print(f'row:{line}')
        caller_id = values[iter_num]
        print(f'DB Cell:{iter_num+1} Caller ID:{caller_id}')
        called_id = values[iter_num+1]
        print(f'DB Cell:{iter_num+2} Called ID:{called_id}')
        caller_list_index=None
        called_list_index=None
        
        if friends_db != []:
            if caller_id == called_id:
                miscalled_values+=1
                #print('Misscall detected!')
            
            for i in range(len(friends_db)):
                if caller_id in friends_db[i]:
                    caller_list_index=i
                    #print(f'caller_list_index = {caller_list_index} caller_id value: {friends_db[caller_list_index]} ')
                if called_id in friends_db[i]:
                    called_list_index=i
                    #print(f'called_list_index = {called_list_index} called_id value: {friends_db[called_list_index]} ')
                if called_list_index !=None and caller_list_index !=None:
                    #print('END broad search from break')
                    break
            #print('END broad search')
            #print('LOGIC -------------- LOGIC')
            #
            if called_list_index == None and caller_list_index == None:
                #print('friends_db.append([called_id,caller_id])')
                friends_db.append([called_id,caller_id])

            #    
            if called_list_index != None and caller_list_index == None:
                #print('friends_db[called_list_index].extend([caller_id])')
                friends_db[called_list_index].extend([caller_id])
            if called_list_index == None and caller_list_index != None:
                #print('friends_db[caller_list_index].extend([called_id])')
                friends_db[caller_list_index].extend([called_id])
            
            #
            if called_list_index !=None and caller_list_index !=None:
                print('friends_db[caller_list_index].extend(friends_db.pop(called_list_index))')
                friends_db[caller_list_index].extend(friends_db.pop(called_list_index))

            #result
            #print(f'END ------ LOGIC --------- END')
            #print(f'RESULT: {friends_db} ')

        else:
            friends_db.append([called_id,caller_id])

        
        for i in range(len(friends_db)):
            if number in friends_db[i]:
                pm_index=i
                break
        if pm_index != None:
            prime_minister_friends_share=(1+len(friends_db[pm_index]))/1000000
        else:
            prime_minister_friends_share=1/abon_base_init
        
        print(f'prime_minister_friends_share {prime_minister_friends_share}')
        iter_num+=2
        if prime_minister_friends_share >= (p/100):
            exit_trigger=True
            result = iter_num/2-miscalled_values
        elif iter_num == abon_base_init:
            exit_trigger=True
        else:
            if iter_num % 10000 == 0:
                print(f'Percent completed={iter_num/100}')
                print(f'prime_minister_friends_share {prime_minister_friends_share}')
                end_1=perf_counter()
                print(f'TIME CUMULATIVE: {end_1-start_0}')
    print(f'Result:{result}')
            
'''
caller=4
called=1
alpha_list=[[0],[1,2],[3],[4,5]]
if caller==called:
    print("skip this is miscall call")
else:
    for i in range(len(alpha_list)):
        if caller in alpha_list[i]:
            caller_list_index=i
        if called in alpha_list[i]:
            called_list_index=i
    if caller_list_index == called_list_index:
        print('already friends')
    if caller_list_index != called_list_index:
        print(alpha_list[caller_list_index].extend(alpha_list.pop(called_list_index)))
print(alpha_list)


'''       








        
        
    