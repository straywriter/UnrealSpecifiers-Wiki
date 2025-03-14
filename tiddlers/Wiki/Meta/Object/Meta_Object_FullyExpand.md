﻿# FullyExpand

- **使用位置：** UPROPERTY
- **元数据类型：** bool
- **关联项：** [ShowInnerProperties](#Meta_Object_ShowInnerProperties)

但是没有发现该Meta被使用的原理代码。

在源码中搜索发现有多处应用，但实际上没有原理代码。

```cpp
	/** The options that are available on the node. */
	UPROPERTY(EditAnywhere, Instanced, Category = "Options", meta=(ShowInnerProperties, FullyExpand="true"))
	TObjectPtr<UMovieGraphValueContainer> SelectOptions;

	/** The currently selected option. */
	UPROPERTY(EditAnywhere, Instanced, Category = "Options", meta=(ShowInnerProperties, FullyExpand="true"))
	TObjectPtr<UMovieGraphValueContainer> SelectedOption;
```