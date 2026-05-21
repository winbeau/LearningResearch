# Zhihu 抓取失败说明

抓取时间：2026-05-21

## 失败原因

通过 Playwright 直接访问以下 4 个 Zhihu URL 时，Zhihu 反爬系统返回错误码
`40362`（"您当前请求存在异常，暂时限制本次访问"），页面 body 只剩纯 JSON 错误
信息，DOM 中没有任何文章正文。

测试样本：
- https://www.zhihu.com/question/524855881/answer/2819447733 → 40362
- https://zhuanlan.zhihu.com/p/111707433 → 40362

两个不同形式（问答页 / 专栏页）都被同一机制拦截，可以确定**未登录的
headless 浏览器无法稳定抓取 Zhihu 内容**。

## 处理方式

本轮放弃抓取 Zhihu 内容，4 个 URL 保留为外部引用（写入 references/ 或对应
内容文件中作"扩展阅读"链接）。

## 完整 URL 清单

来源：从 18 个 Notion 页里聚合（去重后）

- https://www.zhihu.com/question/524855881/answer/2819447733
  来源 Notion 页：1d13fe29-面试反思科研品质
- https://zhuanlan.zhihu.com/p/111707433
  来源 Notion 页：da6ce171-培养想idea能力
- https://zhuanlan.zhihu.com/p/560852116
  来源 Notion 页：da6ce171-培养想idea能力
- https://zhuanlan.zhihu.com/p/1893638374646079902
  来源 Notion 页：59569d7b-设备配置
