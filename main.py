import os

# try:
#     #documentacao https://phoenixnap.com/kb/how-to-install-java-centos-8
#     os.system("sudo yum update -y")
#     os.system("sudo yum upgrade -y")
#     os.system("sudo yum install wget -y")
#     os.system("sudo yum install java-1.7.0-openjdk -y")
#     os.system("java -version")
# except:
#     print("-> OCORREU UM ERRO AO INSTALAR O JAVA")

# try:
#     #documentacao https://www.vultr.com/pt/docs/how-to-install-apache-zeppelin-on-centos-7/
#     os.system("sudo wget https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-all.tgz")
#     os.system("sudo tar xf zeppelin-0.10.1-bin-all.tgz -C /opt")
#     os.system("sudo mv zeppelin-0.10.1-bin-all.tgz /opt/zeppelin")
#     os.system("sudo adduser -d /opt/zeppelin -s /sbin/nologin zeppelin")
#     os.system("sudo chown -R zeppelin:zeppelin /opt/zeppelin")
#     os.system("sudo cp ./zeppelin.service /etc/systemd/system/zeppelin.service")
#     os.system("sudo systemctl start zeppelin")
#     os.system("sudo systemctl enable zeppelin")
#     os.system("sudo systemctl status zeppelin")
# except:
#     print("-> OCORREU UM ERRO AO INSTALAR O ZEPPELIN")

try:
    #documentacao https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/
    with open('lista_usuarios_zeppelin.txt', 'r') as arquivo:
        lista_usuarios= arquivo.readlines()

    with open('shiro_template.txt', 'r') as arquivo:
        lista_shiro= arquivo.readlines()

    aux_qnt_lines_lista_usuarios =0
    aux_qnt_lines_lista_shiro=0

    for linha_shiro in lista_shiro:

        
        if "[users]" in linha_shiro:
            
            with open("shiro.ini", 'a') as arquivo:
                        arquivo.write("[users]\n")
            for linha_usuarios in lista_usuarios:
                if aux_qnt_lines_lista_usuarios >= 1:

                    #retorna o nome do usuario 
                    aux_name_index = linha_usuarios.index(" ")
                    aux_name = linha_usuarios[1 : aux_name_index]
                    
                    #retorna a senha do usuario
                    aux_pass_index = linha_usuarios.index(" ")+1
                    aux_contents_pass =linha_usuarios[aux_pass_index:]
                    aux_pass_index = aux_contents_pass.index(" ")
                    aux_pass = aux_contents_pass[1:aux_pass_index]
                    
                    #retorna o role do usuario
                    aux_role_index = linha_usuarios.index(" ")+1
                    aux_contents_role = linha_usuarios[aux_role_index:]
                    aux_role_index = aux_contents_role.index(" ")+1
                    aux_role = aux_contents_role[aux_role_index:-1]
                    text = aux_name + '=' + aux_pass + ',' + aux_role +'\n'

                    with open("shiro.ini", 'a') as arquivo:
                        arquivo.write(text)
                    
                aux_qnt_lines_lista_usuarios = aux_qnt_lines_lista_usuarios + 1
        else:
            with open("shiro.ini", 'a') as arquivo:
                        arquivo.write(linha_shiro)
        
        aux_qnt_lines_lista_shiro = aux_qnt_lines_lista_shiro + 1

except:
    print("-> OCORREU UM ERRO AO CONFIGURAR USUÁRIOS DO ZEPPELIN")