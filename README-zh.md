## Online  Chatroom with Flask+Vue3

### 功能

1. 用户注册、登录
2. 多房间支持
3. 实时收发消息，查看历史记录



### 部署

##### 前端

安装依赖并打包部署

```shell
cd @/frontend
yarn install
yarn build
```

将生成的`/dist`文件夹部署至nginx服务器上

```shell
# ~/nginx/nginx.conf
http {

	# ...

	server {
		listen	8082
		server_name     localhost;

                location / {
                        alias           /home/ubuntu/flask-vue3-chatroom/frontend/dist/;
                        index           index.html;
                        try_files       $uri $uri/ /index.html;
                }
	}
}
```



##### 后端

修改数据库连接及秘钥

```shell
# @/backend/app/config.py
DATABASE = {
    'dev': {
        'host': ${HOST},
        'port': ${PORT},
        'user': ${USER},
        'passwd': ${PASSWORD} 
    }
}

SECRET_KEY = ${SECRET_KEY}
```

安装`gunicorn`模块

```shell
sudo apt install gunicorn
```

安装依赖并使用gunicorn启动服务

```shell
cd @/backend
pip3 install -r requirements.txt
# -w 为启动进程个数，-b 为启动端口号
nohup gunicorn -w 4 -b 0.0.0.0:23456 app:app > info.log 2>&1 &
```

将服务部署至nginx服务器上，与前端在相同端口下

```shell
# ~/nginx/nginx.conf
http {

	# ...
	
	server {
		listen	8082
		server_name     localhost;

            	# ...
                
                 location /api {
                        proxy_pass              http://0.0.0.0:23456;
                        proxy_set_header        Host $host;
                        proxy_set_header        X-Real-IP $remote_addr;
                        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
                }

                location /socket.io {
                        proxy_pass              http://0.0.0.0:5000;
                        proxy_set_header        Host $host;
                        proxy_set_header        X-Real-IP $remote_addr;
                        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
                }
	}
}
```

