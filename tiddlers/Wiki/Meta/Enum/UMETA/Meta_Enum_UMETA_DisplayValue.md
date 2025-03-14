﻿# DisplayValue

- **功能描述：** Enum /Script/Engine.AnimPhysCollisionType
- **使用位置：** UENUM::UMETA
- **引擎模块：** Enum Property
- **常用程度：** 0

## 源码例子：

```cpp
UENUM()
enum class AnimPhysCollisionType : uint8
{
	CoM UMETA(DisplayName="CoM", DisplayValue="CoM", ToolTip="Only limit the center of mass from crossing planes."),
	CustomSphere UMETA(ToolTip="Use the specified sphere radius to collide with planes."),
	InnerSphere UMETA(ToolTip="Use the largest sphere that fits entirely within the body extents to collide with planes."),
	OuterSphere UMETA(ToolTip="Use the smallest sphere that wholely contains the body extents to collide with planes.")
};
```