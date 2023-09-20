"""

H0 - Эффективность ибупрофена выше чем эффективность парацетамола 
H1 - Эффективность ибупрофена не выше чем эффективность парацетамола

"""

from scipy import stats, mean
import csv
with open('C:/Users/aleks/Documents/pyth/data_analysis/ttest/Drug.csv', 'r', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    Ibuprofen_ef = []
    Acetaminophen_ef = []
    for row in data:
        if row[1] == "Ibuprofen":
            Ibuprofen_ef.append(float(row[5]))
        if row[1] == "Acetaminophen":
            Acetaminophen_ef.append(float(row[5]))
rez = stats.ttest_ind (a=Ibuprofen_ef, b=Acetaminophen_ef)
print(rez) 

"""
т.к. значение р-теста (0.00357) больше, чем альфа = 0,05, мы можем отвергнуть нулевую гипотезу теста.

"""