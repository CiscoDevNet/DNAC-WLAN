## A tool to manuiplate WLAN SSID 
Cisco DNA Center has an API to configure new WLAN SSID.  This tools provides a simple way to get started.

THe main script wlan.py can run in several ways.

## List WLAN SSID
Just run the script with no arguments.

```buildoutcfg
$ ./wlan.py 
https://sandboxdnac2.cisco.com:8080/dna/intent/api/v1/enterprise-ssid
[
  {
    "instanceUuid": "c9a7ec8f-5d70-4282-b157-d11c5c71c47b", 
    "inheritedGroupName": "", 
    "groupUuid": "-1", 
    "ssidDetails": [
      {
        "securityLevel": "open", 
        "name": "sandbox", 
        "enableFastLane": false, 
        "enableBroadcastSSID": true, 
        "authServer": "", 
        "isEnabled": true, 
        "wlanType": "Enterprise", 
        "enableMACFiltering": false, 
        "isFabric": false, 
        "passphrase": "", 
        "trafficType": "data", 
        "fastTransition": "ADAPTIVE", 
        "radioPolicy": "Dual band operation (2.4GHz and 5GHz)"
      }
    ], 
    "inheritedGroupUuid": "", 
    "version": 12
  }  
]
```


