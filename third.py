from dataclasses import dataclass


list = ['H','T','H','H','H','T','T','H']
results = []
@dataclass
class Coin:
    h_probability:float
    t_probability:float
    probability:float
c1 = Coin(0.8,0.2,0.2)
c2 = Coin(0.9,0.1,0.2)
c3 = Coin(0.1,0.9, 0.2)
c4 = Coin(0.2, 0.8,0.2)
c5 = Coin(0.3,0.7,0.2)
H = round(c1.h_probability * c1.probability + c2.h_probability * c2.probability + c3.h_probability * c3.probability + c4.h_probability * c4.probability + c5.h_probability * c5.probability,2)
T = 1-H
print(H)
for i in list:
    if(i == 'H'):
        c1.probability = (c1.probability*c1.h_probability)/H
        c2.probability = (c2.probability*c2.h_probability)/H
        c3.probability = (c3.probability*c3.h_probability)/H
        c4.probability = (c4.probability*c4.h_probability)/H
        c5.probability = (c5.probability*c5.h_probability)/H
    else:
        c1.probability = (c1.probability*c1.t_probability)/T
        c2.probability = (c2.probability*c2.t_probability)/T
        c3.probability = (c3.probability*c3.t_probability)/T
        c4.probability = (c4.probability*c4.t_probability)/T
        c5.probability = (c5.probability*c5.t_probability)/T

    H = c1.h_probability * c1.probability + c2.h_probability * c2.probability + c3.h_probability * c3.probability + c4.h_probability * c4.probability + c5.h_probability * c5.probability
    T = 1-H
    results.append(round(H,2))

c1.probability = (c1.probability*c1.h_probability)/H
c2.probability = (c2.probability*c2.h_probability)/H
c3.probability = (c3.probability*c3.h_probability)/H
c4.probability = (c4.probability*c4.h_probability)/H
c5.probability = (c5.probability*c5.h_probability)/H

H = c1.h_probability * c1.probability + c2.h_probability * c2.probability + c3.h_probability * c3.probability + c4.h_probability * c4.probability + c5.h_probability * c5.probability
results.append(round(H,2))

for i in results:
    print(i)