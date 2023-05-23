"""
CFM = Confirmation
"""
import os 
import subprocess

os.system('cls')


### CONFIRMAÇÃO / CONFIGURAÇÃO DO SISTEMA OPERACIONAL

os.system('systeminfo | findstr /B /C:"Nome do sistema operacional"')
os.system('systeminfo | findstr /B /C:"OS Name"')
os.system('systeminfo | findstr /B /C:"Versão do sistema operacional"')
os.system('systeminfo | findstr /B /C:"OS Version"')
cfmPro = input("A versão do Windows é a PRO? (s/n) \n")
os.system('cls')
if cfmPro != "s":
    print("Para que as configurações possam ser realizadas é necessario que a versão do Windows seja Professional")
    os.system('pause')
    exit()


### FUNÇÕES

def createUser():
    firstName = input ("Qual o seu primeiro nome: ").capitalize()
    lastName = input ("Qual o seu sobrenome: ").capitalize()
    os.system ("cls")
    cfmName = input (f"\033[1m{firstName} {lastName} \033[0m \nO seu nome está correto? (s/n) ")
    while (cfmName != "s"):
        os.system("cls")
        firstName = input ("Reescreva o seu primeiro nome: ").capitalize()
        lastName = input ("Reescreva o seu sobrenome: ").capitalize()
        os.system ("cls")
        cfmName = input (f"\033[1m{firstName} {lastName} \033[0m \nO seu nome está correto? (s/n) ")
        os.system ("cls")

    subprocess.run(f"powershell.exe New-LocalUser -Name {firstName} -Password (ConvertTo-SecureString -String '123@Faciap' -AsPlainText -Force) -FullName '{firstName} {lastName}' -Description 'Agente de Registro'")
    print (f"O usuário {firstName} {lastName} foi criado com sucesso!")

def cfgPw():
    subprocess.run("powershell.exe secedit /export /cfg cfgpw.inf")
    subprocess.run("powershell.exe cfgpw.inf")
    os.system("pause")
    subprocess.run("powershell.exe secedit /configure /db C:\Windows\Security\Database\local.sdb /cfg cfgpw.inf /areas SECURITYPOLICY")


### CRIAÇÃO DOS USUARIOS

createUser()
moreUser = input ("Deseja adicionar mais usuários? (s/n) \n")
os.system("cls")
while (moreUser == 's'):
    createUser()
    moreUser = input ("Deseja adicionar mais usuários? (s/n) \n")
    os.system("cls")

admUser = input ("Deseja criar usuário administrador? (s/n) \n")
if admUser == "s":
    cfgPw()
    subprocess.run("powershell.exe New-LocalUser -Name 'Ar Faciap' -Password (ConvertTo-SecureString -String 'arfaciap@123' -AsPlainText -Force) -FullName 'Ar Faciap' -Description 'Ar Faciap'")
    subprocess.run("powershell.exe Add-LocalGroupMember -Group 'Administradores' -Member 'Ar Faciap'")
    os.system ("pause")

### CONFIGURAÇÃO DOS USUARIOS 

cfgPw()

print("Configuração realizada com sucesso!!")
os.system('pause')