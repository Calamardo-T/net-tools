import platform
import os

current_os = platform.system().lower()
if current_os == "windows":
    parameter = "-n"
else:
    parameter = "-c"

ip = "127.0.0.1"
exit_code = os.system(f"ping {parameter} 1 {ip} > output.txt")
# Probar con el módulo "commands" -> status, output = commands.getstatusoutput("ping {parameter} 1 {ip}")
# donde status is 0, output es lo que saca por pantalla el ping

print(exit_code == 0)