# for i in range(1,10):
#     for i in range(1,10):
#         print(i,end=' ')
#     print()

import random
from timeit import repeat

from numpy import mat

# random integer from 0 to 9
# print(num1)

# mtrx = [[2, 9, 1], [1, 4, 5], [9, 2, 3], [1, 2, 3]]
# a=len(mtrx)
# b=len(mtrx[0])
# print('b lenght is:')7
# for i in range(a):
#     for j in range(b):
#         print(mtrx[i][j],end=' ')
#         if mtrx[i][j]==5:
#             print('\n',i,j,'<<<<<<<<<<')
#             continue
#     print()

matrix=[]
for i in range(9):
    c=[]
    for j in range(9):
        num1 = random.randint(1,9)
        c.append(num1)
    matrix.append(c)

matrix_row_len=len(matrix)
matrix_column_len=len(matrix[0])

print("--------------------9 X 9 Matrix---------------------")
for  i in range(matrix_row_len):
    for j in range(matrix_column_len):
        print(matrix[i][j],end=' ')
    print()
print("-----------------------------------------------------")

user_input=int(input("Please Enter Number"))
#-------rows y------------------------------------------------
#------i0----------------
y_index_i0=[]
count_i0=0
temp_i0=None
#-----------i1--------------
y_index_i1=[]
count_i1=0
temp_i1=None
#------i2----------------
y_index_i2=[]
count_i2=0
temp_i2=None
#------i3----------------
y_index_i3=[]
count_i3=0
temp_i3=None
#---i4----------------
y_index_i4=[]
count_i4=0
temp_i4=None
#--i5---
y_index_i5=[]
count_i5=0
temp_i5=None
#----i6----------
y_index_i6=[]
count_i6=0
temp_i6=None
#------i7----------------
y_index_i7=[]
count_i7=0
temp_i7=None
#------i8----------------
y_index_i8=[]
count_i8=0
temp_i8=None
#----
x0_index=None
x1_index=None
x2_index=None
x3_index=None
x4_index=None
x5_index=None
x6_index=None
x7_index=None
x8_index=None
#------------Column x------------------------
j0_index=None
j1_index=None
j2_index=None
j3_index=None
j4_index=None
j5_index=None
j6_index=None
j7_index=None
j8_index=None
#------------j0------------------------
x_index_j0=[]
temp_j0=None
#-----------j1-------------------------
x_index_j1=[]
temp_j1=None
#-------------j2-----------------------
x_index_j2=[]
temp_j2=None
#-------------j2-----------------------
x_index_j3=[]
temp_j3=None
#-------------j2-----------------------
x_index_j4=[]
temp_j4=None
#-------------j2-----------------------
x_index_j5=[]
temp_j5=None
#-------------j2-----------------------
x_index_j6=[]
temp_j6=None
#-------------j2-----------------------
x_index_j7=[]
temp_j7=None
#-------------j2-----------------------
x_index_j8=[]
temp_j8=None


