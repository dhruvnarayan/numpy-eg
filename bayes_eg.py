#Bayes Theorem

A = 'Student really knows the material'
B = 'Student answered the question correctly'
p_A = 0.6
p_B_A = 0.85
p_B_A_comp = 0.2
p_B = (p_A*p_B_A) + ((1-p_A)*p_B_A_comp)
p_A_B = p_A*p_B_A/p_B
print(p_B)
print(p_A_B)