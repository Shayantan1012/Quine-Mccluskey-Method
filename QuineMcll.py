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
            list3[i]=-1
    return list3        

def  check_same_binary(arr1,cou):
    cou1=0
    
    for i in range(len(arr1)):
        if(arr1[i]==1):
            cou1+=1
            
    if(cou1==cou):return True
    else: return False
    

    
def group_for_same_binary_ones(list):
    ans_list=[]#It carries the total group of the final list
    cou=0
   # length=len(list[0]["binary"])
    length=len(list)
    for x in range(0,length):
        list2=[]
        binaryList=[]
        #Loop for clubing the groups of single bit difference
        dic2 = {}
        for y in list: #Triversing the dictanary
            if (check_same_binary(y["binary"],cou)):
                list2.append(y["minterm"][0])
                binaryList.append(y["binary"])
        if(len(list2)!=0 and len(binaryList)!=0):dic2.update({"minterms":list2,"binaryList":binaryList})    
        if(len(dic2)!=0):ans_list.append(dic2)
        cou+=1
            
    return ans_list

def decimal_to_binary(n):
    if n == 0:
        binary_num = [0]
    else:
        binary_num = []
        while n > 0:
            binary_num.append(int(n % 2))
            n = n // 2
        binary_num.reverse()
    
    binary_array = np.array(binary_num)
    
    return binary_array
    

#Function for Clubing the elements of bitdifference One
def Bit_dif_one(list):
    final_list=[]

    ########################################### l1 is the list of the elements##################
    for k in range (len(list)-1):#Triversing Over the Main List
        l1 = list[k]['binaryList'].copy()#Having Individual List K
        list2=list[k+1]['binaryList'].copy()#Having Individual List K+1
        l1_minterms=list[k]['minterms'].copy()#Having Individual MInterms K
        l2_minterms=list[k+1]['minterms'].copy()#Having Individual MInterms K+1
        
        for i in range(len(l1)):  #Trivarsing over L1 and Take individual elements
            list1=l1[i].copy()

            for j in range (len(list2)): #Trivarsing over L2 and Take individual elements
                    dic={}
                    minterms=[]
                    minterms.append(l1_minterms[i])
                    if(binary_check(list1,list2[j])):
                        list3=binary_change(list1,list2[j])
                        minterms.append(l2_minterms[j])
                        dic.update({'minterm':minterms,'binary':list3})
                        final_list.append(dic)

    
    return final_list;    

#Function for checking two binary numbers in ##########
def check_binary(l1,l2):
    for i in range (len(l1)):
        if(l1[i]==-1 and l2[i]!=-1):
            return False
        elif(l1[i]!=-1 and l2[i]==-1):
            return False
    cou=0
    for i in range(len(l1)):
        if(l1[i]==-1):continue
        if(l1[i]!=l2[i]):cou+=1
        
    if(cou==1):return True
    else: return False         
            
def change_binary(l1,l2):
    for i in range (len(l1)):
        if(l1[i]!=l2[i]):l1[i]=-1    
    return     
def check_minterms_array(l1,l2):
    for i in range(len(l1)):
        flag=False
        for j in range (len(l2)):
            if(l1[i]==l2[j]):flag=True
        if(flag==False):return False;
        
    return True
    
def common_elements_checks(list):
    k=0
    while k < len(list) - 1:  # Traverse over the main list
        l1 = list[k]['binary']  # Individual List K
        l1_minterms = list[k]['minterm']  # Individual Minterms K
        i = k + 1
        while i < len(list):  # Traverse over the remaining elements in the list
            l2 = list[i]['binary']  # Individual List i
            l2_minterms = list[i]['minterm']  # Individual Minterms i
            
            if check_minterms_array(l1_minterms, l2_minterms):
                list.pop(i)  # Remove the combined element                
            else:
                i += 1  # Increment i only if no element is removed
        k += 1  # Move to the next element in the list

    return list


def check_binary_sctrings(list):
    for i in range (len(list)-1):
        binary1=list[i]['binary']
        for j in range (i+1,len(list)):
            binary2=list[j]['binary']
            flag=check_binary(binary1,binary2)
            if(flag==True):return True
    
    return False;         
  
    
    ########################## This Code snippet will return a final list #####################
