import pandas as pd
import glob

# Step 2: Define directory where CSV files are located
dir_path = r'C:/Users/Trist/Downloads/Data/'

# Step 3: Get a list of all CSV files in the directory
short_pointing_T1_files = glob.glob(dir_path + "Short/*/PointingTask_Route1_Trial1.csv")
short_pointing_T2_files = glob.glob(dir_path + "Short/*/PointingTask_Route1_Trial2.csv")
short_pointing_T3_files = glob.glob(dir_path + "Short/*/PointingTask_Route1_Trial3.csv")
long_pointing_T1_files = glob.glob(dir_path + "Long/*/PointingTask_Route1_Trial1.csv")
long_pointing_T2_files = glob.glob(dir_path + "Long/*/PointingTask_Route1_Trial2.csv")
long_pointing_T3_files = glob.glob(dir_path + "Long/*/PointingTask_Route1_Trial3.csv")


# print(short_pointing_files)

# Loop through each CSV file and extract the wanted column
def extractData(files, dataName):
    data_list = []
    for file in files:
        # Use pandas to read the CSV file
        df = pd.read_csv(file, skiprows=[0,2], sep = ',', usecols=[dataName])
        # Extract the column data corresponding to dataName
        # and add it to the angle_data list
        data_list.extend(df[dataName].tolist())
    return data_list

short_angle_T1_data = extractData(short_pointing_T1_files, " Angle")
short_angle_T2_data = extractData(short_pointing_T2_files, " Angle")
short_angle_T3_data = extractData(short_pointing_T3_files, " Angle")
long_angle_T1_data = extractData(long_pointing_T1_files, " Angle")
long_angle_T2_data = extractData(long_pointing_T2_files, " Angle")
long_angle_T3_data = extractData(long_pointing_T3_files, " Angle")

