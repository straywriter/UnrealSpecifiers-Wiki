# Meta = (元数据)

## Actor

| Name                                                                                                                           | 引擎模块                 | 功能描述                                                                                                                                                                                                                                                             | 常用程度  |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| [ChildCanTick](#Meta_Actor_ChildCanTick)                                                                             | Actor                | 标记允许其蓝图子类可以接受响应Tick事件                                                                                                                                                                                                                                            | ★★★   |
| [ChildCannotTick](#Meta_Actor_ChildCannotTick)                  | Actor | 用于Actor或ActorComponent子类，标记允许其蓝图子类不可以接受响应Tick事件，哪怕父类可以Tick | ★★★      |


## AnimationGraph

| Name                                                         | 引擎模块       | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | -------------- | ------------------------------------------------------------ | -------- |
| [AnimNotifyBoneName](#Meta_AnimationGraph_AnimNotifyBoneName) | AnimationGraph | 使得UAnimNotify或UAnimNotifyState下的FName属性作为BoneName的作用。 | ★★       |
| [AnimBlueprintFunction](#Meta_AnimationGraph_AnimBlueprintFunction) | AnimationGraph | 标明是动画蓝图里的内部纯存根函数，只在动画蓝图编译时设置     | 💀        |
| [CustomizeProperty](#Meta_AnimationGraph_CustomizeProperty) | AnimationGraph | 使用在FAnimNode的成员属性上，告诉编辑器不要为它生成默认Details面板控件，后续会在DetailsCustomization里自定义创建相应的编辑控件。 | ★        |
| [AnimNotifyExpand](#Meta_AnimationGraph_AnimNotifyExpand)       | AnimationGraph | 使得UAnimNotify或UAnimNotifyState下的属性直接展开到细节面板里。 | 💀        |
| [OnEvaluate](#Meta_AnimationGraph_OnEvaluate)                   | AnimationGraph |                                                              | 💀        |
| [FoldProperty](#Meta_AnimationGraph_FoldProperty)  | AnimationGraph | 在动画蓝图中使得动画节点的某个属性成为FoldProperty。         | ★        |
| [BlueprintCompilerGeneratedDefaults](#Meta_AnimationGraph_BlueprintCompilerGeneratedDefaults) | AnimationGraph | 指定该属性的值是编译器生成的，因此在编译后无需复制，可以加速一些编译性能。 | 💀        |
| [CustomWidget](#Meta_AnimationGraph_CustomWidget)               | AnimationGraph |                                                              | 💀        |
| [AllowedParamType](#Meta_AnimationGraph_AllowedParamType)       | AnimationGraph |                                                              | 💀        |
| [PinShownByDefault](#Meta_AnimationGraph_PinShownByDefault) | AnimationGraph | 在动画蓝图中使得动画节点的某个属性一开始就暴露出来成为引脚，但也可以改变。 | ★★★      |
| [AnimGetter](#Meta_AnimationGraph_AnimGetter)        | AnimationGraph | 指定UAnimInstance及子类的该函数成为一个AnimGetter函数。      | ★★★      |
| [GetterContext](#Meta_AnimationGraph_GetterContext) | AnimationGraph | 继续限定AnimGetter函数在哪个地方才可以使用，如果不填，则默认都可以用。 | ★★       |


## Asset

| Name                                                         | 引擎模块 | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | -------- |
| [RequiredAssetDataTags](#Meta_Asset_RequiredAssetDataTags) | Asset    | 在UObject*属性上指定Tags来进行过滤，必须拥有该Tags才可以被选择。 | ★★       |
| [DisallowedAssetDataTags](#Meta_Asset_DisallowedAssetDataTags)  | Asset    | 在UObject*属性上指定Tags来进行过滤，必须没有拥有该Tags才可以被选择。 | ★★       |
| [ForceShowEngineContent](#Meta_Asset_ForceShowEngineContent) | Asset    | 指定UObject*属性的资源可选列表里强制可选引擎的内建资源       | ★★       |
| [ForceShowPluginContent](#Meta_Asset_ForceShowEngineContent_ForceShowPluginContent) | Asset    | 指定UObject*属性的资源可选列表里强制可选其他插件里的内建资源 | 💀        |
| [GetAssetFilter](#Meta_Asset_GetAssetFilter)     | Asset    | 指定一个UFUNCTION来对UObject*属性的可选资源进行排除过滤。    | ★★★      |


## Blueprint

| Name                                                         | 引擎模块  | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | --------- | ------------------------------------------------------------ | -------- |
| [IgnoreTypePromotion](#Meta_Blueprint_IgnoreTypePromotion) | Blueprint | 标记该函数不收录进类型提升函数库                             | ★★       |
| [Variadic](#Meta_Blueprint_Variadic)                            | Blueprint | 指定该函数接受多个参数                                       | ★★★      |
| [ForceAsFunction](#Meta_Blueprint_ForceAsFunction) | Blueprint | 把C++里用BlueprintImplementableEvent或NativeEvent定义的事件强制改为函数在子类中覆写。 | ★★★      |
| [CannotImplementInterfaceInBlueprint](#Meta_Blueprint_CannotImplementInterfaceInBlueprint) | Blueprint | 指定该接口不能在蓝图中实现                                   | ★★★      |
| [CallInEditor](#Meta_Blueprint_CallInEditor)                    | Blueprint | 可以在Actor的细节面板上作为一个按钮来调用该函数。            | ★★★★★    |
| [BlueprintProtected](#Meta_Blueprint_BlueprintProtected) | Blueprint | 指定该函数或属性只能在本类以及子类中被调用或读写，类似C++中的protected作用域限制。不可在别的蓝图类里访问。 | ★★★      |
| [AllowPrivateAccess](#Meta_Blueprint_AllowPrivateAccess) | Blueprint | 允许一个在C++中private的属性，可以在蓝图中访问。             | ★★★★★    |
| [BlueprintPrivate](#Meta_Blueprint_BlueprintPrivate) | Blueprint | 指定该函数或属性只能在本类中被调用或读写，类似C++中的private的作用域限制。不可在别的蓝图类里访问。 | ★★       |
| [CommutativeAssociativeBinaryOperator](#Meta_Blueprint_CommutativeAssociativeBinaryOperator) | Blueprint | 标记一个二元运算函数的运算支持交换律和结合律，在蓝图节点上增加一个“+”引脚，允许动态的直接添加多个输入值。 | ★★★★     |
| [CompactNodeTitle](#Meta_Blueprint_CompactNodeTitle) | Blueprint | 使得函数的展示形式变成精简压缩模式，同时指定一个新的精简的名字 | ★★★      |
| [CustomStructureParam](#Meta_Blueprint_Param_CustomStructureParam) | Blueprint | 被CustomStructureParam标记的函数参数会变成Wildcard的通配符参数，其引脚的类型会等于连接的变量类型。 | ★★★★★    |
| [DefaultToSelf](#Meta_Blueprint_DefaultToSelf)    | Blueprint | 用在函数上，指定一个参数的默认值为Self值                     | ★★★★★    |
| [ExpandEnumAsExecs](#Meta_Blueprint_Exec_ExpandEnumAsExecs) | Blueprint | 指定多个enum或bool类型的函数参数，自动根据条目生成相应的多个输入或输出执行引脚，并根据实参值不同来相应改变控制流。 | ★★★★★    |
| [ExpandBoolAsExecs](#Meta_Blueprint_Exec_ExpandBoolAsExecs)     | Blueprint | 是ExpandEnumAsExecs的别名，完全等价其功能。                  | ★★★★★    |
| [ArrayParm](#Meta_Blueprint_Param_ArrayParm)          | Blueprint | 指定一个函数为使用Array<*>的函数，数组元素类型为通配符的泛型。 | ★★★      |
| [ArrayTypeDependentParams](#Meta_Blueprint_Param_ArrayTypeDependentParams) | Blueprint | 当ArryParam指定的函数拥有两个或以上Array参数的时候，指定哪些数组参数的类型也应该相应的被更新改变。 | 💀        |
| [AdvancedDisplay](#Meta_Blueprint_AdvancedDisplay) | Blueprint | 把函数的一些参数折叠起来不显示，需要手动点开下拉箭头来展开编辑。 | ★★★★★    |
| [SetParam](#Meta_Blueprint_SetParam)                   | Blueprint | 指定一个函数为使用Set<TItem>的函数，元素类型为通配符的泛型。 | ★★★      |
| [MapParam](#Meta_Blueprint_Param_MapParam)             | Blueprint | 指定一个函数为使用TMap<TKey,TValue>的函数，元素类型为通配符的泛型。 | ★★★      |
| [MapKeyParam](#Meta_Blueprint_Param_MapParam_MapKeyParam)       | Blueprint | 指定一个函数参数为Map的Key，其根据MapParam指定的实际Map参数的Key类型而相应改变。 | ★★★      |
| [MapValueParam](#Meta_Blueprint_Param_MapParam_MapValueParam)   | Blueprint | 指定一个函数参数为Map的Value，其根据MapParam指定的实际Map参数的Value类型而相应改变。 | ★★★      |
| [InternalUseParam](#Meta_Pin_InternalUseParam) | Blueprint | 用在函数调用上，指定要隐藏的参数名称，也可以隐藏返回值。可以隐藏多个 | ★★★★★    |
| [Keywords](#Meta_Blueprint_Keywords)                   | Blueprint | 指定一系列关键字用于在蓝图内右键找到该函数                   | ★★★★★    |
| [Latent](#Meta_Blueprint_Latent)                         | Blueprint | 标明一个函数是一个延迟异步操作                               | ★★★★★    |
| [NeedsLatentFixup](#Meta_Blueprint_Latent_NeedsLatentFixup)     | Blueprint | 用在FLatentActionInfo::Linkage属性上，告诉蓝图VM生成跳转信息 | ★        |
| [LatentInfo](#Meta_Blueprint_Latent_LatentInfo)                 | Blueprint | 和Latent配合，指明哪个函数参数是LatentInfo参数。             | ★★★      |
| [LatentCallbackTarget](#Meta_Blueprint_Latent_LatentCallbackTarget) | Blueprint | 用在FLatentActionInfo::CallbackTarget属性上，告诉蓝图VM在哪个对象上调用函数。 | ★        |
| [NativeMakeFunc](#Meta_Blueprint_NativeMakeFunc) | Blueprint | 指定一个函数采用MakeStruct的图标                             | ★        |
| [NativeBreakFunc](#Meta_Blueprint_NativeBreakFunc)              | Blueprint | 指定一个函数采用BreakStruct的图标。                          | ★        |
| [UnsafeDuringActorConstruction](#Meta_Blueprint_UnsafeDuringActorConstruction) | Blueprint | 标明该函数不能在Actor的构造函数里调用                        | ★★       |
| [BlueprintAutocast](#Meta_Blueprint_BlueprintAutocast) | Blueprint | 告诉蓝图系统这个函数是用来支持从A类型到B类型的自动转换。     | ★        |
| [DeterminesOutputType](#Meta_Blueprint_Param_DeterminesOutputType) | Blueprint | 指定一个参数的类型作为函数动态调整输出参数类型的参考类型     | ★★★      |
| [DynamicOutputParam](#Meta_Blueprint_Param_DynamicOutputParam)  | Blueprint | 配合DeterminesOutputType，指定多个支持动态类型的输出参数。   | 💀        |
| [ReturnDisplayName](#Meta_Blueprint_ReturnDisplayName) | Blueprint | 改变函数返回值的名字，默认是ReturnValue                      | ★★★★★    |
| [WorldContext](#Meta_Blueprint_WorldContext)       | Blueprint | 指定函数的一个参数自动接收WorldContext对象，以便确定当前运行所处于的World | ★★★★★    |
| [ShowWorldContextPin](#Meta_Blueprint_ShowWorldContextPin) | Blueprint | 放在UCLASS上，指定本类里的函数调用都必须显示WorldContext引脚，无论其本来是否默认隐藏 | 💀        |
| [CallableWithoutWorldContext](#Meta_Blueprint_CallableWithoutWorldContext) | Blueprint | 让函数也可以脱离WorldContextObject而使用                     | 💀        |
| [AutoCreateRefTerm](#Meta_Blueprint_Param_AutoCreateRefTerm) | Blueprint | 指定函数的多个输入引用参数在没有连接的时候自动为其创建默认值 | ★★★★★    |
| [ProhibitedInterfaces](#Meta_Blueprint_ProhibitedInterfaces) | Blueprint | 列出与蓝图类不兼容的接口，阻止实现                           | ★★       |
| [HiddenNode](#Meta_Blueprint_HiddenNode)             | Blueprint | 把指定的UBTNode隐藏不在右键菜单中显示。                      | ★        |
| [HideFunctions](#Meta_Blueprint_HideFunctions)                  | Blueprint | 在属性查看器中不显示指定类别中的所有函数。                   | ★★★      |
| [ExposedAsyncProxy](#Meta_Blueprint_ExposedAsyncProxy) | Blueprint | 在 Async Task 节点中公开此类的一个代理对象。                 | ★★★      |
| [HasDedicatedAsyncNode](#Meta_Blueprint_HasDedicatedAsyncNode) | Blueprint |                                                              | 💀        |
| [HideThen](#Meta_Blueprint_HideThen)                   | Blueprint | 隐藏异步蓝图节点的Then引脚                                   | 💀        |
| [HideSpawnParms](#Meta_Blueprint_Param_HideSpawnParms) | Blueprint | 在UGamelayTask子类生成的蓝图异步节点上隐藏UGamelayTask子类继承链中某些属性。 | 💀        |
| [NotInputConfigurable](#Meta_Blueprint_NotInputConfigurable) | Blueprint | 让一些UInputModifier和UInputTrigger不能在ProjectSettings里配置。 | ★        |
| [BlueprintThreadSafe](#Meta_Blueprint_BlueprintThreadSafe) | Blueprint | 用在类上或函数上，标记类里的函数都是线程安全的。 这样就可以在动画蓝图等非游戏线程被调用了。 | ★★★      |
| [NotBlueprintThreadSafe](#Meta_Blueprint_NotBlueprintThreadSafe) | Blueprint | 用在函数上，标记这个函数是不线程安全的                       | ★        |
| [RestrictedToClasses](#Meta_Blueprint_RestrictedToClasses) | Blueprint | 限制蓝图函数库下的函数只能在RestrictedToClasses指定的类蓝图中右键创建出来 | ★★★      |
| [DontUseGenericSpawnObject](#Meta_Blueprint_DontUseGenericSpawnObject) | Blueprint | 阻止使用蓝图中的Generic Create Object节点来生成本类的对象。  | ★★       |
| [ObjectSetType](#Meta_Blueprint_ObjectSetType)    | Blueprint | 指定统计页面的对象集合类型。                                 | ★        |
| [SparseClassDataTypes](#Meta_Blueprint_SparseClassDataTypes)    | Blueprint |                                                              | ★★★      |
| [KismetHideOverrides](#Meta_Blueprint_KismetHideOverrides) | Blueprint | 不允许被覆盖的蓝图事件的列表。                               | 💀        |
| [BlueprintType](#Meta_Blueprint_BlueprintType)                  | Blueprint | 表明可以作为一个蓝图变量                                     | ★★★★★    |
| [IsConversionRoot](#Meta_Blueprint_IsConversionRoot)            | Blueprint | 允许Actor在自身以及子类之间做转换                            | ★★★      |
| [BlueprintInternalUseOnlyHierarchical](#Meta_Blueprint_BlueprintInternalUseOnlyHierarchical) | Blueprint | 标明该结构及其子类都不暴露给用户定义和使用，均只能在蓝图系统内部使用 | ★        |
| [BlueprintSetter](#Meta_Blueprint_BlueprintSetter)              | Blueprint | 采用一个自定义的set函数来读取。 会默认设置BlueprintReadWrite. | ★★★      |
| [DisplayName](#Meta_Blueprint_DisplayName)                      | Blueprint | 此节点在蓝图中的命名将被此处提供的值所取代，而非代码生成的命名。 | ★★★★★    |
| [ExposeOnSpawn](#Meta_Blueprint_ExposeOnSpawn)    | Blueprint | 使该属性在ContructObject或SpawnActor等创建对象的时候暴露出来。 | ★★★★★    |
| [NativeConst](#Meta_Blueprint_NativeConst)                      | Blueprint | 指定有C++里的const标志                                       | ★        |
| [CPP_Default_XXX](#Meta_Blueprint_CPP_Default_XXX)              | Blueprint | XXX=参数名字                                                 | ★★★★★    |
| [BlueprintGetter](#Meta_Blueprint_BlueprintGetter)              | Blueprint | 采用一个自定义的get函数来读取。 如果没有设置BlueprintSetter或BlueprintReadWrite, 则会默认设置BlueprintReadOnly. | ★★★      |
| [IsBlueprintBase](#Meta_Blueprint_IsBlueprintBase)              | Blueprint | 说明此类是否为创建蓝图的一个可接受基类，与 UCLASS 说明符、Blueprintable 或 'NotBlueprintable` 相似。 | ★★★★★    |
| [BlueprintInternalUseOnly](#Meta_Blueprint_BlueprintInternalUseOnly) | Blueprint | 标明该元素是作为蓝图系统的内部调用或使用，不暴露出来在用户层面直接定义或使用。 | ★★★      |


## Component

| Name                                                         | 引擎模块  | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | --------- | ------------------------------------------------------------ | -------- |
| [UseComponentPicker](#Meta_Component_UseComponentPicker) | Component | 用在ComponentReference属性上，使得选取器的列表里展示出Actor属下的Component以便选择。 | ★★       |
| [AllowAnyActor](#Meta_Component_AllowAnyActor)                  | Component | 用在ComponentReference属性上，在UseComponentPicker的情况下使得组件选取器扩大到场景里其他Actor下的其他组件。 | ★★       |
| [BlueprintSpawnableComponent](#Meta_Component_BlueprintSpawnableComponent) | Component | 允许该组件出现在Actor蓝图里Add组件的面板里。                 | ★★★★     |


## Config

| Name                                                                                                                           | 引擎模块                 | 功能描述                                                                                                                                                                                                                                                             | 常用程度  |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| [ConsoleVariable](#Meta_Config_ConsoleVariable)                                                                   | Config               | 把一个Conifg属性的值同步到一个同名的控制台变量。                                                                                                                                                                                                                                      | ★★★★★ |
| [EditorConfig](#Meta_Config_EditorConfig)                                                                                         | Config               | 保存编辑器的配置                                                                                                                                                                                                                                                         | ★★★   |
| [ConfigHierarchyEditable](#Meta_Config_ConfigHierarchyEditable)                                           | Config               | 使得一个属性可以在Config的各个层级配置。                                                                                                                                                                                                                                          | ★★★   |
| [ConfigRestartRequired](#Meta_Config_ConfigRestartRequired)                                                 | Config               | 使属性在设置里改变后弹出重启编辑器的对话框。                                                                                                                                                                                                                                           | ★★★   |


## Container

| Name                                                         | 引擎模块  | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | --------- | ------------------------------------------------------------ | -------- |
| [ReadOnlyKeys](#Meta_Container_ReadOnlyKeys)       | Container | 使TMap属性的Key不能编辑。                                    | ★★       |
| [ArraySizeEnum](#Meta_Container_ArraySizeEnum)    | Container | 为固定数组提供一个枚举，使得数组元素按照枚举值来作为索引和显示。 | ★★★      |
| [TitleProperty](#Meta_Container_TitleProperty)    | Container | 指定结构数组里的结构成员属性内容来作为结构数组元素的显示标题。 | ★★       |
| [EditFixedOrder](#Meta_Container_EditFixedOrder) | Container | 使数组的元素无法通过拖拽来重新排序。                         | ★★       |
| [NoElementDuplicate](#Meta_Container_NoElementDuplicate) | Container | 去除TArray属性里数据项的Duplicate菜单项按钮。                | ★        |


## Debug

| Name                                                                                                                           | 引擎模块                 | 功能描述                                                                                                                                                                                                                                                             | 常用程度  |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| [DebugTreeLeaf](#Meta_Debug_DebugTreeLeaf)                                                                          | Debug                | 阻止BlueprintDebugger展开该类的属性以加速编辑器里调试器的性能                                                                                                                                                                                                                          | ★     |


## DetailsPanel

| Name                                                         | 引擎模块     | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | ------------ | ------------------------------------------------------------ | -------- |
| [HideInDetailPanel](#Meta_DetailsPanel_HideInDetailPanel) | DetailsPanel | 在Actor的事件面板里隐藏该动态多播委托属性。                  | ★★       |
| [DisplayAfter](#Meta_DetailsPanel_DisplayAfter)    | DetailsPanel | 使本属性在指定的属性之后显示。                               | ★★★      |
| [EditCondition](#Meta_DetailsPanel_EditCondition) | DetailsPanel | 给一个属性指定另外一个属性或者表达式来作为是否可编辑的条件。 | ★★★★★    |
| [EditConditionHides](#Meta_DetailsPanel_EditConditionHides) | DetailsPanel | 在已经有EditCondition的情况下，指定该属性在EditCondition不满足的情况下隐藏起来。 | ★★★★★    |
| [InlineEditConditionToggle](#Meta_DetailsPanel_InlineEditConditionToggle) | DetailsPanel | 使这个bool属性在被用作EditCondition的时候内联到对方的属性行里成为一个单选框，而不是自己成为一个编辑行。 | ★★★★★    |
| [HideEditConditionToggle](#Meta_DetailsPanel_HideEditConditionToggle) | DetailsPanel | 用在使用EditCondition的属性上，表示该属性不想要其EditCondition用到的属性被隐藏起来。 | ★★★★★    |
| [DisplayPriority](#Meta_DetailsPanel_DisplayPriority) | DetailsPanel | 指定本属性在细节面板的显示顺序优先级，越小的优先级越高。     | ★★★      |
| [AdvancedClassDisplay](#Meta_DetailsPanel_AdvancedClassDisplay) | DetailsPanel | 指定该类型的变量在高级显示里显示                             | ★★★      |
| [bShowOnlyWhenTrue](#Meta_DetailsPanel_bShowOnlyWhenTrue) | DetailsPanel | 根据编辑器config配置文件里字段值来决定当前属性是否显示。     | ★        |
| [PrioritizeCategories](#Meta_DetailsPanel_PrioritizeCategories) | DetailsPanel | 把指定的属性目录优先显示在前面                               | ★★★      |
| [AutoExpandCategories](#Meta_DetailsPanel_AutoExpandCategories) | DetailsPanel | 指定类内部的属性目录自动展开起来                             | ★★★      |
| [AutoCollapseCategories](#Meta_DetailsPanel_AutoCollapseCategories) | DetailsPanel | 指定类内部的属性目录自动折叠起来                             | ★★★      |
| [ClassGroupNames](#Meta_DetailsPanel_ClassGroupNames)           | DetailsPanel | 指定ClassGroup的名字                                         | ★★★      |
| [MaxPropertyDepth](#Meta_DetailsPanel_MaxPropertyDepth) | DetailsPanel | 指定对象或结构在细节面板里展开的层数。                       | ★        |
| [DeprecatedNode](#Meta_DetailsPanel_DeprecatedNode) | DetailsPanel | 用于BehaviorTreeNode或EnvQueryNode，说明该类已废弃，在编辑器中红色错误展示并有错误ToolTip提示 | ★★       |
| [UsesHierarchy](#Meta_DetailsPanel_UsesHierarchy)               | DetailsPanel | 说明类使用层级数据。用于实例化“细节”面板中的层级编辑功能。   | 💀        |
| [IgnoreCategoryKeywordsInSubclasses](#Meta_DetailsPanel_IgnoreCategoryKeywordsInSubclasses) | DetailsPanel | 用于让一个类的首个子类忽略所有继承的 ShowCategories 和 HideCategories 说明符。 | ★        |
| [NoResetToDefault](#Meta_DetailsPanel_NoResetToDefault) | DetailsPanel | 禁用和隐藏属性在细节面板上的“重置”功能。                     | ★★★      |
| [ReapplyCondition](#Meta_DetailsPanel_ReapplyCondition)         | DetailsPanel | // Properties that have a ReapplyCondition should be disabled behind the specified property when in reapply mode | ★        |
| [HideBehind](#Meta_DetailsPanel_HideBehind)                     | DetailsPanel | 只在指定的属性为true或不为空的时候本属性才显示               | ★        |
| [Category](#Meta_DetailsPanel_Category)                         | DetailsPanel | 指定属性在细节面板中的分类                                   | ★★★★★    |
| [HideCategories](#Meta_DetailsPanel_HideCategories)             | DetailsPanel | 隐藏的类别                                                   | ★★★      |
| [ShowCategories](#Meta_DetailsPanel_ShowCategories)             | DetailsPanel | 显示类别                                                     | 💀        |
| [EditInline](#Meta_DetailsPanel_EditInline)          | DetailsPanel | 为对象属性创建一个实例，并作为子对象。                       | ★★★      |
| [NoEditInline](#Meta_DetailsPanel_NoEditInline)                 | DetailsPanel | Object properties pointing to an UObject instance whos class is marked editinline will not show their properties inline in property windows. Useful for getting actor components to appear in the component tree but not inline in the root actor details panel. | 💀        |
| [AllowEditInlineCustomization](#Meta_DetailsPanel_AllowEditInlineCustomization) | DetailsPanel | 允许EditInline的对象属性可以自定义属性细节面板来编辑该对象内的数据。 | ★        |
| [ForceInlineRow](#Meta_DetailsPanel_ForceInlineRow) | DetailsPanel | 强制TMap属性里的结构key和其他Value合并到同一行来显示         | ★        |


## Development

| Name                                                         | 引擎模块    | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | ----------- | ------------------------------------------------------------ | -------- |
| [DeprecatedProperty](#Meta_Development_DeprecatedProperty) | Development | 标记弃用，引用到该属性的蓝图会触发一个警告                   | ★        |
| [Deprecated](#Meta_Development_Deprecated)           | Development | 指定该元素要废弃的引擎版本号。                               | ★        |
| [DevelopmentOnly](#Meta_Development_DevelopmentOnly) | Development | 使得一个函数变为DevelopmentOnly，意味着只会在Development模式中运行。适用于调试输出之类的功能，但在最终发布版中会跳过。 | ★        |
| [DeprecationMessage](#Meta_Development_DeprecationMessage)      | Development | 定义弃用的消息                                               | ★        |
| [DeprecatedFunction](#Meta_Development_DeprecatedFunction)      | Development | 标明一个函数已经被弃用                                       | ★        |
| [Comment](#Meta_Development_Comment)                    | Development | 用来记录注释的内容                                           | ★★★      |
| [FriendlyName](#Meta_Development_FriendlyName)                  | Development | 和DisplayName一样？                                          | 💀        |
| [DevelopmentStatus](#Meta_Development_DevelopmentStatus)        | Development | 标明开发状态                                                 | ★        |
| [ToolTip](#Meta_Development_ToolTip)                    | Development | 在Meta里提供一个提示文本，覆盖代码注释里的文本               | ★★★      |
| [ShortTooltip](#Meta_Development_ShortTooltip)                  | Development | 提供一个更简洁版本的提示文本，例如在类型选择器的时候显示     | 💀        |


## Enum

| Name                                                         | 引擎模块 | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | -------- |
| [EnumDisplayNameFn](#Meta_Enum_EnumDisplayNameFn) | Enum     | 在Runtime下为枚举字段提供自定义名称的函数回调                | ★★       |
| [Bitflags](#Meta_Enum_Bitflags)                        | Enum     | 设定一个枚举支持采用位标记赋值，从而在蓝图中可以识别出来是BitMask | ★★★★★    |
| [UseEnumValuesAsMaskValuesInEditor](#Meta_Enum_UseEnumValuesAsMaskValuesInEditor) | Enum     | 指定枚举值已经是位移后的值，而不是位标记的索引下标。         | ★★       |
| [Spacer](#Meta_Enum_UMETA_Spacer)                               | Enum     | 隐藏UENUM的某个值                                            | ★★★★★    |
| [ValidEnumValues](#Meta_Enum_ValidEnumValues)   | Enum     | 指定枚举属性值上可选的枚举值选项                             | ★★★      |
| [InvalidEnumValues](#Meta_Enum_InvalidEnumValues)               | Enum     | 指定枚举属性值上不可选的枚举值选项，用以排除一些选项         | ★★★      |
| [GetRestrictedEnumValues](#Meta_Enum_GetRestrictedEnumValues)   | Enum     | 指定一个函数来指定枚举属性值的哪些枚举选项是禁用的           | ★★★      |
| [EnumValueDisplayNameOverrides](#Meta_Enum_EnumValueDisplayNameOverrides) | Enum     | 改变枚举属性值上的显示名字                                   | ★★       |
| [Enum](#Meta_Enum)                                         | Enum     | 给一个String指定以枚举里值的名称作为选项                     | ★★★      |
| [DisplayName](Enum/UMETA/DisplayName/DisplayName)            | Enum     | 改变枚举值的显示名称                                         | ★★★★★    |
| [Hidden](Enum/UMETA/Hidden/Hidden)                           | Enum     | 隐藏UENUM的某个值                                            | ★★★★★    |
| [DisplayValue](#Meta_Enum_UMETA_DisplayValue)                   | Enum     | Enum /Script/Engine.AnimPhysCollisionType                    | 💀        |
| [Grouping](#Meta_Enum_UMETA_Grouping)                           | Enum     | Enum /Script/Engine.EAlphaBlendOption                        | 💀        |
| [TraceQuery](#Meta_Enum_UMETA_TraceQuery)                       | Enum     | Enum /Script/Engine.ECollisionChannel                        | 💀        |
| [Bitmask](#Meta_Enum_BitmaskEnum)                   | Enum     | 设定一个属性采用Bitmask赋值                                  | ★★★★★    |
| [BitmaskEnum](#Meta_Enum_BitmaskEnum)               | Enum     | 使用位标记后采用的枚举名字                                   | ★★★★★    |


## FieldNotify

| Name                                                                                                                           | 引擎模块                 | 功能描述                                                                                                                                                                                                                                                             | 常用程度  |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| [FieldNotifyInterfaceParam](#Meta_UHT_FieldNotifyInterfaceParam)                                        | FieldNotify          | 指定函数的某个参数提供FieldNotify的ViewModel信息。                                                                                                                                                                                                                              | ★★★   |


## GAS

| Name                                                                                                                           | 引擎模块                 | 功能描述                                                                                                                                                                                                                                                             | 常用程度  |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| [HideInDetailsView](#Meta_GAS_HideInDetailsView)                                                                | GAS                  | 把该UAttributeSet子类里的属性隐藏在FGameplayAttribute的选项列表里。                                                                                                                                                                                                                | ★★★   |
| [SystemGameplayAttribute](#Meta_GAS_SystemGameplayAttribute)                                              | GAS                  | 把UAbilitySystemComponent子类里面的属性暴露到FGameplayAttribute 选项框里。                                                                                                                                                                                                       | ★★★   |
| [HideFromModifiers](#Meta_GAS_HideFromModifiers)                                                                | GAS                  | 指定AttributeSet下的某属性不出现在GameplayEffect下的Modifiers的Attribute选择里。                                                                                                                                                                                                   | ★★★   |


## Material

| Name                                                         | 引擎模块 | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | -------- |
| [MaterialParameterCollectionFunction](#Meta_Material_MaterialParameterCollectionFunction) | Material | 指定该函数是用于操作UMaterialParameterCollection，从而支持ParameterName的提取和验证 | ★★★      |
| [MaterialNewHLSLGenerator](#Meta_Material_MaterialNewHLSLGenerator) | Material | 标识该UMaterialExpression为采用新HLSL生成器的节点，当前在材质蓝图右键菜单中隐藏。 | ★        |
| [ShowAsInputPin](#Meta_Material_ShowAsInputPin)  | Material | 使得UMaterialExpression里的一些基础类型属性变成材质节点上的引脚。 | ★★★      |
| [MaterialControlFlow](#Meta_Material_MaterialControlFlow) | Material | 标识该UMaterialExpression为一个控制流节点，当前在材质蓝图右键菜单中隐藏。 | ★        |
| [OverridingInputProperty](#Meta_Material_OverridingInputProperty) | Material | 在UMaterialExpression中指定本float要覆盖的其他FExpressionInput 属性。 | ★★★      |
| [RequiredInput](#Meta_Material_RequiredInput)                   | Material | 在UMaterialExpression中指定FExpressionInput属性是否要求输入，引脚显示白色或灰色。 | 💀        |
| [Private](#Meta_Material_Private)                       | Material | 标识该UMaterialExpression为私有节点，当前在材质蓝图右键菜单中隐藏。 | ★        |


## Niagara

| Name                                                      | 引擎模块 | 功能描述                                      | 常用程度 |
| --------------------------------------------------------- | -------- | --------------------------------------------- | -------- |
| [NiagaraClearEachFrame](#Meta_Niagara_NiagaraClearEachFrame) | Niagara  | ScriptStruct /Script/Niagara.NiagaraSpawnInfo | 💀        |
| [NiagaraInternalType](#Meta_Niagara_NiagaraInternalType)     | Niagara  | 指定该结构的类型为Niagara的内部类型。         | 💀        |


## Numeric

| Name                                                         | 引擎模块 | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | -------- |
| [CtrlMultiplier](#Meta_Numeric_CtrlMultiplier)   | Numeric  | 指定数字输入框在Ctrl按下时鼠标轮滚动和鼠标拖动改变值的倍率。 | ★★       |
| [ShiftMultiplier](#Meta_Numeric_ShiftMultiplier)                | Numeric  | 指定数字输入框在Shift按下时鼠标轮滚动和鼠标拖动改变值的倍率。 | ★★       |
| [SliderExponent](#Meta_Numeric_SliderExponent)   | Numeric  | 指定数字输入框上滚动条拖动的变化指数分布                     | ★★★★★    |
| [Multiple](#Meta_Numeric_Multiple)                     | Numeric  | 指定数字的值必须是Mutliple提供的值的整数倍。                 | ★★★      |
| [Units](#Meta_Numeric_Units)                              | Numeric  | 设定属性值的单位，支持实时根据数值不同动态改变显示的单位。   | ★★★      |
| [ForceUnits](#Meta_Numeric_ForceUnits)                          | Numeric  | 固定设定属性值的单位保持不变，不根据数值动态调整显示单位。   | ★★★      |
| [Delta](#Meta_Numeric_Delta)                              | Numeric  | 设定数字输入框值改变的幅度为Delta的倍数                      | ★★★      |
| [LinearDeltaSensitivity](#Meta_Numeric_LinearDeltaSensitivity)  | Numeric  | 在设定Delta后，进一步设定数字输入框变成线性改变以及改变的敏感度（值越大越不敏感） | ★★★      |
| [UIMin](#Meta_Numeric_UIMin)                              | Numeric  | 指定数字输入框上滚动条拖动的最小范围值                       | ★★★★★    |
| [UIMax](#Meta_Numeric_UIMax)                                    | Numeric  | 指定数字输入框上滚动条拖动的最大范围值                       | ★★★★★    |
| [ClampMin](#Meta_Numeric_ClampMin)                              | Numeric  | 指定数字输入框实际接受的最小值                               | ★★★★★    |
| [ClampMax](#Meta_Numeric_ClampMax)                              | Numeric  | 指定数字输入框实际接受的最大值                               | ★★★★★    |
| [SupportDynamicSliderMinValue](#Meta_Numeric_SupportDynamicSliderMinValue) | Numeric  | 支持数字输入框上滚动条的最小范围值在Alt按下时被动态改变      | ★        |
| [SupportDynamicSliderMaxValue](#Meta_Numeric_SupportDynamicSliderMaxValue) | Numeric  | 支持数字输入框上滚动条的最大范围值在Alt按下时被动态改变      | ★        |
| [ArrayClamp](#Meta_Numeric_ArrayClamp)               | Numeric  | 限定整数属性的值必须在指定数组的合法下标范围内，[0,ArrayClamp.Size()-1] | ★★★      |
| [HideAlphaChannel](#Meta_Numeric_HideAlphaChannel) | Numeric  | 使FColor或FLinearColor属性在编辑的时候隐藏Alpha通道。        | ★★★      |
| [AllowPreserveRatio](#Meta_Numeric_AllowPreserveRatio) | Numeric  | 在细节面板上为FVector属性添加一个比率锁。                    | ★★★      |
| [NoSpinbox](#Meta_Numeric_NoSpinbox)                  | Numeric  | 使数值属性禁止默认的拖放和滚轮的UI编辑功能，数值属性包括int系列以及float系列。 | ★★       |
| [sRGB](#Meta_Numeric_sRGB)                                      | Numeric  | 使FColor或FLinearColor属性在编辑的时候采用sRGB方式。         | 💀        |
| [WheelStep](#Meta_Numeric_WheelStep)                  | Numeric  | 指定数字输入框上鼠标轮上下滚动产生的变化值                   | ★★★      |
| [InlineColorPicker](#Meta_Numeric_InlineColorPicker) | Numeric  | 使FColor或FLinearColor属性在编辑的时候直接内联一个颜色选择器。 | ★★       |
| [ShowNormalize](#Meta_Numeric_ShowNormalize)      | Numeric  | 使得FVector变量在细节面板出现一个正规化的按钮。              | ★★★      |
| [ColorGradingMode](#Meta_Numeric_ColorGradingMode) | Numeric  | 使得一个FVector4属性成为颜色显示                             | ★★       |


## Object

| Name                                                         | 引擎模块 | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | -------- |
| [DisplayThumbnail](#Meta_Object_DisplayThumbnail) | Object   | 指定是否在该属性左侧显示一个缩略图。                         | ★★★      |
| [ThumbnailSize](#Meta_Object_ThumbnailSize)                     | Object   | 改变缩略图的大小。                                           | 💀        |
| [LoadBehavior](#Meta_Object_LoadBehavior)          | Object   | 用在UCLASS上标记这个类的加载行为，使得相应的TObjectPtr属性支持延迟加载。可选的加载行为默认为Eager，可改为LazyOnDemand。 | ★        |
| [ShowInnerProperties](#Meta_Object_ShowInnerProperties) | Object   | 在属性细节面板中显示对象引用的内部属性                       | ★★★★★    |
| [ShowOnlyInnerProperties](#Meta_Object_ShowOnlyInnerProperties) | Object  | 把结构属性的内部属性直接上提一个层级直接展示                 | ★★★      |
| [FullyExpand](#Meta_Object_FullyExpand)                         | Object   |                                                              | 💀        |
| [CollapsableChildProperties](#Meta_Object_CollapsableChildProperties) | Object  | 在TextureGraph模块中新增加的meta。用于折叠一个结构的内部属性。 | 💀        |
| [Untracked](#Meta_Object_Untracked)                   | Object   | 使得TSoftObjectPtr和FSoftObjectPath的软对象引用类型的属性，不跟踪记录资产的 。 | ★        |
| [HideAssetPicker](#Meta_Object_HideAssetPicker) | Object   | 隐藏Object类型引脚上的AssetPicker的选择列表                  | ★★       |
| [AssetBundles](#Meta_Object_AssetBundles)          | Object   | 标明该属性其引用的资产属于哪一些AssetBundles。               | ★★★      |
| [IncludeAssetBundles](#Meta_Object_IncludeAssetBundles) | Object   | 用于UPrimaryDataAsset的子对象属性，指定应该继续递归到该子对象里去探测AssetBundle数据。 | ★★       |
| [MustBeLevelActor](#Meta_Object_MustBeLevelActor)               | Object   |                                                              |          |
| [ExposeFunctionCategories](#Meta_Object_ExposeFunctionCategories) | Object   | 指定该Object属性所属于的类里的某些目录下的函数可以直接在本类上暴露出来。 | ★★★      |


## Path

| Name                                                         | 引擎模块 | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | -------- |
| [ContentDir](#Meta_Path_ContentDir)                  | Path     | 使用UE的风格来选择Content以及子目录。                        | ★★★      |
| [RelativePath](#Meta_Path_RelativePath)                         | Path     | 使得系统目录选择对话框的结果为当前运行exe的相对路径。        | 💀        |
| [RelativeToGameContentDir](#Meta_Path_RelativeToGameContentDir) | Path     | 使得系统目录选择对话框的结果为相对Content的相对路径。        | 💀        |
| [RelativeToGameDir](#Meta_Path_RelativeToGameDir) | Path     | 如果系统目录选择框的结果为Project的子目录，则转换为相对路径，否则返回绝对路径。 | ★★★      |
| [LongPackageName](#Meta_Path_LongPackageName)                   | Path     | 使用UE的风格来选择Content以及子目录，或者把文件路径转换为长包名。 | ★★★      |
| [FilePathFilter](#Meta_Path_FilePathFilter)                     | Path     | 设定文件选择器的扩展名，规则符合系统对话框的格式规范，可以填写多个扩展名。 | ★★★      |


## Pin

| Name                                                                                                                           | 引擎模块                 | 功能描述                                                                                                                                                                                                                                                             | 常用程度  |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| [HidePin](#Meta_Pin_HidePin)                                                                                              | Pin                  | 用在函数调用上，指定要隐藏的参数名称，也可以隐藏返回值。可以隐藏多个参数                                                                                                                                                                                                                             | ★★    |
| [InternalUseParam](#Meta_Pin_InternalUseParam)                                                                   | Pin                  | 用在函数调用上，指定要隐藏的参数名称，也可以隐藏返回值。可以隐藏多个参数                                                                                                                                                                                                                             | ★★    |
| [HideSelfPin](#Meta_Pin_HideSelfPin)                                                                                  | Pin                  | 用在函数调用上，隐藏默认的SelfPin，也就是Target，导致该函数只能在OwnerClass内调用。                                                                                                                                                                                                            | ★★    |
| [DataTablePin](#Meta_Pin_DataTablePin)                                                                               | Pin                  | 指定一个函数参数为DataTable或CurveTable类型，以便为FName的其他参数提供RowNameList的选择。                                                                                                                                                                                                   | ★★    |
| [DisableSplitPin](#Meta_Pin_DisableSplitPin)                                                                      | Pin                  | 禁用Struct的split功能                                                                                                                                                                                                                                                 | ★★    |
| [HiddenByDefault](#Meta_Pin_HiddenByDefault)                                                                      | Pin                  | Struct的Make Struct和Break Struct节点中的引脚默认为隐藏状态                                                                                                                                                                                                                     | ★     |
| [AlwaysAsPin](#Meta_AnimationGraph_AlwaysAsPin)                                                                       | Pin                  | 在动画蓝图中使得动画节点的某个属性总是暴露出来成为引脚                                                                                                                                                                                                                                      | ★★★   |
| [NeverAsPin](#Meta_AnimationGraph_NeverAsPin)                                                                          | Pin                  | 在动画蓝图中使得动画节点的某个属性总是不暴露出来成为引脚                                                                                                                                                                                                                                     | ★★★   |
| [PinHiddenByDefault](#Meta_Pin_PinHiddenByDefault)                                                             | Pin                  | 使得这个结构里的属性在蓝图里作为引脚时默认是隐藏的。                                                                                                                                                                                                                                       | ★★    |


## RigVMStruct

| Name                                                         | 引擎模块    | 功能描述                                                 | 常用程度 |
| ------------------------------------------------------------ | ----------- | -------------------------------------------------------- | -------- |
| [Input](#Meta_RigVM_Input)                                | RigVMStruct | 指定FRigUnit下的该属性作为输入引脚。                     | ★★★★★    |
| [Constant](#Meta_RigVM_Constant)                                | RigVMStruct | 标识一个属性成为一个常量的引脚。                         | ★★★      |
| [Output](#Meta_RigVM_Output)                                    | RigVMStruct | 指定FRigUnit下的该属性作为输出引脚。                     | ★★★★★    |
| [Visible](#Meta_RigVM_Visible)                          | RigVMStruct | 指定FRigUnit下的该属性为常量引脚，无法连接变量。         | ★★★      |
| [Hidden](#Meta_RigVM_Hidden)                                    | RigVMStruct | 指定FRigUnit下的该属性隐藏                               | ★★★      |
| [DetailsOnly](#Meta_RigVM_DetailsOnly)              | RigVMStruct | 指定FRigUnit下的该属性只在细节面板中显示。               | ★★★      |
| [TemplateName](#Meta_RigVM_TemplateName)           | RigVMStruct | 指定该FRigUnit成为一个泛型模板节点。                     | ★★★      |
| [CustomWidget](#Meta_RigVM_CustomWidget)           | RigVMStruct | 指定该FRigUnit里的属性要用自定义的控件来编辑。           | ★★       |
| [ExpandByDefault](#Meta_RigVM_ExpandByDefault)  | RigVMStruct | 把FRigUnit里的属性引脚默认展开。                         | ★★★      |
| [Aggregate](#Meta_RigVM_Aggregate)                    | RigVMStruct | 指定FRigUnit里的属性引脚为可扩展连续二元运算符的运算数。 | ★★★      |
| [Varying](#Meta_RigVM_Varying)                                  | RigVMStruct | ScriptStruct /Script/RigVM.RigVMFunction_GetDeltaTime    | 💀        |
| [MenuDescSuffix](#Meta_RigVM_MenuDescSuffix)     | RigVMStruct | 标识FRigUnit在蓝图右键菜单项的名字后缀。                 | ★★★      |
| [NodeColor](#Meta_RigVM_NodeColor)                    | RigVMStruct | 指定FRigUnit蓝图节点的RGB颜色值。                        | ★★       |
| [Icon](#Meta_RigVM_Icon)                                   | RigVMStruct | 设定FRigUnit蓝图节点的图标。                             | ★★       |
| [Deprecated](RigVM/Deprecated)                               | RigVMStruct | 标识该FRigUnit为弃用状态，不在蓝图右键菜单中显示。       | ★★       |
| [Abstract](#Meta_RigVM_Abstract)                       | RigVMStruct | 标识该FRigUnit为抽象类，不用实现Execute。                | ★★       |
| [RigVMTypeAllowed](#Meta_RigVM_RigVMTypeAllowed) | RigVMStruct | 指定一个UENUM可以在FRigUnit的UEnum*属性中被选择。        | ★★       |
| [Keywords](#Meta_RigVM_Keywords)                       | RigVMStruct | 设定FRigUnit蓝图节点在右键菜单中的关键字，方便输入查找。 | ★★★      |


## Scene

| Name                                                                                                                           | 引擎模块                 | 功能描述                                                                                                                                                                                                                                                             | 常用程度  |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| [MakeEditWidget](#Meta_Scene_MakeEditWidget)                                                                       | Scene                | 使FVector和FTranform在场景编辑器里出现一个可移动的控件。                                                                                                                                                                                                                             | ★★★   |
| [ValidateWidgetUsing](#Meta_Scene_ValidateWidgetUsing)                                                        | Scene                | 提供一个函数来验证当前属性值是否合法。                                                                                                                                                                                                                                              | ★★★   |
| [AllowedLocators](#Meta_Scene_AllowedLocators)                                                                                    | Scene                | 用来给Sequencer定位可绑定的对象                                                                                                                                                                                                                                             | ★     |


## Script

| Name                                                       | 引擎模块 | 功能描述                                                     | 常用程度 |
| ---------------------------------------------------------- | -------- | ------------------------------------------------------------ | -------- |
| [ScriptName](#Meta_Script_ScriptName)                         | Script   | 在导出到脚本里时使用的名字                                   | ★★★      |
| [ScriptNoExport](#Meta_Script_ScriptNoExport)                 | Script   | 不导出该函数或属性到脚本。                                   | ★★★      |
| [ScriptConstant](#Meta_Script_ScriptConstant)                 | Script   | 把一个静态函数的返回值包装成为一个常量值。                   | ★★★      |
| [ScriptConstantHost](#Meta_Script_ScriptConstantHost)         | Script   | 在ScriptConstant的基础上，指定常量生成的所在类型。           | ★        |
| [ScriptMethod](#Meta_Script_ScriptMethod)                     | Script   | 把静态函数导出变成第一个参数的成员函数。                     | ★★★      |
| [ScriptMethodMutable](#Meta_Script_ScriptMethodMutable)       | Script   | 把ScriptMethod的第一个const结构参数在调用上改成引用参数，函数内修改的值会保存下来。 | ★★       |
| [ScriptMethodSelfReturn](#Meta_Script_ScriptMethodSelfReturn) | Script   | 在ScriptMethod的情况下，指定把这个函数的返回值要去覆盖该函数的第一个参数。 | ★★       |
| [ScriptOperator](#Meta_Script_ScriptOperator)                 | Script   | 把第一个参数为结构的静态函数包装成结构的运算符。             | ★★★      |
| [ScriptDefaultMake](#Meta_Script_ScriptDefaultMake)           | Script   | 禁用结构上的HasNativeMake，在脚本里构造的时候不调用C++里的NativeMake函数，而采用脚本内建的默认初始化方式。 | ★        |
| [ScriptDefaultBreak](#Meta_Script_ScriptDefaultBreak)         | Script   |                                                              | ★        |


## Sequencer

| Name                                                                                                                           | 引擎模块                 | 功能描述                                                                                                                                                                                                                                                             | 常用程度  |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| [TakeRecorderDisplayName](#Meta_Sequencer_TakeRecorderDisplayName)                                        | Sequencer            | 指定UTakeRecorderSource的显示名字。                                                                                                                                                                                                                                      | ★★    |
| [SequencerBindingResolverLibrary](#Meta_Sequencer_SequencerBindingResolverLibrary)                | Sequencer            | 把具有SequencerBindingResolverLibrary标记的UBlueprintFunctionLibrary作为动态绑定的类。                                                                                                                                                                                          | ★★    |
| [CommandLineID](#Meta_Sequencer_CommandLineID)                                                                      | Sequencer            | 标记UMovieSceneCaptureProtocolBase的子类的协议类型。                                                                                                                                                                                                                        | ★★    |


## Serialization

| Name                                                         | 引擎模块      | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | ------------- | ------------------------------------------------------------ | -------- |
| [SkipUCSModifiedProperties](#Meta_Serialization_SkipUCSModifiedProperties) | Serialization | 允许ActorComponent里的属性在Actor构造函数里被修改后依然保存下来 | ★        |
| [MatchedSerializers](#Meta_Serialization_MatchedSerializers)    | Serialization | 只在NoExportTypes.h中使用，标明采用结构序列化器。是否支持文本导入导出 | 💀        |


## SparseDataType

| Name                                                                                                                           | 引擎模块                 | 功能描述                                                                                                                                                                                                                                                             | 常用程度  |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| [NoGetter](#Meta_SparseDataType_NoGetter)                                                                                | SparseDataType       | 阻止UHT为该属性生成一个C++的get函数，只对稀疏类的结构数据里的属性生效。                                                                                                                                                                                                                         | ★     |


## String/Text

| Name                                                         | 引擎模块    | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | ----------- | ------------------------------------------------------------ | -------- |
| [PasswordField](#Meta_String_PasswordField)       | String/Text | 使得文本属性显示为密码框                                     | ★★★★★    |
| [PropertyValidator](#Meta_String_PropertyValidator) | String/Text | 用名字指定一个UFUNCTION函数来进行文本的验证                  | ★★★      |
| [MultiLine](#Meta_String_MultiLine)                   | String/Text | 使得文本属性编辑框支持换行。                                 | ★★★★★    |
| [AllowedCharacters](#Meta_String_AllowedCharacters) | String/Text | 只允许文本框里可以输入这些字符。                             | ★★★      |
| [GetOptions](#Meta_String_GetOptions)                | String/Text | 指定一个外部类的函数提供选项给FName或FString属性在细节面板中下拉选项框提供值列表。 | ★★★★★    |
| [GetKeyOptions](#Meta_String_GetKeyOptions)                     | String/Text | 为TMap里的FName/FString作为Key提供细节面板里选项框的选项值   | 💀        |
| [GetValueOptions](#Meta_String_GetValueOptions)                 | String/Text | 为TMap里的FName/FString作Value提供细节面板里选项框的选项值   | 💀        |
| [MaxLength](#Meta_String_MaxLength)                   | String/Text | 在文本编辑框里限制文本的最大长度                             | ★★★★★    |


## Struct

| Name                                                         | 引擎模块 | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | -------- |
| [MakeStructureDefaultValue](#Meta_Struct_MakeStructureDefaultValue) | Struct   | 存储BP中自定义结构里的属性的默认值。                         | ★        |
| [IgnoreForMemberInitializationTest](#Meta_Struct_IgnoreForMemberInitializationTest) | Struct   | 使得该属性忽略结构的未初始验证。                             | ★★       |
| [HasNativeBreak](#Meta_Struct_HasNativeBreak)    | Struct   | 为该结构指定一个C++内的UFunction函数作为Break节点的实现      | ★★★★★    |
| [HasNativeMake](#Meta_Struct_HasNativeMake)                     | Struct   | 为该结构指定一个C++内的UFunction函数作为Mreak节点的实现      | ★★★★★    |
| [DataflowFlesh](#Meta_Struct_DataflowFlesh)                     | Struct   | ScriptStruct /Script/DataflowNodes.FloatOverrideDataflowNode | 💀        |


## TypePicker

| Name                                                         | 引擎模块   | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | ---------- | ------------------------------------------------------------ | -------- |
| [AllowedTypes](#Meta_TypePicker_AllowedTypes)      | TypePicker | 为FPrimaryAssetId可以指定允许的资产类型。                    | ★★★      |
| [BaseClass](#Meta_TypePicker_BaseClass)               | TypePicker | 只在StateTree模块中使用，限制FStateTreeEditorNode选择的基类类型。 | ★        |
| [AllowedClasses](#Meta_TypePicker_AllowedClasses) | TypePicker | 用在类或对象选择器上，指定选择的对象必须属于某一些类型基类。 | ★★★      |
| [ExactClass](#Meta_TypePicker_ExactClass)            | TypePicker | 在同时设置AllowedClasses和GetAllowedClasses的时候，ExactClass指定只取这两个集合中类型完全一致的类型交集，否则取一致的交集再加上其子类。 | ★        |
| [DisallowedClasses](#Meta_TypePicker_DisallowedClasses) | TypePicker | 用在类或对象选择器上，指定选择的对象排除掉某一些类型基类。   | ★★★      |
| [GetAllowedClasses](#Meta_TypePicker_GetAllowedClasses) | TypePicker | 用在类或对象选择器上，通过一个函数来指定选择的对象必须属于某一些类型基类。 | ★★       |
| [GetDisallowedClasses](#Meta_TypePicker_GetDisallowedClasses) | TypePicker | 用在类选择器上，通过一个函数来指定选择的类型列表中排除掉某一些类型基类。 | ★★       |
| [BaseStruct](#Meta_TypePicker_BaseStruct)            | TypePicker | 指定FInstancedStruct属性选项列表选择的结构都必须继承于BaseStruct指向的结构。 | ★★★      |
| [ExcludeBaseStruct](#Meta_TypePicker_ExcludeBaseStruct)         | TypePicker | 在使用BaseStruct的FInstancedStruct属性上忽略BaseStruct指向的结构基类。 | ★★★      |
| [StructTypeConst](#Meta_TypePicker_StructTypeConst)             | TypePicker | 指定FInstancedStruct属性的类型不能在编辑器被选择。           | ★        |
| [MetaStruct](#Meta_TypePicker_MetaStruct)            | TypePicker | 设定到UScriptStruct*属性上，指定选择的类型的父结构。         | ★★★      |
| [ShowDisplayNames](#Meta_TypePicker_ShowDisplayNames) | TypePicker | 在Class和Struct属性上，指定类选择器显示另外的显示名称而不是类原始的名字。 | ★        |
| [DisallowedStructs](#Meta_TypePicker_DisallowedStructs)         | TypePicker | 只在SmartObject模块中应用，用以在类选择器中排除掉某个类以及子类。 | ★        |
| [RowType](#Meta_TypePicker_RowType)                     | TypePicker | 指定FDataTableRowHandle 属性的可选行类型的基类。             | ★★★      |
| [MustImplement](#Meta_TypePicker_MustImplement)   | TypePicker | 指定TSubClassOf或FSoftClassPath属性选择的类必须实现该接口    | ★★★      |
| [ShowTreeView](#Meta_TypePicker_ShowTreeView)      | TypePicker | 用于选择Class或Struct的属性上，使得在类选取器中显示为树形而不是列表。 | ★★       |
| [BlueprintBaseOnly](#Meta_TypePicker_BlueprintBaseOnly) | TypePicker | 用于类属性，指定是否只接受可创建蓝图子类的基类               | ★★       |
| [MetaClass](#Meta_TypePicker_MetaClass)               | TypePicker | 用在软引用属性上，限定要选择的对象的基类                     | ★★       |
| [AllowAbstract](#Meta_TypePicker_AllowAbstract)   | TypePicker | 用于类属性，指定是否接受抽象类。                             | ★★       |
| [HideViewOptions](#Meta_TypePicker_HideViewOptions) | TypePicker | 用于选择Class或Struct的属性上，隐藏在类选取器中修改显示选项的功能。 | ★        |
| [OnlyPlaceable](#Meta_TypePicker_OnlyPlaceable)   | TypePicker | 用在类属性上，指定是否只接受可被放置到场景里的Actor          | ★★       |


## UHT

| Name                                                    | 引擎模块 | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------- | -------- | ------------------------------------------------------------ | -------- |
| [DocumentationPolicy](#Meta_UHT_DocumentationPolicy)       | UHT      | 指定文档验证的规则，当前只能设为Strict                       | ★        |
| [GetByRef](#Meta_Blueprint_GetByRef)                       | UHT      | 指定UHT为该属性生成返回引用的C++代码                         | 💀        |
| [CustomThunk](#Meta_UHT_CustomThunk)                       | UHT      | 指定UHT不为该函数生成蓝图调用的辅助函数，而需要用户自定义编写。 | ★★★★★    |
| [NativeConstTemplateArg](#Meta_UHT_NativeConstTemplateArg) | UHT      | 指定该属性是一个const的模板参数。                            | 💀        |
| [CppFromBpEvent](#Meta_UHT_CppFromBpEvent)                 | UHT      |                                                              | 💀        |
| [IncludePath](#Meta_UHT_IncludePath)                       | UHT      | 记录UClass的引用路径                                         | 💀        |
| [ModuleRelativePath](#Meta_UHT_ModuleRelativePath)         | UHT      | 记录类型定义的的头文件路径，为其处于模块的内部相对路径。     | 💀        |


## Widget

| Name                                                         | 引擎模块 | 功能描述                                                     | 常用程度 |
| ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | -------- |
| [DisableNativeTick](#Meta_Widget_DisableNativeTick) | Widget   | 禁用该UserWidget的NativeTick。                               | ★★★      |
| [ViewmodelBlueprintWidgetExtension](#Meta_Widget_ViewmodelBlueprintWidgetExtension) | Widget   | 用来验证InListItems的Object类型是否符合EntryWidgetClass的MVVM绑定的ViewModelProperty。 | 💀        |
| [DesignerRebuild](#Meta_Widget_DesignerRebuild) | Widget   | 指定Widget里的某个属性值改变后应该重新刷新UMG的预览界面。    | ★        |
| [DefaultGraphNode](#Meta_Widget_DefaultGraphNode)               | Widget   | 标记引擎默认创建的蓝图节点。                                 | 💀        |
| [BindWidget](#Meta_Widget_BindWidget)                | Widget   | 指定在C++类中该Widget属性一定要绑定到UMG的某个同名控件。     | ★★★★★    |
| [BindWidgetOptional](#Meta_Widget_BindWidgetOptional) | Widget   | 指定在C++类中该Widget属性可以绑定到UMG的某个同名控件，也可以不绑定。 | ★★★      |
| [OptionalWidget](#Meta_Widget_OptionalWidget)                   | Widget   | 指定在C++类中该Widget属性可以绑定到UMG的某个同名控件，也可以不绑定。 | ★★★      |
| [IsBindableEvent](#Meta_Widget_IsBindableEvent) | Widget   | 把一个动态单播委托暴露到UMG蓝图里以绑定相应事件。            | ★★★      |
| [EntryInterface](#Meta_Widget_EntryInterface)    | Widget   | 限定EntryWidgetClass属性上可选类必须实现的接口，用在DynamicEntryBox和ListView这两个Widget上。 | ★★★      |
| [EntryClass](#Meta_Widget_EntryClass)                           | Widget | 限定EntryWidgetClass属性上可选类必须继承自的基类，用在DynamicEntryBox和ListView这两个Widget上。 | ★★★      |
| [BindWidgetAnim](#Meta_Widget_BindWidgetAnim)    | Widget   | 指定在C++类中该UWidgetAnimation属性一定要绑定到UMG下的某个动画 | ★★★★★    |
| [BindWidgetAnimOptional](#Meta_Widget_BindWidgetAnimOptional) | Widget   | 指定在C++类中该UWidgetAnimation属性可以要绑定到UMG下的某个动画，也可以不绑定。 | ★★★      |