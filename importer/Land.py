# Generate ScriptableObject from csv

import csv
import os

guid = ""
load_name = "Land"
save_name = "DB_Land"
save_path = r"."
os.makedirs(save_path, exist_ok=True)
with open(f'../data/{load_name}.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = [row for row in reader]
    
header = f"""%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!114 &11400000
MonoBehaviour:
m_ObjectHideFlags: 0
m_CorrespondingSourceObject: {{fileID: 0}}
m_PrefabInstance: {{fileID: 0}}
m_PrefabAsset: {{fileID: 0}}
m_GameObject: {{fileID: 0}}
m_Enabled: 1
m_EditorHideFlags: 0
m_Script: {{fileID: 11500000, guid: {guid}, type: 3}}
m_Name: {save_name}
m_EditorClassIdentifier: 
data:
    """
txt = f"{header}"

title = data[0]
data = data[1:]
for d in data:    
    txt += f"  - {title[0]}: {d[0]}\n"

    for j in range(1,len(d)): 
        txt += f"    {title[j]}: {d[j]}\n"
print(txt)
f = open(f"{save_path}/DB_{save_name}.asset", 'w', encoding="utf-8")
f.write(txt)
f.close()
    
        