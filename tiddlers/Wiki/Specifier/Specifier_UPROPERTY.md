# UPROPERTY(标识符)

 ## Serialization

| Name                                                                                                     | 引擎模块                 | 功能描述                                                                                                                 | 常用程度  |
|----------------------------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------|-------|
| [Export](#Specifier_UPROPERTY_Serialization_Export)                                                       | Serialization        | 在对Asset导出的时候，决定该类的对象应该导出内部的属性值，而是对象的路径。                                                                              | ★     |
| [SaveGame](#Specifier_UPROPERTY_Serialization_SaveGame)                                                 | Serialization        | 在SaveGame存档的时候，只序列化有SaveGame标记的属性，而不序列化别的属性。                                                                         | ★★★★★ |
| [SkipSerialization](#Specifier_UPROPERTY_Serialization_SkipSerialization)                      | Serialization        | 二进制序列化时跳过该属性，但在ExportText的时候依然可以导出。                                                                                  | ★★★   |
| [TextExportTransient](#Specifier_UPROPERTY_Serialization_TextExportTransient)                                    | Serialization        | 在ExportText导出为.COPY格式的时候，忽略该属性。                                                                                      | ★     |
| [Transient](#Specifier_UPROPERTY_Serialization_Transient)                                              | Serialization        | 不序列化该属性，该属性初始化时候会被0填充。                                                                                               | ★★★★★ |
| [DuplicateTransient](#Specifier_UPROPERTY_Serialization_DuplicateTransient)                   | Serialization        | 在对象复制或COPY格式导出的时候，忽略该属性。                                                                                             | ★★    |
| [NonPIEDuplicateTransient](#Specifier_UPROPERTY_Serialization_NonPIEDuplicateTransient) | Serialization        | 在对象复制的时候，且在不是PIE的场合，忽略该属性。                                                                                           | ★     |


 ## Sequencer

| Name                                                                                                     | 引擎模块                 | 功能描述                                                                                                                 | 常用程度  |
|----------------------------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------|-------|
| [Interp](#Specifier_UPROPERTY_DetaisPanel_Interp)                                                         | Sequencer            | 指定该属性值可暴露到时间轴里编辑，在平常的Timeline或UMG的动画里使用。                                                                             | ★★★   |


 ## Network

| Name                                                                                                     | 引擎模块                 | 功能描述                                                                                                                 | 常用程度  |
|----------------------------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------|-------|
| [Replicated](#Specifier_UPROPERTY_Network_Replicated)                                                            | Network              | 指定该属性应随网络进行复制。                                                                                                       | ★★★★★ |
| [ReplicatedUsing](#Specifier_UPROPERTY_Network_ReplicatedUsing)                                  | Network              | 指定一个通知回调函数，在属性通过网络更新后执行。                                                                                             | ★★★★★ |
| [NotReplicated](#Specifier_UPROPERTY_Network_NotReplicated)                                                      | Network              | 跳过复制。这只会应用到服务请求函数中的结构体成员和参数。                                                                                         | ★★★   |
| [RepRetry](#Specifier_UPROPERTY_Network_RepRetry)                                                                | Network              | 只适用于结构体属性。如果此属性未能完全发送（举例而言：Object引用尚无法通过网络进行序列化），则重新尝试对其的复制。对简单引用而言，这是默认选择；但对结构体而言，这会产生带宽开销，并非优选项。因此在指定此标签之前其均为禁用状态。 | 💀    |


 ## UHT

| Name                                                                                                     | 引擎模块                 | 功能描述                                                                                                                 | 常用程度  |
|----------------------------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------|-------|
| [FieldNotify](#Specifier_UPROPERTY_UHT_FieldNotify)                                                  | MVVM, UHT            | 在打开MVVM插件后，使得该属性变成支持FieldNotify的属性。                                                                                  | ★★★★  |


 ## Instance

| Name                                                                                                     | 引擎模块                 | 功能描述                                                                                                                 | 常用程度  |
|----------------------------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------|-------|
| [Instanced](#Specifier_UPROPERTY_Instance_Instanced)                                                   | Instance             | 指定对该对象属性的编辑赋值应该新创建一个实例并作为子对象，而不是寻找一个对象引用。                                                                            | ★★★   |


 ## Editor

| Name                                                                                                     | 引擎模块                 | 功能描述                                                                                                                 | 常用程度  |
|----------------------------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------|-------|
| [NonTransactional](#Specifier_UPROPERTY_DetaisPanel_NonTransactional)                           | Editor               | 对该属性的改变操作，不会被包含进编辑器的Undo/Redo命令中。                                                                                    | ★★    |


 ## DetailsPanel

| Name                                                                                                     | 引擎模块                 | 功能描述                                                                                                                 | 常用程度  |
|----------------------------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------|-------|
| [Category](#Specifier_UPROPERTY_DetaisPanel_Category)                                                   | DetailsPanel, Editor | 指定属性的类别，使用 &#124; 运算符定义嵌套类目。                                                                                         | ★★★★★ |
| [SimpleDisplay](#Specifier_UPROPERTY_DetaisPanel_SimpleDisplay)                                    | DetailsPanel, Editor | 在细节面板中直接可见，不折叠到高级中。                                                                                                  | ★★★   |
| [AdvancedDisplay](#Specifier_UPROPERTY_DetaisPanel_AdvancedDisplay)                              | DetailsPanel, Editor | 被折叠到高级栏下，要手动打开。一般用在不太常用的属性上面。                                                                                        | ★★★★★ |
| [EditAnywhere](#Specifier_UPROPERTY_DetaisPanel_EditAnywhere)                                       | DetailsPanel, Editor | 在默认值和实例的细节面板上均可编辑                                                                                                    | ★★★★★ |
| [EditDefaultsOnly](#Specifier_UPROPERTY_DetaisPanel_EditDefaultsOnly)                                            | DetailsPanel, Editor | 只能在默认值面板里编辑                                                                                                          | ★★★★★ |
| [EditInstanceOnly](#Specifier_UPROPERTY_DetaisPanel_EditInstanceOnly)                                            | DetailsPanel, Editor | 只能在实例的细节面板上编辑该属性                                                                                                     | ★★★★★ |
| [VisibleAnywhere](#Specifier_UPROPERTY_DetaisPanel_VisibleAnywhere)                                              | DetailsPanel, Editor | 在默认值和实例细节面板均可见，但不可编辑                                                                                                 | ★★★★★ |
| [VisibleDefaultsOnly](#Specifier_UPROPERTY_DetaisPanel_VisibleDefaultsOnly)                                      | DetailsPanel, Editor | 在默认值细节面板可见，但不可编辑                                                                                                     | ★★★★★ |
| [VisibleInstanceOnly](#Specifier_UPROPERTY_DetaisPanel_VisibleInstanceOnly)                                      | DetailsPanel, Editor | 在实例细节面板可见，但不可编辑                                                                                                      | ★★★★★ |
| [EditFixedSize](#Specifier_UPROPERTY_DetaisPanel_EditFixedSize)                                    | DetailsPanel, Editor | 在细节面板上不允许改变该容器的元素个数。                                                                                                 | ★★★   |
| [NoClear](#Specifier_UPROPERTY_DetaisPanel_NoClear)                                                      | DetailsPanel, Editor | 指定该属性的编辑选项中不出现Clear按钮，不允许置null。                                                                                      | ★★★   |


 ## Config

| Name                                                                                                     | 引擎模块                 | 功能描述                                                                                                                 | 常用程度  |
|----------------------------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------|-------|
| [Config](#Specifier_UPROPERTY_Config)                                                                     | Config               | 指定该属性是一个配置属性，该属性可以被序列化读写到ini文件（路径由uclass的config标签指定）中。                                                               | ★★★   |
| [GlobalConfig](#Specifier_UPROPERTY_Config_GlobalConfig)                                            | Config               | 和Config一样指定该属性可作为配置读取和写入ini中，但只会读取写入到配置文件里基类的值，而不会使用配置文件里子类里的值。                                                      | ★★★   |


 ## Blueprint

| Name                                                                                                     | 引擎模块                 | 功能描述                                                                                                                 | 常用程度  |
|----------------------------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------|-------|
| [BlueprintAuthorityOnly](#Specifier_UPROPERTY_Blueprint_BlueprintAuthorityOnly)           | Blueprint, Network   | 只能绑定为BlueprintAuthorityOnly的事件，让该多播委托只接受在服务端运行的事件                                                                    | ★★★   |
| [BlueprintReadWrite](#Specifier_UPROPERTY_Blueprint_BlueprintReadWrite)                       | Blueprint            | 可从蓝图读取或写入此属性。                                                                                                        | ★★★★★ |
| [BlueprintReadOnly](#Specifier_UPROPERTY_Blueprint_BlueprintReadOnly)                          | Blueprint            | 此属性可由蓝图读取，但不能被修改。                                                                                                    | ★★★★★ |
| [BlueprintGetter](#Specifier_UPROPERTY_Blueprint_BlueprintGetter)                                | Blueprint            | 为属性定义一个自定义的Get函数来读取。                                                                                                 | ★★★   |
| [Getter](#Specifier_UPROPERTY_Blueprint_Getter)                                                                  | Blueprint            | 为属性增加一个C++的Get函数，只在C++层面应用。                                                                                          | ★★★   |
| [Setter](#Specifier_UPROPERTY_Blueprint_Setter)                                                           | Blueprint            | 为属性增加一个C++的Set函数，只在C++层面应用。                                                                                          | ★★★   |
| [BlueprintSetter](#Specifier_UPROPERTY_Blueprint_BlueprintSetter)                                                | Blueprint            | 采用一个自定义的set函数来读取。                                                                                                    | ★★★   |
| [BlueprintCallable](#Specifier_UPROPERTY_Blueprint_BlueprintCallable)                          | Blueprint            | 在蓝图中可以调用这个多播委托                                                                                                       | ★★★   |
| [BlueprintAssignable](#Specifier_UPROPERTY_Blueprint_BlueprintAssignable)                    | Blueprint            | 在蓝图中可以为这个多播委托绑定事件                                                                                                    | ★★★   |


 ## Behavior

| Name                                                                                                     | 引擎模块                 | 功能描述                                                                                                                 | 常用程度  |
|----------------------------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------|-------|
| [Localized](#Specifier_UPROPERTY_Asset_Localized)                                                                | Behavior             | 此属性的值将拥有一个定义的本地化值。多用于字符串。暗示为 ReadOnly。该值有一个本地化值。最常标记在string上                                                         | 💀    |
| [Native](#Specifier_UPROPERTY_UHT_Native)                                                                        | Behavior             | 属性为本地：C++代码负责对其进行序列化并公开到垃圾回收 。                                                                                       | 💀    |


 ## Asset

| Name                                                                                                     | 引擎模块                 | 功能描述                                                                                                                 | 常用程度  |
|----------------------------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------|-------|
| [AssetRegistrySearchable](#Specifier_UPROPERTY_Asset_AssetRegistrySearchable)            | Asset                | 标记该属性可以作为AssetRegistry的Tag和Value值来进行资产的过滤搜索                                                                          | ★★★   |