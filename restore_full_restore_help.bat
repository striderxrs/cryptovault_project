start /B cmd.exe
 
cd C:\Users\Strider\Desktop\Cryptovault\s3-backup

python s3restore.py full-restore -h

cmd /k "cd /d C:\Users\Strider\Desktop\Cryptovault\s3-backup\"
