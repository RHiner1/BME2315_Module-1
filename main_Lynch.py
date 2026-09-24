from patient_Lynch import *
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics
import pandas as pd
#import sklearn
#from sklearn.linear_model import LinearRegression

Patient.instantiate_from_csv(r"\Users\jclyn\OneDrive\BME 2315\Module 1\Patient_HW\Metadata and Protein Data for Module 1.csv")

#sorts and prints list of all patients by age of death
Patient.all_patients.sort(key=Patient.getAge, reverse =False)
for patient in Patient.all_patients:
    print(patient)

print ("~~~~~~~~~~~~~~\nFiltered Patients\n~~~~~~~~~~~~~~")
#filters and prints a list of all male patients studied
filtered_list = Patient.filter(Patient.all_patients, sex ="Male")
for patient in filtered_list:
    print(patient)
"""
creates two lists of ages of death for patients,
one with the 3_3 genotype and the other with the 3_4
genotype. Makes a bar graph comparing the means and standard
deviations of age of death in the two genotypes
"""
three_3 = []
three_4 = []
two_2 = []
two_3 = []
two_4 = []
four_4 = []

for patient in Patient.filter(Patient.all_patients, apoe="3_3"):
    three_3.append(patient.deathage)
for patient in Patient.filter(Patient.all_patients, apoe="3_4"):
    three_4.append(patient.deathage)
for patient in Patient.filter(Patient.all_patients, apoe="2_2"):
    two_2.append(patient.deathage)
for patient in Patient.filter(Patient.all_patients, apoe="2_3"):
    two_3.append(patient.deathage)
for patient in Patient.filter(Patient.all_patients, apoe="2_4"):
    two_4.append(patient.deathage)
for patient in Patient.filter(Patient.all_patients, apoe="4_4"):
    four_4.append(patient.deathage)

x_3_3_bar = (statistics.mean(three_3))
x_3_4_bar = (statistics.mean(three_4))
age_3_3_stdev = (statistics.stdev(three_3))
age_3_4_stdev = (statistics.stdev(three_4))

print(f'x_3_3_bar = {x_3_3_bar}, age_3_3_stdev {age_3_3_stdev}')
print(f'x_3_4_bar = {x_3_4_bar}, age_3_4_stdev {age_3_4_stdev}')
Patient_apoe_cols = ['3_3 Genotype', '3_4 Genotype']
mean_apoe = [x_3_3_bar, x_3_4_bar]
stdev_apoe = [age_3_3_stdev, age_3_4_stdev]
yerr = [np.zeros(len(mean_apoe)), stdev_apoe]
t_stat, p_val = stats.ttest_ind(three_3, three_4)
print(f't_stat = {t_stat}, p_val = {p_val}')

f_stat, p_value = stats.f_oneway(three_3, three_4, two_2, two_3, two_4, four_4)
print(f'F-statistic: {f_stat}, p-value: {p_value}')
         
plt.bar(Patient_apoe_cols, mean_apoe, yerr=yerr, capsize=10, color=["blue", "orange"])
plt.title("Average age of death by APOE genotype")
plt.xlabel("APOE Genotype")
plt.ylabel("Age of Death")
plt.show()

"""
Creates a list of ages of death and years of education
for each patient. Compares the two on a scatterplot
"""

patient_deathage = []
patient_educationyears = []
for patient in Patient.all_patients:
    patient_deathage.append(patient.deathage)
for patient in Patient.all_patients:
    patient_educationyears.append(patient.educationyears)

X = [patient_educationyears]
y = [patient_deathage]

#model = LinearRegression()
#model.fit(X, y)

plt.scatter (X, y, color='blue')
plt.xlabel('Years of Education')
plt.ylabel('Age of Death')
plt.title('Scatter Plot of Years of Education vs. Age of Death')
plt.show()

patients_with_onset = [patient for patient in Patient.all_patients if patient.onsetage is not None]
patient_educationyears_filtered = []
patient_onsetage = []

for patient in patients_with_onset:
    patient_educationyears_filtered.append(patient.educationyears)
for patient in patients_with_onset:
    patient_onsetage.append(patient.onsetage)

a = [patient_educationyears_filtered]
b = [patient_onsetage]

plt.scatter (a, b, color = 'blue')
plt.xlabel('Years of Education')
plt.ylabel('Age of onset cognitive symptoms')
plt.title('Years of education vs. Age of onset cognitive symptoms')
plt.show()

dementiaPatient = []
noDementiaPatient = []
for patient in Patient.filter(Patient.all_patients, diagnosis = "Dementia"):
    dementiaPatient.append(patient.educationyears)
for patient in Patient.filter(Patient.all_patients, diagnosis = "No dementia"):
    noDementiaPatient.append(patient.educationyears)
print (dementiaPatient)
print(noDementiaPatient)
dementia_mean = (statistics.mean(dementiaPatient))
noDementia_mean = (statistics.mean(noDementiaPatient))
dementia_stdev = (statistics.stdev(dementiaPatient))
noDementia_stdev = (statistics.stdev(noDementiaPatient))
Patient_dementia_cols = ['Dementia', 'No Dementia']
mean_age = [dementia_mean, noDementia_mean]
stdev_age = [dementia_stdev, noDementia_stdev]
yerr = [np.zeros(len(mean_age)), stdev_age]
plt.bar(Patient_dementia_cols, mean_age, yerr=yerr, capsize=10, color=["blue", "orange"])
plt.title("Average Years of Education for Dementia Patients vs. Non-Dementia Patients")
plt.ylabel("Years of Education")
plt.show()