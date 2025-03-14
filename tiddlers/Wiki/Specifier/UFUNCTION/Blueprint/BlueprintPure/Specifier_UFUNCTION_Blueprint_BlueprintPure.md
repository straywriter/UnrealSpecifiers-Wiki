# BlueprintPure

- **功能描述：** 指定作为一个纯函数，一般用于Get函数用来返回值。
- **元数据类型：** bool
- **引擎模块：** Blueprint
- **作用机制：** 在FunctionFlags增加[FUNC_BlueprintCallable](#Flags_EFunctionFlags_FUNC_BlueprintCallable)、[FUNC_BlueprintPure](#Flags_EFunctionFlags_FUNC_BlueprintPure)
- **常用程度：** ★★★★★

指定作为一个纯函数，一般用于Get函数用来返回值。

- 纯函数是指没有执行引脚的函数，不是指const函数。
- 纯函数可以有多个返回值，用引用参数加到函数里就行。
- 不能用于void函数，否则会报错“error : BlueprintPure specifier is not allowed for functions with no return value and no output parameters.”

## 测试代码：

```cpp
UFUNCTION(BlueprintPure)
	int32 GetMyInt()const { return MyInt; }
private:
	int32 MyInt;
```

## 效果展示：

![Untitled](Specifier_UFUNCTION_Blueprint_BlueprintPure_Untitled.png)