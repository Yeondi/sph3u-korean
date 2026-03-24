#!/usr/bin/env python3
"""Fix broken translations and translate remaining English in sph3u_u1la5.html."""
import re

filepath = 'course_content/lessons/sph3u_u1la5.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# PHASE 1: Fix broken partial replacements from prior scripts
# "따라서me" should be "some", "따라서mething" should be "something" etc.
# These happened because "so" was globally replaced inside words
content = content.replace('따라서me ', 'some ')
content = content.replace('따라서mething', 'something')
content = content.replace('따라서mewhat', 'somewhat')
content = content.replace('따라서meone', 'someone')
content = content.replace('따라서metimes', 'sometimes')
content = content.replace('따라서und', 'sound')
content = content.replace('따라서n', 'son')
content = content.replace('따라서lution', 'solution')
content = content.replace('따라서lve', 'solve')
content = content.replace('따라서lid', 'solid')
content = content.replace('따라서ft', 'soft')
content = content.replace('예제s', 'Examples')

# PHASE 2: Full translation - line by line approach for multiline content
# Use regex-based replacement for multiline spans

REPLACEMENTS = [
    # Fix noscript (different text than expected - has typo "contians")
    ("To ensure the greatest educational experience, this learning activity\n                contians\n                aspects that require Javascript to be enabled.", "최상의 학습 경험을 위해, 이 학습 활동은 Javascript가 활성화되어 있어야 합니다."),
    ("<strong>Warning!</strong>", "<strong>주의!</strong>"),

    # Learning goals (different text in actual file)
    ("<p>We are learning to:</p>", "<p>학습 내용:</p>"),
    ("<li>describe mechanical resonance</li>", "<li>역학적 공명을 설명한다</li>"),
    ("<li>identify sympathetic vibration</li>", "<li>공감 진동을 식별한다</li>"),
    ("calculate resonant frequencies using", "다음을 사용하여 공명 진동수를 계산한다:"),
    ("<li>apply equations involving resonance in air columns</li>", "<li>공기 기둥에서의 공명과 관련된 방정식을 적용한다</li>"),
    ("<li>study the application of resonance in musical instruments</li>", "<li>악기에서의 공명 응용을 학습한다</li>"),
    ("<p>I am able to:</p>", "<p>나는 다음을 할 수 있다:</p>"),
    ("<li>describe when and how resonance occurs</li>", "<li>공명이 언제, 어떻게 발생하는지 설명할 수 있다</li>"),
    ("<li>describe the difference between closed and open-air columns</li>", "<li>닫힌 공기 기둥과 열린 공기 기둥의 차이를 설명할 수 있다</li>"),
    ("<li>calculate the resonant lengths of air columns</li>", "<li>공기 기둥의 공명 길이를 계산할 수 있다</li>"),
    ("<li>describe how resonance is used in musical instruments</li>", "<li>악기에서 공명이 어떻게 사용되는지 설명할 수 있다</li>"),

    # Vocabulary callout (different text in actual file)
    ("Vocabulary: Record the following vocabulary in your notebook. As you complete the\n                                learning\n                                activity\n                                fill in the definition and key terminology pertaining to the vocabulary:", "어휘: 다음 어휘를 노트에 기록하세요. 학습 활동을 완료하면서 어휘에 관련된 정의와 핵심 용어를 채워 넣으세요:"),
    ("<li>amplify </li>", "<li>증폭 </li>"),
    ("<li>resonance </li>", "<li>공명 </li>"),

    # Introduction paragraphs
    ("How can a musical instrument like a trumpet make such a loud noise when the musician barely\n                        makes\n                        a sound blowing into it?", "트럼펫 같은 악기는 음악가가 겨우 소리를 불어넣는데 어떻게 그렇게 큰 소리를 낼 수 있을까요?"),
    ("It's because the length of the tube that the trumpet is made from\n                        naturally amplifies certain frequencies of sound. These frequencies are called natural\n                        frequencies or resonant frequencies.", "이는 트럼펫을 이루는 관의 길이가 자연적으로 특정 진동수의 소리를 증폭시키기 때문입니다. 이러한 진동수를 고유 진동수 또는 공명 진동수라고 합니다."),
    ("Most objects have resonant frequencies at which they naturally vibrate. Sometimes the results\n                        of\n                        this vibration can be spectacular.", "대부분의 물체는 자연적으로 진동하는 공명 진동수를 가지고 있습니다. 때때로 이 진동의 결과는 놀라울 수 있습니다."),
    ("When an earthquake strikes, some buildings will\n                        completely\n                        collapse, while other buildings nearby will only be slightly damaged.", "지진이 발생하면 일부 건물은 완전히 무너지는 반면, 근처의 다른 건물들은 약간만 손상됩니다."),
    ("Something other than\n                        the\n                        strength of the earthquake determines how much damage occurs.", "지진의 강도 외의 다른 요인이 피해 정도를 결정합니다."),
    ("If a building has a resonant\n                        frequency that is close to the frequency of an earthquake, the building will shake\n                        dramatically\n                        during the quake and may even collapse, while nearby buildings stand firm.", "건물의 공명 진동수가 지진의 진동수에 가까우면, 지진 중 건물이 극적으로 흔들리고 무너질 수도 있는 반면, 근처 건물들은 견고하게 서 있습니다."),
    ("There are steps\n                        that\n                        can be taken to keep buildings safe from earthquakes.", "지진으로부터 건물을 안전하게 유지하기 위해 취할 수 있는 조치들이 있습니다."),
    ("What instruments can you think of? Can you describe how they vibrate to make noise?", "어떤 악기들을 떠올릴 수 있나요? 소리를 내기 위해 어떻게 진동하는지 설명할 수 있나요?"),

    # Suggested answer about instruments
    ("Examples of musical instruments are drum, violin, flute, human voice, etc.", "악기의 예로는 드럼, 바이올린, 플루트, 사람의 목소리 등이 있습니다."),
    ("What vibrates to produce sound for different musical instruments are skin of the drum,\n                            string\n                            of the violin, air in the flute, vocal chords, etc.", "다른 악기에서 소리를 내기 위해 진동하는 것은 드럼의 가죽, 바이올린의 현, 플루트의 공기, 성대 등입니다."),

    # Explore video instructions
    ("Explore the following short video of a toy used by children.", "어린이들이 사용하는 장난감에 대한 다음 짧은 영상을 탐구하세요."),
    ("What is causing the sound made by the toy?", "장난감에서 나는 소리의 원인은 무엇인가요?"),
    ("Air in the tube is vibrating at different frequencies.", "관 안의 공기가 다양한 진동수로 진동하고 있습니다."),
    ("What a person just heard is resonance in an air column. This is similar\n                        to blowing across the top\n                        of a glass or plastic bottle. It is the air that is vibrating inside the container.", "방금 들은 것은 공기 기둥에서의 공명입니다. 이것은 유리잔이나 플라스틱 병의 윗부분을 가로질러 바람을 불어넣는 것과 유사합니다. 진동하는 것은 용기 안의 공기입니다."),
    ("The concept of resonance can be used to create beautiful sounds in musical instruments as\n                        well.\n                        You will now explore how resonance is all around us.", "공명의 개념은 악기에서도 아름다운 소리를 만드는 데 사용될 수 있습니다. 이제 공명이 우리 주변에 어떻게 있는지 탐구합니다."),

    # Mechanical resonance section
    ("역학적 공명 occurs when a source of periodic vibrations causes an object to vibrate\n                        back\n                        and forth with large amplitudes of motion, through direct contact. It occurs when the\n                        frequency\n                        of the periodic force is equal to the natural frequency of the object.", "역학적 공명은 주기적 진동의 원천이 직접 접촉을 통해 물체를 큰 진폭으로 앞뒤로 진동하게 할 때 발생합니다. 주기적 힘의 진동수가 물체의 고유 진동수와 같을 때 발생합니다."),
    ("When this happens,\n                        the\n                        object begins to rock back and forth, or resonate, with very large amplitudes. The results\n                        of\n                        resonance always seem surprising, because such a small force seems to cause so much motion.\n                    ", "이 경우, 물체는 매우 큰 진폭으로 앞뒤로 흔들리거나 공명하기 시작합니다. 공명의 결과는 항상 놀랍게 보입니다. 왜냐하면 그렇게 작은 힘이 그렇게 큰 운동을 일으키는 것처럼 보이기 때문입니다.\n                    "),
    ("Small pushes of a child on a swing can cause a large amplitude of vibration (a big\n                            swinging\n                            motion) if the pushes have the same natural frequency as the swing.", "그네의 고유 진동수와 같은 진동수로 밀면, 아이를 그네에서 작게 미는 것만으로도 큰 진폭의 진동(큰 흔들림)을 일으킬 수 있습니다."),

    # Pendulum example
    ("Another simple example of resonance can be demonstrated by tying several pendula\n                                (plural\n                                for\n                                pendulum) to the same support string. The apparatus is demonstrated in the following\n                                video.", "공명의 또 다른 간단한 예는 여러 개의 진자(pendulum의 복수형)를 같은 지지 끈에 묶어서 시연할 수 있습니다. 장치는 다음 영상에서 보여줍니다."),
    ("Press here for a long\n                                    description.", "상세 설명을 보려면 여기를 누르세요."),
    ("Press here for a long description.", "상세 설명을 보려면 여기를 누르세요."),

    # Pendulum paragraphs
    ("The period of a pendulum with small amplitudes of vibration depends only on its length. In this case, the\n                        diagram demonstrates two pendula with the same length (1 and 4), and two others with different lengths (2\n                        and 3).", "작은 진폭의 진동을 하는 진자의 주기는 길이에만 의존합니다. 이 경우, 그림은 같은 길이의 두 진자(1과 4)와 다른 길이의 두 진자(2와 3)를 보여줍니다."),
    ("Give pendulum 1 a push, it will move back and forth over and over again, while the other\n                        three pendula will hardly move at all. The same will happen by giving pendulum 3 a push.\n                    ", "진자 1을 밀면, 계속해서 앞뒤로 움직이지만 나머지 세 진자는 거의 움직이지 않습니다. 진자 3을 밀어도 마찬가지입니다.\n                    "),
    ("However, giving pendulum 2 a push, something strange happens.", "그러나 진자 2를 밀면 이상한 일이 일어납니다."),
    ("Pendulums 1 and 3 will hardly move at all,\n                        but pendulum 4 will start to rock back and forth with large amplitudes after several seconds.", "진자 1과 3은 거의 움직이지 않지만, 진자 4는 몇 초 후 큰 진폭으로 앞뒤로 흔들리기 시작합니다."),
    ("When this\n                        happens, pendulum 2 will start to decrease in amplitude and eventually come to a stop. However, after a\n                        second or two, pendulum 2 will start to swing again, developing large amplitudes of vibration, while\n                        pendulum 4 starts to settle down.", "이 때 진자 2는 진폭이 줄어들기 시작하여 결국 멈춥니다. 그러나 1~2초 후, 진자 2가 다시 흔들리기 시작하여 큰 진폭의 진동을 발전시키고, 진자 4는 안정되기 시작합니다."),
    ("Note that both pendulums 2 and 4 have the same natural frequency, while the other two pendulums have\n                        different frequencies. When pendulum 2 starts to move back and forth, it causes a small periodic vibration\n                        in the horizontal string that supports all of the other pendulums. When one object vibrates in resonance\n                        with another, it is called a sympathetic vibration. The small vibrations in this string will have the same\n                        frequency as both pendulums 2 and 4,", "진자 2와 4는 같은 고유 진동수를 가지고 있고, 나머지 두 진자는 다른 진동수를 가집니다. 진자 2가 앞뒤로 움직이기 시작하면, 다른 모든 진자를 지지하는 수평 끈에 작은 주기적 진동을 일으킵니다. 한 물체가 다른 물체와 공명하여 진동할 때, 이를 공감 진동이라고 합니다. 이 끈의 작은 진동은 진자 2와 4 모두와 같은 진동수를 가지므로,"),
    ("so they can cause resonance in these two pendulums. These small\n                        vibrations in the horizontal support string don't have the same frequency as the other two, so no resonance\n                        occurs in pendulums 1 and 3.", "이 두 진자에서 공명을 일으킬 수 있습니다. 수평 지지 끈의 이 작은 진동은 나머지 두 진자와 같은 진동수를 가지지 않으므로, 진자 1과 3에서는 공명이 발생하지 않습니다."),
    # Alternative in case the "따라서 they" form still exists:
    ("따라서 they can cause resonance in these two pendulums. These small\n                        vibrations in the horizontal support string don't have the same frequency as the other two, 따라서 no resonance\n                        occurs in pendulums 1 and 3.", "이 두 진자에서 공명을 일으킬 수 있습니다. 수평 지지 끈의 이 작은 진동은 나머지 두 진자와 같은 진동수를 가지지 않으므로, 진자 1과 3에서는 공명이 발생하지 않습니다."),

    # Sympathetic vibrations
    ("<h3>Sympathetic vibrations</h3>", "<h3>공감 진동</h3>"),
    ("The previous example demonstrates the concept of sympathetic vibrations. The two pendula with the same\n                        natural frequency resonated together.", "이전 예제는 공감 진동의 개념을 보여줍니다. 같은 고유 진동수를 가진 두 진자가 함께 공명했습니다."),
    ("Play the following video to understand how sympathetic vibrations occur in tuning forks.", "다음 영상을 통해 소리굽쇠에서 공감 진동이 어떻게 발생하는지 이해하세요."),

    # Wine glass
    ("The following video demonstrates the effects of resonance. The speaker\n                        that is to the\n                        left\n                        of the wine glass has the same frequency as the natural frequency of the\n                        glass. The resonance of the glass causes it to vibrate with large amplitude and\n                        eventually\n                        break.", "다음 영상은 공명의 효과를 보여줍니다. 와인 잔 왼쪽의 스피커는 유리잔의 고유 진동수와 같은 진동수를 가지고 있습니다. 유리잔의 공명은 큰 진폭으로 진동하게 하여 결국 깨지게 합니다."),

    # Tuning fork boxes
    ("By striking the tuning fork attached to the box, it is much louder and a person can hear it clearly across\n                        a room.", "상자에 부착된 소리굽쇠를 치면 훨씬 크게 들리며 방 건너편에서도 명확하게 들을 수 있습니다."),
    ("If two tuning forks with equal frequencies are mounted on two different boxes and near each other,\n                        as identified in the first video, sympathetic vibrations can be observed.", "첫 번째 영상에서 보여준 것처럼, 같은 진동수의 두 소리굽쇠가 서로 가까운 두 다른 상자에 장착되면 공감 진동을 관찰할 수 있습니다."),
    ("If one tuning fork is struck, the\n                        other one will start to vibrate shortly afterwards and will produce a sound as well. This is a good example\n                        of resonance.", "하나의 소리굽쇠를 치면, 다른 소리굽쇠도 곧 진동하기 시작하여 소리를 냅니다. 이것은 공명의 좋은 예입니다."),
    ("The sound wave in the air from one tuning fork hits the other and starts to make it vibrate.\n                        Since they have the same frequency, the second tuning fork will also make a loud sound.", "한 소리굽쇠의 공기 중 음파가 다른 소리굽쇠에 도달하여 진동하게 합니다. 같은 진동수를 가지므로, 두 번째 소리굽쇠도 큰 소리를 냅니다."),
    ("By attaching a\n                        weight to one fork, the frequencies no longer match and we do not observe sympathetic vibrations. We can\n                        verify that the frequencies are different because, when both forks are struck, beats are heard in the tones.", "한 소리굽쇠에 무게를 달면 진동수가 더 이상 일치하지 않아 공감 진동이 관찰되지 않습니다. 두 소리굽쇠를 모두 쳤을 때 맥놀이가 들리므로 진동수가 다르다는 것을 확인할 수 있습니다."),

    # Speaker and bridge
    ("If the speaker was producing sound at a frequency different than the natural frequency of the\n                        glass, the glass would not vibrate with such a large amplitude and it would not break.", "스피커가 유리잔의 고유 진동수와 다른 진동수의 소리를 내고 있었다면, 유리잔은 그렇게 큰 진폭으로 진동하지 않았을 것이고 깨지지 않았을 것입니다."),
    ("Another dramatic example of resonance is the Tacoma Narrows bridge. Wind gusts blowing with\n                        the\n                        same frequency as the natural frequency of the bridge cause huge vibrations in the bridge,\n                        eventually causing it to collapse.", "공명의 또 다른 극적인 예는 타코마 내로스 다리입니다. 다리의 고유 진동수와 같은 진동수로 불어오는 돌풍이 다리에 거대한 진동을 일으켜 결국 붕괴시켰습니다."),
    ("The following video provides further explanation for the Tacoma Narrow bridge.", "다음 영상은 타코마 내로스 다리에 대한 추가 설명을 제공합니다."),
    ("If the wind had been blowing with a frequency that was not the same as the natural frequency\n                        of\n                        the bridge, the vibrations would not have become so large and the bridge would probably\n                        still be\n                        standing.", "바람이 다리의 고유 진동수와 같지 않은 진동수로 불고 있었다면, 진동이 그렇게 커지지 않았을 것이고 다리는 아마 아직도 서 있었을 것입니다."),

    # Car in snow
    ("Imagine that a car gets stuck in the snow. When trying to push it out, deep ruts form. How\n                        could\n                        we use resonance to help push the car out while\n                        someone else is driving?", "자동차가 눈에 빠졌다고 상상해 보세요. 밀어내려고 할 때 깊은 바퀴 자국이 형성됩니다. 다른 사람이 운전하는 동안 공명을 이용하여 어떻게 자동차를 밀어낼 수 있을까요?"),
    ("If people push the car from behind, people might be able to rock it back and forth, but\n                            people\n                            probably wouldn't be able to push it right out with one shove. When the car is rocking\n                            back\n                            and forth, people could match the frequency of the car's motion to the frequency of\n                            people's\n                            pushes. This use of resonance would increase the amplitude of the car's motion.\n                            Eventually,\n                            the car will rock back and forth enough so that the person driving is able to drive the\n                            car\n                            out of the ruts.", "사람들이 뒤에서 자동차를 밀면 앞뒤로 흔들 수 있지만, 한 번에 밀어낼 수는 없을 것입니다. 자동차가 앞뒤로 흔들릴 때, 자동차 운동의 진동수에 미는 진동수를 맞출 수 있습니다. 이런 공명의 사용은 자동차 운동의 진폭을 증가시킵니다. 결국, 자동차가 충분히 앞뒤로 흔들려서 운전하는 사람이 바퀴 자국에서 빠져나올 수 있게 됩니다."),

    # Marching soldiers
    ("Why is it dangerous for a group of marching soldiers to cross a small footbridge together,\n                        while\n                        they are marching in unison?", "행진하는 병사들이 보조를 맞추며 작은 보행교를 함께 건너는 것이 왜 위험한가요?"),
    ("If the frequency of the marching soldiers matches the natural frequency of the\n                            footbridge,\n                            the bridge could start to resonate and experience large amplitudes of vibration. These\n                            vibrations might be large enough to make the soldiers lose their footing or might even\n                            damage the bridge.", "행진하는 병사들의 진동수가 보행교의 고유 진동수와 일치하면, 다리가 공명하기 시작하여 큰 진폭의 진동을 경험할 수 있습니다. 이 진동은 병사들이 발을 헛디디게 하거나 다리를 손상시킬 만큼 클 수 있습니다."),

    # Standing waves in strings section
    ("As you may recall, standing waves in strings are produced when two identical waves travel in\n                        opposite directions in the same medium. ", "기억하시겠지만, 현에서의 정상파는 두 개의 동일한 파동이 같은 매질에서 반대 방향으로 이동할 때 만들어집니다. "),
    ("The following diagram has three", "다음 그림에는 세 개의"),
    ("Each loop has a length of half of a\n                        wavelength.", "각 루프는 파장의 절반 길이를 가집니다."),
    ("Standing waves can\n                        be formed with any number of", "정상파는 몇 개의"),
    ("Start by considering a string, anchored at both ends. This is referred to as a string with two fixed ends.", "양쪽 끝에 고정된 현을 생각해 봅시다. 이것을 양쪽 끝이 고정된 현이라고 합니다."),
    ("All stringed instruments, like guitars and violins, have strings with fixed ends.", "기타와 바이올린 같은 모든 현악기는 끝이 고정된 현을 가지고 있습니다."),
    ("Since the\n                        string is fixed at both ends, there must be", "현이 양쪽 끝에 고정되어 있으므로, 정상파가 현에 존재하더라도 이 지점들에는"),
    ("at these points, even if a standing wave\n                        is\n                        present in the string.", "가 있어야 합니다."),
    ("This means that the frequencies that produce a standing wave must make one loop, or two\n                        ", "이것은 정상파를 만드는 진동수가 하나의 루프, 또는 두 개의\n                        "),
    ("Since only certain numbers of", "특정 수의"),
    ("are possible, the wavelength can only be\n                        selected from a limited number of lengths.", "만 가능하므로, 파장은 제한된 수의 길이에서만 선택될 수 있습니다."),
    ("One wavelength corresponds to a single loop, another to two", "하나의 파장은 하나의 루프에 해당하고, 다른 것은 두 개의"),
    (", another to three", ", 또 다른 것은 세 개의"),
    ("In addition, the speed of vibration in the string is a property of\n                        the material and tension on the string,", "또한, 현에서의 진동 속력은 현의 재질과 장력의 특성이므로,"),
    ("so it is a fixed value.", "고정된 값입니다."),
    ("따라서 it is a fixed value.", "고정된 값입니다."),
    ("Considering", ""),
    ("this means that only certain frequencies can produce standing waves in a fixed string.", "고려하면, 고정된 현에서 정상파를 만들 수 있는 진동수는 특정한 것만 가능합니다."),
    ("Also, the speed of\n                        vibration does not change", "또한, 진동 속력은 변하지 않으므로"),
    ("so the number of loops determines the frequency of the standing wave.\n                        This sounds exactly like\n                        resonance!", ", 루프의 수가 정상파의 진동수를 결정합니다. 이것은 마치 공명과 같습니다!"),
    # alt version
    ("따라서 the number of loops determines the frequency of the standing wave.\n                        This sounds exactly like\n                        resonance!", ", 루프의 수가 정상파의 진동수를 결정합니다. 이것은 마치 공명과 같습니다!"),

    # String example
    ("The following example will help to clarify this concept.", "다음 예제가 이 개념을 명확히 하는 데 도움이 될 것입니다."),
    ("Consider a string of length L stretched tightly between two fixed positions.", "길이 L의 현이 두 고정 위치 사이에 팽팽하게 당겨져 있다고 생각해 봅시다."),
    ("In a\n                        stringed instrument, these would be the two ends of the string attached to the instrument.", "현악기에서 이것은 악기에 부착된 현의 양쪽 끝입니다."),
    ("Since only one loop is present, the length of the string is half of a wavelength.", "루프가 하나만 있으므로, 현의 길이는 파장의 절반입니다."),
    ("This can be rearranged to", "이것을 다시 정리하면"),

    # Table headings for string resonance
    ("Harmonic", "배음"),
    ("Diagram", "그림"),
    ("Number of loops", "루프 수"),

    # Additional standalone text patterns
    ("Therefore,", "따라서,"),
    ("therefore,", "따라서,"),
]

for eng, kor in REPLACEMENTS:
    content = content.replace(eng, kor)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Phase 2 done. Checking remaining English...")

# Verify
import re
clean = re.sub(r'<math.*?</math>', '', content, flags=re.DOTALL)
clean = re.sub(r'<script.*?</script>', '', clean, flags=re.DOTALL)
clean = re.sub(r'<style.*?</style>', '', clean, flags=re.DOTALL)
clean = re.sub(r'<!--.*?-->', '', clean, flags=re.DOTALL)
clean = re.sub(r'<[^>]+>', ' ', clean)
english_phrases = re.findall(r'[A-Z][a-z]+(?:\s+[a-zA-Z]+){2,}', clean)
seen = set()
for p in english_phrases:
    if len(p) > 20 and p not in seen:
        seen.add(p)
        print(f'  REMAINING: {repr(p)}')
