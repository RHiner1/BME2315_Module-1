from patient_Lynch import *
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression

Patient.instantiate_from_csv(r"C:\Users\reill\OneDrive - University of Virginia\BME2315\Module 1\BME2315_Module-1\BME2315_Module-1\Metadata and Protein Data for Module 1.csv")

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

X = np.array(patient_educationyears).reshape(-1,1)
y = np.array(patient_deathage)

model = LinearRegression()
model.fit(X,y)

slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X, y)

# Annotate equation
equation = f"y = {slope:.2f}x + {intercept:.2f}\nR² = {r2:.2f}"
plt.text(X.max(), y.max(), equation, color="red", fontsize=12, verticalalignment='top')

plt.scatter (X, y, color='blue')
plt.plot(X, model.predict(X), color='red', linewidth=2)
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

a = np.array(patient_educationyears_filtered).reshape(-1,1)
b = np.array(patient_onsetage)

model = LinearRegression()
model.fit(a,b)

slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(a, b)

# Annotate equation
equation = f"y = {slope:.2f}x + {intercept:.2f}\nR² = {r2:.2f}"
plt.text(a.max(), b.max(), equation, color="red", fontsize=12, verticalalignment='top')

plt.scatter (a, b, color = 'blue')
plt.plot(a, model.predict(a), color='red', linewidth=2)
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
t_stat, p_val = stats.ttest_ind(dementiaPatient, noDementiaPatient)
print(f't_stat = {t_stat}, p_val = {p_val}')

plt.bar(Patient_dementia_cols, mean_age, yerr=yerr, capsize=10, color=["blue", "orange"])
plt.title("Average Years of Education for Dementia Patients vs. Non-Dementia Patients")
plt.ylabel("Years of Education")
plt.show()

testedpatients = [patient for patient in Patient.all_patients if patient.mmse is not None]

highschool = []
tradeschool = []
bachelors = []
graduate = []
professional = []

for patient in Patient.filter(Patient.all_patients, educationlevel = "High School"):
    if patient.mmse is not None:
        highschool.append(patient.mmse)
for patient in Patient.filter(Patient.all_patients, educationlevel = "Trade School/ Tech School"):
    if patient.mmse is not None:
        tradeschool.append(patient.mmse)
for patient in Patient.filter(Patient.all_patients, educationlevel = "Bachelors"):
    if patient.mmse is not None:
        bachelors.append(patient.mmse)
for patient in Patient.filter(Patient.all_patients, educationlevel = "Graduate (PhD/Masters)"):
    if patient.mmse is not None:
        graduate.append(patient.mmse)
for patient in Patient.filter(Patient.all_patients, educationlevel = "Professional"):
    if patient.mmse is not None:
        professional.append(patient.mmse)

highschool_mean = statistics.mean(highschool)
tradeschool_mean = statistics.mean(tradeschool)
bachelors_mean = statistics.mean(bachelors)
graduate_mean = statistics.mean(graduate)
professional_mean = statistics.mean(professional)
highschool_stdev = statistics.stdev(highschool)
tradeschool_stdev = statistics.stdev(tradeschool)
bachelors_stdev = statistics.stdev(bachelors)
graduate_stdev = statistics.stdev(graduate)
professional_stdev = statistics.stdev(professional)

mean_mmse = [highschool_mean, tradeschool_mean, bachelors_mean, graduate_mean, professional_mean]
stdev_mmse = [highschool_stdev, tradeschool_stdev, bachelors_stdev, graduate_stdev, professional_stdev]
yerr = [np.zeros(len(mean_mmse)), stdev_mmse]

f_stat, p_value = stats.f_oneway(highschool, tradeschool, bachelors, graduate, professional)
print("F-statistic:", f_stat)
print("p-value:", p_value)


educationlevel_cols = ['High School', 'Trade School/Tech School', 'Bachelors Degree', 'Graduate Degree', 'Professional Degree']
plt.bar(educationlevel_cols, mean_mmse, yerr=yerr, capsize=10, color=["red", "green", "blue", "orange", "purple"])
plt.title("Highest Level of Education vs. Last MMSE Score")
plt.xlabel("Highest Level of Education")
plt.ylabel("Last MMSE Score")
plt.xticks(fontsize = 6)
plt.show()