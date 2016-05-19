## Api response structure

这个文件定义了接口返回的模板

--------

汽车制造商相关的接口

### 1 创建汽车制造商

简述：创建汽车制造商

#### 1.1 方法 

    POST

#### 1.2 接口 Url

    /car/shows/carmaker/

#### 1.3 请求参数

|参数|类型|必填|说明|状态|
|---|:---|:---:|---:|---:|
|name|str|Yes|汽车制造商名称||
|address|str|Yes|汽车制造商地址||
|xxxx|str|No|xxxx|--已删除--|

#### 1.4 终端请求示例

    http POST http://127.0.0.1:8000/car/shows/carmaker/ name='aodi' address='china'

#### 1.5 结果返回

##### 状态：成功

> 状态码返回

    201

> 返回结果数据和类型

|参数|类型|说明|
|---|:---|---:|
|id|int|唯一标识符|
|name|str|汽车制造商名称|
|address|str|汽车制造商地址|

```json
{
    "id": 9,
    "name": "aodi",
    "address": "china"
}
```

#### 1.6 更新历史

> 更新日期按新旧排列

##### 2015-05-19 添加字段 XXXX

具体描述

##### 2015-05-15 删除字段 XXXX

具体描述
