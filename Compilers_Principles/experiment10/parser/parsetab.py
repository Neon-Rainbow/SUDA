
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "NUMBER PRINT VARIABLEprogram : statementsstatements : statements statement\n                  | statement statement : assignment\n                  | operation\n                  | printassignment : VARIABLE '=' NUMBERoperation : VARIABLE '=' VARIABLE '+' VARIABLE\n                 | VARIABLE '=' VARIABLE '-' VARIABLEprint : PRINT '(' VARIABLE ')' "
    
_lr_action_items = {'VARIABLE':([0,2,3,4,5,6,9,10,11,13,15,16,17,18,19,],[7,7,-3,-4,-5,-6,-2,12,14,-7,18,19,-10,-8,-9,]),'PRINT':([0,2,3,4,5,6,9,13,17,18,19,],[8,8,-3,-4,-5,-6,-2,-7,-10,-8,-9,]),'$end':([1,2,3,4,5,6,9,13,17,18,19,],[0,-1,-3,-4,-5,-6,-2,-7,-10,-8,-9,]),'=':([7,],[10,]),'(':([8,],[11,]),'NUMBER':([10,],[13,]),'+':([12,],[15,]),'-':([12,],[16,]),')':([14,],[17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,],[2,]),'statement':([0,2,],[3,9,]),'assignment':([0,2,],[4,4,]),'operation':([0,2,],[5,5,]),'print':([0,2,],[6,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','py_yacc.py',17),
  ('statements -> statements statement','statements',2,'p_statements','py_yacc.py',24),
  ('statements -> statement','statements',1,'p_statements','py_yacc.py',25),
  ('statement -> assignment','statement',1,'p_statement','py_yacc.py',36),
  ('statement -> operation','statement',1,'p_statement','py_yacc.py',37),
  ('statement -> print','statement',1,'p_statement','py_yacc.py',38),
  ('assignment -> VARIABLE = NUMBER','assignment',3,'p_assignment','py_yacc.py',45),
  ('operation -> VARIABLE = VARIABLE + VARIABLE','operation',5,'p_operation','py_yacc.py',54),
  ('operation -> VARIABLE = VARIABLE - VARIABLE','operation',5,'p_operation','py_yacc.py',55),
  ('print -> PRINT ( VARIABLE )','print',4,'p_print','py_yacc.py',61),
]
