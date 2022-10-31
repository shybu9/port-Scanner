# port-Scanner
THIS TOOL IS USED SCAN PORTS AND DUMP ALL THE OPEN PORTS AND THEIR SERVICE INFO
## TESTED ON 
  
 * KALI LINUX vm(terminal) 
 * BLACKBOX UBUNTU vm(terminal) 
 * ANDROID (termux) 
  
  
 ### PRE-REQUIREMENTS  
 * python3 : 
 ```bash 
     sudo apt-get install python3 
 ``` 
  
  
  
 * script_requirements (after downloading_script) : 
 ```bash 
     sudo pip3 install -r requirements.txt 
 ```  
 ### DOWNLOADING_SCRIPT : 
 ```bash 
     sudo git clone https://github.com/shybu9/portscanner.git 
 ``` 
 ## USAGE  
  
 ### SYNTAX :  
 ```bash 
    sudo python3 portscanner.py -i <ip address> -p1 < from_port_number> -p2 < to_port_number> -T < threads>
 ``` 
  
 ### EXAMPLES : 
 `$ sudo python3 portscanner.py -i 127.0.0.1 -p1 900 -p2 1000 -T 5
  
 1.try to send http requests or simply use web on a mechine which is connected to same network interface given.<br> 
 2.this data will be sniffed and shown on terminal<br> 
 3.any remarks:<br> 
 ####     do write to shy.bu9@gmail.com
