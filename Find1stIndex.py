class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack :
            return haystack.find(needle)               
        else :
            return -1
#return haystack.find(needle) if needle in haystack else -1

class solution:
  def process(self,haystack:str,needle:str)-> int:
    if needle in haystack:
      starts=0
      ni=0
      s=""
      for i in range(len(haystack)):
         
        if haystack[i]==needle[ni] :# 0:0=b:a ,1:0,2:0,3:0,4:0=a:a 5:1=b:b ,6:2=a:b  
          if s=="":
            starts=i
          s+=haystack[i]
          if s==needle:
            starts+=1
            return starts 
          ni+=1
          
        else:
           
          starts+=1 #0,1,2,3,4 -> 
           
          
          print("starts",starts)
    else:
      return -1
 
 
 
test={
  "test1":{
    "Input":["sadoutsad","sad"],
    "output":0
  },
  "test2":{
    "Input":["leetcode","leeto"],
    "output":-1
  },
  "test3":{
    "Input":["python","thon"],
    "output":2
  },
  "test4":{
    "Input":["bbbbababbbaabbba","abb"],
    "output":6
  }
}
 
for i  in test:
  inp=test[i]["Input"]
  out=test[i]["output"]
  class_test=solution()
  myfunc=class_test.process(inp[0],inp[1])
  if out==myfunc:
    print(f" -------Successed...!---------\n\n Input : {inp} \n output: {out} \n Your Output: {myfunc}\n" )
  else:
    print(f"-------- Failed...!-----------\n\n Input : {inp} \n output: {out} \n Your Output: {myfunc}\n" )
    
  
