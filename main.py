from writeDir import MakeProj
from sys import exit

lang_list = ['python', 'python3', 'py', 'py3', 'c#', 'cpp', 'c++', 'java']

dir = input("directory: ")
language = input("language: ")

if language not in lang_list:
   print("language invalid")
   exit(0)

for i in range(4):
  if language == lang_list[i]:
      projtype = "python"

if language == "c#":
    projtype = input("project type: ")

if language == "cpp" or language == "c++":
   projtype = "cpp"

if language == "java":
  projtype == "java"


MakeProj(dir, language, projtype)