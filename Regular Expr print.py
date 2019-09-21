import re

#irregular display string
Data = """
Interface       IP-Address  OK?     Method Status   Protocol

FastEthernet0/0 192.168.1.242   YES     manual up   up
FastEthernet1/0        unassigned   YES     unset       down
Serial2/0               192.168.1.250   YES     manual up   up
Serial3/0               192.168.1.233   YES     manual up   up
FastEthernet4/0        unassigned   YES     unset       down
FastEthernet5/0        unassigned   YES        unset        down
"""

dic_data = dict()

#code to get the above data in proper arranged dictionary
for line in Data.split('\n'):
    line = line.strip()
   
    if line == '' or not (line.startswith('Fast') or line.startswith('Serial')):
        continue

    # replace multiple space with one space
    line = re.sub('\s+', ' ', line)
    data1 = line.split(' ')
   
    
    if len(data1) == 5:
        dic_data[data1[0]] = (data1[0], data1[3])
    else:
        dic_data[data1[0]] = (data1[0], data1[3])

# display the required items
for key in dic_data.keys():
    print(dic_data[key][0], dic_data[key][1])