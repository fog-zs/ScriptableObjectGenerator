import os

class ScriptableObject():
    def __init__(self, variables):
        self.variables = variables

    # ---------------------------------------------------------------
    def make_db_script(self, name, path = ".", stype = 0):

        vtext = ""
        for k, v in self.variables:
            vtext += f"    public {k} {v};\n"

        if stype == 0:
            text = f"""using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "DB_{name}", menuName = "DB/DB_{name}")]
public class DB_{name} : ScriptableObject
{{
{vtext}
}}
            """
        else:
            text = f"""using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "DB_{name}", menuName = "DB/DB_{name}")]
public class DB_{name} : ScriptableObject
{{
    public List<DB_{name}E> data = new List<DB_{name}E>();
}}

[System.Serializable]
public class DB_{name}E
{{
{vtext}
}}
            """

        f = open(f'{path}/DB_{name}.cs', 'w', encoding="utf-8")
        f.write(text)
        f.close()        
    # ---------------------------------------------------------------

    def make_importer(self, name, path="importer"):
        header=f"""# Generate ScriptableObject from csv

import csv
import os

guid = ""
load_name = "{name}"
save_name = "DB_{name}"
save_path = r"."
os.makedirs(save_path, exist_ok=True)
with open(f'../data/{{load_name}}.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = [row for row in reader]
    """
        
        footer=f"""f = open(f"{{save_path}}/DB_{{save_name}}.asset", 'w', encoding="utf-8")
f.write(txt)
f.close()
    """
        
        content = f"""%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!114 &11400000
MonoBehaviour:
m_ObjectHideFlags: 0
m_CorrespondingSourceObject: {{{{fileID: 0}}}}
m_PrefabInstance: {{{{fileID: 0}}}}
m_PrefabAsset: {{{{fileID: 0}}}}
m_GameObject: {{{{fileID: 0}}}}
m_Enabled: 1
m_EditorHideFlags: 0
m_Script: {{{{fileID: 11500000, guid: {{guid}}, type: 3}}}}
m_Name: {{save_name}}
m_EditorClassIdentifier: 
data:
    """

        text = f"""{header}
header = f\"""{content}\"""
txt = f"{{header}}"

title = data[0]
data = data[1:]
for d in data:    
    txt += f"  - {{title[0]}}: {{d[0]}}\\n"

    for j in range(1,len(d)): 
        txt += f"    {{title[j]}}: {{d[j]}}\\n"
print(txt)
{footer}
        """
        os.makedirs(path, exist_ok=True)
        f = open(f'{path}/{name}.py', 'w', encoding="utf-8")
        f.write(text)
        f.close()
        
    # ---------------------------------------------------------------
    def make_csv(self, name, path="data"):
        text = ""

        i = 0
        for k, v in self.variables:
            if i != len(self.variables) - 1:
                text += f"{v},"
            else:
                text += f"{v}\n"
            i += 1

        os.makedirs(path, exist_ok=True)
        f = open(f'{path}/{name}.csv', 'w', encoding="utf-8")
        f.write(text)
        f.close()