for i in range(matrix_row_len):
    for j in range(matrix_column_len):
        try:
            if i==0:
                if matrix[i][j]==user_input:
                    if temp_i0==None and matrix[i][j+1]==user_input:         
                        temp_i0=matrix[i][j]
                        y_index_i0.append(j)
                        x0_index=0
                        count_i0+=1
                    
                    if temp_i0 != None:  
                        if matrix[i][j-1]==user_input and matrix[i][j]== user_input:
                            y_index_i0.append(j)
                            x0_index=0
                            count_i0+=1
            if i==1:
                if matrix[i][j]==user_input:
                    if temp_i1==None  and matrix[i][j+1]==user_input:         
                        temp_i1=matrix[i][j]
                        y_index_i1.append(j)
                        x1_index=1
                        count_i1+=1
                    
                    if temp_i1 != None:  
                        if matrix[i][j-1]==user_input and matrix[i][j]== user_input:
                            y_index_i1.append(j)
                            x1_index=1
                            count_i1+=1
            if i==2:
                if matrix[i][j]==user_input:
                    if temp_i2==None and matrix[i][j+1]==user_input:         
                        temp_i2=matrix[i][j]
                        y_index_i2.append(j)
                        x2_index=2
                        count_i2+=1
                    
                    if temp_i2 != None:  
                        if matrix[i][j-1]==user_input and matrix[i][j]== user_input:
                            y_index_i2.append(j)
                            x2_index=2
                            count_i2+=1
            if i==3:
                if matrix[i][j]==user_input:
                    if temp_i3==None and matrix[i][j+1]==user_input:        
                        temp_i3=matrix[i][j]
                        y_index_i3.append(j)
                        x3_index=3
                        count_i3+=1
                    
                    if temp_i3 != None:  
                        if matrix[i][j-1]==user_input and matrix[i][j]== user_input:
                            y_index_i3.append(j)
                            x3_index=3
                            count_i3+=1
            if i==4:
                if matrix[i][j]==user_input:
                    if temp_i4==None and j==0:# and matrix[i][j+1]==user_input:         
                        temp_i4=matrix[i][j]
                        y_index_i4.append(j)
                        x4_index=4
                        count_i4+=1
                    
                    if temp_i4 != None:  
                        if matrix[i][j-1]==user_input and matrix[i][j]== user_input:
                            y_index_i4.append(j)
                            x4_index=4
                            count_i4+=1
            if i==5:
                if matrix[i][j]==user_input:
                    if temp_i5==None and matrix[i][j+1]==user_input:         
                        temp_i5=matrix[i][j]
                        y_index_i5.append(j)
                        x5_index=5
                        count_i5+=1
                    
                    if temp_i5 != None:  
                        if matrix[i][j-1]==user_input and matrix[i][j]== user_input:
                            y_index_i5.append(j)
                            x5_index=5
                            count_i5+=1
            if i==6:
                if matrix[i][j]==user_input:
                    if temp_i6==None and matrix[i][j+1]==user_input:         
                        temp_i6=matrix[i][j]
                        y_index_i6.append(j)
                        x6_index=6
                        count_i6+=1
                    
                    if temp_i6 != None:  
                        if matrix[i][j-1]==user_input and matrix[i][j]== user_input:
                            y_index_i6.append(j)
                            x6_index=6
                            count_i6+=1
            if i==7:
                if matrix[i][j]==user_input:
                    if temp_i7==None and matrix[i][j+1]==user_input:         
                        temp_i7=matrix[i][j]
                        y_index_i7.append(j)
                        x7_index=7
                        count_i7+=1
                    
                    if temp_i7 != None:  
                        if matrix[i][j-1]==user_input and matrix[i][j]== user_input:
                            y_index_i7.append(j)
                            x7_index=7
                            count_i7+=1
            if i==8:
                if matrix[i][j]==user_input:
                    if temp_i8==None and matrix[i][j+1]==user_input:         
                        temp_i8=matrix[i][j]
                        y_index_i8.append(j)
                        x8_index=8
                        count_i8+=1
                    
                    if temp_i8 != None:  
                        if matrix[i][j-1]==user_input and matrix[i][j]== user_input:
                            y_index_i8.append(j)
                            x8_index=8
                            count_i8+=1
            #--------------------------------------------Column Logic--------------------------------
            if j==0:
                if matrix[i][j]==user_input:
                    if temp_j0==None and matrix[i+1][j]==user_input:
                        temp_j0=matrix[i][j]
                        x_index_j0.append(i)
                        j0_index=0
                        
                    if temp_j0 != None:
                        if matrix[i-1][j]==user_input and matrix[i][j]== user_input:
                            x_index_j0.append(i)
                            j0_index=0
            #---------------------------------        
            if j==1:
                if matrix[i][j]==user_input:
                    if temp_j1==None and matrix[i+1][j]==user_input:
                        temp_j1=matrix[i][j]
                        x_index_j1.append(i)
                        j1_index=1
                        
                    if temp_j1 != None:
                        if matrix[i-1][j]==user_input and matrix[i][j]== user_input:
                            x_index_j1.append(i)
                            j1_index=1
            #---------------------------------        
            if j==2:
                if matrix[i][j]==user_input:
                    if temp_j2==None and matrix[i+1][j]==user_input:
                        temp_j2=matrix[i][j]
                        x_index_j2.append(i)
                        j2_index=2
                        
                    if temp_j2 != None:
                        if matrix[i-1][j]==user_input and matrix[i][j]== user_input:
                            x_index_j2.append(i)
                            j2_index=2
            #---------------------------------        
            if j==3:
                if matrix[i][j]==user_input:
                    if temp_j3==None and matrix[i+1][j]==user_input:
                        temp_j3=matrix[i][j]
                        x_index_j3.append(i)
                        j3_index=3
                        
                    if temp_j3 != None:
                        if matrix[i-1][j]==user_input and matrix[i][j]== user_input:
                            x_index_j3.append(i)
                            j3_index=3
            #---------------------------------        
            if j==4:
                if matrix[i][j]==user_input:
                    if temp_j4==None and matrix[i+1][j]==user_input:
                        temp_j4=matrix[i][j]
                        x_index_j4.append(i)
                        j4_index=4
                        
                    if temp_j4 != None:
                        if matrix[i-1][j]==user_input and matrix[i][j]== user_input:
                            x_index_j4.append(i)
                            j4_index=4
            #---------------------------------        
            if j==5:
                if matrix[i][j]==user_input:
                    if temp_j5==None and matrix[i+1][j]==user_input:
                        temp_j5=matrix[i][j]
                        x_index_j5.append(i)
                        j5_index=5
                        
                    if temp_j5 != None:
                        if matrix[i-1][j]==user_input and matrix[i][j]== user_input:
                            x_index_j5.append(i)
                            j5_index=5
            #---------------------------------        
            if j==6:
                if matrix[i][j]==user_input:
                    if temp_j6==None and matrix[i+1][j]==user_input:
                        temp_j6=matrix[i][j]
                        x_index_j6.append(i)
                        j6_index=6
                        
                    if temp_j6 != None:
                        if matrix[i-1][j]==user_input and matrix[i][j]== user_input:
                            x_index_j6.append(i)
                            j6_index=6
            #---------------------------------
            if j==7:
                if matrix[i][j]==user_input:
                    if temp_j7==None and matrix[i+1][j]==user_input:
                        temp_j7=matrix[i][j]
                        x_index_j7.append(i)
                        j7_index=7
                        
                    if temp_j7 != None:
                        if matrix[i-1][j]==user_input and matrix[i][j]== user_input:
                            x_index_j7.append(i)
                            j7_index=7
            #--------------------------------
            if j==8:
                if matrix[i][j]==user_input:
                    if temp_j8==None and matrix[i+1][j]==user_input:
                        temp_j8=matrix[i][j]
                        x_index_j8.append(i)
                        j8_index=8
                        
                    if temp_j8 != None:
                        if matrix[i-1][j]==user_input and matrix[i][j]== user_input:
                            x_index_j8.append(i)
                            j8_index=8
            #---------------------------------        
        except Exception as e:
            print("--->handle",e)
            
