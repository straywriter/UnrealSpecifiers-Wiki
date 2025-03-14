# UCLASS()

- **功能描述：** 留空的默认行为是不能在蓝图中被继承，不能在蓝图中定义变量，但拥有反射的功能。

- **引擎模块：** UHT
- **元数据类型：** bool
- **作用机制：** 在ClassFlags中增加[CLASS_MatchedSerializers](#Flags_EClassFlags_CLASS_MatchedSerializers), [CLASS_Native](#Flags_EClassFlags_CLASS_Native), [CLASS_RequiredAPI](#Flags_EClassFlags_CLASS_RequiredAPI), [CLASS_TokenStreamAssembled](#Flags_EClassFlags_CLASS_TokenStreamAssembled), [CLASS_Intrinsic](#Flags_EClassFlags_CLASS_Intrinsic), [CLASS_Constructed](#Flags_EClassFlags_CLASS_Constructed)
- **关联项：** [Without_UCLASS](#Specifier_UCLASS_UHT_Without_UCLASS)
- **常用程度：★★★★★**

不能在蓝图中被继承，不能在蓝图中定义变量。

但依然都可以通过蓝图ConstructObject创建出来。对于想要拥有反射功能，但是并不想在蓝图中被使用会挺适合。

## 示例代码：

```cpp
/*
[MyClass_Default	Class->Struct->Field->Object	/Script/Insider.MyClass_Default] [IncludePath = Class/MyClass_Default.h, ModuleRelativePath = Class/MyClass_Default.h]
ObjectFlags:	RF_Public | RF_Standalone | RF_Transient
Outer:	Package /Script/Insider
ClassFlags:	CLASS_MatchedSerializers | CLASS_Native | CLASS_RequiredAPI | CLASS_TokenStreamAssembled | CLASS_Intrinsic | CLASS_Constructed
Size:	48
{
public: void ExecuteUbergraph(int32 EntryPoint);
};
*/

UCLASS()
class INSIDER_API UMyClass_Default :public UObject
{
	GENERATED_BODY()
public:
};
```

默认的拥有这些标志：CLASS_MatchedSerializers | CLASS_Native | CLASS_RequiredAPI | CLASS_TokenStreamAssembled | CLASS_Intrinsic | CLASS_Constructed