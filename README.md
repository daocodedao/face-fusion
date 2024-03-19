
# 安装
## 环境 
```
cd 到代码目录
python3.10 -m venv venv
source venv/bin/activate

基于 cuda11.8
requirements.txt 添加 --extra-index-url https://download.pytorch.org/whl/cu118

pip install -r requirements.txt 
```



## 使用
```
# java1 java2 机器调用
# 参数 -t 图片1绝对路径
# 参数 -s 图片2绝对路径
# 参数 -o 合并后的图片保存路径
/mnt/data/face-fusion/start-mergeface.sh -t "./images/liudehua.jpg" -s "./images/zhoujielun.jpg"  -o "out/out.jpg"
```

