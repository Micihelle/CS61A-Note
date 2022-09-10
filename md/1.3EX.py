from operator import mul
"""
def square(x):
        return mul(x, x)
  """  
Names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
B_Name= filter(lambda x: x.startswith('B'),Names)
print(B_Name)
print( (lambda x: x.startswith('B')).__name__)

