# PropertyFlags :
| Name                               | Feature       | Value              | Description                                                  | UPARAM                                            | UPROPERTY                                                    |
| ---------------------------------- | ------------- | ------------------ | ------------------------------------------------------------ | ------------------------------------------------- | ------------------------------------------------------------ |
| CPF_Edit                           | Editor        | 0x0000000000000001 | Property is user-settable in the editor.                     |                                                   | [EditAnywhere](#Specifier_UPROPERTY_DetaisPanel_EditAnywhere), [EditDefaultsOnly](#Specifier_UPROPERTY_DetaisPanel_EditDefaultsOnly), [EditInstanceOnly](#Specifier_UPROPERTY_DetaisPanel_EditInstanceOnly), [VisibleAnywhere](#Specifier_UPROPERTY_DetaisPanel_VisibleAnywhere), [VisibleDefaultsOnly](#Specifier_UPROPERTY_DetaisPanel_VisibleDefaultsOnly), [VisibleInstanceOnly](#Specifier_UPROPERTY_DetaisPanel_VisibleInstanceOnly), [Interp](#Specifier_UPROPERTY_DetaisPanel_Interp) |
| CPF_ConstParm                      | Trait         | 0x0000000000000002 | This is a constant function parameter                        | Const (Specifier/UPARAM/Const.md)                 |                                                              |
| CPF_BlueprintVisible               | Blueprint     | 0x0000000000000004 | This property can be read by blueprint code                  |                                                   | [BlueprintReadWrite](#Specifier_UPROPERTY_Blueprint_BlueprintReadWrite), [BlueprintReadOnly](#Specifier_UPROPERTY_Blueprint_BlueprintReadOnly), [BlueprintSetter](#Specifier_UPROPERTY_Blueprint_BlueprintSetter), [BlueprintGetter](#Specifier_UPROPERTY_Blueprint_BlueprintGetter), [Interp](#Specifier_UPROPERTY_DetaisPanel_Interp) |
| CPF_ExportObject                   | Serialization | 0x0000000000000008 | Object can be exported with actor.                           |                                                   | [Instanced](#Specifier_UPROPERTY_Instance_Instanced), [Export](#Specifier_UPROPERTY_Serialization_Export) |
| CPF_BlueprintReadOnly              | Blueprint     | 0x0000000000000010 | This property cannot be modified by blueprint code           |                                                   | [BlueprintReadOnly](#Specifier_UPROPERTY_Blueprint_BlueprintReadOnly), [BlueprintGetter](#Specifier_UPROPERTY_Blueprint_BlueprintGetter) |
| CPF_Net                            | Network       | 0x0000000000000020 | Property is relevant to network replication.                 |                                                   | [Replicated](#Specifier_UPROPERTY_Network_Replicated), [ReplicatedUsing](#Specifier_UPROPERTY_Network_ReplicatedUsing) |
| CPF_EditFixedSize                  | Editor        | 0x0000000000000040 | Indicates that elements of an array can be modified, but its size cannot be changed. |                                                   | [EditFixedSize](#Specifier_UPROPERTY_DetaisPanel_EditFixedSize) |
| CPF_Parm                           | Function      | 0x0000000000000080 | Function/When call parameter.                                |                                                   |                                                              |
| CPF_OutParm                        | Function      | 0x0000000000000100 | Value is copied out after function call.                     |                                                   |                                                              |
| CPF_ZeroConstructor                | Trait         | 0x0000000000000200 | memset is fine for construction                              |                                                   |                                                              |
| CPF_ReturnParm                     | Function      | 0x0000000000000400 | Return value.                                                |                                                   |                                                              |
| CPF_DisableEditOnTemplate          | Editor        | 0x0000000000000800 | Disable editing of this property on an archetype/sub-blueprint |                                                   | [EditInstanceOnly](#Specifier_UPROPERTY_DetaisPanel_EditInstanceOnly), [VisibleInstanceOnly](#Specifier_UPROPERTY_DetaisPanel_VisibleInstanceOnly) |
| CPF_NonNullable                    | Trait         | 0x0000000000001000 | Object property can never be null                            |                                                   |                                                              |
| CPF_Transient                      | Serialization | 0x0000000000002000 | Property is transient: shouldn't be saved or loaded, except for Blueprint CDOs. |                                                   | [Transient](#Specifier_UPROPERTY_Serialization_Transient) |
| CPF_Config                         | Config        | 0x0000000000004000 | Property should be loaded/saved as permanent profile.        |                                                   | [Config](#Specifier_UPROPERTY_Config)            |
| CPF_RequiredParm                   | Editor        | 0x0000000000008000 | Parameter must be linked explicitly in blueprint. Leaving the parameter out results in a compile error. | Required (Specifier/UPARAM/Required.md)           |                                                              |
| CPF_DisableEditOnInstance          | Editor        | 0x0000000000010000 | Disable editing on an instance of this class                 |                                                   | [EditDefaultsOnly](#Specifier_UPROPERTY_DetaisPanel_EditDefaultsOnly), [VisibleDefaultsOnly](#Specifier_UPROPERTY_DetaisPanel_VisibleDefaultsOnly) |
| CPF_EditConst                      | Editor        | 0x0000000000020000 | Property is uneditable in the editor.                        |                                                   | [VisibleAnywhere](#Specifier_UPROPERTY_DetaisPanel_VisibleAnywhere) |
| CPF_GlobalConfig                   | Config        | 0x0000000000040000 | Load config from base class, not subclass.                   |                                                   | [GlobalConfig](#Specifier_UPROPERTY_Config_GlobalConfig) |
| CPF_InstancedReference             | Trait         | 0x0000000000080000 | Property is a component references.                          |                                                   | [Instanced](#Specifier_UPROPERTY_Instance_Instanced) |
| CPF_DuplicateTransient             | Serialization | 0x0000000000200000 | Property should always be reset to the default value during any type of duplication (copy/paste, binary duplication, etc.) |                                                   | [DuplicateTransient](#Specifier_UPROPERTY_Serialization_DuplicateTransient) |
| CPF_SaveGame                       | Serialization | 0x0000000001000000 | Property should be serialized for save games, this is only checked for game-specific archives with ArIsSaveGame |                                                   |                                                              |
| CPF_NoClear                        | Editor        | 0x0000000002000000 | Hide clear button.                                           |                                                   | [NoClear](#Specifier_UPROPERTY_DetaisPanel_NoClear) |
| CPF_ReferenceParm                  | Function      | 0x0000000008000000 | Value is passed by reference; CPF_OutParam and CPF_Param should also be set. | ref (Specifier/UPARAM/ref.md)                     |                                                              |
| CPF_BlueprintAssignable            | Blueprint     | 0x0000000010000000 | MC Delegates only.  Property should be exposed for assigning in blueprint code |                                                   | [BlueprintAssignable](#Specifier_UPROPERTY_Blueprint_BlueprintAssignable) |
| CPF_Deprecated                     | Trait         | 0x0000000020000000 | Property is deprecated.  Read it from an archive, but don't save it. |                                                   |                                                              |
| CPF_IsPlainOldData                 | Trait         | 0x0000000040000000 | If this is set, then the property can be memcopied instead of CopyCompleteValue / CopySingleValue |                                                   |                                                              |
| CPF_RepSkip                        | Network       | 0x0000000080000000 | Not replicated. For non replicated properties in replicated structs | NotReplicated (Specifier/UPARAM/NotReplicated.md) | [NotReplicated](#Specifier_UPROPERTY_Network_NotReplicated) |
| CPF_RepNotify                      | Network       | 0x0000000100000000 | Notify actors when a property is replicated                  |                                                   | [ReplicatedUsing](#Specifier_UPROPERTY_Network_ReplicatedUsing) |
| CPF_Interp                         | Editor        | 0x0000000200000000 | interpolatable property for use with cinematics              |                                                   | [Interp](#Specifier_UPROPERTY_DetaisPanel_Interp) |
| CPF_NonTransactional               | Editor        | 0x0000000400000000 | Property isn't transacted                                    |                                                   | [NonTransactional](#Specifier_UPROPERTY_DetaisPanel_NonTransactional) |
| CPF_EditorOnly                     | Editor        | 0x0000000800000000 | Property should only be loaded in the editor                 |                                                   |                                                              |
| CPF_NoDestructor                   | Trait         | 0x0000001000000000 | No destructor                                                |                                                   |                                                              |
| CPF_AutoWeak                       | Trait         | 0x0000004000000000 | Only used for weak pointers, means the export type is autoweak |                                                   |                                                              |
| CPF_ContainsInstancedReference     | Trait         | 0x0000008000000000 | Property contains component references.                      |                                                   |                                                              |
| CPF_AssetRegistrySearchable        | Editor        | 0x0000010000000000 | asset instances will add properties with this flag to the asset registry automatically |                                                   | [AssetRegistrySearchable](#Specifier_UPROPERTY_Asset_AssetRegistrySearchable) |
| CPF_SimpleDisplay                  | Editor        | 0x0000020000000000 | The property is visible by default in the editor details view |                                                   | [SimpleDisplay](#Specifier_UPROPERTY_DetaisPanel_SimpleDisplay) |
| CPF_AdvancedDisplay                | Editor        | 0x0000040000000000 | The property is advanced and not visible by default in the editor details view |                                                   | [AdvancedDisplay](#Specifier_UPROPERTY_DetaisPanel_AdvancedDisplay) |
| CPF_Protected                      | Editor        | 0x0000080000000000 | property is protected from the perspective of script         |                                                   |                                                              |
| CPF_BlueprintCallable              | Blueprint     | 0x0000100000000000 | MC Delegates only.  Property should be exposed for calling in blueprint code |                                                   | [BlueprintCallable](#Specifier_UPROPERTY_Blueprint_BlueprintCallable) |
| CPF_BlueprintAuthorityOnly         | Network       | 0x0000200000000000 | MC Delegates only.  This delegate accepts (only in blueprint) only events with BlueprintAuthorityOnly. |                                                   | [BlueprintAuthorityOnly](#Specifier_UPROPERTY_Blueprint_BlueprintAuthorityOnly) |
| CPF_TextExportTransient            | Serialization | 0x0000400000000000 | Property shouldn't be exported to text format (e.g. copy/paste) |                                                   | [TextExportTransient](#Specifier_UPROPERTY_Serialization_TextExportTransient) |
| CPF_NonPIEDuplicateTransient       | Serialization | 0x0000800000000000 | Property should only be copied in PIE                        |                                                   | [NonPIEDuplicateTransient](#Specifier_UPROPERTY_Serialization_NonPIEDuplicateTransient) |
| CPF_ExposeOnSpawn                  | Trait         | 0x0001000000000000 | Property is exposed on spawn                                 |                                                   |                                                              |
| CPF_PersistentInstance             | Serialization | 0x0002000000000000 | A object referenced by the property is duplicated like a component. (Each actor should have an own instance.) |                                                   | [Instanced](#Specifier_UPROPERTY_Instance_Instanced) |
| CPF_UObjectWrapper                 | Trait         | 0x0004000000000000 | Property was parsed as a wrapper class like TSubclassOf<T>, FScriptInterface etc., rather than a USomething* |                                                   |                                                              |
| CPF_HasGetValueTypeHash            | Trait         | 0x0008000000000000 | This property can generate a meaningful hash value.          |                                                   |                                                              |
| CPF_NativeAccessSpecifierPublic    | Trait         | 0x0010000000000000 | Public native access specifier                               |                                                   |                                                              |
| CPF_NativeAccessSpecifierProtected | Trait         | 0x0020000000000000 | Protected native access specifier                            |                                                   |                                                              |
| CPF_NativeAccessSpecifierPrivate   | Trait         | 0x0040000000000000 | Private native access specifier                              |                                                   |                                                              |
| CPF_SkipSerialization              | Serialization | 0x0080000000000000 | Property shouldn't be serialized, can still be exported to text |                                                   | [SkipSerialization](#Specifier_UPROPERTY_Serialization_SkipSerialization) |