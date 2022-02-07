import copy as cp

class State:
  def __init__(self, init):
    self.identifier="I" # I for 'Initial' as in starting config
    self.height = 0
    self.board=init

  def __repr__(self):
    return "<State: identifier = " + self.identifier + ">"

  def leftS(self, state):
    self.identifier+="L"
    self.height+=1
    for row in self.board:
      if 0 in row:
        i=self.board.index(row)
        j=row.index(0)
    self.board[i][j]=self.board[i][j-1]
    self.board[i][j-1]=0
  
  def rightS(self, state):
    self.identifier+="R"
    self.height+=1
    for row in self.board:
      if 0 in row:
        i=self.board.index(row)
        j=row.index(0)
    self.board[i][j]=self.board[i][j+1]
    self.board[i][j+1]=0

  def upS(self, state):
    self.identifier+="U"
    self.height+=1
    for row in self.board:
      if 0 in row:
        i=self.board.index(row)
        j=row.index(0)
    self.board[i][j]=self.board[i-1][j]
    self.board[i-1][j]=0

  def downS(self, state):
    self.identifier+="D"
    self.height+=1
    for row in self.board:
      if 0 in row:
        i=self.board.index(row)
        j=row.index(0)
    self.board[i][j]=self.board[i+1][j]
    self.board[i+1][j]=0
# -------------------------------------
def Print(op):
  for p in op:
    print(*p)
  print("\n")

def generateTree(tree, current, goal, visited, depth_limit):
  if goal not in visited and current.height<=depth_limit:
    tree[current] = []
    visited.append(current.board)
    for row in current.board:
        if 0 in row:
          i=current.board.index(row)
          j=row.index(0)
    if j!=0:
      l=cp.deepcopy(current)
      l.leftS(current)
      if l.board not in visited:
        tree[current].append(l)
        generateTree(tree, tree[current][-1], goal, visited, depth_limit)

    if j!=2:
      r=cp.deepcopy(current)
      r.rightS(current)
      if r.board not in visited:
        tree[current].append(r)
        generateTree(tree, tree[current][-1], goal, visited, depth_limit)
    if i!=0:
      u=cp.deepcopy(current)
      u.upS(current)
      if u.board not in visited:
        tree[current].append(u)
        generateTree(tree, tree[current][-1], goal, visited, depth_limit)
    if i!=2:
      d=cp.deepcopy(current)
      d.downS(current)
      if d.board not in visited:
        tree[current].append(d)
        generateTree(tree, tree[current][-1], goal, visited, depth_limit)

# -------------------------------------
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

print("Enter the depth limit for DFS search:")
depth_limit = int(input())
print("\n")
visited = []
initial = State(init)
visited.append(initial.board)
opState=cp.deepcopy(initial)
generateTree(tree, initial, goal, visited, depth_limit)
solutionstr = list(tree.keys())[-1].identifier

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
