# Speaker-recognition-
Speaker recognition project for fun. Aim to find the voice of special speaker in videos

基础架构

1、语音提取模块
   从视频中分辨出人声并提取成语音文件，每个文件包含10s语音信息。
2、说话人识别引擎
    从训练集中学习说话人声音特征，并能对预测集进行打分，当高于一定阈值，则判定为被识别人声音
3、视频剪辑模块
     根据结果，对视频文件进行剪辑（从离散的信号合成意识基本连贯的视频片段）