if (len(x_index_j1) >=2):
    print('Y Index:-',j1_index,'X Index:-',x_index_j1)
if (len(x_index_j2) >=2):
    print('Y Index:-',j2_index,'X Index:-',x_index_j2)
if (len(x_index_j3) >=2):
    print('Y Index:-',j3_index,'X Index:-',x_index_j3)
if (len(x_index_j4) >=2):
    print('Y Index:-',j4_index,'X Index:-',x_index_j4)
if (len(x_index_j5) >=2):
    print('Y Index:-',j5_index,'X Index:-',x_index_j5)
if (len(x_index_j6) >=2):
    print('Y Index:-',j6_index,'X Index:-',x_index_j6)
if (len(x_index_j7) >=2):
    print('Y Index:-',j7_index,'X Index:-',x_index_j7)
if (len(x_index_j8) >=2):
    print('Y Index:-',j8_index,'X Index:-',x_index_j8)
exit()
if (len(y_index_i0) >=2) >= (len(y_index_i1) >=2) and  (len(y_index_i0) >=2) >= (len(y_index_i2) >=2) and  (len(y_index_i0) >=2) >= (len(y_index_i3) >=2) and  (len(y_index_i0) >=2) >= (len(y_index_i4) >=2) and  (len(y_index_i0) >=2) >= (len(y_index_i5) >=2) and  (len(y_index_i0) >=2) >= (len(y_index_i6) >=2) and  (len(y_index_i0) >=2) >= (len(y_index_i7) >=2) and  (len(y_index_i0) >=2) >= (len(y_index_i8) >=2):
    print('X Index:-',x0_index,'Y Index:-',y_index_i0)
    