def final_step_minimization(list1):
    list=list1.copy()
    not_stop=True
    while(not_stop):
        k = 0
        while k < len(list) - 1:  # Traverse over the main list
            l1 = list[k]['binary']  # Individual List K
            l1_minterms = list[k]['minterm']  # Individual Minterms K
            i = k + 1
            while i < len(list):  # Traverse over the remaining elements in the list
                l2 = list[i]['binary']  # Individual List i
                l2_minterms = list[i]['minterm']  # Individual Minterms i
                if check_binary(l1, l2):
                    change_binary(l1, l2)
                    list[k]['minterm'] = l1_minterms + l2_minterms
                    list.pop(i)  # Remove the combined element
                    
                else:
                    i += 1  # Increment i only if no element is removed
            k += 1  # Move to the next element in the list
        common_elements_checks(list)
        not_stop=check_binary_sctrings(list)

    return list;    
def finalStringGenarator(minterm,binaryList):
    epi=[]

    res=str()
    for i in range(len(binaryList)):
        if(binaryList[i]['minterm']==minterm):
         string=''
         for j in range(len(binaryList[i]['binary'])):
             if(binaryList[i]['binary'][j]==1):
                 string=string+chr(65+j)
             elif(binaryList[i]['binary'][j]==0):
                 string=string+chr(65+j)+'`'
         res+=str(string)
    return res

def Essential_prime_implicants(list,binaryList):
    grid=[]
    del_cols=[]
    essi_pi=[]
    for i in range(len(list)):
        minterms=list[i]['Minterms']
        grid=list[i]['Grid']
        for i in range(len(minterms)):
            grid[minterms[i]]=1;
    ########### List ##########
    for i in range(len(grid)):
        couOne=[]
        for j in range (len(list)):
            if(list[j]['Grid'][i]==1):couOne.append(j)
        finalAns=''
        if(len(couOne)==1): #This is a Essential Prime Implicant
            finalAns=finalStringGenarator(list[couOne[0]]['Minterms'],binaryList) 
            if(essi_pi.count(finalAns)==0):essi_pi.append(finalAns)  
            if(del_cols.count(couOne) == 0):del_cols.append(couOne)
            
    final=''
    for i in range (len(essi_pi)):
                 final+=essi_pi[i]+'+'
    if final.endswith('+'):
        final = final[:-1]   
        
        
    return final,del_cols;   


#####COL dominace#######
def check_cols(final_grid,i,j):
    cou1_i=0
    cou1_j=0
    max_col_pre=True
    for k in range (len(final_grid)):
        grid=final_grid[k]['Grid']
        if((grid[j]==1 and grid[i]!=1)):
            max_col_pre=False
        else:
            if(grid[i]==1):cou1_i+=1
            if(grid[j]==1):cou1_j+=1
    max_one_col=0;        
    if(cou1_i==0 or cou1_j==0):max_col_pre=False
    if(cou1_i>=cou1_j):max_one_col=i
    else:max_one_col=j
    return max_one_col,max_col_pre
    

def ColumnDominance(final_grid):
    i=0
    n=len(final_grid[0]['Grid'])
    while(i<n):
        j=0
        while(j<n):
            if(j==i):
                j+=1
                continue
            max_one_col,max_col_pre=check_cols(final_grid,i,j)
            if(max_col_pre):
                k=max_one_col
                for l in range(len(final_grid)):
                    col=final_grid[l]['Grid']
                    col[k]=0
                        
            j+=1              
        i+=1

    
  
#####Row dominace#######
def check_rows(final_grid,i,j):
    cou1_i=0
    cou1_j=0
    min_row_pre=True
    for k in range (len(final_grid[0]['Grid'])):
        grid1=final_grid[i]['Grid']
        grid2=final_grid[j]['Grid']
        if(grid1[k]==1 and grid2[k]!=1):
            min_row_pre=False
        else:
            if(grid1[k]==1):cou1_i+=1
            if(grid2[k]==1):cou1_j+=1
    min_one_row=0;        
    if(cou1_i==0 or cou1_j==0):min_row_pre=False
    if(cou1_i<=cou1_j):min_one_row=i
    else:min_one_row=j
    return min_one_row,min_row_pre

