import os

def pyProj(dir):

  filename = dir + "\main.py"

  # makes the main.py file
  file = open(filename, "x")
  file.close()
  file = open(filename, "w")
  file.write(
    "from lib import helloworld\n" + 
    "helloworld()"
  )
  file.close()

  # makes the lib.py file
  filename = dir + "\lib.py"
  file = open(filename, "x")
  file.close()
  file = open(filename, "w")
  file.write(
  "def helloworld():\n" +
  " print(\"hello there\")"
  )


# makes a c#
def csProj(dir, projtype):
  os.chdir(dir)
  os.system(f"dotnet new {projtype}")


# makes a c++ project
def cppProj(dir):

  filename = dir + "\main.cpp"

  #makes the main.cpp file
  file = open(filename, "x")
  file.close()

  # lib.cpp
  filename = dir + "\lib.h"

  # makes the lib.cpp file
  file = open(filename, "x")
  file.close()


# makes a java project
def javProj(dir):
  filename = dir + "\main.java"
  file = open(filename, "x")
  file.close()



# makes a project according to main.py

def MakeProj(dir=str, language=str, proj_type=str):
  
  print(f"{language}, {proj_type}")

  if not os.path.exists(dir):
    os.mkdir(dir)

  if language == "python":
    pyProj(dir)

  if language == "c#":
    csProj(dir, proj_type)

  if language == "cpp":
    cppProj(dir)

  if language == "java":
    javProj(dir)