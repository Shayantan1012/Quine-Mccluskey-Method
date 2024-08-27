import numpy as np

def binary_check(list1,list2):
    cou=0
    for i in range(len(list1)):
        if(list1[i]!=list2[i]):
            cou+=1
    if(cou==1):return True
    else :return False 
    
           
def binary_change(list1,list2):
    list3 = list1.copy()
    for i in range(len(list1)):
        if(list1[i]!=list2[i]):
            list3[i]=3
    return list3        

list1=np.array([0, 0, 1, 1])
list2=[np.array([0, 0, 1, 1]),np.array([0, 1, 0, 1]),np.array([1, 0, 1, 1]),np.array([0, 1, 1, 1])]
final_list=[]
for j in range (len(list2)):
        if(binary_check(list1,list2[j])):
            list3=binary_change(list1,list2[j])
            final_list.append(list3)
            
print(list2)
print(final_list)