elif (len(y_index_i1) >=2) > (len(y_index_i0) >=2) and (len(y_index_i1) >=2) > (len(y_index_i2) >=2) and  (len(y_index_i1) >=2) > (len(y_index_i3) >=2) and  (len(y_index_i1) >=2) > (len(y_index_i4) >=2) and  (len(y_index_i1) >=2) > (len(y_index_i5) >=2) and  (len(y_index_i1) >=2) > (len(y_index_i6) >=2) and  (len(y_index_i1) >=2) > (len(y_index_i7) >=2) and  (len(y_index_i1) >=2) > (len(y_index_i8) >=2):
    print('X Index:-',x1_index,'Y Index xxx:-',y_index_i1)
    #--done
elif (len(y_index_i2) >=2) > (len(y_index_i0) >=2) and  (len(y_index_i2) >=2) > (len(y_index_i1) >=2) and  (len(y_index_i2) >=2) > (len(y_index_i3) >=2) and  (len(y_index_i2) >=2) > (len(y_index_i4) >=2) and  (len(y_index_i2) >=2) > (len(y_index_i5) >=2) and  (len(y_index_i2) >=2) > (len(y_index_i6) >=2) and  (len(y_index_i2) >=2) > (len(y_index_i7) >=2) and  (len(y_index_i2) >=2) > (len(y_index_i8) >=2):
    print('X Index:-',x2_index,'Y Index:-',y_index_i2)
    #--done----
elif (len(y_index_i3) >=2) > (len(y_index_i0) >=2) and  (len(y_index_i3) >=2) > (len(y_index_i1) >=2) and  (len(y_index_i3) >=2) > (len(y_index_i2) >=2) and  (len(y_index_i3) >=2) > (len(y_index_i4) >=2) and  (len(y_index_i3) >=2) > (len(y_index_i5) >=2) and  (len(y_index_i3) >=2) > (len(y_index_i6) >=2) and  (len(y_index_i3) >=2) > (len(y_index_i7) >=2) and  (len(y_index_i3) >=2) > (len(y_index_i8) >=2):
    print('X Index:-',x3_index,'Y Index:-',y_index_i3)
    #---done-----
elif (len(y_index_i4) >=2) > (len(y_index_i0) >=2) and  (len(y_index_i4) >=2) > (len(y_index_i1) >=2) and  (len(y_index_i4) >=2) > (len(y_index_i2) >=2) and  (len(y_index_i4) >=2) > (len(y_index_i3) >=2) and  (len(y_index_i4) >=2) > (len(y_index_i5) >=2) and  (len(y_index_i4) >=2) > (len(y_index_i6) >=2) and  (len(y_index_i4) >=2) > (len(y_index_i7) >=2) and  (len(y_index_i4) >=2) > (len(y_index_i8) >=2):
    print('X Index:-',x4_index,'Y Index:-',y_index_i4)
    #-----done-----
elif (len(y_index_i5) >=2) > (len(y_index_i0) >=2) and  (len(y_index_i5) >=2) > (len(y_index_i1) >=2) and  (len(y_index_i5) >=2) > (len(y_index_i2) >=2) and  (len(y_index_i5) >=2) > (len(y_index_i3) >=2) and  (len(y_index_i5) >=2) > (len(y_index_i4) >=2) and  (len(y_index_i5) >=2) > (len(y_index_i6) >=2) and  (len(y_index_i5) >=2) > (len(y_index_i7) >=2) and  (len(y_index_i5) >=2) > (len(y_index_i8) >=2):
    print('X Index:-',x5_index,'Y Index:-',y_index_i5)
    #-done---
elif (len(y_index_i6) >=2) > (len(y_index_i0) >=2) and  (len(y_index_i6) >=2) > (len(y_index_i1) >=2) and  (len(y_index_i6) >=2) > (len(y_index_i2) >=2) and  (len(y_index_i6) >=2) > (len(y_index_i3) >=2) and  (len(y_index_i6) >=2) > (len(y_index_i4) >=2) and  (len(y_index_i6) >=2) > (len(y_index_i5) >=2) and  (len(y_index_i6) >=2) > (len(y_index_i7) >=2) and  (len(y_index_i6) >=2) > (len(y_index_i8) >=2):
    print('X Index:-',x6_index,'Y Index:-',y_index_i6)
    #----done------
