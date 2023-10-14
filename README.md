# MiniCloudDisk

## 简介

MiniCloudDisk 是一个简洁美观的文件夹浏览程序，它提供了一个优雅的方式来浏览服务器上的文件和文件夹。与浏览器自带的文件夹浏览功能相比，MiniCloudDisk 提供了更丰富的视觉体验和更直观的用户界面。

## 功能

- **文件浏览**：MiniCloudDisk 允许用户浏览服务器上的所有文件和文件夹。只需点击链接，即可轻松导航到任何文件或文件夹。

- **文件下载**：MiniCloudDisk 不仅可以浏览文件，还可以下载文件。只需点击文件链接，即可开始下载。

- **目录导航**：MiniCloudDisk 提供了一个简单的目录导航系统。在每个页面的顶部，都有一个链接可以返回上一级目录。

## 使用方法

1. 首先，将 MiniCloudDisk 部署到你的服务器上。通常来说，只要将 `.ApplyChanges.py` 和 `.initindex` 这两个文件复制到你的目标目录中。

2. 修改 `.ApplyChanges.py` 文件中的 `APP_PATH` 变量，使其指向 MiniCloudDisk 的根目录。

3. 运行 `python .ApplyChanges.py` 后启动你的Web应用程序，开放 `.ApplyChanges.py` 所在的目录，这样你就可以浏览这个目录中的文件了。

4. 当文件或目录结构发生变化时，请运行 `.ApplyChanges.py` 程序。这将更新 `index.html` 文件，以反映最新的文件和目录结构。

## 注意事项

- MiniCloudDisk 需要 Python 3.6 或更高版本才能运行。

- 在运行 `.ApplyChanges.py` 之前，请确保你已经正确设置了 `APP_PATH` 变量。

- `.ApplyChanges.py` 程序会覆盖现有的 `index.html` 文件。如果你不希望这样做，请在运行程序之前备份你的 `index.html` 文件。

- MiniCloudDisk 只提供了文件下载功能。如果你需要上传文件，你需要在你的Web应用程序上编写上传代码，不要忘了在你的代码末尾加上运行 `.ApplyChanges.py` 的指令。

- 建议部署到网站托管平台（如Vercel）上，这样就相当于一个免费的云盘。

## 结语

MiniCloudDisk 是一个简洁的文件夹浏览工具，它可以帮助你更好地管理和分享你的文件。无论你是需要在多个设备之间共享文件，还是只是想在网页上浏览你的文件，MiniCloudDisk 都是一个理想的选择。