# gpg --full-generate-key

# needed to have interactive session for password
export GPG_TTY=$(tty)

input=$1
output=$2

cmd="tar --zstd "
key=$3


# $3 is of the form path1;path2;path3...
for x in ${3//;/ }; do
    cmd="$cmd --exclude=$x"
done

# cmd="$cmd -cv $input | gpg -c | split -b 100M  - $output.tar.zst.gpg."
cmd="$cmd -cv $input | gpg --encrypt -r $key | split -b 100M  - $output.tar.zst.gpg."

echo $cmd

eval $cmd


# server=pi@192.168.1.166



# rsync -aP --partial-dir=.rsync-partial $archname.* $server:$output

# rm -r tmp
