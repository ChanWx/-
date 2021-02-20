## 线程

# 1. 线程的介绍
#     在Python中，想要实现多任务除了使用进程，还可以使用线程来完成，线程是实现多任务的另外一种方式。

# 2. 线程的概念
#     线程是进程中执行代码的一个分支，每个执行分支（线程）要想工作执行代码需要cpu进行调度 ，也就是说线程是cpu调度的基本单位，每个进程至少都有一个线程，而这个线程就是我们通常说的主线程。

# 3. 线程的作用
#     多线程可以完成多任务
#     TODO:程序启动默认会有一个主进程,程序员自己创建的进程可以称为子进程,多线程可以完成多任务.

# 4. 小结
#     线程是Python程序实现多任务的另外一种方式,线程的执行需要CPU调度来完成

## 多线程的使用

# 1. 导入线程模块
#     import threading

# 2. 线程类Thread参数说明
#     Thread([group [, target [, name [, args [, kwargs]]]]])
#         group: 线程组，目前只能使用None
#         target: 执行的目标任务名
#         args: 以元组的方式给执行任务传参
#         kwargs: 以字典方式给执行任务传参
#         name: 线程名，一般不用设置

# 3. 启动线程
# 启动线程使用start()方法

# 4. 多线程完成多任务代码


# 5. 小结
#     1. 导入线程模块
#         import threading
#     2. 创建子进程并指定执行的任务
#         subthread = threading.Thread(target=任务名)
#     3. 启动线程执行任务
#         subthread.start()

## 线程执行带有参数的任务

# 1. 线程执行带有参数任务介绍
#     前面我们使用线程执行的任务是没有参数的，假如我们使用线程执行的任务带有参数，如何给函数传参呢?
#     Thread类执行任务并给任务传参数有两种方式
#         args 表示以元组的方式给执行任务传参
#         kwargs 表示以字典方式给执行任务传参

# 2. args参数的使用

# 3. kwargs参数的使用

# 4. 小结

## 线程的注意点

# 1. 线程的注意点介绍
#     线程之间执行是无序的
#     主线程会等待所有的子线程执行结束再结束
#     线程之间共享全局变量
#     线程之间共享全局变量数据出现错误问题

# 2. 线程之间执行是无序的

# 3. 主进程会等待所有的子线程执行结束再结束

# 4. 线程之间共享全局变量数据出现错误问题


## 互斥锁

# 1. 互斥锁的概念
#     对共享数据进行锁定,保证同一时刻只有一个线程去操作
#     TODO:互斥锁是多个线程一起去抢,抢到锁的线程先执行,没有抢到锁的线程需要等待,等互斥锁使用完释放后,其它等待的线程再去抢这个锁

# 2. 互斥锁的使用

# 3. 使用互斥锁完成2个线程对同一个全局变量各加100万次的操作

# 4. 小结
#     互斥锁的作用就是保证同一时刻只能有一个线程去操作共享数据,保证共享数据不会出现错误问题
#     使用互斥锁的好处确保某段关键代码只能由一个线程从头到尾完整地去执行
#     使用互斥锁会影响代码的执行效率,多任务改成了单任务执行
#     互斥锁如果没有使用好容易出现死锁的情况

## 死锁

# 1. 死锁的概念
#     一直等待对方释放锁的情景就是死锁,结果就是会造成应用程序停止响应,不再处理其他任务

# 2. 死锁示例

# 3. 避免死锁

# 4. 小结
#     使用互斥锁的时候需要注意死锁的问题,要在合适的地方注意释放锁
#     死锁一旦产生就会造成应用程序的停止响应,应用程序无法再继续往下执行了 