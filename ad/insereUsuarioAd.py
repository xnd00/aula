## pip install pyad

from pyad import pyad

# Configuração do servidor Active Directory
pyad.set_defaults(ldap_server="seu_servidor_ad")

# Nome do usuário a ser criado
nome_usuario = "NovoUsuario"
senha = "Senha123"  # Defina a senha desejada

# Crie o objeto de usuário
novo_usuario = pyad.aduser.ADUser.create(nome_usuario)

# Defina a senha do usuário
novo_usuario.set_password(senha)

# Salve o usuário no Active Directory
novo_usuario.update_attribute("userAccountControl", 512)


# Localize o usuário e o grupo no Active Directory
usuario = pyad.aduser.ADUser.from_cn(nome_usuario)
grupo = pyad.adgroup.ADGroup.from_cn(nome_grupo)

# Adicione o usuário ao grupo
grupo.add_members([usuario])

print(f"Usuário {nome_usuario} criado com sucesso.")
