# UE5标识符详解

- **作者：** 大钊
- **文档版本：** 1.1
- **修订日期：** 2024/10/23
- **适用引擎版本：** UE5.4
- **GitHub地址：** https://github.com/fjz13/UnrealSpecifiers
- **知乎地址：** https://www.zhihu.com/people/fjz13
- **邮箱：** fjz13@live.cn
- **版权声明：** 本文档和示例工程作为开源免费阅读学习使用，版权所有归于作者（大钊），其他人不得用于商业用途。

大家好，我是大钊。有感于虚幻社区内经常有人会提问UE中标识符以及各种meta的使用，也不满足于虚幻官方文档对每个标识符解释的匮乏，因此特整理了此文档。包括100多个标识符和300多个meta的详解。本文档库持续维护中。

一般情况下，建议在GitHub上或者clone下来，查看各种md文件文档，这样有更好的目录划分以及链接跳转。网络不畅的也可以查看pdf版本电子书。在文档的开头有各个标识符的整体表格，方便你简单一览所有标识符的作用。然后对特定的标识符，请善用搜索功能查找。

文档必然有各种缺漏错误不足之处，欢迎提交PR或与我反馈联系，让虚幻社区更多人受益。

# Specifier

以下是各个标识符的表格链接：

- [UCLASS](#Specifier_UCLASS)
- [UINTERFACE](#Specifier_UINTERFACE)

- [USTRUCT](#Specifier_USTRUCT)

- [UENUM](#Specifier_UENUM)
- [UFUNCTION](#Specifier_UFUNCTION)

- [UPARAM](#Specifier_UPARAM)

- [UPROPERTY](#Specifier_UPROPERTY)

# Meta

以下是meta表格链接：

- [Meta](Meta/Meta.md)

# Flags

以下是各个Flags表格链接，列出来只是因为标识符的内部作用机制会添加和移除Flags，放在这里供你阅读参考。不用去细研究每个flags的用处。

- [EClassFlags](#Flags_EClassFlags)

- [EStructFlags](#Flags_EStructFlags)

- [EEnumFlags](#Flags_EEnumFlags)

- [EFunctionFlags](#Flags_EFunctionFlags)

- [EPropertyFlags](#Flags_EPropertyFlags)