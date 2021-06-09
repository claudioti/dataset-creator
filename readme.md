#Pre-Requisites
* pip install -r requirements.txt

Make sure to add log files (non malicious and malicious) from a DNS server to the respective data subfolder and rename each log file to "all.log" ie:

* MX non malicious records log file (all.log) -> /data/input/benign/mx/all.log

* Malicious records log file (all.log) -> /data/input/malign/all.log

The log files used was from Bind Server with the following format:<br>
<b>queries: info: client @0x7f891f5aea30 192.168.1.113#63760 (awebsite.com): query: awebsite.com IN AAAA + (192.168.1.100)</b>

Some constants from /utils/Constants.py file can be modified to customize the script.

#Run the script
* python main_create_datasets.py

#Generated dataset:
* http://dx.doi.org/10.17632/623sshkdrz.5
