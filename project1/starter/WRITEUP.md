Azure Virtual Machines provide infrastructure as a service (IaaS) by allowing you to create and use virtual machines in the cloud. 
Install whatever you want in the server in the region you want to install, it can install windows or webserver service,
Full control of your server, choose the operating system
+ Operational overhead: Reduced upfront costs compared to buying and maintaining hardware.
	0.0060 USD/hr
	size: Standard_B1ls - 1 vcpu, 0.5 GiB memory (4,38 US$/month)
+ Scalability
		Support of both Linux and Windows.
		Azure Virtual Machines allow for the installation of custom image, virtual machine size, network parameters
		Memory-optimized Azure Virtual Machines, along with varying amounts of CPU, RAM, and storage.
+Availability, and workflow	
	Support of both Linux and Windows.
	Only pay for each VM instance that you create

	
Azure App Service is an HTTP-based service for hosting web applications, REST APIs, and mobile back ends. 
It is a Platform as a Service (PaaS) that allows a developer to focus on the application while Azure takes care of the infrastructure.
+ Operational overhead: less management overhead
Change size: Spec Picker (dev/test, Production, isoiated): F1 1GB memory 60 minutes/day compute Free 
			 B1 100 total ACU, 1.75 GB memory, A-Series compute equivalent, 13.14 USD/Month 			 
+ Scalability
	Support of multiple languages, such as .NET, .NET Core, Java, Ruby, Node.js, PHP, or Python
	Continuous deployment using GitHub, Azure DevOps, Git repo.	
+ Availability, and workflow	
	High availability, auto-scaling, support of both Linux and Windows environments.
	Scale up to many servers
	Choice of many frameworks

I find Azure Virtual Machines usually better, it can install web server or windows, Linux services, 
optimized for computers, full control over the server, choose the operating system, scaling, deploy applications to environments quickly, with flexibility. 
what about the Azure App service is still limited, such as a maximum of 14GB of memory and 4 vCPU cores per instance, cannot control the operating system