def RowDominance(final_grid):
    i=0
    n=len(final_grid)
    while(i<n):
        j=0
        while(j<n):
            if(j==i):
                j+=1
                continue
            min_one_row,min_row_pre=check_rows(final_grid,i,j)
            if(min_row_pre):
                k=min_one_row
                final_grid[k]['Grid'].fill(0)
                       
            j+=1              
        i+=1
        
                                            #Main code for Exicution#

                                
# Input for the number of variables
x = int(input("How many variables do you want? -> "))

print("\nGive the minterms--->")

power = pow(2, x)  # Calculate the power of 2 raised to the number of variables

# Input for the minterms (all at once, separated by spaces)
minterms = list(map(int, input("Enter the minterms separated by spaces -> ").split()))

# Validate the minterms
minterms = [m for m in minterms if 0 <= m < power]  # Keep only valid minterms within the range

print("\nGive the don't cares--->")

# Input for the don't cares (all at once, separated by spaces)
dont_cares = list(map(int, input("Enter the don't cares separated by spaces -> ").split()))

# Validate the don't cares
dont_cares = [d for d in dont_cares if 0 <= d < power]  # Keep only valid don't cares within the range

# Print the final lists
print("\nMinterms:", minterms)
print("Don't Cares:", dont_cares)



print("Minterms->",str(minterms).ljust(5)+"     "+"DONT'CARES->",str(dont_cares).ljust(5))

minterms=minterms+dont_cares

minterms.sort()
#minterms=[2,3,4,5,6,7,9,10,11,13,14,15]
#minterms=[4,5,6,8,9,10,13,14,15]

#minterms=[0,2,4,9,11,14,15,16,17,19,23,25,29,31]
a=0
#a=int(input("Give the number of minterms ->"))

#minterms = list(map(int, input("Enter the minterms separated by space: ").split()))
max_len=0
list_min_binary=[]
max_len = len(decimal_to_binary(max(minterms)))
for x in minterms:
    
    binary = decimal_to_binary(x)# Convert the decimal number to binary
    for i in range(0,max_len-len(binary)):
        binary = np.insert(binary, 0, 0)
    min=[]
    min.append(x)
    dic1={
        "minterm":min,
        "binary":binary,
    }
    
    list_min_binary.append(dic1)
#print(list_min_binary)

not_stop=True;
print("The List for Decimal To Binary Convertion->>>>>>>") 
print("    ")
   
max_minterm_length = max(len(str(item['minterm'][0])) for item in list_min_binary)
max_binary_length = max(len(str(item['binary'])) for item in list_min_binary)
minterm_column_width = max_minterm_length + 5
binary_column_width = max_binary_length + 5
for item in list_min_binary:
    print(f"MINTERM: {str(item['minterm'][0]).ljust(minterm_column_width)} Binary Conversion-> {str(item['binary']).ljust(binary_column_width)}")
print("    ")


print("The List for the Binary digits of one Bit Difference->>>>>>>>>")    
print("    ")

grouped_binary=group_for_same_binary_ones(list_min_binary)
#print(grouped_binary)

max_minterm_length = max(len(str(item)) for group in grouped_binary for item in group['minterms'])
max_binary_length = max(len(str(item)) for group in grouped_binary for item in group['binaryList'])

minterm_column_width = max_minterm_length + 5
binary_column_width = max_binary_length + 5
for group in grouped_binary:
    for minterm, binary in zip(group['minterms'], group['binaryList']):
        print(f"MINTERM: {str(minterm).ljust(minterm_column_width)} Binary Conversion-> {str(binary).ljust(binary_column_width)}")
    print('---------------------------------------------------------------------------------')    
print("    ")



final_list=Bit_dif_one(grouped_binary)

print("The List for the binary digits with one Bit Difference------->>>>>>>>>")    
max_minterm_length = max(len(str(item['minterm'])) for item in final_list)
max_binary_length = max(len(str(item['binary'])) for item in final_list)

minterm_column_width = max_minterm_length + 5
binary_column_width = max_binary_length + 5

