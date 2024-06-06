## On-Box-Auto-QoS

## On-Box Application : Automated Dynamic QoS Adjustment Based on Traffic Analysis
Overview
Analyze traffic patterns and dynamically adjust QoS policies to optimize network performance.
Key Features:
-Real-time traffic analysis.
-Automated adjustment of QoS policies.
-Alerts terminal on traffic anomalies or policy changes.


## Files

- `On-Box-Auto-QoS.py`: Contains the on-box python script.

## Installation

1. Clone the repository:

    git clone https://github.com/CobraTamer/On-Box-Auto_QoS.git


## Usage


	1.	Access Your NX-OS Device:
	•	Open your terminal or SSH client (like PuTTY, SecureCRT, or a terminal emulator on Linux/Mac).
	•	Connect to your NX-OS device using SSH. Example:

ssh admin@your-nxos-device-ip


	2.	Enable Bash Shell:
	•	On the NX-OS device, enable the Bash shell to use Linux-like commands. Enter configuration mode and enable Bash:

conf t
feature bash-shell
exit
run bash


	3.	Create the Script:
	•	Use a text editor like vim to create the script file. Example:

vim AutoQoS.py

	3.	
	•	In vim, press i to enter insert mode, then copy and paste the script above into the editor.
	•	Press Esc, then type :wq and press Enter to save and exit.
	4.	Make the Script Executable:
	•	Change the permissions to make the script executable:

chmod +x interface_health_check.py


	5.	Run the Script:
	•	Execute the script using Python, do this in NX-OS mode not bash:

python3 interface_health_check.py




## Example Output

When you run the app and traffic is below the exceeded limit on interface Eth1/1, you should see this on your terminal: 
"Alert: Traffic rate normal: 1029 bps, adjusted QoS policy."

When the script detects issue, you will see output similar to this in your terminal:
"Traffic rate high: {traffic_rate} bps, adjusted QoS policy"

 
