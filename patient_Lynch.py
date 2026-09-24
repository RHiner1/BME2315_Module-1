import csv
class Patient:
    all_patients = []
    #constructor for patient, containing donorID, sex, whether or not they have dementia, apoe genotype, age of death, and years of education
    def __init__(self, donorID:str, sex: str, diagnosis: str, apoe: str, deathage: int, educationyears: int, onsetage: int, brainweight: int, educationlevel: str, mmse: int):
        self.donorID = donorID
        self.sex = sex
        self.diagnosis = diagnosis
        self.apoe = apoe
        self.deathage = deathage
        self.educationyears = educationyears
        self.onsetage = onsetage
        self.brainweight = brainweight
        self.educationlevel = educationlevel
        self.mmse = mmse

        Patient.all_patients.append(self)
    #representor for patient
    def __repr__(self):
        return f"{self.donorID}: ({self.sex} | {self.diagnosis} | {self.apoe} | {self.onsetage} | {self.educationyears})"

    def getAge(self):
        return self.deathage
    #instantiates all patients from csv data
    @classmethod
    def instantiate_from_csv(cls, filename:str):
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)
            for row in rows_of_patients:
                Patient(donorID = row['Donor ID'], sex = row['Sex'], diagnosis = row['Cognitive Status'], apoe = row['APOE Genotype'], deathage = int(row['Age at Death']), educationyears = int(row['Years of education']), onsetage = int(row['Age of onset cognitive symptoms'].strip()) if row['Age of onset cognitive symptoms'].strip() else None, brainweight = int(row['Fresh Brain Weight']) if row['Fresh Brain Weight'] != "Unavailable" else None, educationlevel = row['Highest level of education'], mmse = int(row['Last MMSE Score'].strip()) if row['Last MMSE Score'].strip() else None)
    #filters list of patients by sex, diagnosis, and/or apoe genotype
    @classmethod
    def filter(cls, list, sex:str = "any", diagnosis:str = "any", apoe:str = "any", onsetage = "any", educationlevel = "any"):
        all_patients = list
        remove_list = []
        attr_list = (sex, diagnosis, apoe, onsetage, educationlevel)
        attr_name = ("sex", "diagnosis", "apoe", "onsetage", "educationlevel")
        for attr in range(len(attr_list)):
            if attr_list[attr] != "any":
                for patient in all_patients:
                    if getattr(patient,attr_name[attr]) !=attr_list[attr]:
                        remove_list.append(patient)
                all_patients = [patient for patient in all_patients if patient not in remove_list]
                remove_list.clear()
        return all_patients
