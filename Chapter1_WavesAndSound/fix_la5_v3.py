#!/usr/bin/env python3
"""Line-by-line English->Korean replacement for remaining text in la5."""

filepath = 'course_content/lessons/sph3u_u1la5.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line-level replacements: (English fragment, Korean replacement)
# These match substrings within individual lines
R = [
    # Remaining intro text
    ("These frequencies are called natural", "이러한 진동수를 고유"),
    ("frequencies or resonant frequencies.", "진동수 또는 공명 진동수라고 합니다."),
    ("These small", "이 작은"),
    ("vibrations in the horizontal support string don't have the same frequency as the other two,", "수평 지지 끈의 진동은 나머지 두 진자와 같은 진동수를 가지지 않으므로,"),
    ("If people push the car from behind, people might be able to rock it back and forth, but", "사람들이 뒤에서 자동차를 밀면 앞뒤로 흔들 수 있지만,"),
    ("people", "사람들은"),
    # Actually, let's be more careful. Let me handle this differently.

    # Standing wave text
    ("Each loop has a length of half of a", "각 루프는 파장의 절반"),
    ("wavelength.", "길이를 가집니다."),
    ("This sounds exactly like", "이것은 마치"),
    ("resonance!", "공명과 같습니다!"),

    # String instrument paragraph
    ("In a", ""),
    ("stringed instrument, the source would be a bow or it could be a person's fingers.", "현악기에서 소스는 활이거나 사람의 손가락일 수 있습니다."),

    ("Since only one loop is present,", "루프가 하나만 있으므로,"),
    ("This is called the fundamental frequency.", "이것을 기본 진동수라고 합니다."),
    ("It is the lowest frequency that will produce a standing wave in the string.", "이것은 현에서 정상파를 만들 수 있는 가장 낮은 진동수입니다."),
    ("If the frequency is increased,", "진동수를 증가시키면,"),
    ("the string will not produce a standing wave until the frequency is high enough that two", "진동수가 충분히 높아져 두 개의"),
    ("If the frequency", "진동수를"),
    ("continues to increase, eventually another standing wave with three", "계속 증가시키면, 결국 세 개의"),
    ("will form.", "을 가진 또 다른 정상파가 형성됩니다."),
    ("The frequency that causes a standing wave with two", "두 개의"),
    ("is called the second harmonic.", "를 가진 정상파를 만드는 진동수를 제2배음이라고 합니다."),
    ("Since it is the same string,", "같은 현이므로,"),
    ("Given the length of the string and the speed of the wave,", "현의 길이와 파동의 속력이 주어지면,"),
    ("This is the second smallest", "이것은 현에서 정상파를"),
    ("frequency that will create a standing wave in the string.", "만드는 두 번째로 작은 진동수입니다."),
    ("Compare the two equations side by side:", "두 공식을 나란히 비교하면:"),
    ("Compare the two equations side by side", "두 공식을 나란히 비교하면"),
    ("This demonstrates that the frequency that produces two", "이것은 두 개의"),
    ("is exactly twice the fundamental frequency.", "를 만드는 진동수가 기본 진동수의 정확히 두 배임을 보여줍니다."),
    ("Continuing to increase the frequency from", "에서 진동수를 계속 증가시키면,"),
    ("Resonance will not take place again until the frequency increases to", "진동수가"),
    ("where three", "로 증가하여 세 개의"),
    ("are formed.", "이 형성될 때까지 공명이 다시 일어나지 않습니다."),
    ("This trend is illustrated in the following", "이 경향은 다음"),
    ("table.", "표에 나타나 있습니다."),
    ("In general, the frequency", "일반적으로, 진동수"),
    ("that", "는"),
    ("produces", "을(를) 만들며"),

    # GUESS headings (handle various forms)
    ("State the information given, including the usual variable names.", "일반적인 변수 이름을 포함하여 주어진 정보를 적으세요."),
    ("State the information given.", "주어진 정보를 적으세요."),
    ("State the variable you want to find.", "구하려는 변수를 적으세요."),
    ("Select an equation that includes the unknown and given values that could lead to a solution.", "미지수와 주어진 값을 포함하는 공식을 선택하세요."),
    ("Substitute into the equation and solve for the desired value.", "공식에 대입하고 원하는 값을 구하세요."),
    ("Explain any work that isn't obvious, and write a sentence restating the answer to the original question. Include significant digits and units.", "명확하지 않은 풀이를 설명하고, 원래 질문에 대한 답을 다시 문장으로 작성하세요. 유효 숫자와 단위를 포함하세요."),
    ("Explain any work that isn't obvious,", "명확하지 않은 풀이를 설명하고,"),
    ("and write a sentence restating the answer to the original question.", "원래 질문에 대한 답을 다시 문장으로 작성하세요."),
    ("Include significant digits and units.", "유효 숫자와 단위를 포함하세요."),

    # Problem texts
    ("1. What is the speed of the waves in the string?", "1. 현에서의 파동의 속력은 얼마인가요?"),
    ("What is the speed of the waves in the string?", "현에서의 파동의 속력은 얼마인가요?"),
    ("The wave travels the full length of the string in the time period.", "파동은 주기 동안 현의 전체 길이를 이동합니다."),
    ("Use your knowledge about standing waves to work through the following example in your", "정상파에 대한 지식을 사용하여 다음 예제를"),
    ("notebook. Compare your work with the suggested answers to check your understanding.", "노트에 풀어 보세요. 풀이 예시와 비교하여 이해도를 확인하세요."),
    ("notebook.", "노트에 풀어 보세요."),
    ("Compare your work with the suggested answers to check your understanding.", "풀이 예시와 비교하여 이해도를 확인하세요."),

    # Note that when you use
    ("Note that when you use a previously-calculated value for another", "이전에 계산한 값을 다른"),
    ("question, you use all available digits, not just the final statement", "문제에 사용할 때는, 유효 숫자로 반올림한 최종 결론이 아닌"),
    ("that was rounded due to significant digits.", "모든 자릿수를 사용한다는 점에 유의하세요."),

    # Either equation
    ("Either equation would be appropriate, but if you used the one with L you should include L in", "두 공식 모두 적절하지만, L이 포함된 공식을 사용했다면"),
    ("the list of given values.", "주어진 값 목록에 L을 포함해야 합니다."),
    ("This problem can be solved multiple ways.", "이 문제는 여러 방법으로 풀 수 있습니다."),
    ("This suggested answer provides", "이 풀이 예시는"),
    ("just one way.", "한 가지 방법만 제시합니다."),
    ("If you used another way, compare your final answer and ensure that the work is", "다른 방법을 사용했다면, 최종 답을 비교하고 풀이가"),
    ("reasonable.", "합리적인지 확인하세요."),
    ("Either way is acceptable.", "어느 방법이든 허용됩니다."),
    ("by rearranging the universal wave equation.", "파동의 기본 방정식을 변형하여."),

    # Problem 4 string
    ("Find the frequency that will produce a standing wave with 3", "3개의 루프를 가진 정상파를 만드는 진동수를 구하세요"),
    ("The frequency with three", "세 개의"),
    ("is called", "를 가진 진동수를"),
    ("We could instead have referred back to the length", "대신 현의 길이를 참고할 수도"),
    ("of the string, and let", "있고,"),
    ("This suggested answer uses the given equation, but other solutions are possible and also", "이 풀이 예시는 주어진 공식을 사용하지만, 다른 풀이도 가능하고"),
    ("valid.", "유효합니다."),
    ("The frequency that creates a standing wave with three", "세 개의 루프를 가진 정상파를 만드는 진동수는"),

    # Problem 5 string
    ("Identify another frequency that will produce a standing wave in the string.", "현에서 정상파를 만드는 다른 진동수를 구하세요."),
    ("How many loops will it have?", "몇 개의 루프를 가지나요?"),
    ("With reference to", "를 참고하여"),
    (", we also want to know", ", 또한 알아야 하는 것은"),
    ("which is the subscript, which we named n.", "아래 첨자인 n입니다."),
    ("There are two unknowns in this question, so we put them both here.", "이 문제에는 미지수가 두 개이므로 둘 다 여기에 적습니다."),
    ("(from the table before this section)", "(이 단원 앞의 표 참조)"),
    ("Any number could be chosen.", "아무 수나 선택할 수 있습니다."),
    ("2 is a good choice, but this could just as easily have been 4, or 5, and so on.", "2가 좋은 선택이지만, 4, 5 등도 마찬가지로 가능합니다."),
    ("Another frequency that will produce a standing wave is", "정상파를 만드는 다른 진동수는"),
    ("which will have 2 loops.", "이며, 2개의 루프를 가집니다."),
    ("Hz must be reported in scientific notation since it", "Hz는 유효 숫자가"),
    ("has 2 significant digits", "2자리이고"),
    ("only has 1.", "은 1자리뿐이므로, 과학적 표기법으로 나타내야 합니다."),

    # Problem 6 string
    ("You certainly could use it, but it can be answered in words instead.", "물론 사용할 수 있지만, 말로 답할 수도 있습니다."),
    ("In some other strings, other fundamental frequencies are possible.", "다른 현에서는 다른 기본 진동수가 가능합니다."),
    ("But in this string, the only frequencies that create standing waves are multiples of 5.0 Hz.", "하지만 이 현에서는 5.0 Hz의 배수인 진동수만 정상파를 만들 수 있습니다."),

    # Air column guitar text
    ("Plucking a tight string does not produce a very loud noise.", "팽팽한 현을 뜯으면 그다지 큰 소리가 나지 않습니다."),
    ("A guitar uses a tight string that is mounted over what is essentially a wooden box", "기타는 본질적으로 나무 상자인 것 위에 팽팽한 현을 장착하여 사용합니다"),
    ("a box of air.", "— 공기 상자입니다."),
    ("The result is a loud sound.", "그 결과 큰 소리가 납니다."),
    ("As you will learn, a box of air can use resonance to increase the volume of a quiet string into something that can be heard throughout a room.", "배우게 되겠지만, 공기 상자는 공명을 이용하여 조용한 현의 소리를 방 전체에 들릴 수 있을 만큼 증폭시킬 수 있습니다."),
    ("Most tuning forks are not very loud when struck.", "대부분의 소리굽쇠는 쳤을 때 그다지 크지 않습니다."),
    ("Sometimes, to help increase the volume, they are mounted on top of wooden boxes that are open at one end, as shown in the following diagram.", "때때로 소리를 키우기 위해, 다음 그림과 같이 한쪽 끝이 열린 나무 상자 위에 장착합니다."),
    ("A vibrating tuning fork will make a nearby tuning fork vibrate sympathetically", "진동하는 소리굽쇠는 근처의 소리굽쇠를 공감 진동시킵니다"),
    ("You have encountered this apparatus before.", "이 장치는 이전에 접한 적이 있습니다."),
    ("This apparatus is the same as the one demonstrated in the video about sympathetic vibrations occurring in tuning forks.", "이 장치는 소리굽쇠에서 발생하는 공감 진동에 대한 영상에서 시연된 것과 동일합니다."),
    ("Musician playing an acoustic guitar", "어쿠스틱 기타를 연주하는 음악가"),

    # Remaining misc
    ("If the speaker was producing sound at a frequency different than the natural frequency of the", "스피커가 유리잔의 고유 진동수와 다른 진동수의 소리를 내고 있었다면,"),
    ("glass, the glass would not vibrate with such a large amplitude and it would not break.", "유리잔은 그렇게 큰 진폭으로 진동하지 않았을 것이고 깨지지 않았을 것입니다."),

    # Set up lab
    ("Set up of air column lab", "공기 기둥 실험 장치 설치"),

    # Image alt descriptions that should be translated
    ("Diagram of first resonant wave length of 0.25", "첫 번째 공명 파장 0.25 그림"),
    ("Diagram of second resonant wave length of 0.75", "두 번째 공명 파장 0.75 그림"),
    ("Diagram of first resonant wave length of 0.5", "첫 번째 공명 파장 0.5 그림"),
    ("Diagram of second resonant wave length of 1", "두 번째 공명 파장 1 그림"),
    ("Diagram of third resonant wave length of 1.5", "세 번째 공명 파장 1.5 그림"),
    ("wave diagram with wavelength of", "파장이"),

    # Remaining suggested answer labels
    ("Suggested Answer", "풀이 예시"),
    ("Show Suggested Answer", "풀이 보기"),

    # Remaining Given/Unknown/etc
    ("Given:", "주어진 값:"),
    ("Unknown:", "구하는 값:"),
    ("Equation:", "공식:"),
    ("Solve:", "풀이:"),
    ("Statement:", "결론:"),
    ("Hint", "힌트"),
    ("Another 힌트", "추가 힌트"),
    ("Example", "예제"),
    ("Summary", "요약"),
    ("Try it!", "풀어 보세요!"),
    ("Review", "복습"),
    ("Length", "길이"),
    ("Number of loops in standing wave", "정상파의 루프 수"),
    ("Diagram of standing wave", "정상파 그림"),
    ("and so on.", "등등."),

    # Remaining from first round
    ("Therefore,", "따라서,"),
    ("therefore,", "따라서,"),

    # Fix "따라서 " at start of remaining English
    ("따라서 the", "따라서"),
    ("따라서 it", "따라서 그것"),
    ("따라서 they", "따라서 그들"),
    ("따라서 no", "따라서 아무"),
]

# Apply line-by-line
for i, line in enumerate(lines):
    for eng, kor in R:
        if eng in line:
            line = line.replace(eng, kor, 1)
    lines[i] = line

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(lines)

# Count remaining
import re
content = ''.join(lines)
clean = re.sub(r'<math.*?</math>', '', content, flags=re.DOTALL)
clean = re.sub(r'<script.*?</script>', '', clean, flags=re.DOTALL)
clean = re.sub(r'<style.*?</style>', '', clean, flags=re.DOTALL)
clean = re.sub(r'<!--.*?-->', '', clean, flags=re.DOTALL)
clean = re.sub(r'<[^>]+>', ' ', clean)
english = re.findall(r'[A-Z][a-z]+(?:\s+[a-zA-Z\',\-]+){3,}', clean)
seen = set()
count = 0
for p in english:
    if len(p) > 25 and p not in seen:
        seen.add(p)
        count += 1
print(f'Remaining English phrases (>25 chars): {count}')
