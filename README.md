基于TCP/UDP的socket套接字编程
===

### OSI七层和TCP/IP四层关系

1. OSI引入了服务，接口，协议，分层的概念．TCP/IP借鉴了OSI的这些概念建立TCP/IP模型
2. OSI先有模型，后有协议，先有标准，后进行实践．TCP/IP则相反，先有协议和应用在提出了模型，且是参照的OSI模型
3. OSI是一种理论下的模型，而TCP/IP已被广泛使用，成为网络互联事实上的标准

### 四层模型(TCP/IP模型)
* #### 应用层
>负责处理应用程序的逻辑
>e.g. 电子邮件传输(SMTP)，文件传输协议(FTP)，网络远程访问协议(Telnet)
* #### 传输层
>提供了节点间的数据传输服务
>e.g. 传输控制协议(TCP)，用户数据报协议(UDP)
* #### 网络层
>负责提供基本的数据封包传送功能
>e.g. 网际协议(IP)
* #### 网络接口
>对实际的网络媒体的管理
>e.g. 定义如何使用实际网络来传送数据

### TCP协议
* 传输特征：提供了可靠的数据传输，可靠性指数据传输过程过程中无丢失，无失序，无差错，无重复
* 实现手段：在通信前需要建立数据连接，通信结束要正常断开连接
* 适用情况：对数据传输准确性有明确要求，传输文件较大，需要确保可靠性的情况．比如：网页获取，文件下载，邮件收发

>三次握手(建立连接)
>>客户端向服务器发送消息报文请求连接

>>服务器收到请求后，回复报文确定可以连接

>>客户端收到回复，发送最终报文建立连接

>四次挥手(断开连接)
>>主动发送报文请求断开连接

>>被动方收到请求后，立刻回复，表示准备断开

>>被动方准备就绪，再次发送报文准备可以断开

>>主动方收到确定，发送最终报文完成断开

### UDP协议
* 传输特点：不保证传输的可靠性，传输过程没有连接诶和断开，数据收发自由随意
* 适用情况： 网络较差，对传输可靠性要求不高．比如：网络视频，群聊，广播

### socket套接字编程
#### 套接字介绍
* 套接字：实现网络编程进行数据传输的一种技术手段
* Python实现套接字编程：**import socket**
* 套接字分类
>流式套接字(SOCK_STREAM)：以字节流方式传输数据，实现tcp网路传输方案．（面向连接--tcp协议--可靠的--流式套接字）

>数据报套接字(SOCK_DGRAM)：以数据报形式传输数据，时间udp网络传输方案．（无连接--udp协议--不可靠--数据报套接字）

#### TCP套接字编程

>服务端
>>基本流程 | 关键字
>> :---: | :---: 
>>创建套接字 | socket
>>绑定地址 | bind
>>设置监听 | listen
>>等待处理客户端连接请求 | accept
>>消息收发 | send / recv
>>关闭套接字 | close

>客户端
>>基本流程 | 关键字
>> :---: | :---: 
>>创建套接字 | socket
>>请求连接 | connect
>>收发消息 | send / recv
>>关闭套接字 | close

##### tcp套接字数据传输特点
* tcp连接中当一端退出，另一端如果阻塞在recv，此时recv会立刻返回一个空字符串
* tcp连接中如果一端已经不存在，仍然试图通过send发送则会产生BrokenPipeError
* 一个监听套接字可以同时连接多个客户端，也能够重复被连接
##### 网络收发缓冲区
* 网络缓冲区有效的协调了消息的收发速度
* send和recv实际是向缓冲区发送接收消息，当缓存区不为空recv就不会阻塞
##### tcp粘包
* 原因：tcp以字节流方式传输，没有消息边界，多次发送的消息被一次接收，此时就会形成粘包
* 影响：如果每次发送内容是一个独立的含义，需要接收端独立解析此时粘包会有影响
* 处理方式
>* 人为的增加消息边界
>* 控制发送速度

#### UDP套接字编程
>服务端
>>基本流程 | 关键字
>> :---: | :---: 
>>创建套接字 | socket
>>绑定地址 | bind
>>消息接收 | recvfrom
>>消息发送 | sendto
>>关闭套接字 | close

>客户端
>>基本流程 | 关键字
>> :---: | :---: 
>>创建套接字 | socket
>>消息接收 | recvfrom
>>消息发送 | sendto
>>关闭套接字 | close

#### TCP|UDP套接字编程区别
* 流式套接字是以字节流方式传输数据，数据报套接字以数据报形式传输
* tcp套接字会有粘包，udp套接字有消息边界不会粘包
* tcp套接字保证数据的完整性,udp套接字则不能
* tcp套接字依赖listen,accept建立连接才能收发消息，udp套接字则不需要
* tcp套接字使用send, recv收发消息，udp套接字使用sendto, recvfrom收发消息




































