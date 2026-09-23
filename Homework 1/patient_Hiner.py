import csv
#defines class patient with attributes ID, age, sex, education, yrs_ed, genotype, cog_stat, onset_age, age_dementia, injury, and pH
class patient:
    def __init__(self, ID: str, age: float, sex: str, education: str, yrs_ed: float, genotype: str, cog_stat: str, onset_age: int, age_dementia: int, injury: str, pH: float, ): 
        self.ID = ID
        self.age = age
        self.sex = sex
        self.education = education
        self.yrs_ed = yrs_ed
        self.genotype = genotype 
        self.cog_stat = cog_stat 
        self.onset_age = onset_age 
        self.age_dementia = age_dementia 
        self.injury = injury 
        self.pH = pH

    @classmethod
    def filter_patients(cls, patients, sex, cog_stat):
        for p in patients:
            if p.sex == sex and p.cog_stat == cog_stat:
                print(p.ID, p.age, p.sex, p.cog_stat)

        