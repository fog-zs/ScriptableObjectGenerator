using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "DB_Land", menuName = "DB/DB_Land")]
public class DB_Land : ScriptableObject
{
    public List<DB_LandE> data = new List<DB_LandE>();
}

[System.Serializable]
public class DB_LandE
{
    public string areaId;
    public string userId;
    public string custom;

}
            