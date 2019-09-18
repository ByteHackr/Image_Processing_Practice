# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 18:13:27 2019

@author: BILU
"""

import numpy as np

tic_arr = (-1) * np.ones((3,3),np.uint8)

"""
tic_com = np.array([
                    ([[1,2,3],[1,4,7],[1,5,9]]),
                    ([[1,2,3],[2,5,6]]),
                    ([[1,2,3],[3,5,7],[3,6,9]]),
                    ([[1,4,7],[4,5,6]]),
                    ([[1,5,9],[3,5,7],[4,5,6],[2,5,8]]),
                    ([[3,6,9],[4,5,6]]),
                    ([[1,4,7],[7,5,3],[7,8,9]]),
                    ([[7,8,9],[2,5,8]]),
                    ([[1,5,9],[7,8,9],[3,6,9]])
                    ])
"""
tic_pos = np.array([[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]])

tic_com = np.array([
                    [[1,2,3],[1,4,7],[1,5,9]],
                    [[1,2,3],[2,5,8]],
                    [[1,2,3],[3,5,7],[3,6,9]],
                    [[1,4,7],[4,5,6]],
                    [[4,5,6],[2,5,8],[1,5,9],[3,5,7]],
                    [[3,6,9],[4,5,6]],
                    [[1,4,7],[7,5,3],[7,8,9]],
                    [[7,8,9],[2,5,8]],
                    [[1,5,9],[7,8,9],[3,6,9]]
                    ])

machine_turn = 0
machine_t = []

def Get_arr_items(arr):
    a = tic_arr[tic_pos[arr[0]-1][0]][tic_pos[arr[0]-1][1]]
    b = tic_arr[tic_pos[arr[1]-1][0]][tic_pos[arr[1]-1][1]]
    c = tic_arr[tic_pos[arr[2]-1][0]][tic_pos[arr[2]-1][1]]
    return a,b,c

def Arr_add(arr):
    a,b,c = Get_arr_items(arr)
    return (a+b+c)

def Put_val(pos,val):
    pos = pos - 1
    tic_arr[tic_pos[pos][0]][tic_pos[pos][1]] = val
     
def Tic_logic(t_u):
    print(tic_arr)
    global machine_turn
    flag = 0
    
    if machine_turn != 0:
       for i in range(0,len(tic_com[machine_turn-1])):
            
            get_com = tic_com[machine_turn-1][i]
            ans = Arr_add(get_com)
            
            if ans == -1:
                print(get_com)
                flag=1
                it1 , it2 , it3 = Get_arr_items(get_com)
                if it1 == -1:
                    machine_turn = get_com[0]
                    
                if it2 == -1:
                    machine_turn = get_com[1] 
                    
                if it3 == -1:
                    machine_turn = get_com[2]
                    
                pos = machine_turn
                Put_val(pos,0)
                machine_t.append(machine_turn)
                break
    print(flag,machine_turn)
    
    
    if flag == 0:   
        for i in range(0,len(tic_com[t_u-1])):
            get_com = tic_com[t_u-1][i]
            ans = Arr_add(get_com)
            
            if ans == 1:
                it1 , it2 , it3 = Get_arr_items(get_com)
                if it1 == -1:
                    machine_turn = get_com[0]
                    flag = 1
                    
                if it2 == -1:
                    machine_turn = get_com[1]
                    flag = 1
                    
                if it3 == -1:
                    machine_turn = get_com[2]
                    flag = 1
         
            if flag == 1:
                 machine_t.append(machine_turn)
                 pos = machine_turn
                 Put_val(pos,0)
                 break 
    print(flag,machine_turn)
    
    
    """ FOR FIRST TURN OF THE MACHINE"""
    if machine_turn == 0:
        if tic_arr[tic_pos[4][0]][tic_pos[4][1]] == -1:
            machine_turn = 5
            flag=1
        
        if flag == 0:
            l = 0
            for i in range(0,len(tic_com[t_u-1])):
                get_com = tic_com[t_u-1][i]
                it = Get_arr_items(get_com)
                for j in range(0,len(it)):
                    if it[j] == -1:
                        if len(tic_com[it[j]-1])>l:
                            flag=1
                            machine_turn = get_com[j]
        machine_t.append(machine_turn)
        pos = machine_turn
        Put_val(pos,0)
    ####
    
    
    print(flag,machine_turn)    
    if flag == 0:
        l_m = len(machine_t)
        print(machine_t)
        for k in range(l_m-1,-1,-1):
            for i in range(0,(len(tic_com[machine_t[k]-1]))):
                print(len(tic_com[machine_t[k]-1]))
                get_com = tic_com[machine_t[k]-1][i]
                ans = Arr_add(get_com)
                print(machine_t[k])
                if ans <= -1:
                    print(get_com)
                    #it1 , it2 , it3 = Get_arr_items(get_com)
                    it = Get_arr_items(get_com)
                    for j in range(0,len(it)):
                        if it[j] == -1:
                            machine_turn = get_com[j]
                            flag=1
                            break
                    """
                    if it1 == -1:
                        machine_turn = get_com[0]
                        
                    if it2 == -1:
                        machine_turn = get_com[1] 
                        
                    if it3 == -1:
                        machine_turn = get_com[2]
                    
                    """
                if flag == 1:
                    machine_t.append(machine_turn)
                    pos = machine_turn
                    Put_val(pos,0)
                    break
            if flag == 1:
                    break
            
     
    print(flag,machine_turn)
    
       
def User_input():
    for i in range(0,5):
        turn_user = int(input('ENTER ANY NUM BETWEEEN (1-9) : '))
        pos = turn_user
        Put_val(pos,1)
        Tic_logic(turn_user)
    

User_input()