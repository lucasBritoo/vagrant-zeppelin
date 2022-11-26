## DESAFIO 2: VAGRANT E ZEPPELIN

Desafio para testar os conhecimentos sobre Vagrant + Zeppelin + Pyhon

## 🔨 Funcionalidades do projeto

- `Funcionalidade 1`: ✔️ Criar um script Vagrant que suba uma máquina CentOS 7.x com 2 CPUs (2 cores de processador), 4 GB de memória RAM e 50gb de HD chamada “teste-zeppelin”;
- `Funcionalidade 2`: ✔️ O acesso a VM deve ser através de uma chave privada, não com senha;
- `Funcionalidade 3`: ✔️ Criar um programa em python que faça a instalação do Java e do Apache Zeppelin nessa máquina recém criada;
- `Funcionalidade 4`: ✔️ O programa deve subir o webserver do Zeppelin na porta 8888;
- `Funcionalidade 5`: ✔️ Criar usuários a partir da lista presente no arquivo 'Lista_Usuarios_Zeppelin.txt'.

## ⚙ Ambiente de desenvolvimento

A máquina de desenvolvimento está com o sistema operacional Ubuntu Desktop 22.04.1 LTS. Neste ambiente há configurado o Vagrant e VirtualBox.

## 📌 Vagrant

O provider utilizado para desenvolvimento foi o VirtualBox. O box utilizado foi o sistema operacional default do 'centos/7'. Para conseguir manipular o tamanho do disco da VM foi necessário instalar um plugin no Vagrant. Veja o comando abaixo:

```
$ vagrant plugin install vagrant-disksize
```

É importante ressaltar que o IP da VM está configurado como fixo dentro do 'vagrantfile', para os testes de desenvolvimento local foi atribuído o seguinte IP: '192.168.56.56'. Devido a algumas limitações de hardware, a VM foi configurada com 2 'vcpus' e com 4096MB (4GB) de RAM .

## 🔒 SSH

Para a configuração do ssh é necessário gerar novas chaves. O nome da chave gerada é 'id_rsa_slave' e ela precisa estar no mesmo diretório do 'vagrantfile'. Os comandos abaixo vão gerar novas chaves ssh para nossa conexão:

```
$ ssh-keygen -t rsa -b 4096 -C "id_rsa_slave"
$ eval $(ssh-agent) 
$ ssh-add ./id_rsa_slave
```

Para se conectar é necessário copiar o arquivo 'config' para ~/.ssh/. Depois a conexão será estabelecida usando o arquivo config_ssh:

```
$ cp ./config ~/.ssh/
$ ssh teste-zeppelin
```
É essencial que as chaves estejam no mesmo diretório do 'Vagrantfile', pois a chave pública será inserida dentro da VM ao iniciar o processo.

Há um arquivo de configuração chamado 'ssh.config' que contém os parâmetros de conexão ssh (IP, user, port, key). Este arquivo já está configurado com as configurações estáticas para o ambiente de desenvolvimento.


## 🔀 Python

Toda a documentação que foi consultada durante o desenvolvimento está referenciada logo abaixo: 

- `Instalação Openjdk7 no CentOs`: <br>
-   [oficial] https://openjdk.org/install/ <br>
-   [externo] https://phoenixnap.com/kb/how-to-install-java-centos-8

- `Instalação Zeppelin`: <br>
-   [oficial] https://zeppelin.apache.org/docs/latest/quickstart/install.html <br>
-   [externo] https://www.vultr.com/pt/docs/how-to-install-apache-zeppelin-on-centos-7/

- `Manusear txt com Python`: <br>
-   [externo] https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/

Para o processo de criação dos usuários através do 'txt' foi necessário salvar este arquivo dentro da VM, para que durante a inicialização já seja possível criar os usuários, logo após instalar o zepplin. 

O arquivo que sofreu alteração é o 'shiro.ini', é neste arquivo que se faz as configurações dos usuários. Então, basta adicionar os usuários do txt logo abaixo de "[users]" dentro do arquivo 'shiro.ini'.
