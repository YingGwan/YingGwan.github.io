from livereload import Server, shell
server = Server()
# 监听文件/目录
server.watch('index.html')
server.watch('static/', delay=0.2)
# 启动静态服务器（根目录即站点根）
server.serve(root='.', port=8000, host='127.0.0.1', open_url_delay=0.5)