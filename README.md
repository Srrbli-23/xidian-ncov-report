
# 疫情通 懒狗版本

非常感谢 @Apache553 (apache553@outlook.com)  提供的原始代码

非常感谢 @xinian (1161678627@qq.com) 提供的思路

## Feature

1. 自动填报 自动配置
2. 随机生成地理位置 (坐标和地址)
3. 可以在树莓派等平台上后台运行

## Usage

### 配置

```bash
vim ./config_lazy.py
```
打开之后,在 `user_name` 和 `user_pswd` 中 按顺序填入需要填报的 **统一认证账号和密码**
```python3
# Demo
user_name = ["16020110001","16020138001"]
user_pswd = ["ThisUnitLoss","MyP@ssWord"]
```
之后程序会自动遍历字典并尝试对每一个用户进行填写

### 测试

```bash
python3 ./submit_lazy.py
```

* 结果输出至控制台

### 使用 (Linux/Debian下)
 
 挂机使用

```bash
python3 ./submit_lazy.py &
```

 开启自启动 (经常断电的宿舍)

在控制台里

```bash
sudo vim /etc/rc.local
```

在键盘上按下i键(进入编辑模式),之后在 exit 0 之前 填入

```bash
sudo python3 /home/pi/xidian-ncov-report/submit_lazy.py &
```

然后按下Esc键退出编辑,再敲入 `:w` 退出vim