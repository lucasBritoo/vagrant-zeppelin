# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.disksize.size = "50GB"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "private_network", ip: "192.168.56.56"
  config.vm.provision :file, source: './id_rsa_slave.pub', destination: "~/.ssh/authorized_keys"
  
  config.ssh.private_key_path = ['./id_rsa_slave', '~/.vagrant.d/insecure_private_key']
  config.ssh.insert_key = false

  config.vm.provider "virtualbox" do |v|
    v.memory = 4096
    v.cpus = 2
    v.name = "teste-zeppelin"
  end


end
