﻿# DeprecatedProperty

- **功能描述：** 标记弃用，引用到该属性的蓝图会触发一个警告

- **使用位置：** UPROPERTY

- **引擎模块：** Development

- **元数据类型：** bool

- **关联项：**

  UCLASS：[Deprecated](#Specifier_UCLASS_Development_Deprecated)

- **常用程度：** ★

标记弃用，引用到该属性的蓝图会触发一个警告

## 示例代码：

```cpp
// Simple
UPROPERTY(BlueprintReadWrite, meta=(DeprecatedProperty, DeprecationMessage="This is deprecated"))
FString PlantName;

// Better
UPROPERTY(BlueprintReadWrite, meta=(DisplayName="PlantName", DeprecatedProperty, DeprecationMessage="PlantName is deprecated, instead use PlantDisplayName."))
FString DEPRECATED_PlantName;
```

![Untitled](Meta_Development_DeprecatedProperty_Untitled.png)

![Untitled%201](Meta_Development_DeprecatedProperty_Untitled_1.png)