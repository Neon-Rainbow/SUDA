#! /usr/bin/env python
#coding=utf-8
from __future__ import division


f_table={} # function table

class Tran:
    
    def __init__(self):
        self.v_table={} # variable table

    def update_v_table(self,name,value):
        self.v_table[name]=value

    def trans(self,node):

        
        # Translation

        # Assignment
        if node.getdata()=='[ASSIGNMENT]': 
            ''' statement : VARIABLE '=' NUMBER'''
            value=node.getchild(2).getvalue()
            node.getchild(0).setvalue(value)
            # update v_table
            self.update_v_table(node.getchild(0).getdata(),value)
            

            
        
        # Operation
        elif node.getdata()=='[OPERATION]':
            '''operation : VARIABLE '=' VARIABLE '+' VARIABLE
                         | VARIABLE '=' VARIABLE '-' VARIABLE'''
            arg0=self.v_table[node.getchild(2).getdata()]
            arg1=self.v_table[node.getchild(4).getdata()]
            op=node.getchild(3).getdata()
            
            if op=='+':
                value=arg0+arg1
            else:
                value=arg0-arg1
            
            node.getchild(0).setvalue(value)
            # update v_table
            self.update_v_table(node.getchild(0).getdata(),value)
            
          
            
        # Print
        elif node.getdata()=='[PRINT]':
            '''print : PRINT '(' VARIABLE ')' '''
            arg0=self.v_table[node.getchild(2).getdata()]
            print(arg0)
        
        # If
        elif node.getdata()=='[IF]':
            r'''if : IF '(' condition ')' '{' statements '}' '''
            children=node.getchildren()
            self.trans(children[0])
            condition=children[0].getvalue()
            if condition:
                for c in children[1:]:
                    self.trans(c)
                    
        # While
        elif node.getdata()=='[WHILE]':
            r'''while : WHILE '(' condition ')' '{' statements '}' '''
            children=node.getchildren()
            while self.trans(children[0]):
                for c in children[1:]:
                    self.trans(c)
                
                    
        # Condition
        elif node.getdata()=='[CONDITION]':
            '''condition : VARIABLE '>' VARIABLE
                         | VARIABLE '<' VARIABLE'''
            
            arg0=self.v_table[node.getchild(0).getdata()]
            arg1=self.v_table[node.getchild(2).getdata()]
            op=node.getchild(1).getdata()
            if op=='>':
                node.setvalue(arg0>arg1)
            elif op=='<':
                node.setvalue(arg0<arg1)
                
        elif node.getdata()=='[FUNCTION]':
            r'''function : DEF VARIABLE '(' VARIABLE ')' '{' statements RETURN VARIABLE '}' ''' 

            fname=node.getchild(0).getdata()
            vname=node.getchild(1).getdata()
            f_table[fname]=(vname,node.getchild(2)) # function_name : (variable_names, function)
        
        elif node.getdata()=='[RUNFUNCTION]':
            r'''runfunction : VARIABLE '(' VARIABLE ')' '''
        
            fname=node.getchild(0).getdata()
            vname1=node.getchild(1).getdata()
            
            vname0,fnode=f_table[fname]
            
            t=Tran()
            t.v_table[vname0]=self.v_table[vname1]
            
            t.trans(fnode)
            
            print(t.v_table)

                    
        else:
            for c in node.getchildren():
                self.trans(c)
        
        return node.getvalue()
            
                
                
            
            

