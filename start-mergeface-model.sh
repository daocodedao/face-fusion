#!/bin/bash
# 翻译英文视频 为 中文视频

workdir="$PWD"
cd $workdir

echo $workdir

. colors.sh

venvBinDir=venv/bin/
pythonPath=${workdir}/${venvBinDir}python
echo "Python path:  $pythonPath"

echo "${YELLOW}source ${venvBinDir}activate${NOCOLOR}"
source ${venvBinDir}activate

helpFunction()
{
   echo ""
   echo "Usage: $0  -t templateFilePath -s srcFilePath -o outputFilePath"
   echo -e "\t-t template file path"
   echo -e "\t-s src file path"
   echo -e "\t-o output file path"
   exit 1 # Exit script after printing help
}


jobName=utilMergeFaceFromModel.py 
echo "${YELLOW}check $jobName pid${NOCOLOR}"
echo "ps aux | grep "$jobName" | grep -v grep  | awk '{print $2}'"
TAILPID=`ps aux | grep "$jobName" | grep -v grep | awk '{print $2}'`  
if [[ "0$TAILPID" != "0" ]]; then
echo "${RED}kill process $TAILPID${NOCOLOR}"
sudo kill -9 $TAILPID
fi


while getopts "t:s:o:" opt
do
   case "$opt" in
      t ) templateFilePath="$OPTARG" ;;
      s ) srcFilePath="$OPTARG" ;;
      o ) outputFilePath="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

[[ -z  $templateFilePath ]] &&  echo -e "${RED}templateFilePath is empty ${NOCOLOR}" &&  exit 1
[[ -z  $srcFilePath ]] &&  echo -e "${RED}srcFilePath is empty ${NOCOLOR}" &&  exit 1
[[ -z  $outputFilePath ]] &&  echo -e "${RED}outputFilePath is empty ${NOCOLOR}" &&  exit 1



echo -e "${YELLOW}${pythonPath} $jobName  -t '$templateFilePath' -s '$srcFilePath' -o '$outputFilePath'${NOCOLOR}"
${pythonPath} $jobName  -t "$templateFilePath" -s "$srcFilePath"  -o "$outputFilePath"


# /data/work/face-fusion/start-mergeface.sh -t "./images/liudehua.jpg" -s "./images/zhoujielun.jpg"  -o "out/out.jpg"

# /mnt/data/face-fusion/start-mergeface.sh -t "./images/liudehua.jpg" -s "./images/zhoujielun.jpg"  -o "out/out.jpg"