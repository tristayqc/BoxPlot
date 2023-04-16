import pandas as pd
import glob
import matplotlib.pyplot as plt


# Define directory where CSV files are located
dir_path = r'C:/Users/Trist/Downloads/Data/'

# Get a list of all CSV files in the directory
short_pointing_T1_files = glob.glob(dir_path + "Short/*/PointingTask_Route1_Trial1.csv")
short_pointing_T2_files = glob.glob(dir_path + "Short/*/PointingTask_Route1_Trial2.csv")
short_pointing_T3_files = glob.glob(dir_path + "Short/*/PointingTask_Route1_Trial3.csv")
long_pointing_T1_files = glob.glob(dir_path + "Long/*/PointingTask_Route1_Trial1.csv")
long_pointing_T2_files = glob.glob(dir_path + "Long/*/PointingTask_Route1_Trial2.csv")
long_pointing_T3_files = glob.glob(dir_path + "Long/*/PointingTask_Route1_Trial3.csv")


# print(short_pointing_files)

# Loop through each CSV file and extract the wanted column
def extractData(files, dataName):
    dfs = []
    for file in files:
        # Use pandas to read the CSV file
        df = pd.read_csv(file, skiprows=[0,2], sep = ',', usecols=[dataName])
        # Extract the column data corresponding to dataName
        # and add it to the angle_data list
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

short_angle_T1_data = extractData(short_pointing_T1_files, " Angle")
short_angle_T2_data = extractData(short_pointing_T2_files, " Angle")
short_angle_T3_data = extractData(short_pointing_T3_files, " Angle")
long_angle_T1_data = extractData(long_pointing_T1_files, " Angle")
long_angle_T2_data = extractData(long_pointing_T2_files, " Angle")
long_angle_T3_data = extractData(long_pointing_T3_files, " Angle")

labels = ['Short_T1', 'Long_T1', 'Short_T2', 'Long_T2', 'Short_T3', 'Long_T3']
df_all6 = pd.concat([short_angle_T1_data, long_angle_T1_data, 
                     short_angle_T2_data, long_angle_T2_data,
                     short_angle_T3_data, long_angle_T3_data], axis = 1)
df_all6.columns = labels

# print(df_all6)

# # Create a figure and axis object
# fig, ax = plt.subplots()

# # Create a boxplot of the data
# bp = ax.boxplot(df_all6.values)

# # Set the x-axis tick labels
# ax.set_xticklabels(labels)

# # Set the y-axis label
# ax.set_ylabel('Angle')

# # Set the title
# ax.set_title('Boxplot of Angle Data')

# # Show the plot
# plt.show()

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(10,5))

# Create boxplots for each dataframe
df_all6.boxplot(ax=ax)

# Set the x-axis label and title
ax.set_xlabel('Angle')
ax.set_title('Boxplot of Angle Data')

# Show the plot
plt.show()
