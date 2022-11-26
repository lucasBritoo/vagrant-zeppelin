# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<-SCRIPT
ls
python ./main.py
SCRIPT

#doc https://developer.hashicorp.com/vagrant/docs/provisioning/file
Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.disksize.size = "50GB"
  config.vm.network "forwarded_port", guest: 8888, host: 8888
  config.vm.network "private_network", ip: "192.168.56.56"
  config.vm.provision :file, source: './id_rsa_slave.pub', destination: "~/.ssh/authorized_keys"
  config.vm.provision :file, source: 'main.py', destination: "main.py"
  config.vm.provision :file, source: 'lista_usuarios_zeppelin.txt', destination: "lista_usuarios_zeppelin.txt"
  config.vm.provision :file, source: 'shiro_template.txt', destination: "shiro_template.txt"
  #config.vm.provision :file, source: 'zeppelin.service', destination: "zeppelin.service"
  #config.vm.provision :file, source: 'zeppelin.conf', destination: "zeppelin.conf"
  config.vm.provision :file, source: 'zeppelin-env.sh', destination: "zeppelin-env.sh"
  config.vm.provision :file, source: 'zeppelin-site.xml', destination: "zeppelin-site.xml"
  config.vm.provision "shell", inline: $script

  
  config.ssh.private_key_path = ['./id_rsa_slave', '~/.vagrant.d/insecure_private_key']
  config.ssh.insert_key = false

  config.vm.provider "virtualbox" do |v|
    v.memory = 4096
    v.cpus = 4
    v.name = "teste-zeppelin"
  end


end
