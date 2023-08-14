using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class CSVLoader : MonoBehaviour
{

    public int _exp = 0;

    void Start()
    {
        List<Dictionary<string, object>> data = CSVReader.Read("knightIdle - playerChar");

        for (var i = 0; i < data.Count; i++)
        {
            Debug.Log("index " + (i).ToString() + " : " + data[i]["attack"] + " " + data[i]["attackSpeed"] + " " + data[i]["criticalChance"]);
        }

        _exp = (int)data[0]["attack"];
        Debug.Log(_exp);
    }
}
 
