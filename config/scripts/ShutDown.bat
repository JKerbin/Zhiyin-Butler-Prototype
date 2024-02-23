CHCP 65001 

:: 正常关机 
@echo off
echo ready to shutdown your computer...
shutdown -s -t 60
echo already shutdown!

:: 取消关机
shutdown -a


:: 设定在多久后关机
@echo off
echo 请输入关机时间 （单位：秒）：
set /p time=
echo 将在 %time% 秒后关机。
shutdown -s -t %time%

