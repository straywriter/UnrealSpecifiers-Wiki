# BlueprintCallable

- **功能描述：** 暴露到蓝图中可被调用

- **元数据类型：** bool
- **引擎模块：** Blueprint
- **作用机制：** 在FunctionFlags增加[FUNC_BlueprintCallable](#Flags_EFunctionFlags_FUNC_BlueprintCallable)
- **常用程度：** ★★★★★

## 测试代码：

```cpp
UFUNCTION(BlueprintCallable)
void MyFunc_BlueprintCallable() {}
```

## 效果展示：

![Untitled](Specifier_UFUNCTION_Blueprint_BlueprintCallable_Untitled.png)