@tool
extends DialogicPortrait

func _update_portrait(_passed_character: DialogicCharacter, _passed_portrait: String) -> void:
	var maleSprite: AnimatedSprite2D = $male
	var femaleSprite: AnimatedSprite2D = $female
	if _passed_portrait == "":
		_passed_portrait == "neutral"
	var currentGender = Dialogic.VAR._get("selectedGender")
	var activeSprite: AnimatedSprite2D
	if currentGender == "female":
		maleSprite.visible = false
		femaleSprite.visible = true
		activeSprite = femaleSprite
	else:
		maleSprite.visible = true
		femaleSprite.visible = false
		activeSprite = maleSprite
	if activeSprite.sprite_frames.has_animation(_passed_portrait) && activeSprite.animation != _passed_portrait:
		activeSprite.play(_passed_portrait)
		
		
