# png-compress 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=png-compress&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=png-compress" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=png-compress&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=png-compress" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=png-compress&type=packageDownload">
  </a>
</p>

<description>

> ***基于 pngquant 的高质量 PNG 图片压缩功能***

</description>

<table>

## 前期准备
使用该项目，推荐您拥有以下的产品权限 / 策略：

| 服务/业务 | 函数计算 |     
| --- |  --- |   
| 权限/策略 | AliyunFCFullAccess |     


</table>

<codepre id="codepre">

# 代码 & 预览

- [:smiley_cat: 源代码](https://github.com/anycodes/png-compress)

        

</codepre>

<deploy>

## 部署 & 体验

<appcenter>

- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=png-compress) ，
[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=png-compress)  该应用。 

</appcenter>

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 初始化项目：`s init png-compress -d png-compress`   
    - 进入项目，并进行项目部署：`cd png-compress && s deploy -y`

</deploy>

<appdetail id="flushContent">

# 应用详情

当前应用仅支持 PNG 图片的压缩，压缩效果如下：

![](http://image.editor.devsapp.cn/evBw7lh8ktv6xDBzSSzvjr1ykchAF9hG41gf1ek1sk8tr4355A/7bExa4bcCCEEC8BwatAb)

部署当前应用之后，可以通过返回的地址进行测试，也可以通过api进行调用：

地址：`http://你的域名/compress`
参数：
```
  Headers:
     Content-type: application/json
  Body:
     image: 图片Base64后的字符串(base64后最大不可以超过5M)
     min_quality: 质量区间，默认65
     max_quality: 质量区间，默认80
     speed: 压缩速度（默认3，最高10）
```
案例：
```
import requests
import base64
def getResult(imagePath):
    with open(imagePath, 'rb') as f:
        data = f.read()
    image = str(base64.b64encode(data), encoding='utf-8')
    data = json.dumps({"image": 'data:image/png;base64,'+image, "min_quality": "65", "max_quality": "80", "speed": "3"})
    txt = requests.post("http://localhost:7291/compress", data=data,
                        headers={'Content-Type': 'application/json'})
    return txt.content.decode("utf-8")
print(getResult("./test.png"))
```

</appdetail>

<devgroup>

## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
|--- | --- | --- |
| <center>微信公众号：`serverless`</center> | <center>微信小助手：`xiaojiangwh`</center> | <center>钉钉交流群：`33947367`</center> | 

</p>

</devgroup>