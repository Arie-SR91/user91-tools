echo -e "\e[92mHello World\e[0m";
read -p '
Input command word to install all pkg & tool  : $' userinput1;
#
if [ "${userinput1:-}" = "user91" 6]
then
	pkg  update && pkg upgrade && pkg install python && pkg install python2 && pkg install wget && pkg install curl && pkg install git && pkg install ruby && pkg install lolcat && pkg install php && pip2 install mechanize && pip2 install requests && pkg install neofetch && pkg install nano && pkg install perl && pkg install nodejs && pkg install micro && pkg install joe && pkg install vim && pkg install jupp && pkg install zile && pkg install ne && pkg install figlet && pkg install fish && pkg install toilet
fi
if [ "${userinput1:-}" != "user91" ]
then
	echo -e "\e[31mWrong please input user91\e[0m";
fi
echo -e "\e[92mAll pkg & tools is ready

Lets start hacking now...\e[0m";
