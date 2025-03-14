# UINTERFACE(标识符)

## DllExport

| Name                                                         | 引擎模块  | 功能描述                                                | 常用程度 |
| ------------------------------------------------------------ | --------- | ------------------------------------------------------- | -------- |
| [MinimalAPI](#Specifier_UINTERFACE_UHT_MinimalAPI)                   | DllExport | 指定该UInterface对象不导出到别的模块                    | ★        |


## Blueprint

| Name                                                         | 引擎模块  | 功能描述                                                | 常用程度 |
| ------------------------------------------------------------ | --------- | ------------------------------------------------------- | -------- |
| [Blueprintable](#Specifier_UINTERFACE_Blueprint_Blueprintable) | Blueprint | 可以在蓝图中实现                                        | ★★★★★    |
| [NotBlueprintable](#Specifier_UINTERFACE_Blueprint_NotBlueprintable) | Blueprint | 指定不可以在蓝图中实现                                  | ★★★      |
| [ConversionRoot](#Specifier_UINTERFACE_UHT_ConversionRoot)           | Blueprint | Sets IsConversionRoot metadata flag for this interface. | 💀        |