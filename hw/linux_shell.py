import sys
import paramiko
import random
from . import view_all



def getport():
	return random.randint(20000,65000)

def main():
	def getport():
		return random.randint(20000,65000)
	
	server=0
	server_client=[]
	server_client.append({
		"ip":view_all.ip,
		"port":22,
		"user":'root',
		"password": 'xx',
	})


	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


	ssh.connect(server_client[server]['ip'],server_client[server]['port'],server_client[server]['user'],server_client[server]['password'],timeout = 10)


	newport=getport()
	print(newport)
	stdin,stdout,stderr = ssh.exec_command("sh /root/1.sh "+str(newport))
	result = stdout.read()
	print(result)
	return str(newport)+"\n  -- "+str(result)
	ssh.close()

if __name__ == "__main__":
	main()