image bg room = "/wood.jpg"


label start:
    scene bg room 
    show Тимаз normal
    "Ты готов запускать гаму?"
    $score = 0
    $name = ""  

    menu:  
        "Да":
            $score += 1
            hide Тимаз
            "Едем едем"
            "Можешь тогда и имя свое сказать"
            $name = renpy.input("Введите имя персонажа:")
            $e = Character(name, color="#000000") 
            jump after_name_input  
         
        "Нет": 
            pass
            hide Тимаз

  
label after_name_input:
    scene bg room
    show Тимаз normal
    "Ну привет, "

    menu: 
        "Давай":
            $score += 1
            hide Тимаз
            "Едем едем"
            jump after_choice  
                
        "Не хочу": 
            pass
            hide Тимаз
            jump after_choice  


label after_choice:
    if score >= 1:
        jump good_ending
    else:
        jump bad_ending

label good_ending:
    scene bg room
    show Тимаз with dissolve
    "Тимаз хорошая концовка"
    return

label bad_ending:
    scene bg room
    hide Тимаз with dissolve
    "Тимаз плохая концовка"
    return