elif (len(y_index_i7) >=2) > (len(y_index_i0) >=2) and  (len(y_index_i7) >=2) > (len(y_index_i1) >=2) and  (len(y_index_i7) >=2) > (len(y_index_i2) >=2) and  (len(y_index_i7) >=2) > (len(y_index_i3) >=2) and  (len(y_index_i7) >=2) > (len(y_index_i4) >=2) and  (len(y_index_i7) >=2) > (len(y_index_i5) >=2) and  (len(y_index_i7) >=2) > (len(y_index_i6) >=2) and  (len(y_index_i7) >=2) > (len(y_index_i8) >=2):
    print('X Index:-',x7_index,'Y Index:-',y_index_i7)
    #--done----
elif (len(y_index_i8) >=2) > (len(y_index_i0) >=2) and  (len(y_index_i8) >=2) > (len(y_index_i1) >=2) and  (len(y_index_i8) >=2) > (len(y_index_i2) >=2) and  (len(y_index_i8) >=2) > (len(y_index_i3) >=2) and  (len(y_index_i8) >=2) > (len(y_index_i4) >=2) and  (len(y_index_i8) >=2) > (len(y_index_i5) >=2) and  (len(y_index_i8) >=2) > (len(y_index_i6) >=2) and  (len(y_index_i8) >=2) > (len(y_index_i7) >=2):
    print('X Index:-',x8_index,'Y Index:-',y_index_i8)
