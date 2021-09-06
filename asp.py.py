
s=("Hindustan Aeronautics Limited\tis headquartered in Bangalore")
s2=("Hindustan Aeronautics\\Limited is headquartered in Bangalore")
s3=("Hindustan\nAeronautics limited is headquartered in Bangalore")
s4=("Hindustan Aeronautics\'Limited is headquartered in Bangalore")
print(s)
print(s2)
print(s3)
print(s4)
import json5
sample='{"we\'had not\ttake dinner together yet"}'
d=json5.dumps(sample)
print(d)

