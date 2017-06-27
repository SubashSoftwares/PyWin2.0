###The base of this library is python 2.7.x and you can make changes manually to make this run on later versions if possible;
###This library is made and distributed without any sorts of warrenties.
import os, system
try:
  import win32api as win32
  import win32clipboard
  
except NameError as err:
  print ("Please Install The Required Modules Or Libraries");

#Some self closing clipboard functions
def getClipboardData():
  OpenClipboard()
  

if __name__=="__main__":
  print("welcome to Pywin2.0");
