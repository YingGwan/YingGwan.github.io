这是一个基于 Jekyll 的个人网站。要在本地预览您的网站并立即看到修改效果，您可以按照以下步骤操作：

### 1. 确保已安装 Ruby 和 Bundler

您的电脑上需要安装 Ruby 环境。如果您还没有安装，推荐使用 [RubyInstaller for Windows](https://rubyinstaller.org/) 进行安装（建议包含 DevKit）。

安装完成后，在命令行（PowerShell 或 CMD）中运行以下命令安装 `Bundler`（用于管理项目的依赖）：

```
powershell







gem install bundler
```

### 2. 安装项目依赖

打开您的终端（PowerShell），导航到您的网站项目文件夹 `e:\DropboxFolder\Dropbox\x-codeBase\x-personalWebpage`，然后运行：

```
powershell







bundle install
```

这个命令会根据您项目中的 `Gemfile` 自动下载并安装所需的所有包（也就是 gems，比如 `github-pages` 等）。

### 3. 启动本地服务器

依赖安装完成后，运行以下命令启动本地预览服务器：

```
powershell







bundle exec jekyll serve
```

或者，如果您希望在修改文件后网页能够**自动实时刷新**（Live Reload），可以加上 `--livereload` 参数：

```
powershell







bundle exec jekyll serve --livereload
```

### 4. 在浏览器中查看效果

服务器启动成功后，终端会输出一个本地网络地址，通常是： `http://127.0.0.1:4000/` 或 `http://localhost:4000/`

把这个地址复制到您的浏览器里打开，您就可以在本地实时看到 `SensorOpt` 这篇文章排版出来的实际效果了！每次您保存修改，网页都会自动更新。
