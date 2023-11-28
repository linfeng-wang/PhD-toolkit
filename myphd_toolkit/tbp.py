import os
import json
import pandas as pd

def getting_lin_info(FOLDER_PATH, wgs_id):
    # with open(NAME_FILE, 'w') as f:
    #     subprocess.run(f"cd {FOLDER_PATH}; ls", shell=True, stdout=f, text=True)
    # df_all_filtered = df_all_filtered[df_all_filtered['Islands']=='Visayas']
    lin = []
    lin_no_sep = []
    for x in wgs_id:
        name = f'{x}.results.json'
        FILE_PATH = os.path.join(FOLDER_PATH, name)
        json_results = json.load(open(FILE_PATH))
        # lin.extend(json_results["main_lin"].split(';'))
        # lin.extend(json_results["main_lin"])
        lin.append(json_results["main_lin"])
        # if len(json_results["main_lin"].split(';')) > 1:
        #     print(name)
        #     print(json_results["main_lin"].split(';'))
        lin_no_sep.append(json_results["main_lin"])
    # with open(NAME_FILE, 'r') as f:
    #     lin = []
    #     for line in f:
    #         name = line.rstrip().split('\n')[0]
    #         FILE_PATH = os.path.join(FOLDER_PATH, name)
    #         json_results = json.load(open(FILE_PATH))
    #         lin.append(json_results["main_lin"])
    lin_list = []
    lin_list.append('1')
    lin_list.append(lin.count('lineage1'))
    lin_list.append(lin.count('lineage1')/len(lin))
    lin_list.append('2')
    lin_list.append(lin.count('lineage2'))
    lin_list.append(lin.count('lineage2')/len(lin))
    lin_list.append('3')
    lin_list.append(lin.count('lineage3'))
    lin_list.append(lin.count('lineage3')/len(lin))
    lin_list.append('4')
    lin_list.append(lin.count('lineage4'))
    lin_list.append(lin.count('lineage4')/len(lin))
        
    df_lin = pd.DataFrame(lin_list[i:i+3] for i in range(0, len(lin_list), 3))
    df_lin.insert(0, "Characteristics", "Lineage", True)
    df_lin.columns = ['Characteristics', 'Group', 'N', '%']
    df_lin = df_lin.sort_values(by=['Group'])
    
    return df_lin