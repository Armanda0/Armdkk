#example 1
def myfunc():
  x = 300
  print(x)

myfunc()

#example 2
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#example 3
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

#example 4
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#example 5
def myfunc():
  global x
  x = 300

myfunc()

print(x)

#example 6
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)