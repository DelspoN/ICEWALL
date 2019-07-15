apt install -y docker.io unzip
adduser ctf

# password : ctfpassword

usermod -aG docker ctf
usermod -aG sudo ctf



wget http://delspon.com/share/set.zip

unzip set.zip
rm -rf __MACOSX

python shuffleFlag.py

cd ~/login-test
./dockerbuild.sh
./dockerrun.sh

cd ~/php-practice
./dockerbuild.sh
./dockerrun.sh

cd ~
rm -rf shuffleFlag.py
rm -rf set.zip

cat login-test/set.sql
cat php-practice/flag
