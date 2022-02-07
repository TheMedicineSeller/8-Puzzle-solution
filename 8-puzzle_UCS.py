import copy as cp
import heapdict

class State:
  def __init__(self, init):
    self.identifier="I" # I for 'Initial' as in starting config
    self.cost = 0
    self.board=init

  def __repr__(self):
    return "<State: identifier = " + self.identifier + ">"

  def leftS(self, state):
    self.identifier+="L"
    self.cost+=2
    for row in self.board:
      if 0 in row:
        i=self.board.index(row)
        j=row.index(0)
    self.board[i][j]=self.board[i][j-1]
    self.board[i][j-1]=0
  
  def rightS(self, state):
    self.identifier+="R"
    self.cost+=4
    for row in self.board:
      if 0 in row:
        i=self.board.index(row)
        j=row.index(0)
    self.board[i][j]=self.board[i][j+1]
    self.board[i][j+1]=0

  def upS(self, state):
    self.identifier+="U"
    self.cost+=1
    for row in self.board:
      if 0 in row:
        i=self.board.index(row)
        j=row.index(0)
    self.board[i][j]=self.board[i-1][j]
    self.board[i-1][j]=0

  def downS(self, state):
    self.identifier+="D"
    self.cost+=3
    for row in self.board:
      if 0 in row:
        i=self.board.index(row)
        j=row.index(0)
    self.board[i][j]=self.board[i+1][j]
    self.board[i+1][j]=0
  # ---------------------------------------
def Print(op):
  for p in op:
    print(*p)
  print("\n")

def generateTree(tree, goal, PriorityQ):
  closedList = []
  while PriorityQ.peekitem()[0].board != goal:
    current=cp.deepcopy(PriorityQ.peekitem()[0])
    tree[current]=[]
    for row in current.board:
        if 0 in row:
          i=current.board.index(row)
          j=row.index(0)
    if j!=0:
      l=cp.deepcopy(current)
      l.leftS(current)
      if l.board not in closedList:
        tree[current].append(l)
        PriorityQ[l] = l.cost
        closedList.append(l.board)
    if j!=2:
      r=cp.deepcopy(current)
      r.rightS(current)
      if r.board not in closedList:
        tree[current].append(r)
        PriorityQ[r] = r.cost
        closedList.append(r.board)
    if i!=0:
      u=cp.deepcopy(current)
      u.upS(current)
      if u.board not in closedList:
        tree[current].append(u)
        PriorityQ[u] = u.cost
        closedList.append(u.board)
    if i!=2:
      d=cp.deepcopy(current)
      d.downS(current)
      if d.board not in closedList:
        tree[current].append(d)
        PriorityQ[d] = d.cost
        closedList.append(d.board)
    PriorityQ.popitem()
  return PriorityQ.peekitem()[0]
# -------------------------------------
PriorityQ = heapdict.heapdict()
tree = {}
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

initial = State(init)
PriorityQ[initial] = initial.cost
opState = cp.deepcopy(initial)
solution = generateTree(tree, goal, PriorityQ)
solutionstr = solution.identifier
print("Solution sequence found with cost = ", solution.cost)
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
