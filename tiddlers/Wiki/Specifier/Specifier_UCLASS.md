# UCLASS(标识符)

## UHT

| Name                                                       | 引擎模块 | 功能描述                                                     | 常用程度 |
| ---------------------------------------------------------- | -------- | ------------------------------------------------------------ | -------- |
| [NoExport](#Specifier_UCLASS_UHT_NoExport)                         | UHT      | 指定UHT不要用来自动生成注册的代码，而只是进行词法分析提取元数据。 | 💀        |
| [Intrinsic](#Specifier_UCLASS_UHT_Intrinsic)                       | UHT      | 指定UHT完全不为此类生成代码，需要自己手写。                  | 💀        |
| [Interface](#Specifier_UCLASS_UHT_Interface)                       | UHT      | 标识这个Class是个Interface。                                 | 💀        |
| [UCLASS_Empty](#Specifier_UCLASS_UHT_UCLASS_Empty)                         | UHT      | 留空的默认行为是不能在蓝图中被继承，不能在蓝图中定义变量，但拥有反射的功能。 | ★★★★★    |
| [Without_UCLASS](#Specifier_UCLASS_UHT_Without_UCLASS)                 | UHT      | 只是作为一个普通的C++对象，没有反射功能。                    | ★        |
| [CustomThunkTemplates](#Specifier_UCLASS_UHT_CustomThunkTemplates) | UHT      | Specifies the struct that contains the CustomThunk implementations | 💀        |
| [CustomConstructor](#Specifier_UCLASS_UHT_CustomConstructor)       | UHT      | 阻止构造函数声明自动生成。                                   | 💀        |
| [CustomFieldNotify](#Specifier_UCLASS_UHT_CustomFieldNotify)       | UHT      | 阻止UHT为该类生成FieldNotify的相关代码。                     | 💀        |


## Blueprint

| Name                                                         | 引擎模块  | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | --------- | ------------------------------------------------------------ | -------- |
| [Blueprintable](#Specifier_UCLASS_Blueprint_Blueprintable) | Blueprint | 可以在蓝图里被继承，隐含的作用也可当变量类型                 | ★★★★★    |
| [NotBlueprintable](#Specifier_UCLASS_Blueprint_NotBlueprintable)     | Blueprint | 不可在蓝图里继承，隐含作用也不可当作变量                     | ★★★★     |
| [BlueprintType](#Specifier_UCLASS_Blueprint_BlueprintType) | Blueprint | 可当做变量类型                                               | ★★★★★    |
| [NotBlueprintType](#Specifier_UCLASS_Blueprint_NotBlueprintType)     | Blueprint | 不可当做变量类型                                             | ★★★★     |
| [Abstract](#Specifier_UCLASS_Blueprint_Abstract)            | Blueprint | 指定此类为抽象基类。可被继承，但不可生成对象。               | ★★★★★    |
| [Const](#Specifier_UPARAM_Blueprint_Const)                     | Blueprint | 表示本类的内部属性不可在蓝图中被修改，只读不可写。           | ★★★      |
| [ShowFunctions](#Specifier_UCLASS_Blueprint_ShowFunctions)           | Blueprint | 在子类的函数覆盖列表里重新打开某些函数。                     | ★★       |
| [HideFunctions](#Specifier_UCLASS_Blueprint_HideFunctions) | Blueprint | 在子类的函数覆盖列表里隐藏掉某些函数。                       | ★★       |
| [SparseClassDataType](#Specifier_UCLASS_Blueprint_SparseClassDataType) | Blueprint | 让Actor的一些重复不变的数据存放在一个共同的结构里，以达到减少内容使用量的目的 | ★★★      |
| [NeedsDeferredDependencyLoading](#Specifier_UCLASS_Blueprint_NeedsDeferredDependencyLoading) | Blueprint |                                                              | 💀        |


## DllExport

| Name                                       | 引擎模块  | 功能描述                                      | 常用程度 |
| ------------------------------------------ | --------- | --------------------------------------------- | -------- |
| [MinimalAPI](#Specifier_UINTERFACE_UHT_MinimalAPI) | DllExport | 不dll导出该类的函数，只导出类型信息当作变量。 | ★★★      |


## Category

| Name                                                         | 引擎模块         | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | ---------------- | ------------------------------------------------------------ | -------- |
| [ClassGroup](#Specifier_UCLASS_Category_ClassGroup)       | Category | 指定组件在Actor的AddComponent面板里的分组，以及在蓝图右键菜单中的分组。 | ★★★     |
| [ShowCategories](#Specifier_UCLASS_Category_ShowCategories) | Category         | 在类的ClassDefaults属性面板里显示某些Category的属性。        | ★★★     |
| [HideCategories](#Specifier_UCLASS_Category_HideCategories) | Category         | 在类的ClassDefaults属性面板里隐藏某些Category的属性。        | ★★★★    |
| [CollapseCategories](#Specifier_UCLASS_Category_CollapseCategories) | Category         | 在类的属性面板里隐藏所有带Category的属性，但是只对带有多个嵌套Category的属性才起作用。 | ★★      |
| [DontCollapseCategories](#Specifier_UCLASS_Category_DontCollapseCategories) | Category         | 使继承自基类的CollapseCatogories说明符无效。                 | ★★      |
| [AutoExpandCategories](#Specifier_UCLASS_Category_AutoExpandCategories) | Category         | 指定此类的对象在细节面板中应该自动展开的Category。           | ★       |
| [AutoCollapseCategories](#Specifier_UCLASS_Category_AutoCollapseCategories) | Category         | AutoCollapseCategories说明符使父类上的 AutoExpandCategories 说明符的列出类别的效果无效。 | ★       |
| [DontAutoCollapseCategories](#Specifier_UCLASS_Category_DontAutoCollapseCategories) | Category         | 使列出的类别的继承自父类的AutoCollapseCategories说明符无效。 | ★       |
| [PrioritizeCategories](#Specifier_UCLASS_Category_PrioritizeCategories) | Category         | 把指定的属性目录优先显示在细节面板的前面。                   | ★★★     |
| [ComponentWrapperClass](#Specifier_UCLASS_Category_ComponentWrapperClass) | Category         | 指定该类为一个简单的封装类，忽略掉子类的Category相关设置。   | ★★      |
| [AdvancedClassDisplay](#Specifier_UCLASS_Category_AdvancedClassDisplay) | Category         | 把该类下的所有属性都默认显示在高级目录下                     | ★★★★    |


## TypePicker

| Name                                                         | 引擎模块   | 功能描述             | 常用程度 |
| ------------------------------------------------------------ | ---------- | -------------------- | -------- |
| [HideDropDown](#Specifier_UCLASS_TypePicker_HideDropDown) | TypePicker | 在类选择器中隐藏此类 | ★★       |

## Development

| Name                                                         | 引擎模块    | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | ----------- | ------------------------------------------------------------ | -------- |
| [Deprecated](#Specifier_UCLASS_Development_Deprecated)    | Development | 标明该类已经弃用。                                           | ★★★      |
| [Experimental](#Specifier_UCLASS_Development_Experimental) | Development | 标明该类是试验性版本，当前没有文档描述，之后有可能废弃掉。   | ★★★      |
| [EarlyAccessPreview](#Specifier_UCLASS_Development_EarlyAccessPreview) | Development | 标明该类是早期预览版，比试验版要更完善一些，但还是没到产品级。 | ★★★      |

## Instance

| Name                                                         | 引擎模块 | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | -------- |
| [Within](#Specifier_UCLASS_Instance_Within)                          | Instance | 指定对象创建的时候必须依赖于OuterClassName的对象作为Outer。  | ★★★      |
| [DefaultToInstanced](#Specifier_UCLASS_Instance_DefaultToInstanced) | Instance | 指定该类的所有实例属性都默认是UPROPERTY(instanced)，即都默认创建新的实例，而不是对对象的引用。 | ★★★★     |
| [EditInlineNew](#Specifier_UCLASS_Instance_EditInlineNew) | Instance | 指定该类的对象可以在属性细节面板里直接内联创建，要和属性的Instanced配合。 | ★★★★★    |
| [NotEditInlineNew](#Specifier_UCLASS_Instance_NotEditInlineNew)      | Instance | 不能通过EditInline按钮创建                                   | ★        |


## Scene

| Name                                                         | 引擎模块         | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | ---------------- | ------------------------------------------------------------ | -------- |
| [NotPlaceable](#Specifier_UCLASS_Scene_NotPlaceable)    | Scene         | 标明该Actor不可被放置在关卡里                                | ★★★     |
| [Placeable](#Specifier_UCLASS_Scene_Placeable)             | Scene            | 标明该Actor可以放置在关卡里。                                | ★★★     |
| [ConversionRoot](#Specifier_UCLASS_Scene_ConversionRoot) | Scene            | 在场景编辑器里允许Actor在自身以及子类之间做转换              | ★       |

## Config

| Name                                                         | 引擎模块         | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | ---------------- | ------------------------------------------------------------ | -------- |
| [Config](#Specifier_UCLASS_Config)                            | Config           | 指定配置文件的名字，把该对象的值保存到ini配置文件中。        | ★★★★★   |
| [PerObjectConfig](#Specifier_UCLASS_Config_PerObjectConfig)          | Config           | 在已经有config配置文件名字的情况下，指定应该按每个对象实例来存储值，而不是一个类一个存储值。 | ★★★★★   |
| [ConfigDoNotCheckDefaults](#Specifier_UCLASS_Config_ConfigDoNotCheckDefaults) | Config           | 指定在保存配置值的时候忽略上一级的配置值的一致性检查。       | ★       |
| [DefaultConfig](#Specifier_UCLASS_Config_DefaultConfig) | Config           | 指定保存到的配置文件层级是Project/Config/DefaultXXX.ini。    | ★★★     |
| [GlobalUserConfig](#Specifier_UCLASS_Config_GlobalUserConfig) | Config           | 指定保存到的配置文件层级是全局用户设置 Engine/Config/UserXXX.ini。 | ★★★     |
| [ProjectUserConfig](#Specifier_UCLASS_Config_ProjectUserConfig) | Config           | 指定保存到的配置文件层级是项目用户设置 Project/Config/UserXXX.ini。 | ★★★     |
| [EditorConfig](#Specifier_UCLASS_Config_EditorConfig)   | Config   | 用来在编辑器状态下保存信息。                                 | ★       |


## Serialization

| Name                                                         | 引擎模块      | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | ------------- | ------------------------------------------------------------ | -------- |
| [Transient](#Specifier_UCLASS_Serialization_Transient)     | Serialization | 指定该类的所有对象都略过序列化。                             | ★★★      |
| [NonTransient](#Specifier_UCLASS_Serialization_NonTransient)         | Serialization | 使继承自基类的Transient说明符无效。                          | ★★★      |
| [Optional](#Specifier_UCLASS_Serialization_Optional)        | Serialization | 标记该类的对象是可选的，在Cooking的时候可以选择是否要忽略保存它们。 | ★        |
| [MatchedSerializers](#Specifier_UCLASS_Serialization_MatchedSerializers) | Serialization | 指定类支持文本结构序列化                                     | 💀        |