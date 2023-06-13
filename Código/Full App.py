import os 
import subprocess
import getpass
from zipfile import ZipFile

os.system('cls')

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

def unzip_archives (archive, destination_folder):
    with zipfile.ZipFile(archive, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)
      
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

configpw = input ('Deseja realizar a configuração de usuário? ')
if configpw == 's':
    import shutil
    unzip_archives('Apps\\bat_archives.zip', 'Apps\\unzipped\\bat')    
    print("Favor rodar script de habilitação do usuario ADMINISTRADOR!!")
    os.system('pause')
    search = ', '.join(search_docs('CfgPwRequirements.bat', 'C:\\'))
    print(' ' * 10, 'CONFIGURAÇÃO DE POLÍTICAS DE USUÁRIOS!!')
    cfgPw ()
    os.system ('pause')

unzip_archives("Apps\\Aplicativos.zip", "Apps\\unzipped\\to Install")
os.chdir("Apps\\unzipped\\to Install")
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
        cfmInstall = input("Todas as instalações foram realizadas com sucesso? (s/n) \n")

shutil.rmtree('Apps\\unzipped')

os.system('powershell "Disable-PSRemoting -Force"')

os.system(f'Powershell "$pw = ConvertTo-SecureString "{pwBitLocker}" -AsPlainText -Force"')
os.system('powershell "Get-Command -Module BitLocker"')
os.system('powershell "Get-BitLockerVolume"')
os.system('powershell "Get-Tpm"')
os.system('powershell "Enable-BitLocker -MountPoint "C:" -PasswordProtector -Password $pw"')

os.system("powershell 'net start w32time'")
os.system("powershell 'w32tm /config /manualpeerlist:ntp.certisign.com.br,0x8 /syncfromflags:manual /update'")