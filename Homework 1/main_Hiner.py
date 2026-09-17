from patient_Hiner import *

# patient1 = patient("H19.33.004", 80, "Female", "Bachelors", 17, "3_3", "No dementia", None, None, None, "Unknown", 1035, 7.0)
# patient2 = patient("H20.33.001", 82, "Male", "Bachelors", 16, "3_3", "No dementia", None, None, None, "Unknown", 1338, 6.8)
# patient3 = patient("H20.33.002", 97, "Female", "High School", 12, "2_3", "No dementia", None, None, None, "Unknown", 1078, 7.3)
# patient4 = patient("H20.33.004", 86, "Male", "Trade School/ Tech School", 15, "3_4", "Dementia", 80, 81, "No", "Yes", 1261, 6.7)
# patient5 = patient("H20.33.005", 99, "Female", "High School", 12, "2_3", "No dementia", None, None, None, "Unknown", 1003, 6.8)
# patient6 = patient("H20.33.008", 92, "Female", "Graduate (PhD/Masters)", 18, "3_4", "No dementia", None, None, None, "Unknown", 1105, 6.4)
# patient7 = patient("H20.33.011", 93, "Female", "Bachelors", 16, "3_4", "Dementia", 87, 92, None, "Unknown", 1156, 7.0)

import csv

patients = []
#creates patient objects from the csv file and appends them to the patients list
with open(r"C:\Users\reill\OneDrive - University of Virginia\BME2315\Module 1\Homework 1\Metadata and Protein Data for Module 1.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader)  # skips the header row
    for row in reader:
        print (row)
        ID = row[0]
        age = float(row[3])
        sex = row[4]
        education = row[14]
        yrs_ed = float(row[15])
        genotype = row[16]
        cog_stat = row[17]
        onset_age = int(row[19]) if row[19] else None
        age_dementia = (row[20])
        injury = row[21] if row[21] else None
        pH = float(row[39])

        new_patient = patient(ID, age, sex, education, yrs_ed, genotype, cog_stat, onset_age, age_dementia, injury, pH)

        patients.append(new_patient)

#sorts patients by age and prints the ID and age of each patient
def get_age(p):
    return p.age

patients_sorted = sorted(patients, key=get_age)

print("Patients sorted by age:")

for p in patients_sorted:
    print(p.ID, p.age)

print("Female patients with dementia:")

patient.filter_patients(patients, "Female", "Dementia")

import numpy as np
import matplotlib.pyplot as plt

female_dementia_age = []
male_dementia_age = []

for p in patients:
    if p.cog_stat == "Dementia" and p.age_dementia != "No" and p.age_dementia != "":
        if p.sex == "Female":
            female_dementia_age.append(p.age_dementia)
        elif p.sex == "Male":
            male_dementia_age.append(p.age_dementia)

female_mean = np.mean(female_dementia_age)
male_mean = np.mean(male_dementia_age)

female_std = np.std(female_dementia_age, ddof=1)
male_std = np.std(male_dementia_age, ddof=1)
#creates a bar graph comparing the mean age at dementia for female and male patients 
plt.bar(
    ["Female", "Male"],
    [female_mean, male_mean],
    yerr=[female_std, male_std],
    capsize=5
)

plt.ylabel("Mean Age at Dementia")
plt.title("Mean Age at Dementia by Sex")
plt.show()
#defines two empty lists to hold the age and pH values of all patients
age_values = []
pH_values = []
#iterates through the patients list and appends the age and pH values of each patient to the respective lists, then creates a scatter plot of age vs. pH
for p in patients:
    age_values.append(p.age)
    pH_values.append(p.pH)
plt.scatter(age_values, pH_values)

plt.xlabel("Age")
plt.ylabel("pH")
plt.title("Age vs. pH")
plt.show()