import random
import time
import sqlite3
import winsound#소리 저장
import datetime 


#DB
conn = sqlite3.connect('C:/Users/ttony/Desktop/sqllite/SQLiteDatabaseBrowserPortable/Score.db', isolation_level=None)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cnt INTEGER, record text, regdate text)")

#now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
words = []
n = 1 #게임 시도 회숫
cnt = 0 #정답 횟수 
with open('C:/Users/ttony/Desktop/python/resource/word.txt', 'r')as f:
    for c in f:
        words.append(c.strip())
#print(words)
input("Ready? Press Enter")

start = time.time()
while (n <= 5):
    random.shuffle(words)
    q = random.choice(words)

    print()
    print('Question # {}'.format(n))
    print(q)

    x = input()
    print()

    if str(q).strip() == str(x).strip():
        print('Correct!')
        winsound.PlaySound('C:/Users/ttony/Desktop/python/sound/good.wav', winsound.SND_FILENAME)
        cnt += 1
    else:
        print('Worng!')
        winsound.PlaySound('C:/Users/ttony/Desktop/python/sound/bad.wav', winsound.SND_FILENAME)
    n += 1

end = time.time()
PlayTime = end - start
PlayTime = format(PlayTime, ".3f")

if cnt >= 4:
    print('합격')
else:
    print('불합격')

cur.execute('INSERT INTO records("cnt", "record", "regdate") VALUES (?, ?, ?)', (cnt, PlayTime, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),))

conn.close()
print("게임 시간 : ", PlayTime, '초', "정답 개수 : {}".format(cnt))

#시작지점
if __name__ == '__main__':
    pass