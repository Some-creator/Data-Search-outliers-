import statistics as math
import json
import numpy as np
import matplotlib.pyplot as plt
import sys

# getting data
def getdata(nameoffile):
  if nameoffile == None or nameoffile == '':
    nameoffile = "data.json"
  with open(nameoffile, "r") as f:
    data = json.load(f)
  return data

# getting data from User

u_i_fn = str(input("Filename: "))
uifn = str(input("Data Directory: "))
try:
  data = getdata(u_i_fn)
except FileNotFoundError:
  sys.exit("Directory/File not found")
try:
    data_area = data[uifn]
except:
    sys.exit("File not found")


is_average = []
notaverage = []

average = math.mean(data_area)

for values in data_area:
  if values > average:
    notavg = values
    notaverage.append(notavg)
  else:
    avg = values
    is_average.append(avg)

# Storing

is_average_dict = {
  "values": [is_average]
}

notaverage_dict = {
  "values":[notaverage]
}

# sending to store.json

data["Data_Get"] = { "Average":[is_average_dict], "Not_Average":notaverage_dict}



with open("store.json", "w") as file:
  json.dump(data , file)

print("Successfuly sent to store.json")

print("")

# plotting
# a = []
# len_notaverage = len(notaverage)
# abc = 0
# while abc != int(len_notaverage):
#     a.append(int(abc))
#
#     abc = abc + 1
#
# x = np.array(a)
# y = np.array(notaverage)
# plt.scatter(x, y)

abc = 0
a = []
len_average = len(is_average)

while abc != int(len_average):
    a.append(abc)


    abc = abc + 1

x = np.array(a)
y = np.array(is_average)

plt.scatter(x, y)

plt.title("Data")
plt.show()



