def f():
  print( 3 ) # without this, running it causes no visible effect
  return 3   # without this, x = f() will leave x with the value "None"

def g(x):
  if type(x) == int:
    print( "it's an integer!" )
  elif type(x) == str:
    print( "it's a string!" )
  else: print( "it's something else." )

def foo(a,b):
  if (type(a) != int) | (type(b) != int):
    raise ValueError( "one of those two arguments is not an integer" )
  return a+b

# recursion
def lastInList( ls ):
  if len( ls ) == 1:
    return ls[0]
  if len( ls ) < 1:
    raise ValueError( "not supposed to get an empty list" )
  else:
    return lastInList( ls[1:] )

lastInList( [1,2,3] )
= lastInList( lastInList( [,2,3] ) )
= lastInList( lastInList( lastInList( [3] ) ) )
= 3

# for loops and while loops
for i in [1,2,3]:
  for j in [11,22,33]:
    print( (i,j), "inner" )
  print( (i,j), "   outer" )

i = 10
while i > 0:
  print(i)
  i = i-1

# loops introduce global variables you might not want;
# here's how to get rid of, for instance, the variables `i` and `j`
del(i,j)

# arguments are local to a function
def f(a):
  a = a+1
  return a

# higher-order functions
x = [1,2,3]
y = list( map( lambda i: i**2, x ) )
z = list( map( lambda i: i**3, x ) )

def applyToX( func : str ):
  return list( map( func, x ) )

# defining your own types
class Politician:
  """ This comment is accessible from within the interpreter,
  by typing `Politician.__doc__` """
  def __init__(self,party,origin):
    # This comment, by contrast, is only visible in the code.
    self.party = party
    self.origin = origin
  def party_backwards(self):
    return self.party[::-1]

fidel = Politician( "communist", "havana" )
