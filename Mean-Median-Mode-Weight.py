import csv
from collections import Counter

with open("height-weight.csv", newline = '') as f:
   reader = csv.reader(f)
   file_data = list(reader)
    
file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    value = file_data[i][2]
    new_data.append(float(value))
    
len_of_data = len(new_data)
total = 0

for i in new_data:
    total = total+i
    
mean = total/len_of_data

print("The Average is ",mean)

    
len_of_data = len(new_data)
new_data.sort()

if len_of_data % 2 == 0:
    median1 = float(new_data[len_of_data//2])
    median2 = float(new_data[len_of_data//2-1])
    median  = (median1 + median2)/2
    
else:
    median = new_data[len_of_data//2]
    
print("The Median is",median)

data = Counter(new_data)
mode_data_for_range={
    "100-110":0,
    "110-120":0,
    "120-130":0,
    "140-150":0,
    "150-160":0
}

for height,occurence in data.items():
    if 100<float(height)<110:
        mode_data_for_range["100-110"]+=occurence
    elif 110<float(height)<120:
        mode_data_for_range["110-120"]+=occurence
    elif 120<float(height)<130:
        mode_data_for_range["120-130"]+=occurence   
    elif 130<float(height)<140:
        mode_data_for_range["130-140"] +=occurence
    elif 140<float(height)<150:
        mode_data_for_range["140-150"]+=occurence   
    elif 150<float(height)<160:
        mode_data_for_range["150-160"]+=occurence   
        
mode_range,mode_occurence = 0,0

for range,occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range,mode_occurence = [int(range.split("-")[0]),int(range.split("-")[2])],occurence 
        print(mode_range)
        print(mode_occurence)
        
mode = float(((mode_range[0]+mode_range[2])))/2

print("The mode is ",mode)