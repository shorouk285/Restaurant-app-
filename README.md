##Item Catalog - Restaurants and Menus

* This application views restaurants called from a database and their menu items.
* All CRUD operations are working efficiently
* Authenticated users can add new restaurants and menu items.
* Only the creator of a restaurant can edit it.


###Third-party
* This application uses google sign in, and facebook sign in.


##OAuth
* oAuth is used to authenticate users.
###How to run?

1. After downloading this files, Place it in the same folder as vagrant file.
2. In your terminal change directory to where you downloaded the files.
3. Run vagrant up then vagrant ssh
4. Make sure that  database required for this project python database_setup.py & python lotsofmenus.py included in the folder
5. Run the application python project.py
6. Open your favorite browser and head to [(http://localhost:8000)] and enjoy the application.


###We're using the Vagrant software to configure and manage the VM. Here are the tools you'll need to install to get it running:
You will need Git to install the configuration for the VM.

####Git
If you don't already have Git installed, download Git from **git-scm.com**. Install the version for your operating system.

**On Windows**, Git will provide you with a Unix-style terminal and shell (Git Bash).
(On **Mac or Linux** systems you can use the regular terminal program.)



####VirtualBox
VirtualBox is the software that actually runs the VM. You can download it from **virtualbox.org**, here. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

**Ubuntu 14.04 Note**: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

####Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. You can download it from **vagrantup.com**. Install the version for your operating system.

**Windows Note**: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

Fetch the Source Code and VM Configuration
**Windows**: Use the Git Bash program (installed with Git) to get a Unix-style terminal.
**Other systems**: Use your favorite terminal program.

##From the terminal:
1. Go to the vagrant directory
2. Run **vagrant up**, and wait until it finishes
3. After vagrant is ready, Run **vagrant ssh**


Now that you have Vagrant up and running type vagrant ssh to log into your VM. change to the /vagrant directory by typing cd /vagrant. This will take you to the shared folder between your virtual machine and host machine.

Type ls to ensure that you are inside the directory that contains project.py, database_setup.py, and two directories named 'templates' and 'static'

Now type python database_setup.py to initialize the database.

Type python lotsofmenus.py to populate the database with restaurants and menu items. (Optional)

Type python project.py to run the Flask web server. In your browser visit http://localhost:8000 to view the restaurant menu app. You should be able to view, add, edit, and delete menu items and restaurants.

##References
This code is based on Udacity Course.
Database files are from Udacity.
