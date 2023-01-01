import subprocess
packages = ('pandas', 'numpy', 'openpyxl')


# function to install the required packages
def install_packages(packages: list):
    for package in packages:
        subprocess.call(['pip', 'install', package])


install_packages(packages)


import pandas as pd
import numpy as np


def file_reader(path: str):  
    """
    Reads the file of most of the formats supported by Pandas library.

    Parameters:

    path: string

    Path to the file to be read.

    Returns:

    data: pandas.DataFrame

    Dataframe with the data from the chosen file.
    """

    if path.lower().endswith('.csv') or path.lower().endswith('.txt'):
        data = pd.read_csv(path)
    elif path.lower().endswith('.tsv'):
        data = pd.read_table(path)
    elif path.lower().endswith('.xls') or path.lower().endswith('.xlsx') \
    or path.lower().endswith('.ods'):
        data = pd.read_excel(path)
    elif path.lower().endswith('.json'):
        data = pd.read_json(path)
    elif path.lower().endswith('.fasta'):
        data = pd.read_fasta(path)
    elif path.lower().endswith('.xml'):
        install_packages(['lxml'])
        data = pd.read_xml(path)
    elif path.lower().endswith('.parquet'):
        install_packages(['pyarrow'])
        data = pd.read_parquet(path)
    elif path.lower().endswith('.orc'):
        data = pd.read_orc(path)
    elif path.lower().endswith('.dta'):
        data = pd.read_stata(path)
    elif path.lower().endswith('.xpt') or path.lower().endswith('.sas7bdat'):
        data = pd.read_sas(path)
    elif path.lower().endswith('.sav'):
        data = pd.read_spss(path)
    elif path.lower().endswith('.pkl'):
        data = pd.read_pickle(path)
    elif path.lower().endswith('.sql'):
        data = pd.read_sql(path)
    elif path.lower().endswith('.html'):
        sub_data = pd.read_html(path)
        data = sub_data[0]
    return data


# enter the path to the file
path_to_file = 'test_test.xml'
data = file_reader(path_to_file)

# add the column for SubC population
sub_c_ser = pd.Series(data['Total'] - data['SubA'] - data['SubB'], name='SubC')
data = data.merge(sub_c_ser, left_index=True, right_index=True)

# add columns with the percentage of each population in the total amount of cells
sub_a_percent = pd.Series(np.divide(data['SubA'], data['Total']) * 100, name='SubA_percent')
sub_b_percent = pd.Series(np.divide(data['SubB'], data['Total']) * 100, name='SubB_percent')
sub_c_percent = pd.Series(np.divide(data['SubC'], data['Total']) * 100, name='SubC_percent')

for series in [sub_a_percent, sub_b_percent, sub_c_percent]:
  data = data.merge(series, left_index=True, right_index=True)

uniq_samples = data['Sample'].unique()

# create the dataset with features to be extracted during data analysis with sample numbers as indexes
result_ds = pd.DataFrame(columns=['SubA_mean', 'SubA_percent_variance',
                                  'SubB_mean', 'SubB_percent_variance', 'SubC_mean',
                                  'SubC_percent_variance'],
                          index=data['Sample'].unique())

# divide the whole dataset into chunks containing data for each sample,
# find the required features and write their values to the final dataset according to sample numbers
for sample in uniq_samples:
  sub_ds = data[data['Sample'] == sample]
  for population in ['SubA', 'SubB', 'SubC']:
    sub_pop_mean = sub_ds[population].mean()
    result_ds.loc[sample, population + '_mean'] = sub_pop_mean
    sub_pop_var = sub_ds[population + '_percent'].var(ddof=0)
    result_ds.loc[sample, population + '_percent_variance'] = sub_pop_var

# save the final dataset
filename_to_save = 'processed_data.xlsx'
result_ds.to_excel(filename_to_save)