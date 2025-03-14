﻿# DetailsOnly

- **功能描述：** 指定FRigUnit下的该属性只在细节面板中显示。
- **使用位置：** UPROPERTY
- **引擎模块：** RigVMStruct
- **元数据类型：** bool
- **限制类型：** FRigUnit下的属性
- **关联项：** [Input](#Meta_RigVM_Input)
- **常用程度：** ★★★

指定FRigUnit下的该属性只在细节面板中显示。

## 测试代码：

```cpp
	UPROPERTY(meta = (Input, DetailsOnly))
	float MyFloat_DetailsOnly = 456.f;
```

## 测试效果：

![Untitled](Meta_RigVM_DetailsOnly_Untitled.png)

## 原理：

根据DetailsOnly判断返回是否ShowInDetailsPanelOnly。

```cpp
bool URigVMPin::ShowInDetailsPanelOnly() const
{
#if WITH_EDITOR
	if (GetParentPin() == nullptr)
	{
		if (URigVMUnitNode* UnitNode = Cast<URigVMUnitNode>(GetNode()))
		{
			if (UScriptStruct* ScriptStruct = UnitNode->GetScriptStruct())
			{
				if (FProperty* Property = ScriptStruct->FindPropertyByName(GetFName()))
				{
					if (Property->HasMetaData(FRigVMStruct::DetailsOnlyMetaName))
					{
						return true;
					}
				}
			}
		}
		else if(const URigVMTemplateNode* TemplateNode = Cast<URigVMTemplateNode>(GetNode()))
		{
			if(const FRigVMTemplate* Template = TemplateNode->GetTemplate())
			{
				return !Template->GetArgumentMetaData(GetFName(), FRigVMStruct::DetailsOnlyMetaName).IsEmpty();
			}
		}
	}
#endif
	return false;
}
```