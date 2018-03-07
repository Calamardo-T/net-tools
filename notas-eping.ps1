Get-WmiObject ### resolver nombre netbios (creo)

$range=1..255 | %{"10.2.2.$_"} ## rango

$i = Test-Connection -count 1 -comp 1.2.3.4 -quiet #### ping

$machine = '8.8.8.8'
[System.Net.Dns]::GetHostByAddress($machine).HostName ## resolver FQDN