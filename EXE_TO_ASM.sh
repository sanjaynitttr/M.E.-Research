for file in ./*.exe
do
  objdump -D "$file"> /home/sanjayme2014/Desktop/asm/"$file".asm
done
