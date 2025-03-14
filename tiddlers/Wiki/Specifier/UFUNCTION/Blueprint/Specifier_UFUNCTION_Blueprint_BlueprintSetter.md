# BlueprintSetter

- **功能描述：** 指定该函数作为属性的自定义Set函数。
- **元数据类型：** bool
- **引擎模块：** Blueprint
- **作用机制：** 在Meta中加入[BlueprintSetter](#Meta_Blueprint_BlueprintSetter)，在FunctionFlags中加入[FUNC_BlueprintCallable ](#Flags_EFunctionFlags_FUNC_BlueprintCallable)
- **常用程度：** ★★

指定该函数作为属性的自定义Set函数。

此说明符隐含BlueprintCallable。

更多可以参考UPROPERTY的BlueprintSetter