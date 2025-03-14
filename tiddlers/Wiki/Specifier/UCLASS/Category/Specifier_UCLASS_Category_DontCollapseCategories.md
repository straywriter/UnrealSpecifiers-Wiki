# DontCollapseCategories

- **功能描述：**  使继承自基类的CollapseCatogories说明符无效。
- **引擎模块：** Category
- **元数据类型：** bool
- **作用机制：** 在ClassFlags中去除[CLASS_CollapseCategories](#Flags_EClassFlags_CLASS_CollapseCategories)
- **关联项：** [CollapseCategories](#Specifier_UCLASS_Category_CollapseCategories)
- **常用程度：★★**

理论上是去除类标志上的CLASS_CollapseCategories标志。可以重新打开所有的属性显示。