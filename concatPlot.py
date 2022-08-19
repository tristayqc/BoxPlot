# %%
from codecs import ignore_errors
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import matplotlib.patches as PathPatch

pathFS = r'C:\Users\Trist\Documents\GitHub\BoxPlot\ForestS'
pathFNS = r'C:\Users\Trist\Documents\GitHub\BoxPlot\ForestNS'
pathUS = r'C:\Users\Trist\Documents\GitHub\BoxPlot\UrbanS'
pathUNS = r'C:\Users\Trist\Documents\GitHub\BoxPlot\UrbanNS'


# concatenate all files in a directory
def concat(path):
    # get files from the path provided
    all_files = glob.glob(os.path.join(path, "*.csv"))
#     # read_csv()
#     # header default = 0, column names are inferred from 1st line of file
#     # skip row number 1 while reading the data
    df_from_each_file = (pd.read_csv(f, sep = ';', usecols = [' Angle']) for f in all_files)
    concatenated_df = pd.concat(df_from_each_file, ignore_index=True).dropna()
    return concatenated_df

df_us = concat(pathUS)
df_uns = concat(pathUNS)
df_fs = concat(pathFS)
df_fns = concat(pathFNS)
df_S = pd.concat([df_us, df_fs], ignore_index=True)
df_NS = pd.concat([df_uns, df_fns], ignore_index=True)

df_us.columns = ['Urban_S']
df_uns.columns = ['Urban_NS']
df_fs.columns = ['Forest_S']
df_fns.columns = ['Forest_NS']
df_S.columns = ['Salient']
df_NS.columns = ['Non-salient']

plt.figure(figsize=(5, 8))

# df of all four conditions
df_all4 = pd.concat([df_us, df_uns, df_fs, df_fns], axis = 1)
box_4 = plt.boxplot(df_all4, vert=True, labels = ['Urban_S', 'Urban_NS', 'Forest_S', 'Forest_NS'], patch_artist=True, showfliers=False, widths=(0.25, 0.25, 0.25, 0.25))

# df of 2 saliency condition
# df_bothS = pd.concat([df_S, df_NS], axis = 1)
# box_SNS = plt.boxplot(df_bothS, vert = True, labels = ['Salient', 'Non-salient'], patch_artist = True, showfliers = False, widths=(0.25, 0.25))

# fill with colors
# colorsSNS = ['#FED8B1', '#E5E4E2']
# for patch, color in zip(box_SNS['boxes'], colorsSNS):
#     patch.set_facecolor(color)
colors4 = ['#50EBEC', '#CCFFFF', '#6CC417', '#DBF9DB']
for patch, color in zip(box_4['boxes'], colors4):
    patch.set_facecolor(color)

plt.show()


# pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(df_S)
