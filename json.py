import json
s='{"Hindustan Aeronautics Limited is headquartered in Bangalore"}'
s2="Hindustan Aeronautics\\Limited is headquartered in Bangalore"
s3="Hindustan \n Aeronautics limited is headquartered in Bangalore"
s4="Hindustan Aeronautics \" Limited is headquartered in Bangalore"
d=json.loads(s)
print(d)
print(s)
print(s2)
print(s3)
print(s4)