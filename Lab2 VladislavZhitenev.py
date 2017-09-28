def find_min(array):
  if len(array) == 0:
    return -1
    
  min_value = array[0]
  for value in array:
    if value <= min_value:
      min_value = value
  return min_value
      
      

def average(array):
  summ = 0;
  for v in array:
    summ += v
  return summ / len(array)
#
#
#
#
#
def reverse_string(stroka):
  result = ''
  index = len(stroka)-1
  if len(stroka)==0:
    return -1
  while index > 0:
    result += stroka[index]
    index -= 1
  return result
#
#
#
#
#
#
def find_child(emp):
  for f in emp:
    for g in f["children"]:
      if g["age"] >= 18:
        print ("Child name :", g["name"], "Child age : ", g["age"], "Parent name :", f["name"])
        break
  return 0

#
#
#
#
#
#
ivan = {
  "name": "ivan",
  "age": 34,
  "children": [{
    "name": "vasja",
    "age": 19,
  },{
    "name": "petja",
    "age": 12,
  }]
        } 

darja = {
  "name": "darja",
  "age": 41,
  "children": [{
    "name": "kirill",
    "age": 21,
  },{
    "name": "pavel",
    "age": 15,
  }]
        } 
        
emps = [ivan, darja]
#
#
#
#
#
def main():
  massiv = [1,2,3,4,5,6,7,8]
  print("min =", find_min(massiv))
  print ("average =", average(massiv))
  s1='Hello, world'
  print ("reverse = ",s1, "->", reverse_string(s1))
  reverse_string(s1)
  find_child(emps)
 
  
main()


