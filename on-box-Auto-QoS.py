from cli import *
import time
normal_T= "conf t ; policy-map ALL_TRAFFIC_POLICY ; class class-default ; police cir percent 80 pir percent 80 conform transmit exceed drop ; interface Ethernet1/1 ; service-policy output ALL_TRAFFIC_POLICY"
high_T= "conf t ; policy-map ALL_TRAFFIC_POLICY ; class class-default ; police cir percent 50 pir percent 50 conform transmit exceed drop ; interface Ethernet1/1 ; service-policy output ALL_TRAFFIC_POLICY"

def monitor_traffic():
    output = cli("show interface ethernet1/1 | include rate")
    traffic_rate = int(output.split()[-2])  # Extract the traffic rate value
    return traffic_rate

def adjust_qos(traffic_rate):
    if traffic_rate > 1000000:  # Example threshold
        cli(high_T)
        send_alert(f"Traffic rate high: {traffic_rate} bps, adjusted QoS policy.")
    else:
        cli(normal_T)
        send_alert(f"Traffic rate normal: {traffic_rate} bps, adjusted QoS policy.")

def send_alert(message):
    print(f"Alert: {message}")  # This can be replaced with actual alerting logic

while True:
    traffic_rate = monitor_traffic()
    adjust_qos(traffic_rate)
    time.sleep(60)  # Check every 1 minute

