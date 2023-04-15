
server=$1 # user@ip
archname=$2
output=$3

rsync -aP --partial-dir=.rsync-partial $archname.* $server:$output
