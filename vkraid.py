import vk_api
from numpy import random
import time
from threading import Thread
from enum import Enum
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import six
import traceback
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


vk_session = vk_api.VkApi(token='vk1.a.UAANC0SGU9HmPQRx_2Ff1uenmXBOH95_2X71lZBH-rbCoKd-in-l7geq1hEpRxjGwW_In0FHrMXdEY3AfNui5BILgWzlDbGWDbamiyMgJZXy3CRunOGpXioJSoUgcVdFuNFPQONFuL_YC5xDjsN3e9STw7uBvURWa9Na5pB-OPrMnjv06Q-Ji-XhpnYIykXK9c-LJj8-l6UCZg1d-_b8UQ') #Токен мне не нужен,но буду благодарен если вы не будете его использовать.
vk = vk_session.get_api()
print('Bot started!')
def pizda():
    longpoll = VkBotLongPoll(vk_session,     '219619471')
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_chat:
                while True:
                       colorr = random.choice(['negative','primary', 'positive', 'secondary'])
                       color = random.choice(['negative','positive', 'primary', 'secondary'])
                       colo = random.choice(['negative','primary', 'positive', 'secondary'])
                       col = random.choice(['negative','primary', 'positive', 'secondary'])
                       textfobot = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       textfobo = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       textfob = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       textfo = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       keyboard = VkKeyboard(one_time=False)
                       keyboard.add_button(textfobot, color=colorr)
                       keyboard.add_button(textfobo, color=color)
                       keyboard.add_button(textfob, color=colo)
                       keyboard.add_button(textfo, color=col)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative','primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative','primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative','primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative','primary', 'positive', 'secondary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])                                                                                                                                                                                        
                       keyboard.add_button(text1,color=col1)
                       keyboard.add_button(text2,color=col2)
                       keyboard.add_button(text3,color=col3)                                                                                                                                            
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])                                                                                             
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])                                                                                               
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       vk.messages.send(chat_id=event.chat_id,attachment='wall-219619471_3',random_id='0',keyboard=keyboard.get_keyboard())
                       vk.messages.send(chat_id=event.chat_id,message='😀😁😂🤣😃😄😅😆😉😊😋😎😍😘😗😆😙😚☺🙂🤩🤗🤨🤔😐😑😶🙄😏😜🤐😔🤬😡😷😱😬😧🤤☹😳🤢🤢🤧😇😈😈👿🙀🤖👽💀☠👻😻😹😸😻🙊🙉🙈👩🧒👴👦👨‍⚕️👨‍🎓️👨‍🍳️👨‍✈️🧕👲👳‍♀️👳🤴🕵💂👩‍🎤️👨‍🎤️👩‍💻️👨‍💻️💆🙋‍♂️🧘🧗👯💆‍♂️🏃‍♀️🏃‍♀️🛌⛷🤸‍♂️🏋‍♀️🏄🚵🤹🤾🤼🤹🤾🏄💑💗🤚💅✋✋🖕👆👆☝👉👊🤟🙌✍🤞🖖👏👃👍🤙🤜🤝💕💝💦💨💥💣💤💌🧣👑💭🛍🎒👠👔💬🦒🐿🦉🐓🐓🐓🐓🐳🐚🐛🐌🦑🕸🦂🕷🕸💐💮🏵🦐🦕🐧🐤🍔🥕🥝🍳🍿🍄🍞🎏🎍🎍🎏🎏🏉🏉🏉🏒🏒🏑🎟🎟🎟🎎🎎🎑🏅🏅🏉🏸🏸🌏🌏🗺🗺🥌🥌🎴⛺⛲⛲⛩⛩🏯🏯🏯🏦♨🚆🎪🛸🌆🛩🛎🕠🕜🕡🕥🕠🕓🕒🚽🚽💺⛴🛋🌩🌛🌔🌕🌠🌞🌗🌤🌈🔉🔇📻🎹📢📯🎤🔌📜🔎🖲🔭📚💸🏷📰🕯📘📮✏🖋🖊📋✂📏📍⛏⚒💊🚹🚰🏧🚳🛃⚠🚷🔞🚯🔂🕎♈♒🔽🎦©❇✖📛🔆📳📴⃣🆓🔠💯🈺🉐🈹🈚🉑🈳🈴🔸🔷⬛🇦🇬🚩🏳‍🌈️🏃‍♀️😀😁😂🤣😃😄😅😆😉😊😋😎😍😘😗😆😙😚☺🙂🤩🤗🤨🤔😐😑😶🙄😏😜🤐😔🤬😡😷😱😬😧🤤☹😳🤢🤢🤧😇😈😈👿🙀🤖👽💀☠👻😻😹😸😻🙊🙉🙈👩🧒👴👦👨‍⚕️👨‍🎓️👨‍🍳️👨‍✈️🧕👲👳‍♀️👳🤴🕵💂👩‍🎤️👨‍🎤️👩‍💻️👨‍💻️💆🙋‍♂️🧘🧗👯💆‍♂️🏃‍♀️🏃‍♀️🛌⛷🤸‍♂️🏋‍♀️🏄🚵🤹🤾🤼🤹🤾🏄💑💗🤚💅✋✋🖕👆👆☝👉👊🤟🙌✍🤞🖖👏👃👍🤙🤜🤝💕💝💦💨💥💣💤💌🧣👑💭🛍🎒👠👔💬🦒🐿🦉🐓🐓🐓🐓🐳🐚🐛🐌🦑🕸🦂🕷🕸💐💮🏵🦐🦕🐧🐤🍔🥕🥝🍳🍿🍄🍞🎏🎍🎍🎏🎏🏉🏉🏉🏒🏒🏑🎟🎟🎟🎎🎎🎑🏅🏅🏉🏸🏸🌏🌏🗺🗺🥌🥌🎴⛺⛲⛲⛩⛩🏯🏯🏯🏦♨🚆🎪🛸🌆🛩🛎🕠🕜🕡🕥🕠🕓🕒🚽🚽💺⛴🛋🌩🌛🌔🌕🌠🌞🌗🌤🌈🔉🔇📻🎹📢📯🎤🔌📜🔎🖲🔭📚💸🏷📰🕯📘📮✏🖋🖊📋✂📏📍⛏⚒💊🚹🚰🏧🚳🛃⚠🚷🔞🚯🔂🕎♈♒🔽🎦©❇✖📛🔆📳📴⃣🆓🔠💯🈺🉐🈹🈚🉑🈳🈴🔸🔷⬛🇦🇬🚩🏳‍🌈️🏃‍♀️😀😁😂🤣😃😄😅😆😉😊😋😎😍😘😗😆😙😚☺🙂🤩🤗🤨🤔😐😑😶🙄😏😜🤐😔🤬😡😷😱😬😧🤤☹😳🤢🤢🤧😇😈😈👿🙀🤖👽💀☠👻😻😹😸😻🙊🙉🙈👩🧒👴👦👨‍⚕️👨‍🎓️👨‍🍳️👨‍✈️🧕👲👳‍♀️👳🤴🕵💂👩‍🎤️👨‍🎤️👩‍💻️👨‍💻️💆🙋‍♂️🧘🧗👯💆‍♂️🏃‍♀️🏃‍♀️🛌⛷🤸‍♂️🏋‍♀️🏄🚵🤹🤾🤼🤹🤾🏄💑💗🤚💅✋✋🖕👆👆☝👉👊🤟🙌✍🤞🖖👏👃👍🤙🤜🤝💕💝💦💨💥💣💤💌🧣👑💭🛍🎒👠👔💬🦒🐿🦉🐓🐓🐓🐓🐳🐚🐛🐌🦑🕸🦂🕷🕸💐💮🏵🦐🦕🐧🐤🍔🥕🥝🍳🍿🍄🍞🎏🎍🎍🎏🎏🏉🏉🏉🏒🏒🏑🎟🎟🎟🎎🎎🎑🏅🏅🏉🏸🏸🌏🌏🗺🗺🥌🥌🎴⛺⛲⛲⛩⛩🏯🏯🏯🏦♨🚆🎪🛸🌆🛩🛎🕠🕜🕡🕥🕠🕓🕒🚽🚽💺⛴🛋🌩🌛🌔🌕🌠🌞🌗🌤🌈🔉🔇📻🎹📢📯🎤🔌📜🔎🖲🔭📚💸🏷📰🕯📘📮✏🖋🖊📋✂📏📍⛏⚒💊🚹🚰🏧🚳🛃⚠🚷🔞🚯🔂🕎♈♒🔽🎦©❇✖📛🔆📳📴⃣🆓🔠💯🈺🉐🈹🈚🉑🈳🈴🔸🔷⬛🇦🇬🚩🏳‍🌈️🏃‍♀️',random_id='0',keyboard=keyboard.get_keyboard())
                       vk.messages.send(chat_id=event.chat_id,attachment='wall-219619471_1',random_id='0',keyboard=keyboard.get_keyboard())
                       vk.messages.send(chat_id=event.chat_id,message='ГОСПОДА ЛИБЕРАСТЫ! ВЫ ОКРУЖЕНЫ! ВАМ БЕЖАТЬ НЕКУДА! СЛАВА РОССИИ! СИЛА V ПРАВДЕ! СЛАВА РУСИ56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏',random_id='0',keyboard=keyboard.get_keyboard())
                       vk.messages.send(chat_id=event.chat_id,message='😮🤢✔☝👦🧒👍😑56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉🐱‍💻🐱‍💻🐱‍💻🐱‍🏍🐱‍🏍🐱‍👤🤳🤳🎂👀✨😆😆🤔🎁 😮🤢✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢💖😜👏💋🌹🎉🐱‍🚀🐱‍🚀🐱‍👓🐱‍🐉✔☝👦🧒👍😑👎✅❌😃🤷‍♂️😍🤣56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏56#͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏#͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓͓̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏̏😘😁👌🤞❤🔥😊😂😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉😎🎶😢😒💕🙌🤦‍♀️🤦‍♂️🤷‍♀️✌😉',random_id='0',keyboard=keyboard.get_keyboard())
while True:
          try:
          	  pizda()
          except Exception as e:
                   print('Error', traceback.format_exc())
