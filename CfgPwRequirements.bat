@echo off
secedit /export /cfg cfgpw.inf
cfgpw.inf
sleep 20
secedit /configure /db C:\Windows\Security\Database\local.sdb /cfg cfgpw.inf /areas SECURITYPOLICY