for item in final_list:
    print(f"MINTERM: {str(item['minterm']).ljust(minterm_column_width)} Binary Conversion-> {str(item['binary']).ljust(binary_column_width)}")
print("    ")

list=final_step_minimization(final_list)
print('---------------------------------------------------------------------------------')    
max_minterm_length = max(len(str(item['minterm'])) for item in list)
max_binary_length = max(len(str(item['binary'])) for item in list)
minterm_column_width = max_minterm_length + 5
binary_column_width = max_binary_length + 5
for i in range(len(list)):
    print(f"MINTERM: {str(list[i]['minterm']).ljust(minterm_column_width)} Binary Conversion-> {str(list[i]['binary']).ljust(binary_column_width)}")
print("    ")###############This is the List that we need #################

max_num =max(minterms);



final_grid_dic=[]

for i in range(len(list)):
    arr=np.zeros((max_num+1),dtype=int)
    minterms=list[i]['minterm']
    if (len(dont_cares)!=0):
        for i in range(len(dont_cares)):
            if(minterms.count(dont_cares[i])!=0):
                minterms.remove(dont_cares[i])
    if(len(minterms)!=0):            
        row={"Minterms":minterms,
            "Grid":arr,}
        final_grid_dic.append(row)
print("------------------------------->>>>>")


epi,del_col=Essential_prime_implicants(final_grid_dic,list)

print("  ")

# Calculate column widths based on the longest string representations of Minterms and Grid
max_minterms_length = max(len(str(final_grid_dic[i]['Minterms'])) for i in range(len(final_grid_dic)))
minterms_column_width = max_minterms_length 

# Determine the number of columns in the grid
num_grid_columns = len(final_grid_dic[0]['Grid'])
grid_column_width = 3 * num_grid_columns + 5

# Creating header and subheader strings
header = f"{'MINTERMS'.ljust(minterms_column_width)} | {'GRID'.ljust(grid_column_width)}"
subheader = f"{' '.ljust(minterms_column_width)} | {'  '.join(f'{i}'.center(0) for i in range(num_grid_columns))}"

# Print the main header and subheader with separators
separator = '-' * len(header)
print(header)
print(subheader)
print(separator)

# Loop through the dictionary to print each row with formatted columns
for i in range(len(final_grid_dic)):
    # Extract Minterms and Grid values for each entry
    minterms = final_grid_dic[i]['Minterms']
    grid = final_grid_dic[i]['Grid']
    
    # Convert Grid: Replace 1 with 'X', keep other values as empty spaces
    grid_str = '  '.join(['X' if x == 1 else ' ' for x in grid])

    # Print the formatted table row with column separators
    print(f"{str(minterms).ljust(minterms_column_width)} | {grid_str.ljust(grid_column_width)}")

    # Print a line separator after each row
    print(separator)
    
    

#####Fill the remaining prime implicants with all zeroes####
for i in range(len(del_col)):
    arr=final_grid_dic[del_col[i][0]]['Grid']
    arr.fill(0)
    
        
print("--------------------------------------------------")
if(len(epi)!=0):
    print("The essential prime Implicants are->",epi) 
else:
    print("No essential prime Implicants Exists.") 
print(" ")


print("After deliting the essential prime implicants------>")

print("   ")

print("  ")

# Calculate column widths based on the longest string representations of Minterms and Grid
max_minterms_length = max(len(str(final_grid_dic[i]['Minterms'])) for i in range(len(final_grid_dic)))
minterms_column_width = max_minterms_length 

# Determine the number of columns in the grid
num_grid_columns = len(final_grid_dic[0]['Grid'])
grid_column_width = 3 * num_grid_columns + 5

# Creating header and subheader strings
header = f"{'MINTERMS'.ljust(minterms_column_width)} | {'GRID'.ljust(grid_column_width)}"
subheader = f"{' '.ljust(minterms_column_width)} | {'  '.join(f'{i}'.center(0) for i in range(num_grid_columns))}"

# Print the main header and subheader with separators
separator = '-' * len(header)
print(header)
print(subheader)
print(separator)

