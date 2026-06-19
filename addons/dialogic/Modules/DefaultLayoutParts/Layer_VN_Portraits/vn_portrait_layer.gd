@tool
extends DialogicLayoutLayer

## A layer that allows showing 5 portraits, like in a visual novel.
const COLOR_ACTIVE = Color(1,1,1,1)
const COLOR_DIMMED = Color(.4,.4,.4,1)
const FADE_TIME = .2
## The canvas layer that the portraits are on.
@export var portrait_size_mode: DialogicNode_PortraitContainer.SizeModes = DialogicNode_PortraitContainer.SizeModes.FIT_SCALE_HEIGHT
func _on_speaker_updated(character: DialogicCharacter) -> void:
	for container in get_child(0).get_children():
		if container.get_child_count() > 0:
			var portraitNode = container.get_child(0)
			var tween = create_tween()
			print(portraitNode.get_meta('character'))
			print(character)
			if portraitNode.get_meta('character') == character:
				tween.tween_property(container,"modulate",COLOR_ACTIVE, FADE_TIME)
			else:
				tween.tween_property(container,"modulate",COLOR_DIMMED, FADE_TIME)
func _ready() -> void:
	Dialogic.Text.speaker_updated.connect(_on_speaker_updated)
func _apply_export_overrides() -> void:
	# apply portrait size
	for child: DialogicNode_PortraitContainer in %Portraits.get_children():
		child.size_mode = portrait_size_mode
		child.update_portrait_transforms()
		
