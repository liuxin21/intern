1. 在github上建立新的repository

2. 使用ssh-keygen生成公私钥： `$ ssh-keygen` 一直空格下去

```
    lisaideiMac:~ liuxin$ ssh-keygen
    Generating public/private rsa key pair.
    Enter file in which to save the key (/Users/liuxin/.ssh/id_rsa): 
    Created directory '/Users/liuxin/.ssh'.
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in /Users/liuxin/.ssh/id_rsa.
    Your public key has been saved in /Users/liuxin/.ssh/id_rsa.pub.
    The key fingerprint is:
    SHA256:nsNei99FxiS8kD98P3P69V21aa2YikiACYEoUHz57mc liuxin@lisaideiMac.local
    The key's randomart image is:
    +---[RSA 2048]----+
    |*o.  .           |
    |+.. o      o     |
    |o  . .    o o .  |
    | . o  .    + =   |
    |  o ..  S   = = .|
    |     ..o .   = .=|
    |     .. = .   .**|
    |     ..oE= o +.oO|
    |      .o+.+.+ o.+|
    +----[SHA256]-----+
```

`~/.ssh/` 路径下，可以看到生成了两个密钥文件，后缀为 `.pub` 的就是公钥文件，另一个没有后缀的就是私钥文件。

    lisaideiMac:~ liuxin$ cd .ssh
    lisaideiMac:.ssh liuxin$ ls
    id_rsa		id_rsa.pub

首先复制公钥文件中的内容，也就是 ssh-rsa 开头到 用户名@主机名 这段字符串 

    lisaideiMac:.ssh liuxin$ cat id_rsa.pub
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC6FV9hxmPra19RK1ak/qkCbZrQeTEOuHI+hg9Et1vx1Xd5Y6bz0+TyGCEZ/EDlWj68DC9JpGj1A+yPeNJEonDYGuWwoEU9UMYkWFzQY8x1AmrX4pqZqMK2e1je07uVtL3jOEfdoy3gfWVC0jYk4c5re2zbWsRlpchKAFaMeqnVU6KHHyfd/oMaJqs+sx9LF5Dit+Xw6WM3SSP25NgHeFBBdgRq8QBcl2x51vLtDF+vLeglV8yJHY2ieVQQLbUHHiJ8DcAPdervWttLel65iU+cv0p3WC5a8TH4UnRN0ebyaIwYD2rQ9mRpdqGtRmrAS1auRC+Q0LEq9f5VNPINnOk1 liuxin@lisaideiMac.local

复制到github的设置里面的ssh keys

3. 安装git

首先在终端下面敲入 `git --version`， 如果正确回显版本号，则说明已经安装好，如果没有则在终端敲入下面这条命令进行安装:

    $ sudo apt-get install git -y

配置用户名与邮箱:

    ### 如果想设置为全局生效，添加 --global 参数
    $ git config --global user.name "你的用户名"
    $ git config --global user.email "你的邮箱"


4. 克隆刚建的repository到本地

```
    lisaideiMac:~ liuxin$ cd desktop
    lisaideiMac:desktop liuxin$ cd internship
    lisaideiMac:internship liuxin$ git clone git@github.com:liuxin21/intern.git
```