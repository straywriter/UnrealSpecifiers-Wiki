# CallInEditor

- **功能描述：** 可以在属性细节面板上作为一个按钮来调用该函数。

- **元数据类型：** bool
- **引擎模块：** Editor
- **作用机制：** 在Meta中增加[CallInEditor](#Meta_Blueprint_CallInEditor)
- **常用程度：** ★★★★★

可以在属性细节面板上作为一个按钮来调用该函数。

该函数写在AActor或UObject子类里都是可以的，只要有对应的属性细节面板。

注意这一般是处于Editor运行环境的。典型的例子是ASkyLight的Recapture按钮。因此函数里有时会调用编辑器环境下函数。但也要注意不要在runtime下混用了，比较容易出错。

## 测试代码：

```cpp
UCLASS(Blueprintable, BlueprintType)
class INSIDER_API AMyFunction_Default :public AActor
{
public:
	GENERATED_BODY()
public:
	UFUNCTION(CallInEditor)
	void MyFunc_CallInEditor(){}
};
```

## 蓝图展示：

![Untitled](Specifier_UFUNCTION_Blueprint_CallInEditor_Untitled.png)