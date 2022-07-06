#딕션너리 만들기
lux={'health':490,'mana':334,'melee':550,'armor':18.72} #딕셔너리는 해시기법을 이용하여 데이터를 저장한다딕셔너리와 같은 키-값 형태의 자료형을 해시,해시맵,해시테이블 등으로 부른다.
print(lux) #키 이름이 중복되면 딕션너리에서 마지막 키의 값을 사용한다.
print('1--------------------')

#딕션너리 키의 자료형
x={100:'hundred',False:0,3.5:[3.5,3.5]}
print(x)
print('2--------------------') #키에는 리스트와 딕션너리를 사용할 수 없다.

#빈 딕션너리 만들기
x={}
print(x)
y=dict()
print(y)
print('3--------------------')

#dict로 딕션너리 만들기
lux1=dict(health=490,mama=334,melee=550,armor=18.72) #키=값
print(lux1)
lux2=dict(zip(['health','mana','melee','armor'],[490,334,550,18.72])) #zip(키 리스트, 값 리스트)
print(lux2)
print('4--------------------')
lux3=dict([('health',490),('mana',334),('melee',550),('armor',18.72)]) #(키,값)의 튜플형식
print(lux3)
lux4=dict({'health':490,'mana':334,'melee':550,'armor':18.72}) #dict 안에 {}로 만듦
print(lux4)
print('4--------------------')

#딕션너리의 키에 접근하고 값 할당하기
lux={'health':490,'mana':334,'melee':550,'armor':18.72}
print(lux['health'])
print(lux['armor'])
lux['health']=2037
lux['mana']=1184
print(lux)
lux['mana_regen']=3.28
print(lux)
print('5--------------------')

#딕셔너리에서 키가 있는지 확인하기
lux={'health':490,'mana':334,'melee':550,'armor':18.72}
print('health' in lux)
print('attack_speed' in lux)
print('health' not in lux)
print('5--------------------')

#틱셔너리의 키 개수 구하기
lux={'health':490,'mana':334,'melee':550,'armor':18.72}
print(len(lux))
print(len({'health':490,'mana':334,'melee':550,'armor':18.72}))
print('6--------------------')

#연습문제
camile={
    'health':575.6,
    'health_ragen':1.7,
    'mana':338.8,
    'mana_regan':1.63,
    'melee':125,
    'attack_damage':60,
    'attack_speed':0.625,
    'armor':26,
    'magic_resistance':32.1,
    'movement_speed':340
}

print(camile['health'])
print(camile['movement_speed'])
print('7--------------------')

#심사문제
st_name=input().split()
num=list(map(int,input().split())) #map(int,input().split())을 리스트 자료형으로 변환없이 사용시 
if len(st_name) == len(num):
    st=dict(zip(st_name,num))
print(st)