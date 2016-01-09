# Ass2Lrc

This is a simple script that can convert the .ass file generated in Aegisub or other conventional ass generator(untested) into .lrc lyrics file, running in Python 2.7.x terminal.

Please note that in this version all information in .ass file other than lyrics and starting timeline will be discarded in the generated .lrc file.

The generated .lrc file will have the same filename but different format with the .ass file. 


这个脚本可以把Aegisub或者其他字幕制作软件的ass文件转换成lrc歌词文件。此脚本可运行在Python 2.7.x控制台下。

在目前版本生成的.lrc文件只会保留歌词与起始时间线，其余ass信息均不会保留

生成的lrc文件与ass文件同名不同格式




##Usage
<code>python ass2lrc.py filename.ass</code>

**filename.ass** is the original .ass file and the script will generate **filename.lrc** if no exception occurs.
