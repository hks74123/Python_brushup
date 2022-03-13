"""Try Except

When a Python script raises an exception,to handle it we uses try except method

Syntax:
    try:
        code block...
    except Exception1:
        if there is exception1 then execute this
        code block...
    except Exception2:
        if there is exception2 then execute this
        code block...
    else:
        code block...
"""
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
finally:#The finally block, if specified, will be executed regardless if the try block raises an error or not.
  print("The 'try except' is finished")
