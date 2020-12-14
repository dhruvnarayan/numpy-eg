#Candidate Poll - Project 3

#import codecademylib
import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

#Generating numpy array from list
responses = np.array(survey_responses)

total_ceballos = sum([1 for n in survey_responses if n =='Ceballos'])

percentage_ceballos = 1.0 * total_ceballos/len(survey_responses)
print(percentage_ceballos)

possible_surveys = 1.0*np.random.binomial(len(survey_responses),0.54,size=10000)/len(survey_responses)
plt.hist(possible_surveys,range=(0,1), bins=20)
plt.show()

ceballos_loss_surveys = np.mean(possible_surveys<0.5)
print(ceballos_loss_surveys)

large_survey = 1.0*np.random.binomial(7000,0.54,10000)/7000
ceballos_loss_new = np.mean(large_survey<0.5)
plt.hist(large_survey,range=(0,1), bins=20)
plt.show()
print(ceballos_loss_new)
