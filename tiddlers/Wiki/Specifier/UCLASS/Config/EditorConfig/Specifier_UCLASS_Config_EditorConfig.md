# EditorConfig

- **功能描述：**  用来在编辑器状态下保存信息。
- **引擎模块：** Config, Editor
- **元数据类型：** string="abc"
- **作用机制：** 在Meta中增加[EditorConfig](#Meta_Config_EditorConfig)
- **常用程度：★**

用来在编辑器状态下保存信息。

一般用在EditorTarget的Module里，用于配置相应编辑器的信息，比如列宽，收藏夹之类的，用json保存。

保存在：C:\Users\{user name}\AppData\Local\UnrealEngine\Editor。当前有：

![Untitled](Specifier_UCLASS_Config_EditorConfig_Untitled.png)

在源码里搜索后，使用的时候必须继承于基类：

```cpp
/** Inherit from this class to simplify saving and loading properties from editor configs. */
UCLASS()
class EDITORCONFIG_API UEditorConfigBase : public UObject
{
	GENERATED_BODY()

public:

	/** Load any properties of this class into properties marked with metadata tag "EditorConfig" from the class's EditorConfig */
	bool LoadEditorConfig();

	/** Save any properties of this class in properties marked with metadata tag "EditorConfig" into the class's EditorConfig. */
	bool SaveEditorConfig() const;
};
```

## 示例代码：

```cpp
UCLASS(EditorConfig = "MyEditorGame")
class INSIDER_API UMyClass_EditorConfig : public UEditorConfigBase
{
public:
	GENERATED_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadWrite, meta = (EditorConfig))
	int32 MyPropertyWithConfig = 123;
};

void UMyClass_EditorConfig_Test::TestConfigSave()
{
	//must run after editor initialization
	auto* testObject = NewObject<UMyClass_EditorConfig>(GetTransientPackage(), TEXT("testObject_EditorConfig"));
	testObject->MyPropertyWithConfig = 777;
	testObject->SaveEditorConfig();

}

void UMyClass_EditorConfig_Test::TestConfigLoad()
{
	auto* testObject = NewObject<UMyClass_EditorConfig>(GetTransientPackage(), TEXT("testObject_EditorConfig"));
	testObject->LoadEditorConfig();
}

//运行Save后的保存结果：C:\Users\jack.fu\AppData\Local\UnrealEngine\Editor\MyEditorGame.json

{
	"$type": "MyClass_EditorConfig",
	"MyPropertyWithConfig": 777
}
```