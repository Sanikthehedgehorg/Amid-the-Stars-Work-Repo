# The script of the game goes in this file.


# CHARACTERS


define Pearl = Character("Pearl", color="ADEEFF")
define Cam = Character ("Cam", color="C70053")
define Austin = Character("Austin", color="FFFFFF")
define Joline = Character("Joline", color="99C700")
define Amanda = Character("Amanda", color="4630AB")
define You = Character("You", color="FF6900")


# CUSTOM DEFINITIONS
   default affection_points_cam = 0
   default acquiredItem = False


transform midleft:
   xalign 0.25
   yalign 1.0


transform midright:
   xalign 0.75
   yalign 1.0


# PROLOGUE START


label start: 
   "Cam's Bedroom - September 14th, 2025 6:31 p.m."
   play music "audio/.."
   scene bg bedroom
   with fade
   show cam sleepy
   "*Ring ring!*"
   show bg half bedroom call
   show cam normal at midright
   Cam "Hello?"
   show bg call
   show joline normal at midleft
   Joline "The time has come. {color=#FF0000}Space Imposters.{/color} is imminent. The gods have chosen me as the messenger... but I request your aid in assembling a proper group."
   Cam "Um.. What?"
   show joline concerned at midleft
   Joline "You know. Among Us. The murder mystery video game that EXPLODED during the COVID-19 epidemic?"
   Cam "No, I know. You're just, like, a little weird about propositioning it."
   show joline normal at midleft
   Joline "Okay, well maybe you're not weird enough. Have you ever thought of that? Anyways, do you know anyone interesting who would be willing to play with us?"
   Cam "Uhh, I think I can invite some people? Do you know Amanda?"
   Joline "Amanda who?"
   Cam "The Asian one. She's a friend of mine. Among Us doesn't seem really her speed but I think she would be fun to play with. Can I invite her and Pearl?"
   Joline "I think anyone is fine. I trust your judgement. I'm gonna make a server for everyone to voice chat in. Could you invite the others?"
   Cam "Yeah, sure. Is it okay if I ask Amanda to invite some of her friends, too? Because I don't know if I'm chill with enough people."
   Joline "That's fine, yeah. We only need, like, ten people."
   Cam "What if we don't get that many?"
   Joline "Ughh, then the game won't be as cool. But I guess we can figure it out. Like, there's not enough people to kill and stuff."
   Cam "It'll be fine. We can play in public lobbies if we really want more people."
   Joline "Public lobbies are LAME. I want to play with people I can actually talk to."
   Cam "Okay, fine... I'm gonna text Amanda now."
   Joline "Okay, then that's all! I've just been really craving some Among Us, so. You know."
   Cam "Um, yeah. I haven't played in a long time but I'm down."
   Joline "Yay, okay! Talk to you in a bit."
   Cam "See ya."
   "7:14 p.m."
   Amanda "Wait, so how do I change my color?"
   Pearl "You see my little blue astronaut? Follow me. Yeah, so right here is the player customization desk thing..."
   Amanda "Ohh."
   Austin "Yeah, you can wear different hats and stuff."
   Cam "Wait! Let me be brown. I'm rejoining right now."
   Cam "Um... what's the code, again?"
   Joline "BRO. Why do you keep leaving and rejoining.."
   Cam "I'm on mobile and I keep tabbing off because this is taking forever, sorry. The code?"
   Pearl "Can we just paste it in chat so we don't have to go through this AGAIN."
   Joline "That is a genius idea, Ms. Pung."
   Pearl "Boi."
   Cam "Okay, thank you. Anyways, are we ready?"
   Joline "Uh, we only have five people. Can't we get, like, one more?"
   Austin "Why can't we just do fi-"
   Joline "Because that's lame as fuck, man. Does anyone know someone else who can join?"
   Amanda "I can invite Nathan?"
   Joline "Sure, whoever. Just hurry up, though."
   Joline "I mean- Be hasty, soldier! Time is a-ticking."
   Amanda "Riiight..."
   "PLACEHOLDERUSERNAME joined the call"
   play sound "audio/..."
   Amanda "Hey hey PLACEHOLDER NAME!"
   You "Hi, what's up?"
   Pearl "We're playing Space Imposters! We were wondering if you'd be interested in joining."
   Amanda "Is that okay?"
   You "Yeah, sure. I'm down. What's the code?"
   Austin "It's in the chat."
   You "Cool, cool. I'll be right there."
   "You type in the code. Strangely, your game glitches a bit before you spawn in. Must be your internet, or you're so tired that you're beginning to see things."
   Joline "Okay, cool! I'm gonna start the game now. Is everyone good?"
   Cam "Yeah."
   Austin "Just to check, do we have any custom game settings?"
   Joline "Yes, I increased movement speed a bit and increased kill cooldown. Is there anything else we need, or?"
   Austin "Nah, that's fine. How long is the cooldown?"
   Joline "Five days."
   Austin "...."
   Joline "Kidding. It's forty-five seconds. Good?"
   Pearl "Sounds fine to me!"
   Joline "Okay, I'm clicking start guys!"
   Amanda "Wait, so what do I do if I'm the murderer?"
   Cam "You'll figure it out, Amanda. The game mechanics aren't that hard. Just don't tell anyone if you do get it."
   Amanda "Okayyy-"
   Austin "Woah-"
   Joline "What the fuck?!"
   "!!!"
   play sound "audio/..."
   scene bg white
   "You hear a thud."
   scene bg black
   scene bg cafeteria
   show cam shocked
   Cam "What the sigma..."
   show pearl normal at midleft
   Pearl "Uh-"
   show joline shocked
   Joline "What the FUCK just happened."