#--done---start compair----
#---i0-----
else:
    if (len(y_index_i0) >=2) == (len(y_index_i1) >=2):  
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        
    elif (len(y_index_i0) >=2) == (len(y_index_i2) >=2): 
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        
    elif (len(y_index_i0) >=2) == (len(y_index_i3) >=2): 
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        
    elif (len(y_index_i0) >=2) == (len(y_index_i4) >=2): 
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        
    elif (len(y_index_i0) >=2) == (len(y_index_i5) >=2):
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    elif (len(y_index_i0) >=2) == (len(y_index_i6) >=2): 
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    elif (len(y_index_i0) >=2) == (len(y_index_i7) >=2): 
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    elif (len(y_index_i0) >=2) == (len(y_index_i8) >=2): 
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)
    #---i1-----
    elif (len(y_index_i1) >=2) == (len(y_index_i0) >=2):  
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    elif (len(y_index_i1) >=2) == (len(y_index_i2) >=2):
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        
    elif (len(y_index_i1) >=2) == (len(y_index_i3) >=2): 
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        
    elif (len(y_index_i1) >=2) == (len(y_index_i4) >=2): 
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        
    elif (len(y_index_i1) >=2) == (len(y_index_i5) >=2): 
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    elif (len(y_index_i1) >=2) == (len(y_index_i6) >=2): 
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    elif (len(y_index_i1) >=2) == (len(y_index_i7) >=2): 
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    elif (len(y_index_i1) >=2) == (len(y_index_i8) >=2):
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        
    #------i2----------------
    elif (len(y_index_i2) >=2) == (len(y_index_i0) >=2):  
        print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    elif (len(y_index_i2) >=2) == (len(y_index_i1) >=2):
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        
    elif (len(y_index_i2) >=2) == (len(y_index_i3) >=2): 
        print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        
    elif (len(y_index_i2) >=2) == (len(y_index_i4) >=2): 
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        
    elif (len(y_index_i2) >=2) == (len(y_index_i5) >=2): 
        print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    elif (len(y_index_i2) >=2) == (len(y_index_i6) >=2): 
        print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    elif (len(y_index_i2) >=2) == (len(y_index_i7) >=2): 
        print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    elif (len(y_index_i2) >=2) == (len(y_index_i8) >=2):
        print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        
    #---i3--------------------
    elif (len(y_index_i3) >=2) == (len(y_index_i0) >=2):  
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    elif (len(y_index_i3) >=2) == (len(y_index_i1) >=2):
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        
    elif (len(y_index_i3) >=2) == (len(y_index_i2) >=2): 
        print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        
    elif (len(y_index_i3) >=2) == (len(y_index_i4) >=2): 
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        
    elif (len(y_index_i3) >=2) == (len(y_index_i5) >=2): 
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    elif (len(y_index_i3) >=2) == (len(y_index_i6) >=2): 
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    elif (len(y_index_i3) >=2) == (len(y_index_i7) >=2): 
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    elif (len(y_index_i3) >=2) == (len(y_index_i8) >=2):
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)
    #------i4----------------
    elif (len(y_index_i4) >=2) == (len(y_index_i0) >=2):  
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    elif (len(y_index_i4) >=2) == (len(y_index_i1) >=2):
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        
    elif (len(y_index_i4) >=2) == (len(y_index_i2) >=2): 
        print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        
    elif (len(y_index_i4) >=2) == (len(y_index_i3) >=2): 
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        
    elif (len(y_index_i4) >=2) == (len(y_index_i5) >=2): 
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    elif (len(y_index_i4) >=2) == (len(y_index_i6) >=2): 
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    elif (len(y_index_i4) >=2) == (len(y_index_i7) >=2): 
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    elif (len(y_index_i4) >=2) == (len(y_index_i8) >=2):
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)

    #----------i5-----
        
    elif (len(y_index_i5) >=2) == (len(y_index_i0) >=2):  
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    elif (len(y_index_i5) >=2) == (len(y_index_i1) >=2):
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    elif (len(y_index_i5) >=2) == (len(y_index_i2) >=2): 
        print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    elif (len(y_index_i5) >=2) == (len(y_index_i3) >=2): 
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    elif (len(y_index_i5) >=2) == (len(y_index_i4) >=2):
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    elif (len(y_index_i5) >=2) == (len(y_index_i6) >=2): 
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    elif (len(y_index_i5) >=2) == (len(y_index_i7) >=2): 
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    elif (len(y_index_i5) >=2) == (len(y_index_i8) >=2):
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)

    #------i6------------
    
    elif (len(y_index_i6) >=2) == (len(y_index_i0) >=2):  
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    elif (len(y_index_i6) >=2) == (len(y_index_i1) >=2):
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    elif (len(y_index_i6) >=2) == (len(y_index_i2) >=2): 
        print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    elif (len(y_index_i6) >=2) == (len(y_index_i3) >=2): 
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    elif (len(y_index_i6) >=2) == (len(y_index_i4) >=2):
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    elif (len(y_index_i6) >=2) == (len(y_index_i5) >=2): 
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    elif (len(y_index_i6) >=2) == (len(y_index_i7) >=2): 
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    elif (len(y_index_i6) >=2) == (len(y_index_i8) >=2):
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)

    #---i7-----
    elif (len(y_index_i7) >=2) == (len(y_index_i0) >=2):  
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    elif (len(y_index_i7) >=2) == (len(y_index_i1) >=2):
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        
    elif (len(y_index_i7) >=2) == (len(y_index_i2) >=2): 
        print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    elif (len(y_index_i7) >=2) == (len(y_index_i3) >=2): 
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    elif (len(y_index_i7) >=2) == (len(y_index_i4) >=2):
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    elif (len(y_index_i7) >=2) == (len(y_index_i5) >=2): 
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    elif (len(y_index_i7) >=2) == (len(y_index_i6) >=2): 
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    elif (len(y_index_i7) >=2) == (len(y_index_i8) >=2):
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)
    #-----i8-----  
    elif (len(y_index_i8) >=2) == (len(y_index_i0) >=2):  
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    elif (len(y_index_i8) >=2) == (len(y_index_i1) >=2):
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        
    elif (len(y_index_i8) >=2) == (len(y_index_i2) >=2): 
        print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        
    elif (len(y_index_i8) >=2) == (len(y_index_i3) >=2): 
        print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        
    elif (len(y_index_i8) >=2) == (len(y_index_i4) >=2):
        print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        
    elif (len(y_index_i8) >=2) == (len(y_index_i5) >=2): 
        print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        
    elif (len(y_index_i8) >=2) == (len(y_index_i6) >=2): 
        print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        
    elif (len(y_index_i8) >=2) == (len(y_index_i8) >=2):
        print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        print('X Index:-',x8_index,'Y Index:-',y_index_i8)
    
# else:
#     if (len(y_index_i0) >=2) == (len(y_index_i1) >=2) and  (len(y_index_i0) >=2) > (len(y_index_i2) >=2) and  (len(y_index_i0) >=2) > (len(y_index_i3) >=2) and  (len(y_index_i0) >=2) > (len(y_index_i4) >=2) and  (len(y_index_i0) >=2) > (len(y_index_i5) >=2) and  (len(y_index_i0) >=2) > (len(y_index_i6) >=2) and  (len(y_index_i0) >=2) > (len(y_index_i7) >=2) and  (len(y_index_i0) >=2) > (len(y_index_i8) >=2):
#         print('X Index:-',x0_index,'Y Index:-',y_index_i0)       
    
    
    
    
    
    
    
    


