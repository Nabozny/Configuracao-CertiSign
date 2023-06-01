"""
CFM = Confirmation
"""
import os 
import subprocess
import getpass

os.system ('cls')

### FUNÇÕES

def createUser ():
    firstName = input ("Qual o seu primeiro nome: ").capitalize()
    lastName = input ("Qual o seu sobrenome: ").capitalize()
    cfmName = input (f"\033[1m{firstName} {lastName} \033[0m \nO seu nome está correto? (s/n) ")
    while (cfmName != "s"):
        firstName = input ("Reescreva o seu primeiro nome: ").capitalize()
        lastName = input ("Reescreva o seu sobrenome: ").capitalize()
        os.system ("cls")
        cfmName = input (f"\033[1m{firstName} {lastName} \033[0m \nO seu nome está correto? (s/n) ")
        os.system ("cls")

    subprocess.run (f"powershell.exe New-LocalUser -Name {firstName} -Password (ConvertTo-SecureString -String '123@Faciap' -AsPlainText -Force) -FullName '{firstName} {lastName}' -Description 'Agente de Registro'")
    print (f"O usuário {firstName} {lastName} foi criado com sucesso!")

def cfgPw ():
    print (os.system('net localgroup administradores'))
    adm = input ('Qual usuário ADMINISTRADOR irá usar? \n')
    user = getpass.getuser()
    os.system (f'runas /user:{adm} "C:\\Users\\{user}\\Desktop\\teste\\CfgPwRequirements.bat"')



### CONFIRMAÇÃO / CONFIGURAÇÃO DO SISTEMA OPERACIONAL
print ("-" * 30)
print(' ' * 10, 'CONFIRMAÇÃO DO SISTEMA OPERACIONAL!!')

os.system ('systeminfo | findstr /B /C:"Nome do sistema operacional"')
os.system ('systeminfo | findstr /B /C:"OS Name"')
os.system ('systeminfo | findstr /B /C:"Versão do sistema operacional"')
os.system ('systeminfo | findstr /B /C:"OS Version"')
cfmPro = input ("A versão do Windows é a PRO? (s/n) \n")

if cfmPro != "s":
    print ("Para que as configurações possam ser realizadas é necessario que a versão do Windows seja Professional")
    os.system ('pause')
    exit ()
print (linha, '\n')

print ("-" * 30)

### CRIAÇÃO DOS USUARIOS
print ("-" * 30)
print(' ' * 10, 'CRIAÇÃO DE USUÁRIOS!!')
createUser ()
moreUser = input ("Deseja adicionar mais usuários? (s/n) \n")

while (moreUser == 's'):
    createUser ()
    moreUser = input ("Deseja adicionar mais usuários? (s/n) \n")
    

admUser = input ("Deseja criar usuário administrador? (s/n) \n")
if admUser == "s":
    subprocess.run ("powershell.exe New-LocalUser -Name 'Ar Faciap' -Password (ConvertTo-SecureString -String 'arfaciap@123' -AsPlainText -Force) -FullName 'Ar Faciap' -Description 'Ar Faciap'")
    subprocess.run ("powershell.exe Add-LocalGroupMember -Group 'Administradores' -Member 'Ar Faciap'")
    os.system ('pause')
print ("-" * 30)
### CONFIGURAÇÃO DOS USUARIOS 
print ("-" * 30)
print(' ' * 10, 'CONFIGURAÇÃO DE POLÍTICAS DE USUÁRIOS!!')
cfgPw ()
print ("-" * 30)
print ("Configuração realizada com sucesso!!")
os.system ('pause')