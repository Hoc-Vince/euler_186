number=000000
p=1

def generator(end):
    values=[]
    for i in range (1,end):
        if i >= 1 and i <=55:
            values.append((100003 - (i*200003) + 300007*(i**(3))) % 1000000)
        else:
            values.append((values[i-24]+values[i-55]) % 1000000)
    return values

def misscalled(list_1):
    for i in range(0,len(list_1),2):
        if list_1[i] == list_1[i+1]:
            print(f'Miscalled!!! Element k:{i} -> value{list_1[i]} to k+1:{i+1} -> value{list_1[i+1]}')
        else:
            pass



if __name__ == "__main__":
    print(misscalled(generator(1000)))




        

    


        
        
    