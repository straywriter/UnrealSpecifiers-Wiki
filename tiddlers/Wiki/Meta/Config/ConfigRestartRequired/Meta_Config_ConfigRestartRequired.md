﻿# ConfigRestartRequired

- **功能描述：** 使属性在设置里改变后弹出重启编辑器的对话框。
- **使用位置：** UPROPERTY
- **引擎模块：** Config
- **元数据类型：** bool
- **常用程度：** ★★★

使属性在设置里改变后弹出重启编辑器的对话框。

自然的，一般是用于真的需要重启编辑器的设置。

## 测试代码：

```cpp
public:
	UPROPERTY(Config, EditAnywhere, BlueprintReadWrite, Category = ConfigRestartRequired, meta = (ConfigRestartRequired="true"))
	FString MyString_ConfigRestartRequired;
```

## 测试效果：

![Untitled](Meta_Config_ConfigRestartRequired_Untitled.png)

## 原理：

在SSettingsEditor生效，可见得是在UI窗口发生改变。然后弹出对话框。

```cpp
void SSettingsEditor::NotifyPostChange( const FPropertyChangedEvent& PropertyChangedEvent, class FEditPropertyChain* PropertyThatChanged )
{
		static const FName ConfigRestartRequiredKey = "ConfigRestartRequired";
		if (PropertyChangedEvent.Property->GetBoolMetaData(ConfigRestartRequiredKey) || PropertyChangedEvent.MemberProperty->GetBoolMetaData(ConfigRestartRequiredKey))
		{
						OnApplicationRestartRequiredDelegate.ExecuteIfBound();
		}
}
```