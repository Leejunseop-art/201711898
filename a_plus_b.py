fruits = {
    '사과': 1000,
    '바나나': 2000,
    '자두': 500,
    '복숭아': 4000,
}
key = input("어떤 과일을 찾으세요? ")

if key in fruits:
    value = fruits[key]
    print(f"{key}는 {value}원입죠~.")
else:
    print(f"아이고, {key}는 매장에 없네요.")