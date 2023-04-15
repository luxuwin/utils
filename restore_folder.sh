input=$1
output=$2
# receipt of the gpg key. usually an email
key=$3
cmd="cat $input | gpg --decrypt | zstd -d | tar -x -C $2"
#cmd="cat $input | gpg --decrypt -r $key | tar -x --use-compress-program=zstd -C $2"
echo $cmd
eval $cmd
