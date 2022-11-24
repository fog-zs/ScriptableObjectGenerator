## What is this
This script generates a ScriptableObject for Unity. 
It can also generate files to create assets from CSV files.

## How to use

```python
from generator import ScriptableObject

save_path = r"."
name = "Land"
db = ScriptableObject(        
    variables=[
        ("string", "areaId"),
        ("string", "userId"),
        ("string", "custom"),
    ]        
)
db.make_db_script(path = save_path, name = name, stype=1)
db.make_importer(name=name)
db.make_csv(name=name)
```