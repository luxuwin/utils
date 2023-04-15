# cleanup

rm -rf ./testdest/*
rm -rf ./testrestore/*

# archive
python3 ./archive.py

# restore
python3 ./restore.py
