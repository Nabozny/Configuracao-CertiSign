"""
CFM = Confirmation
"""
import os 
import subprocess
from zipfile import ZipFile

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
pwBitLocker = input("Senha para o BitLocker: ")


### CRIAÇÃO DOS USUARIOS

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

createUser()
moreUser = input ("Deseja adicionar mais usuários? (s/n) \n")
os.system("cls")
while (moreUser == 's'):
    createUser()
    moreUser = input ("Deseja adicionar mais usuários? (s/n) \n")
    os.system("cls")

admUser = input ("Deseja criar usuário administrador? (s/n) \n")
if admUser == "s":
    subprocess.run("powershell.exe New-LocalUser -Name 'Ar Faciap' -Password (ConvertTo-SecureString -String 'arfaciap@123' -AsPlainText -Force) -FullName 'Ar Faciap' -Description 'Ar Faciap'")
    subprocess.run("powershell.exe Add-LocalGroupMember -Group 'Administradores' -Member 'Ar Faciap'")

os.system("lusrmgr.msc")
os.system("pause")


### CONFIGURAÇÃO DOS USUARIOS 

os.system('powershell "net accounts /minpwlen:8"')
os.system('powershell "net accounts /maxpwage:30"')
os.system('powershell "net accounts /uniquepw:5"')


### DOWNLOAD, INSTALAÇÃO E EXCLUSÃO DOS APLICATIVOS 

os.system("cls")
unzip = ZipFile('aplicativos.zip', 'r')
unzip.extractall('\\unzip')
filePath = os.listdir("\\unzip")
os.chdir("\\unzip")
for file in filePath:
    os.startfile(file)
    print(file)
    os.system("pause")

cfmInstall = input("Todas as instalações foram realizadas com sucesso? (s/n) \n")
while cfmInstall != "s":
    for file in filePath:
        os.startfile(file)
        print(file)
        os.system("pause")
os.removedir("\\unzip")



### DESABILITAR ACESSO REMOTO 

os.system('powershell "Disable-PSRemoting -Force"')
      


### CONFIGURAÇÃO DO BITLOCKER

os.system(f'Powershell "$pw = ConvertTo-SecureString "{pwBitLocker}" -AsPlainText -Force"')
os.system('powershell "Get-Command -Module BitLocker"')
os.system('powershell "Get-BitLockerVolume"')
os.system('powershell "Get-Tpm"')
os.system('powershell "Enable-BitLocker -MountPoint "C:" -PasswordProtector -Password $pw"')



### AJUSTE DE HORARIO

os.system("powershell 'net start w32time'")
os.system("powershell 'w32tm /config /manualpeerlist:ntp.certisign.com.br,0x8 /syncfromflags:manual /update'")