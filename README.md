# mozhe-doc-merge
墨者写作软件由于近日官方不再支持，软件无法登录，里面的存稿也无法导出，故自己动手写了一个程序，将墨者里的存稿提取出并合并为一个Markdown文件导出。

## 使用方式
- 找到并进入mozhes_backups文件夹。
![1](https://github.com/haomingdouranggouqil/mozhe-doc-merge/blob/main/1.png)
- 进入该文件夹后，可以看到墨者中建立的书籍在这里保存为不同名称的文件夹，如图，在墨者中所建立的名为《遗音》的书籍，对应文件夹为“500-遗音”（其中每卷为一个子文件夹，每个卷文件夹中又有多个txt文件对应章节内容），将gen.exe文件或gen.py文件粘贴进来（能运行python文件就粘gen.py,不能运行python文件就粘gen.exe，两个程序作用一致）
![2](https://github.com/haomingdouranggouqil/mozhe-doc-merge/blob/main/2.png)
- 运行python文件或双击运行exe文件，在弹出的命令行窗口输入想要提取出的书籍对应的文件夹名称，如“500-遗音”，然后回车。
![3](https://github.com/haomingdouranggouqil/mozhe-doc-merge/blob/main/3.png)
- 生成一个Markdown文件


![4](https://github.com/haomingdouranggouqil/mozhe-doc-merge/blob/main/4.png)
![5](https://github.com/haomingdouranggouqil/mozhe-doc-merge/blob/main/5.png)
