# image-compress-ssim 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=image-compress-ssim&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=image-compress-ssim" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=image-compress-ssim&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=image-compress-ssim" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=image-compress-ssim&type=packageDownload">
  </a>
</p>

<description>

> ***图片压缩功能***

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

- [:smiley_cat: 源代码](https://github.com/rsonghuster/image-compress-ssim)

        

</codepre>

<deploy>

## 部署 & 体验

<appcenter>

- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=image-compress-ssim) ，
[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=image-compress-ssim)  该应用。 

</appcenter>

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 初始化项目：`s init image-compress-ssim -d image-compress-ssim`   
    - 进入项目，并进行项目部署：`cd image-compress-ssim && s deploy -y`

</deploy>

<appdetail id="flushContent">

# 应用详情

比如 PNG 图片压缩效果如下：

![](http://image.editor.devsapp.cn/evBw7lh8ktv6xDBzSSzvjr1ykchAF9hG41gf1ek1sk8tr4355A/7bExa4bcCCEEC8BwatAb)

您可以使用 s 工具/控制台/sdk代码调用函数， 其中调用函数的 payload 是:

```
{
  "bucket": "mybucket",
  "region": "cn-hangzhou",
  "image": "src/a.png",
  "quality": 75,
  "dst": "dest",
  "get_ssim": true
}
```

其中 

- bucket: bucket 名字
- region: 参数是可选的， 不填默认为和 FC 函数相同的 region
- image: 表示图片在 bucket 上的 objectkey
- quality: 压缩质量 0-100, 默认值为 75
- dst: 保存压缩后图片的目录
- get_ssim: 可选，是否计算原图片和压缩后图片的 SSIM 值作为函数返回值
  
> SSIM 是一种全参考的图像质量评价指标，分别从亮度、对比度、结构三个方面度量图像相似性。SSIM取值范围[0, 1]，值越大，表示图像失真越小， 因为 SSIM 可以作为压缩后图像的指标。


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