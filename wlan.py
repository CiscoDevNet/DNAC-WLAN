#!/usr/bin/env python
from __future__ import print_function
import sys
import json
import logging
import urllib
from argparse import ArgumentParser, REMAINDER
from util import get_url, post_sync, put_and_wait, delete_sync

def create_provision_wlan(ssid, passphrase, location_list):
    payload={
    "managedAPLocations": location_list,
    "ssidDetails": {
        "name": ssid,
        "securityLevel": "WPA2_PERSONAL",
        "enableFastLane": False,
        "passphrase": passphrase,
        "trafficType": "voicedata",
        "enableBroadcastSSID": True,
        "radioPolicy": "Dual band operation (2.4GHz and 5GHz)",
        "enableMACFiltering": False,
        "fastTransition": "ADAPTIVE",
        "webAuthURL": ""
    },
    "ssidType": "Enterprise",
    "enableFabric": False,
    }
    logging.debug("playload for create {}".format(json.dumps(payload)))
    url = 'dna/intent/api/v1/business/ssid'
    response = post_sync(url, payload)
    print (json.dumps(response))

def delete_provision_wlan(ssid, location_list):
    # fix this
    url = "dna/intent/api/v1/business/ssid/{}/{}".format(ssid,urllib.quote(location_list[0], safe=''))
    logging.debug("DeleteSSID URL:{}".format(url))
    response= delete_sync(url)
    print(json.dumps(response))

def show_wlan():
    response = get_url('dna/intent/api/v1/enterprise-ssid')
    print (json.dumps(response, indent=2))


if __name__ == "__main__":
    parser = ArgumentParser(description='Select options.')
    parser.add_argument('--passphrase', type=str, required=False,
                        help="passphrase ssid of WLAM")
    parser.add_argument('--ssid', type=str, required=False,
                        help="ssid of WLAM")
    parser.add_argument('--addssid', type=str, required=False,
                        help="ssid to create")
    parser.add_argument('--delssid', type=str, required=False,
                        help="ssid to delete")
    parser.add_argument('-v', action='store_true',
                        help="verbose")
    parser.add_argument('rest', nargs=REMAINDER)
    args = parser.parse_args()
    if args.v:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    if args.addssid:
        create_provision_wlan(args.addssid, args.passphrase, args.rest)
    elif args.delssid:
        delete_provision_wlan(args.delssid, args.rest)
    else:
     show_wlan()