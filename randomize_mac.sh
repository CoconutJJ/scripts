
RAND_MAC=$(openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//')
sudo /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport en0 -z
sudo /sbin/ifconfig en0 ether $RAND_MAC
echo "Changed MAC Address to ${RAND_MAC}"