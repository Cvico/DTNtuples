mkdir /eos/home-j/jleonhol/www/resolutionsAM
mkdir /eos/home-j/jleonhol/www/resolutionsHB
mkdir /eos/home-j/jleonhol/www/resolutionsAMAllST
rm /eos/home-j/jleonhol/www/resolutionsAM/*
rm /eos/home-j/jleonhol/www/resolutionsHB/*
rm /eos/home-j/jleonhol/www/resolutionsAMST/*
cp /eos/home-j/jleonhol/backup/index_resol_php /eos/home-j/jleonhol/www/resolutionsAM/index.php
cp /eos/home-j/jleonhol/backup/index_resol_php /eos/home-j/jleonhol/www/resolutionsAMST/index.php
cp /eos/home-j/jleonhol/backup/index_resol_php /eos/home-j/jleonhol/www/resolutionsHB/index.php
cp ./plotsPU0ST/*AM*.png /eos/home-j/jleonhol/www/resolutionsAMST 
cp ./plotsPU0/*AM*.png /eos/home-j/jleonhol/www/resolutionsAM 
cp ./plotsPU0/*HB*.png /eos/home-j/jleonhol/www/resolutionsHB
