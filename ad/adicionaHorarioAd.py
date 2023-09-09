from pyad import pyad
import datetime

# Configuração do servidor Active Directory
pyad.set_defaults(ldap_server="seu_servidor_ad")

# Nome do usuário a ser adicionado ao grupo
nome_usuario = "NomeDoUsuario"
nome_grupo = "NomeDoGrupo"  # Substitua pelo nome do grupo que deseja adicionar o usuário

# Localize o usuário e o grupo no Active Directory
usuario = pyad.aduser.ADUser.from_cn(nome_usuario)
grupo = pyad.adgroup.ADGroup.from_cn(nome_grupo)

# Adicione o usuário ao grupo
grupo.add_members([usuario])

# adicionando data de expiração
# Data de expiração da conta (substitua com a data desejada)
data_expiracao = datetime.datetime(2023, 12, 31)  # Exemplo: 31 de dezembro de 2023
# Defina a data de expiração da conta
usuario.accountExpires = data_expiracao
# Salve as alterações no Active Directory
usuario.update_attribute("accountExpires", usuario.accountExpires)


print(f"O usuário {nome_usuario} foi adicionado ao grupo {nome_grupo} com sucesso.")
