class solution:
  def process(self,haystack:str,needle:str)-> int:
    if needle in haystack:
      starts=0
      ni=0
      s=""
      print("starts1:",starts)
      for i in range(len(haystack)):
        print("starts1:",starts)
        if haystack[i]==needle[ni] :# 0:0=s:s,1:1=a:a
          s+=haystack[i]
          if s==needle:
            return starts 
          ni+=1
        else:
          print("starts1:",starts)
          starts+=ni
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
  }
}
 
for i  in test:
  inp=test[i]["Input"]
  out=test[i]["output"]
  class_test=solution()
  myfunc=class_test.process(inp[0],inp[1])
  if out==myfunc:
    print(f" -------Successed... !---------\n\n Input : {inp} \n output: {out} \n Your Output: {myfunc}\n" )
  else:
    print(f"-------- Failed... !-----------\n\n Input : {inp} \n output: {out} \n Your Output: {myfunc}\n" )
    
  
