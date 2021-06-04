sudo run 

### Check top prcoesses by CPU of container
sudo sysdig -pc -c topprocs_cpu container.name=calibre-web

### Save strace cap file to disk
sudo sysdig -w calibre-web.scap &

### Close the file being read
fg and ctr-c

### Read file saved earlier
sysdig -r calibre-web.scap