#----dublicate
    # if (len(y_index_i0) >=2) == (len(y_index_i1) >=2):  
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        
    # if (len(y_index_i0) >=2) == (len(y_index_i2) >=2): 
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
    #     print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        
    # if (len(y_index_i0) >=2) == (len(y_index_i3) >=2): 
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        
    # if (len(y_index_i0) >=2) == (len(y_index_i4) >=2): 
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        
    # if (len(y_index_i0) >=2) == (len(y_index_i5) >=2):
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    # if (len(y_index_i0) >=2) == (len(y_index_i6) >=2): 
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    # if (len(y_index_i0) >=2) == (len(y_index_i7) >=2): 
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    # if (len(y_index_i0) >=2) == (len(y_index_i8) >=2): 
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)
    # #---i1-----
    # if (len(y_index_i1) >=2) == (len(y_index_i0) >=2):  
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    # if (len(y_index_i1) >=2) == (len(y_index_i2) >=2):
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
    #     print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        
    # if (len(y_index_i1) >=2) == (len(y_index_i3) >=2): 
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        
    # if (len(y_index_i1) >=2) == (len(y_index_i4) >=2): 
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        
    # if (len(y_index_i1) >=2) == (len(y_index_i5) >=2): 
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    # if (len(y_index_i1) >=2) == (len(y_index_i6) >=2): 
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    # if (len(y_index_i1) >=2) == (len(y_index_i7) >=2): 
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    # if (len(y_index_i1) >=2) == (len(y_index_i8) >=2):
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        
    # #------i2----------------
    # if (len(y_index_i2) >=2) == (len(y_index_i0) >=2):  
    #     print('X Index:-',x2_index,'Y Index:-',y_index_i2)
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    # if (len(y_index_i2) >=2) == (len(y_index_i1) >=2):
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
    #     print('X Index:-',x2_index,'Y Index:-',y_index_i2)
        
    # if (len(y_index_i2) >=2) == (len(y_index_i3) >=2): 
    #     print('X Index:-',x2_index,'Y Index:-',y_index_i2)
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        
    # if (len(y_index_i2) >=2) == (len(y_index_i4) >=2): 
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        
    # elif (len(y_index_i2) >=2) == (len(y_index_i5) >=2): 
    #     print('X Index:-',x2_index,'Y Index:-',y_index_i2)
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    # if (len(y_index_i2) >=2) == (len(y_index_i6) >=2): 
    #     print('X Index:-',x2_index,'Y Index:-',y_index_i2)
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    # if (len(y_index_i2) >=2) == (len(y_index_i7) >=2): 
    #     print('X Index:-',x2_index,'Y Index:-',y_index_i2)
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    # if (len(y_index_i2) >=2) == (len(y_index_i8) >=2):
    #     print('X Index:-',x2_index,'Y Index:-',y_index_i2)
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        
    # #---i3--------------------
    # if (len(y_index_i3) >=2) == (len(y_index_i0) >=2):  
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    # if (len(y_index_i3) >=2) == (len(y_index_i1) >=2):
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        
    # if (len(y_index_i3) >=2) == (len(y_index_i2) >=2): 
    #     print('X Index:-',x2_index,'Y Index:-',y_index_i2)
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
        
    # if (len(y_index_i3) >=2) == (len(y_index_i4) >=2): 
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        
    # if (len(y_index_i3) >=2) == (len(y_index_i5) >=2): 
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    # if (len(y_index_i3) >=2) == (len(y_index_i6) >=2): 
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    # if (len(y_index_i3) >=2) == (len(y_index_i7) >=2): 
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    # if (len(y_index_i3) >=2) == (len(y_index_i8) >=2):
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)
    # #------i4----------------
    # if (len(y_index_i4) >=2) == (len(y_index_i0) >=2):  
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    # if (len(y_index_i4) >=2) == (len(y_index_i1) >=2):
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        
    # if (len(y_index_i4) >=2) == (len(y_index_i2) >=2): 
    #     print('X Index:-',x2_index,'Y Index:-',y_index_i2)
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        
    # if (len(y_index_i4) >=2) == (len(y_index_i3) >=2): 
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
        
    # if (len(y_index_i4) >=2) == (len(y_index_i5) >=2): 
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    # if (len(y_index_i4) >=2) == (len(y_index_i6) >=2): 
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    # if (len(y_index_i4) >=2) == (len(y_index_i7) >=2): 
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    # if (len(y_index_i4) >=2) == (len(y_index_i8) >=2):
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)

    # #----------i5-----
        
    # if (len(y_index_i5) >=2) == (len(y_index_i0) >=2):  
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    # if (len(y_index_i5) >=2) == (len(y_index_i1) >=2):
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    # if (len(y_index_i5) >=2) == (len(y_index_i2) >=2): 
    #     print('X Index:-',x2_index,'Y Index:-',y_index_i2)
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    # if (len(y_index_i5) >=2) == (len(y_index_i3) >=2): 
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    # if (len(y_index_i5) >=2) == (len(y_index_i4) >=2):
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
        
    # if (len(y_index_i5) >=2) == (len(y_index_i6) >=2): 
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    # if (len(y_index_i5) >=2) == (len(y_index_i7) >=2): 
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    # if (len(y_index_i5) >=2) == (len(y_index_i8) >=2):
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)

    # #------i6------------
    
    # if (len(y_index_i6) >=2) == (len(y_index_i0) >=2):  
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    # if (len(y_index_i6) >=2) == (len(y_index_i1) >=2):
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    # if (len(y_index_i6) >=2) == (len(y_index_i2) >=2): 
    #     print('X Index:-',x2_index,'Y Index:-',y_index_i2)
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    # if (len(y_index_i6) >=2) == (len(y_index_i3) >=2): 
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    # if (len(y_index_i6) >=2) == (len(y_index_i4) >=2):
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    # if (len(y_index_i6) >=2) == (len(y_index_i5) >=2): 
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
        
    # if (len(y_index_i6) >=2) == (len(y_index_i7) >=2): 
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    # if (len(y_index_i6) >=2) == (len(y_index_i8) >=2):
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)

    # #---i7-----
    # if (len(y_index_i7) >=2) == (len(y_index_i0) >=2):  
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    # if (len(y_index_i7) >=2) == (len(y_index_i1) >=2):
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        
    # if (len(y_index_i7) >=2) == (len(y_index_i2) >=2): 
    #     print('X Index:-',x2_index,'Y Index:-',y_index_i2)
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    # if (len(y_index_i7) >=2) == (len(y_index_i3) >=2): 
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    # if (len(y_index_i7) >=2) == (len(y_index_i4) >=2):
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    # if (len(y_index_i7) >=2) == (len(y_index_i5) >=2): 
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    # if (len(y_index_i7) >=2) == (len(y_index_i6) >=2): 
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
        
    # if (len(y_index_i7) >=2) == (len(y_index_i8) >=2):
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)
    # #-----i8-----  
    # if (len(y_index_i8) >=2) == (len(y_index_i0) >=2):  
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)
    #     print('X Index:-',x0_index,'Y Index:-',y_index_i0)
        
    # if (len(y_index_i8) >=2) == (len(y_index_i1) >=2):
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)
    #     print('X Index:-',x1_index,'Y Index:-',y_index_i1)
        
    # if (len(y_index_i8) >=2) == (len(y_index_i2) >=2): 
    #     print('X Index:-',x2_index,'Y Index:-',y_index_i2)
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        
    # if (len(y_index_i8) >=2) == (len(y_index_i3) >=2): 
    #     print('X Index:-',x3_index,'Y Index:-',y_index_i3)
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        
    # if (len(y_index_i8) >=2) == (len(y_index_i4) >=2):
    #     print('X Index:-',x4_index,'Y Index:-',y_index_i4)
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        
    # if (len(y_index_i8) >=2) == (len(y_index_i5) >=2): 
    #     print('X Index:-',x5_index,'Y Index:-',y_index_i5)
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        
    # if (len(y_index_i8) >=2) == (len(y_index_i6) >=2): 
    #     print('X Index:-',x6_index,'Y Index:-',y_index_i6)
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)
        
    # if (len(y_index_i8) >=2) == (len(y_index_i8) >=2):
    #     print('X Index:-',x7_index,'Y Index:-',y_index_i7)
    #     print('X Index:-',x8_index,'Y Index:-',y_index_i8)
