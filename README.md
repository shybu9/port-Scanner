# port_Scanner
       ~ THIS TOOL IS TO USED SCAN PORTS AND DUMP ALL THE OPEN PORTS AND THEIR SERVICE INFO
![portscanner help](https://user-images.githubusercontent.com/112984045/201478041-a8c84132-b5b8-4bda-91df-16f3d13ac5ea.png)
![portscanner 1](https://user-images.githubusercontent.com/112984045/201478076-0e223306-ad44-4463-ae55-f62c6fdc5c5b.png)
![portscanner 0](https://user-images.githubusercontent.com/112984045/201478081-581bde0e-616f-40cf-8131-924f0c415c59.png)

## TESTED ON
* KALI LINUX VM(terminal) <br>
* BLACKBOX UBUNTU VM <br>
* ANDROID (termux) <br>  

### PRE-REQUIREMENTS  
* Python3 :
 ```bash 
     sudo apt-get install python3 
 ``` 
  
  
  
* script_requirements (after downloading_script) : 
 ```bash 
     sudo pip3 install -r requirements.txt 
 ```
### DOWNLOADING_SCRIPT :
 ```bash 
     sudo git clone https://github.com/shybu9/portscanner.git 
 ``` 

## USAGE
### SYNTAX :
 ```bash 
    sudo python3 portscanner.py -i <ip address> -p1 < from_port_number> -p2 < to_port_number> -v < select 0 (or) 1 level verbose > -T < threads>
 ```
### EXAMPLES : <br>
 `$ sudo python3 portscanner.py -i 127.0.0.1 -p1 900 -p2 905 -v 0 -T 5`
  
 - After a successful scan you would get all the open ports and their services.
 
* any remarks:<br> 
####      do write to shy.bu9@gmail.com
