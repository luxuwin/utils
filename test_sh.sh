# cleanup

rm -rf ./testdest/*
rm -rf ./testrestore/*

key=test@key

# archive
./tar_folder.sh ./testsource  ./testdest/testsource_arch $key "./testsource/l1/" 
#./tar_folder.sh ./testsource  ./testdest/testsource_arch $key "./testsource/l1/;./testsource/l2/" 

# restore
./restore_folder.sh ./testdest/testsource_arch.tar.zst.gpg.aa ./testrestore/ $key