# Loop through the dictionary to print each row with formatted columns
for i in range(len(final_grid_dic)):
    # Extract Minterms and Grid values for each entry
    minterms = final_grid_dic[i]['Minterms']
    grid = final_grid_dic[i]['Grid']
    
    # Convert Grid: Replace 1 with 'X', keep other values as empty spaces
    grid_str = '  '.join(['X' if x == 1 else ' ' for x in grid])

    # Print the formatted table row with column separators
    print(f"{str(minterms).ljust(minterms_column_width)} | {grid_str.ljust(grid_column_width)}")

    # Print a line separator after each row
    print(separator)
    
#################### COLUMN Dominance ##########

ColumnDominance(final_grid_dic);    

print("Now After checking the COLUMN Dominance The Matrix becomes----------------")

print("  ")

print("  ")

# Calculate column widths based on the longest string representations of Minterms and Grid
max_minterms_length = max(len(str(final_grid_dic[i]['Minterms'])) for i in range(len(final_grid_dic)))
minterms_column_width = max_minterms_length 

# Determine the number of columns in the grid
num_grid_columns = len(final_grid_dic[0]['Grid'])
grid_column_width = 3 * num_grid_columns + 5

# Creating header and subheader strings
header = f"{'MINTERMS'.ljust(minterms_column_width)} | {'GRID'.ljust(grid_column_width)}"
subheader = f"{' '.ljust(minterms_column_width)} | {'  '.join(f'{i}'.center(0) for i in range(num_grid_columns))}"

# Print the main header and subheader with separators
separator = '-' * len(header)
print(header)
print(subheader)
print(separator)

# Loop through the dictionary to print each row with formatted columns
for i in range(len(final_grid_dic)):
    # Extract Minterms and Grid values for each entry
    minterms = final_grid_dic[i]['Minterms']
    grid = final_grid_dic[i]['Grid']
    
    # Convert Grid: Replace 1 with 'X', keep other values as empty spaces
    grid_str = '  '.join(['X' if x == 1 else ' ' for x in grid])

    # Print the formatted table row with column separators
    print(f"{str(minterms).ljust(minterms_column_width)} | {grid_str.ljust(grid_column_width)}")

    # Print a line separator after each row
    print(separator)
    
    
RowDominance(final_grid_dic)
print(" ")
print("Now After checking the ROW Dominance The Matrix becomes----------------")

print("  ")

# Calculate column widths based on the longest string representations of Minterms and Grid
max_minterms_length = max(len(str(final_grid_dic[i]['Minterms'])) for i in range(len(final_grid_dic)))
minterms_column_width = max_minterms_length 

# Determine the number of columns in the grid
num_grid_columns = len(final_grid_dic[0]['Grid'])
grid_column_width = 3 * num_grid_columns + 5

# Creating header and subheader strings
header = f"{'MINTERMS'.ljust(minterms_column_width)} | {'GRID'.ljust(grid_column_width)}"
subheader = f"{' '.ljust(minterms_column_width)} | {'  '.join(f'{i}'.center(0) for i in range(num_grid_columns))}"

# Print the main header and subheader with separators
separator = '-' * len(header)
print(header)
print(subheader)
print(separator)

# Loop through the dictionary to print each row with formatted columns
for i in range(len(final_grid_dic)):
    # Extract Minterms and Grid values for each entry
    minterms = final_grid_dic[i]['Minterms']
    grid = final_grid_dic[i]['Grid']
    
    # Convert Grid: Replace 1 with 'X', keep other values as empty spaces
    grid_str = '  '.join(['X' if x == 1 else ' ' for x in grid])

    # Print the formatted table row with column separators
    print(f"{str(minterms).ljust(minterms_column_width)} | {grid_str.ljust(grid_column_width)}")

    # Print a line separator after each row
    print(separator)
    


finalAns_str="";
for i in range (len(final_grid_dic)):
    minterm=final_grid_dic[i]['Minterms']
    grid=final_grid_dic[i]['Grid']
    if(  np.sum(grid == 1)!=0):
        finalAns_str+=finalStringGenarator(minterm,list)+"+"
        
     
        
print("   ")
print("The final minimized answer is->>>",finalAns_str+epi);   
print("   ")
            