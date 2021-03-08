# 静态web服务器命令行启动动态绑定端口号

# # 1. 开发命令行启动动态绑定端口号的静态web服务器
#     实现步骤
#         1. 获取执行python程序的终端命令行参数
#         2. 判断参数的类型,设置端口号必须是整数
#         3. 给web服务器类的初始化方法添加一个端口号参数,用于绑定端口号

# 2. 示例代码

import os
import sys
import socket
import threading


class HttpWebServer(object):

    def __init__(self, port):
        # 创建TCP服务端套接字
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        serverSocket.bind(('', port))
        # 设置监听
        serverSocket.listen(128)
        # 把TCP服务器的套接字作为web服务器对象的属性
        self.serverSocket = serverSocket

    @staticmethod
    def handleClientRequest(newSocket):
        # 接受客户端的请求信息
        recvdata = newSocket.recv(4096)
        # 判断接受数据长度是否为0
        if len(recvdata) == 0:
            newSocket.close()
            return
        # 对二进制数据进行解码
        recvcont = recvdata.decode('utf-8')
        print(recvcont)
        # 对数据按照空格分割
        requestlist = recvcont.split(' ', maxsplit=2)
        # 获取请求资源路径
        requestpath = requestlist[1]
        print(requestpath)
        # 判断请求的是否是跟目录,如果是跟目录返回指定首页
        if requestpath == "/":
            requestpath = '/index.html'

        # TODO: 返回404界面
        # 方式一:os.path.exits
        # os.path.exits('static'+requestpath)

        try:
            # 打开文件读取文件中的数据
            with open('static'+requestpath, 'rb') as f:
                filedata = f.read()
        # TODO: 返回404页面
        except Exception as e:
            # 代码执行到此,说明没有请求的文件,需要返回404页面
            # 404响应行
            responseline = 'HTTP/1.1 404 NOT FOUND\r\n'
            # 404响应头
            responseheader = 'SERVER: PWS\r\n'
            # 打开404指定页面文件内容
            with open('static/error.html', 'rb') as f:
                filedata = f.read()
            # 404响应体
            responsebody = filedata
            # 404响应内容
            response = (responseline + responseheader +
                        '\r\n').encode('utf-8') + responsebody
            # 把数据封装成HTTP响应报文格式数据
            newSocket.send(response)
        else:
            # 代码执行到此,说明文件存在,返回200状态信息
            # 响应行
            responseline = 'HTTP/1.1 200 OK\r\n'
            # 响应头
            responseheader = 'SERVER: PWS\r\n'
            # requestStr = "static\" + requestpath
            # 响应体二进制的数据
            responsebody = filedata
            # 响应行响应头转二进制
            response = (responseline + responseheader +
                        '\r\n').encode('utf-8') + responsebody
            # 把数据封装成HTTP响应报文格式数据
            newSocket.send(response)
        finally:
            # 关闭服务于客户端套接字
            newSocket.close()

    # 启动服务器的方法
    def start(self):
        while True:
            # 等待接受客户端的连接请求
            newSocket, ipPort = self.serverSocket.accept()
            # 代码执行到此,说明连接建立成功
            subthread = threading.Thread(
                target=self.handleClientRequest, args=(newSocket,))
            # 设置成为守护主线程
            subthread.setDaemon(True)
            # 启动子线程执行对应任务
            subthread.start()


def main():

    # 获取终端命令行参数,返回字符串类型
    params = sys.argv
    if len(params) != 2:
        print('执行命令格式:python fileName.py PortNum')
        return

    # 代码执行到此,说明命令行参数是2个
    print(params)

    # 判断第二个参数是由数字组成的字符串
    if not params[1].isdigit():
        print('执行命令格式:python fileName.py PortNum')
        return

    # 代码执行到此,说明命令行参数是2个,第二个参数是由数字组成的
    port = int(params[1])

    # 创建web服务器
    webServer = HttpWebServer(port)
    # 启动服务器
    webServer.start()


if __name__ == '__main__':
    main()
