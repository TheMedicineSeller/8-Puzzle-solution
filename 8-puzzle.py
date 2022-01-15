import copy as cp
from collections import deque

class State:
  def __init__(self, init):
    self.identifier="I" # I for 'Initial' as in starting config
    self.board=init

  def __repr__(self):
    return "<__main__.State: identifier = " + self.identifier + ">"

  def leftS(self, state):
    self.identifier+="L"
    for row in self.board:
      if 0 in row:
        i=self.board.index(row)
        j=row.index(0)
    self.board[i][j]=self.board[i][j-1]
    self.board[i][j-1]=0
  
  def rightS(self, state):
    self.identifier+="R"
    for row in self.board:
      if 0 in row:
        i=self.board.index(row)
        j=row.index(0)
    self.board[i][j]=self.board[i][j+1]
    self.board[i][j+1]=0

  def upS(self, state):
    self.identifier+="U"
    for row in self.board:
      if 0 in row:
        i=self.board.index(row)
        j=row.index(0)
    self.board[i][j]=self.board[i-1][j]
    self.board[i-1][j]=0

  def downS(self, state):
    self.identifier+="D"
    for row in self.board:
      if 0 in row:
        i=self.board.index(row)
        j=row.index(0)
    self.board[i][j]=self.board[i+1][j]
    self.board[i+1][j]=0

def Print(op):
  for p in op:
    print(*p)
  print("\n")

def generateTree(tree, goal, Q):
  while Q[0].board!=goal:
    current=cp.deepcopy(Q[0])
    tree[current]=[]
    for row in current.board:
        if 0 in row:
          i=current.board.index(row)
          j=row.index(0)
    if j!=0:
      l=cp.deepcopy(current)
      l.leftS(current)
      tree[current].append(l)
      Q.append(l)
    if j!=2:
      r=cp.deepcopy(current)
      r.rightS(current)
      tree[current].append(r)
      Q.append(r)
    if i!=0:
      u=cp.deepcopy(current)
      u.upS(current)
      tree[current].append(u)
      Q.append(u)
    if i!=2:
      d=cp.deepcopy(current)
      d.downS(current)
      tree[current].append(d)
      Q.append(d)
    Q.popleft()
  return Q[0].identifier

tree={}
init = [[0 for x in range(3)] for y in range(3)]
goal = [[0 for x in range(3)] for y in range(3)]
print("Enter the initial tile numbers as an array:")
for i in range(3):
  for j in range(3):
    init[i][j]=int(input()) # Enter 0 for the empty tile

print("Enter the goal state tile numbers as an array:")
for i in range(3):
  for j in range(3):
    goal[i][j]=int(input())

initial=State(init)
tree[initial]=[]
Q=deque()
Q.append(initial)
opState=cp.deepcopy(initial)
solutionstr=generateTree(tree, goal, Q)
for i in solutionstr:
  if i=="L":
    opState.leftS(opState)
  elif i=="R":
    opState.rightS(opState)
  elif i=="U":
    opState.upS(opState)
  elif i=="D":
    opState.downS(opState)
  Print(opState.board)
