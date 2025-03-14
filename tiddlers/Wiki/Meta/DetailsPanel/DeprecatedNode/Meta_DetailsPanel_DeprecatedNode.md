﻿# DeprecatedNode

- **功能描述：** 用于BehaviorTreeNode或EnvQueryNode，说明该类已废弃，在编辑器中红色错误展示并有错误ToolTip提示
- **使用位置：** UCLASS
- **引擎模块：** DetailsPanel
- **元数据类型：** bool
- **限制类型：** BehaviorTreeNode，EnvQueryNode
- **常用程度：** ★★

在AI行为树或EQS的节点上设置，标记该节点已经弃用。

## 源码中的例子：

```cpp
UCLASS(meta = (DeprecatedNode, DeprecationMessage = "Please use IsAtLocation decorator instead."), MinimalAPI)
class UBTDecorator_ReachedMoveGoal : public UBTDecorator
{
	GENERATED_UCLASS_BODY()
};

UCLASS(MinimalAPI, meta=(DeprecatedNode, DeprecationMessage = "This class is now deprecated, please use RunMode supporting random results instead."))
class UEnvQueryTest_Random : public UEnvQueryTest
{
	GENERATED_UCLASS_BODY()
};
```

## C++测试代码：

```cpp
UCLASS(meta = (DeprecatedNode, DeprecationMessage = "This BT node is deprecated. Don't use this anymore."), MinimalAPI)
class UBTTask_MyDeprecatedNode : public UBTTaskNode
{
	GENERATED_UCLASS_BODY()
};
```

行为树里的结果，如果加上DeprecatedNode，就会红色显示，并提示错误信息。

![Untitled](Meta_DetailsPanel_DeprecatedNode_Untitled.png)

## 源码里测试的代码：

```cpp
FString FGraphNodeClassHelper::GetDeprecationMessage(const UClass* Class)
{
	static FName MetaDeprecated = TEXT("DeprecatedNode");
	static FName MetaDeprecatedMessage = TEXT("DeprecationMessage");
	FString DefDeprecatedMessage("Please remove it!");
	FString DeprecatedPrefix("DEPRECATED");
	FString DeprecatedMessage;

	if (Class && Class->HasAnyClassFlags(CLASS_Native) && Class->HasMetaData(MetaDeprecated))
	{
		DeprecatedMessage = DeprecatedPrefix + TEXT(": ");
		DeprecatedMessage += Class->HasMetaData(MetaDeprecatedMessage) ? Class->GetMetaData(MetaDeprecatedMessage) : DefDeprecatedMessage;
	}

	return DeprecatedMessage;
}
```