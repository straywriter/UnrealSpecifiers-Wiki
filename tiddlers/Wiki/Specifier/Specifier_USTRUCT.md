# USTRUCT(标识符)

 ## UHT

| Name                                                         | 引擎模块      | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | ------------- | ------------------------------------------------------------ | -------- |
| [NoExport](#Specifier_USTRUCT_UHT_NoExport)                 | UHT           | 指定UHT不要用来自动生成注册的代码，而只是进行词法分析提取元数据。 | ★        |
| [Atomic](#Specifier_USTRUCT_UHT_Atomic)                       | UHT           | 指定该结构在序列化的时候总是一整个输出全部属性，而不是只输出改变的属性。 | ★        |
| [IsAlwaysAccessible](#Specifier_USTRUCT_UHT_IsAlwaysAccessible)      | UHT           | 指定UHT在生成文件的时候总是可以访问到改结构的声明，否则要在gen.cpp里生成镜像结构定义 | 💀        |
| [HasDefaults](#Specifier_USTRUCT_UHT_HasDefaults)                    | UHT           | 指定该结构的字段拥有默认值。这样如果本结构作为函数参数或返回值时候，函数则可以为其提供默认值。 | 💀        |
| [HasNoOpConstructor](#Specifier_USTRUCT_UHT_HasNoOpConstructor)      | UHT           | 指定该结构拥有ForceInit的构造函数，这样在作为BP function返回值的时候，可以调用来初始化 | 💀        |
| [IsCoreType](#Specifier_USTRUCT_UHT_IsCoreType)                      | UHT           | 指定该结构是核心类，UHT在用它的时候不需要前向声明。          | 💀        |


 ## Blueprint

| Name                                                         | 引擎模块      | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | ------------- | ------------------------------------------------------------ | -------- |
| [BlueprintType](#Specifier_USTRUCT_Blueprint_BlueprintType) | Blueprint     | 允许这个结构在蓝图中声明变量                                 | ★★★★★    |
| [BlueprintInternalUseOnly](#Specifier_USTRUCT_Blueprint_BlueprintInternalUseOnly) | Blueprint     | 不可定义新BP变量，但可作为别的类的成员变量暴露和变量传递     | ★★       |
| [BlueprintInternalUseOnlyHierarchical](#Specifier_USTRUCT_Blueprint_BlueprintInternalUseOnlyHierarchical) | Blueprint     | 在BlueprintInternalUseOnly的基础上，增加了子类也不能定义新BP变量的限制。 | ★        |


 ## Serialization

| Name                                                         | 引擎模块      | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | ------------- | ------------------------------------------------------------ | -------- |
| [immutable](#Specifier_USTRUCT_Serialization_immutable)              | Serialization | Immutable is only legal in Object.h and is being phased out, do not use on new structs! | 💀        |