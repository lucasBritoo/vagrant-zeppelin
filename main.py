import os

try:
    #documentacao https://phoenixnap.com/kb/how-to-install-java-centos-8
    os.system("sudo yum check-update -y")
    os.system("sudo yum update -y")
    os.system("sudo yum install wget -y")
    os.system("sudo yum install java-1.8.0-openjdk -y")
    os.system("java -version")
except:
    print("-> OCORREU UM ERRO AO INSTALAR O JAVA")

try:
    os.system("sudo wget https://rpm.nodesource.com/setup_14.x")
    os.system("sudo chmod +x setup_14.x")
    os.system("sudo ./setup_14.x")
    os.system("sudo yum install -y nodejs")
    os.system("sudo wget http://www.apache.org/dist/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz")
    os.system("sudo tar -zxf apache-maven-3.6.3-bin.tar.gz -C /usr/local/")
    os.system("sudo ln -s /usr/local/apache-maven-3.6.3/bin/mvn /usr/local/bin/mvn")
except:
    print("-> OCORREU UM ERRO AO INSTALAR AS DEPENDENCIAS")
try:
    #documentacao https://www.vultr.com/pt/docs/how-to-install-apache-zeppelin-on-centos-7/
    os.system("sudo wget https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-all.tgz")
    os.system("sudo tar xf zeppelin-0.10.1-bin-all.tgz -C /opt")
    os.system("sudo mv zeppelin-0.10.1-bin-all.tgz /opt/zeppelin-0.10.1-bin-all")
    
    os.system("export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.17.0.8-2.el7_9.x86_64/")
    
except:
    print("-> OCORREU UM ERRO AO INSTALAR O ZEPPELIN")
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
                    x=0
                    aux_linha = linha_usuarios.split(' ')
                    for i in aux_linha:
                        
                        if x == 0: aux_name = i
                        elif x == 1: aux_pass = i
                        else: aux_role = i
                        x = x+1

                    text = aux_name+ '=' + aux_pass + ',' + aux_role +'\n'
                    
                    if aux_qnt_lines_lista_usuarios <= 8:
                        with open("shiro.ini", 'a') as arquivo:
                            arquivo.write(text)
                         
                aux_qnt_lines_lista_usuarios = aux_qnt_lines_lista_usuarios + 1
        else:
            with open("shiro.ini", 'a') as arquivo:
                arquivo.write(linha_shiro)
        
        aux_qnt_lines_lista_shiro = aux_qnt_lines_lista_shiro + 1
        
except:
    print("-> OCORREU UM ERRO AO CONFIGURAR USUARIOS")

try:
    os.system("sudo cp zeppelin-env.sh /opt/zeppelin-0.10.1-bin-all/conf")
    os.system("sudo cp zeppelin-site.xml /opt/zeppelin-0.10.1-bin-all/conf")
    os.system("sudo cp shiro.ini /opt/zeppelin-0.10.1-bin-all/conf")
    os.system("sudo adduser -d /opt/zeppelin-0.10.1-bin-all -s /sbin/nologin zeppelin")
    os.system("sudo chown -R zeppelin:zeppelin /opt/zeppelin-0.10.1-bin-all")
    os.system("sudo sh /opt/zeppelin-0.10.1-bin-all/bin/install-interpreter.sh  -a")
    os.system("sudo sh /opt/zeppelin-0.10.1-bin-all/bin/zeppelin-daemon.sh start")
    print("\n\n----> ZEPPELIN INICIADO COM SUCESSO NA PORTA 8888")
    print()

except:
    print("-> OCORREU UM ERRO AO INICIAR ZEPPELIN")