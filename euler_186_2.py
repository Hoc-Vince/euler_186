from time import perf_counter


number=11112
p=1
abon_base_init = 1000000


if __name__ == "__main__":
    values=[]
    for i in range (1,10000000):
        if i >= 1 and i <=55:
            values.append((100003 - (i*200003) + 300007*(i**(3))) % 1000000)
        else:
            values.append((values[i-25]+values[i-56]) % 1000000)
    print(f'Telecom db generated with {len(values)} rows')
    abon_base=[]
    for abon in range(abon_base_init):
        abon_base.append([abon])
    print(f'Clients db generated with {len(abon_base)} rows')
    miscalled_values=0
    exit_trigger=False
    iter_num=0
    while exit_trigger!=True:
        #get line
        start_0 = perf_counter()
        line = (iter_num //2 +1)
        print(f'row:{line}')
        caller_id = values[iter_num]
        print(f'DB Cell:{iter_num+1} Caller ID:{caller_id}')
        called_id = values[iter_num+1]
        print(f'DB Cell:{iter_num+2} Called ID:{called_id}')
        caller_list_index=0
        called_list_index=0
        abon_base_len = (len(abon_base))
        end_0 = perf_counter()
        if called_id == caller_id:
            miscalled_values+=1
            #print('Misscall detected!')
        else:
            precise_search= False
            start1 = perf_counter()
            try:
                print('Start presice search')
                pst_1=perf_counter()
                for j in range(caller_id-(abon_base_init-abon_base_len-10),caller_id+(abon_base_init-abon_base_len+10)):
                    print(j)
                    if caller_id in abon_base[j]:
                        caller_list_index=j
                        print(f'FOUND caller_list_index = {j}')
                pst_2=perf_counter()
                for k in range(called_id-(abon_base_init-abon_base_len-10),called_id+(abon_base_init-abon_base_len+10)):
                    print(k)
                    if called_id in abon_base[k]:
                        called_list_index=k
                        print(f'FOUND called_list_index = {k}')
                pst_3=perf_counter()
                if called_list_index !=0 and caller_list_index !=0:
                    precise_search=True
                print('END presice search')
                pst_4=perf_counter()
                print(f'presice search result:/n  abon_base[caller]: {abon_base[j]} abon_base[called]: {abon_base[k]}')
            except:
                pass
            finally:
                print('Start broad search')
                if precise_search != True:
                    for i in range(abon_base_len):
                        #let's search around initial position
                        if caller_id in abon_base[i]:
                            caller_list_index=i
                        if called_id in abon_base[i]:
                            called_list_index=i
                        if called_list_index !=0 and caller_list_index !=0:
                            print('END broad search from break')
                            break
            end1_1 = perf_counter()
            if caller_list_index != called_list_index:
                print(f'abon_base[caller_list_index]= {abon_base[caller_list_index]} abon_base[called_list_index]= {abon_base[called_list_index]} ')
                abon_base[caller_list_index].extend(abon_base.pop(called_list_index))
            end1_2 = perf_counter()
            for i in range(abon_base_len):
                if number in abon_base[i]:
                    pm_index=i
                    break
            end1_3 = perf_counter()
            prime_minister_friends_share=len(set(abon_base[pm_index]))/1000000
            end = perf_counter()
            print(f'prime_minister_friends_share {prime_minister_friends_share}')
            print(f'Abon_base: {abon_base_len}')
            print(f'Presice search duration {pst_4-pst_1}')
            print(f'Presice search {pst_2-pst_1} {pst_3-pst_2} {pst_4-pst_3}')
            print(f'iteration duration {end-start_0}')
            print(f'init {end_0-start_0}')
            print(f'for_1 {end1_1-start1}')
            print(f'list extending {end1_2-end1_1}')
            print(f'for_2 {end1_3-end1_2}')

        iter_num+=2
        if prime_minister_friends_share >= (p/1000):
            exit_trigger=True
            result = iter_num/2-miscalled_values
        elif iter_num == 10000000:
            exit_trigger=True
        else:
            if iter_num % 1000 == 0:
                print(f'Percent completed={iter_num/100}')
                print(f'prime_minister_friends_share {prime_minister_friends_share}')
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








        
        
    