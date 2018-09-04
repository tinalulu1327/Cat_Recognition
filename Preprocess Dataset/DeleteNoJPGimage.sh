ls | while read name
do
file $name |  grep "JPEG image data" >/dev/null
if [ $? != 0 ]; then
echo $name >> ../delete.txt
rm -rf $name
fi
done
