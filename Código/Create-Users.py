import os 
import subprocess
import getpass
from zipfile import ZipFile

os.system ('cls')

### FUNÇÕES

def createUser ():
    firstName = input ("Qual o seu primeiro nome: ").capitalize()
    lastName = input ("Qual o seu sobrenome: ").capitalize()
    cfmName = input (f"O nome: \033[1m{firstName} {lastName}\033[0m, está correto? (s/n)   \n")
    while cfmName != "s":
        firstName = input ("Reescreva o seu primeiro nome: ").capitalize()
        lastName = input ("Reescreva o seu sobrenome: ").capitalize()    
        cfmName = input (f"O nome: \033[1m{firstName} {lastName}\033[0m, está correto? (s/n)   \n")

    subprocess.run (f"powershell.exe New-LocalUser -Name {firstName} -Password (ConvertTo-SecureString -String '123@Faciap' -AsPlainText -Force) -FullName '{firstName} {lastName}' -Description 'Agente de Registro'")
    print (f"O usuário {firstName} {lastName} foi criado com sucesso!")

def search_docs(name, directory):
    results = []  
    for root, dirs, files in os.walk(directory):
        for file in files:
            if name in file:
                results.append(os.path.join(root, file)) 

    return results

def cfgPw ():

    os.system (f'runas /user:"Administrador" "{search}"')
    ### PRECISA CRIAR UM ZIP PARA O ARQUIVO .BAT



### CONFIRMAÇÃO / CONFIGURAÇÃO DO SISTEMA OPERACIONAL
print ('-' * 30)
print (' ' * 10, 'CONFIRMAÇÃO DO SISTEMA OPERACIONAL!! \n')

os.system ('systeminfo | findstr /B /C:"Nome do sistema operacional"')
os.system ('systeminfo | findstr /B /C:"OS Name"')
os.system ('systeminfo | findstr /B /C:"Versão do sistema operacional"')
os.system ('systeminfo | findstr /B /C:"OS Version"')
cfmPro = input ("A versão do Windows é a PRO? (s/n) \n")

if cfmPro != "s":
    print ("Para que as configurações possam ser realizadas é necessario que a versão do Windows seja Professional")
    os.system ('pause')
    exit ()
print('\n')


### CRIAÇÃO DOS USUARIOS
print ('-' * 30)
print ('-' * 30)
print('\n')
print(' ' * 10, 'CRIAÇÃO DE USUÁRIOS!! \n')
createUser ()
moreUser = input ("Deseja adicionar mais usuários? (s/n) \n")

while moreUser == 's':
    createUser()
    moreUser = input ("Deseja adicionar mais usuários? (s/n) \n")
    
admUser = input ("Deseja criar usuário administrador? (s/n) \n")
if admUser == "s":
    subprocess.run ("powershell.exe New-LocalUser -Name 'Ar Faciap' -Password (ConvertTo-SecureString -String arfaciap@123 -AsPlainText -Force) -FullName 'Ar Faciap' -Description 'Ar Faciap'")
    subprocess.run ("powershell.exe Add-LocalGroupMember -Group 'Administradores' -Member 'Ar Faciap'")
    os.system ('pause')

### CONFIGURAÇÃO DOS USUARIOS 
configpw = input ('Deseja realizar a configuração de usuário?')
if configpw == 's':
    print("Favor rodar script de habilitação do usuario ADMINISTRADOR!!")
    os.system('pause')
    search = ', '.join(search_docs('CfgPwRequirements.bat', 'C:\\'))
    print(' ' * 10, 'CONFIGURAÇÃO DE POLÍTICAS DE USUÁRIOS!!')
    cfgPw ()
    os.system ('pause')

print ("Configuração realizada com sucesso!!")
os.system ('pause')