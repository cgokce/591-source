'''
Flatten the given nested dictionary

Restrictions
- Maps key -> generic object +
- If key is empty "" -> Exclude from the output  +
- Nested dictionary is concatanted keys with dots. +
  - a -> b -> c .... "a.b.c"
- Return all of the values in a dictionary format +

Algo()
prefix = ""
- For elem in dict

  # Base 3 - Failure
  if elem = "":
    return None

  if elem is sub_dict
    # Base1 - Successful
    if prefix !="":
      prefix += "."
    prefix = prefix + curr_key
    return Algo(prefix,sub_dict)
  else
    # Base2 - Successful
    return value

Test cases
traverse
Key1: not dict 1
return "Key1": "1"
Key2: dict
  prefix = ket2
  traverse key2
  a: 2 
  return prefix + "."+ a  :2
  "key.a" :2
  ...
  "": 1
  return None
  c: dict
    prefix = key2 + "."
'''

def flatten_dictionary1(dictionary):
  
  prefix = ""
  keys = []
  vals = []
  return dfs(dictionary, prefix, keys, vals)
  
  
def dfs1(dictionary, prefix, keys, vals):

  if isinstance(dictionary, str):
    # Base2 - Successful
    keys.append(prefix)
    vals.append(dictionary)
    return keys, vals
  
  for key in dictionary.keys():
    elem = dictionary[key]
    
    if prefix !="":
      prefix += "."
    prefix = prefix + key
    
    # Base 3 - Failure
    if elem == "":
      return keys, vals

    if isinstance(elem, str):
      # Base2 - Successful
      keys.append(prefix)
      vals.append(elem)
      
    else:
      # Base1 - Successful
      
      # Recursion Part, Need to accumulate
      k,v = dfs(prefix, elem, keys, vals)
      keys.extend(k)
      vals.extend(v)
    
    return keys, vals



# Sample Input
input_dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

# Function Call
keys, vals = flatten_dictionary(input_dict)

for i in range(len(keys)):
  print(keys[i], vals[i])
  print("\n")

