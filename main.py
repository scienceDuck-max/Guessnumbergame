import random
#정답 숫자 생성 3개 : 1~9사이 모두 다를 것

answer=[0,0,0]

answer[0] = random.randint(1,9)
answer[1] = random.randint(1,9)
while(answer[0]==answer[1]):
  answer[1]=random.randint(1,9)


answer[2 ]= random.randint(1,9)

while(answer[2]==answer[0] or answer[2]==answer[1]):
  answer[2]=random.randint(1,9)



#생성된 숫자 print
#print(answer[0],answer[1], answer[2])

while(True):
    
  userinput = input("3개의 서로 다른 숫자를 입력하세요:")
  print(userinput)

  userAnswer = [0,0,0]

  userAnswer [0] = int(userinput[0])
  userAnswer [1] = int(userinput[1])
  userAnswer [2] = int(userinput[2])

  #strike

  strikeCount=0
  ballCount=0
  outCount=0

  if(answer[0]==userAnswer[0]):
    strikeCount=strikeCount+1
  elif(answer[1]==userAnswer[0] or answer[2]==userAnswer[0]):
    ballCount = ballCount+1
  else:
    outCount=outCount+1


  if(answer[1]==userAnswer[1]):
    strikeCount=strikeCount+1
  elif(answer[2]==userAnswer[1] or answer[0]==userAnswer[1]):
    ballCount = ballCount+1
  else:
    outCount=outCount+1

  if(answer[2]==userAnswer[2]):
    strikeCount=strikeCount+1
  elif(answer[0]==userAnswer[2] or answer[1]==userAnswer[2]):
    ballCount = ballCount+1
  else:
    outCount=outCount+1

  print(outCount, "Out") 
  print(ballCount, "Ball")
  print(strikeCount, "STRIKE!")
  if(strikeCount ==3):
    print("이겼습니다!")
    break
  else:
    print("땡! 다시 한 번 도전해보세요!")