scene bg cafeteria
menu:
# OPTION 1 CHOICES1_COMMON
   "' I think- I think we're on the... spaceship? '":
      show joline normal at midleft
      Joline "Seems like it."
      show amanda shocked at midright
      Amanda "Wait, what does that mean? This is definitely NOT part of the game."
      Amanda "Right?"
      show player normal
      You "No, I don't think it is."
      hide joline normal
      show austin normal at midleft
      Austin "It appears as though we've been teleported to the map featured in Space Imposters."
      hide amanda shocked
      show cam normal at midright
      Cam "Oh my god."
      hide player normal
      Austin "It's hard to tell, though. The pixelated interface of the game isn't very comparable to what appears to be--"
      show joline normal
      Joline "A real ass space ship."
      Austin "Precisely."
# OPTION 2 CHOICES1_COMMON
   "' Yo, this is sick! '":
      Cam "Sure is."
      Amanda "Are you crazy?!"
      Austin "I think we're all just shocked right now."
label choices1_common:
   show austin normal
   "You look around. Austin seems calm, outwardly, but you're not so sure."
   hide austin normal
   show cam shocked
   "Cam looks pale, and he's chewing on his nails."
   hide cam shocked
   show joline angry
   "Joline looks a little frustrated that she doesn't get to play Space Imposters."
   hide joline angry
   show amanda shocked
   "Amanda looks confused" 
   hide amanda shocked
   show pearl normal
   "...and Pearl is expressionless. You wonder what you look like right now. Scared?"
   Pearl "So. We all agree we have no idea what's going on, right?"
   Cam "I sure don't."
   Joline "Should we look around, then?"
   Austin "That sounds like a good idea to me. Would we be more effective if we split into smaller groups?"
   Amanda "I mean, maybe. But we don't know at all where we are or how big this ship is. What if we get lost and can't find each other?"
   Amanda "It's a big risk to consider. We might be safer if we stay as one big group."
   Cam "I agree. I'm... a little scared. Like. Yeah."
   Austin "That is a fair point."
   Joline "Come on, guys. Just trace your steps and we'll reconvene here in this.. uh.. Cafeteria? Yeah."
   You "That might work."
   Cam "I have a fuckass memory, man."
   Pearl "Well, if we all work together in our mini-groups it probably won't be too bad. You know?"
   You "It might be best to try to learn as much as we can about our surroundings and situation as fast as possible."
   Amanda "But it might be safer to stick together!"
   Austin "Hm... How about we all vote?"
   "Cam rolls his eyes."
   Amanda "Fine."
   Joline "I think we split up. Two groups. It's better than splitting up individually, ain't it?"
   Austin "I agree with Joline."
   Pearl "I really don't mind either way."
   Cam "I say we stick together. We don't know what's out there and, frankly, this ship creeps me out. Can you not hear that creaking?"
   Amanda "Stick together."
   "Everyone turns to you."
   Austin "What do you say?"
menu:
   "' I think it would be best if we sticked together. '":
      Amanda "I knew you would think so!"
      Pearl "Wait, on second thought... I actually think it would be better if we split up."
      Cam "What? Are you serious?"
      Austin "It would appear we have a tie."
      Joline "Can we please just explore in little groups? See the reason in this, guys. It's so obviously the better plan."
      Amanda "..." 
      Amanda "Maybe to you guys, but what's the point in exploring a little faster?"
   "' We should split up, definitely. '":
      Austin "Good call."