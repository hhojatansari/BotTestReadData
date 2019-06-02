import os
import pandas as pd
import numpy as np

path = os.path.dirname(os.path.realpath(__file__))

babak_positive_path = os.listdir('Dataset/Babak_Skelet_Positive/')
babak_negative_path = os.listdir('Dataset/Babak_Skelet_Negative/')
babak_positive_list = []
babak_negative_list = []
babak_positive_data = []
babak_negative_data = []

hosein_positive_path = os.listdir('Dataset/Hosein_Skelet_Positive/')
hosein_negative_path = os.listdir('Dataset/Hosein_Skelet_Negative/')
hosein_positive_list = []
hosein_negative_list = []
hosein_positive_data = []
hosein_negative_data = []

milad_positive_path = os.listdir('Dataset/Milad_Skelet_Positive/')
milad_negative_path = os.listdir('Dataset/Milad_Skelet_Negative/')
milad_positive_list = []
milad_negative_list = []
milad_positive_data = []
milad_negative_data = []


# --- Babak ---
for example in babak_positive_path:
    if example.split("_")[1] == '2D.txt':
        continue
    elif example.split("_")[1] == '3D.txt':
        babak_positive_list.append(example)
    else:
        print("Error: ", example)

for lst in babak_positive_list:
    file_path = path + "/Dataset/Babak_Skelet_Positive/" + lst
    record = "Babak,1"
    with open(file_path, "r") as file:
        for line in file:
            record += "," + line.split(" ")[1] + "," + line.split(" ")[2] + "," + line.split(" ")[3]
    babak_positive_data.append(record)

babak_positive_df = pd.DataFrame(babak_positive_data)

for example in babak_negative_path:
    if example.split("_")[1] == '2D.txt':
        continue
    elif example.split("_")[1] == '3D.txt':
        babak_negative_list.append(example)
    else:
        print("Error: ", example)

for lst in babak_negative_list:
    file_path = path + "/Dataset/Babak_Skelet_Negative/" + lst
    record = "Babak,0"
    with open(file_path, "r") as file:
        for line in file:
            record += "," + line.split(" ")[1] + "," + line.split(" ")[2] + "," + line.split(" ")[3]
    babak_negative_data.append(record)

babak_negative_df = pd.DataFrame(babak_negative_data)


# --- Hosein ---
for example in hosein_positive_path:
    if example.split("_")[1] == '2D.txt':
        continue
    elif example.split("_")[1] == '3D.txt':
        hosein_positive_list.append(example)
    else:
        print("Error: ", example)

for lst in hosein_positive_list:
    file_path = path + "/Dataset/Hosein_Skelet_Positive/" + lst
    record = "Hosein,1"
    with open(file_path, "r") as file:
        for line in file:
            record += "," + line.split(" ")[1] + "," + line.split(" ")[2] + "," + line.split(" ")[3]
    hosein_positive_data.append(record)

hosein_positive_df = pd.DataFrame(hosein_positive_data)

for example in hosein_negative_path:
    if example.split("_")[1] == '2D.txt':
        continue
    elif example.split("_")[1] == '3D.txt':
        hosein_negative_list.append(example)
    else:
        print("Error: ", example)

for lst in hosein_negative_list:
    file_path = path + "/Dataset/Hosein_Skelet_Negative/" + lst
    record = "Hosein,0"
    with open(file_path, "r") as file:
        for line in file:
            record += "," + line.split(" ")[1] + "," + line.split(" ")[2] + "," + line.split(" ")[3]
    hosein_negative_data.append(record)

hosein_negative_df = pd.DataFrame(hosein_negative_data)


# --- Milad ---
for example in milad_positive_path:
    if example.split("_")[1] == '2D.txt':
        continue
    elif example.split("_")[1] == '3D.txt':
        milad_positive_list.append(example)
    else:
        print("Error: ", example)

for lst in milad_positive_list:
    file_path = path + "/Dataset/Milad_Skelet_Positive/" + lst
    record = "Milad,1"
    with open(file_path, "r") as file:
        for line in file:
            record += "," + line.split(" ")[1] + "," + line.split(" ")[2] + "," + line.split(" ")[3]
    milad_positive_data.append(record)

milad_positive_df = pd.DataFrame(milad_positive_data)

for example in milad_negative_path:
    if example.split("_")[1] == '2D.txt':
        continue
    elif example.split("_")[1] == '3D.txt':
        milad_negative_list.append(example)
    else:
        print("Error: ", example)

for lst in milad_negative_list:
    file_path = path + "/Dataset/Milad_Skelet_Negative/" + lst
    record = "Milad,0"
    with open(file_path, "r") as file:
        for line in file:
            record += "," + line.split(" ")[1] + "," + line.split(" ")[2] + "," + line.split(" ")[3]
    milad_negative_data.append(record)

milad_negative_df = pd.DataFrame(milad_negative_data)

data = pd.concat([babak_positive_df, milad_negative_df, hosein_positive_df,
                  babak_negative_df, milad_positive_df, hosein_negative_df], ignore_index=True)

print("all data shape:", data.shape)
np.savetxt("bot_data.csv", data, delimiter=",", fmt='%s')
