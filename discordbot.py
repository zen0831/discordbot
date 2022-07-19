import discord
import random

client = discord.Client()
start = flag = name=0

@client.event
async def on_ready():
    print("ready　" + client.user.name)

@client.event
async def on_message(message):
    if message.author != client.user:
        global start,name,flag,xy11,xy21,xy31,xy12,xy22,xy32,xy13,xy23,xy33,senkou,kr,s,k
        if message.content == "/ox" and start == 0:#ゲーム開始
            start = flag =1
            await client.send_message(message.channel, message.author.mention +"さんが◯ｘゲームを開始しました。")
            name = message.author.name
            xy11,xy21,xy31,xy12,xy22,xy32,xy13,xy23,xy33="１","２","３","４","５","６","７","８","９"
            print(message.author.name + "がゲームを開始しました。")
            senkou = random.randint(0,1)#先攻後攻決め

            if senkou == 0 and flag ==1:
                flag=2
                print("プレイヤーが先攻")
                await client.send_message(message.channel, message.author.mention +"は先攻です")
                await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
                await client.send_message(message.channel, message.author.mention +"さん1~9を選択してください。")
                print("＃"+ xy11+ "＃"+ xy21+ "＃"+ xy31 + "＃\r\n＃"+ xy12+ "＃"+ xy22+ "＃"+ xy32+ "＃\r\n＃"+xy13 + "＃"+ xy23+ "＃"+ xy33+ "＃")
            if senkou == 1 and flag==1:
                print("プレイヤーが後攻")
                cpu=random.randint(1,9)
                if cpu == 1: xy11 ="◯"
                if cpu == 2: xy21 ="◯"
                if cpu == 3: xy31 ="◯"
                if cpu == 4: xy12 ="◯"
                if cpu == 5: xy22 ="◯"
                if cpu == 6: xy32 ="◯"
                if cpu == 7: xy13 ="◯"
                if cpu == 8: xy23 ="◯"
                if cpu == 9: xy33 ="◯"
                cpu,flag= 0,2
                await client.send_message(message.channel, message.author.mention +"は後攻です")
                await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
                await client.send_message(message.channel, message.author.mention +"さん1~9を選択してください。")
                print("＃"+ xy11+ "＃"+ xy21+ "＃"+ xy31 + "＃\r\n＃"+ xy12+ "＃"+ xy22+ "＃"+ xy32+ "＃\r\n＃"+xy13 + "＃"+ xy23+ "＃"+ xy33+ "＃")

        #プレイヤーマス選択
        if message.content == "1" and name==message.author.name and flag==2 and xy11=="１":
            flag=3
            print("1に設置")
            if senkou==0: xy11="◯"
            if senkou==1: xy11="ｘ"
        if message.content == "1" and name==message.author.name and flag==2 and xy11!="１":
            await client.send_message(message.channel, "そこには置けません。")
            await client.delete_message(message)
        if message.content == "2" and name==message.author.name and flag==2 and xy21=="２":
            flag=3
            print("2に設置")
            if senkou==0: xy21="◯"
            if senkou==1: xy21="ｘ"
        if message.content == "2" and name==message.author.name and flag==2 and xy21!="２":
            await client.send_message(message.channel, "そこには置けません。")
            await client.delete_message(message)
        if message.content == "3" and name==message.author.name and flag==2 and xy31=="３":
            flag=3
            print("3に設置")
            if senkou==0: xy31="◯"
            if senkou==1: xy31="ｘ"
        if message.content == "3" and name==message.author.name and flag==2 and xy31!="３":
            await client.send_message(message.channel, "そこには置けません。")
            await client.delete_message(message)
        if message.content == "4" and name==message.author.name and flag==2 and xy12=="４":
            flag=3
            print("4に設置")
            if senkou==0: xy12="◯"
            if senkou==1: xy12="ｘ"
        if message.content == "4" and name==message.author.name and flag==2 and xy12!="４":
            await client.send_message(message.channel, "そこには置けません。")
            await client.delete_message(message)
        if message.content == "5" and name==message.author.name and flag==2 and xy22=="５":
            flag=3
            print("5に設置")
            if senkou==0: xy22="◯"
            if senkou==1: xy22="ｘ"
        if message.content == "5" and name==message.author.name and flag==2 and xy22!="５":
            await client.send_message(message.channel, "そこには置けません。")
            await client.delete_message(message)
        if message.content == "6" and name==message.author.name and flag==2 and xy32=="６":
            flag=3
            print("6に設置")
            if senkou==0: xy32="◯"
            if senkou==1: xy32="ｘ"
        if message.content == "6" and name==message.author.name and flag==2 and xy32!="６":
            await client.send_message(message.channel, "そこには置けません。")
            await client.delete_message(message)
        if message.content == "7" and name==message.author.name and flag==2 and xy13=="７":
            flag=3
            print("7に設置")
            if senkou==0: xy13="◯"
            if senkou==1: xy13="ｘ"
        if message.content == "7" and name==message.author.name and flag==2 and xy13!="７":
            await client.send_message(message.channel, "そこには置けません。")
            await client.delete_message(message)
        if message.content == "8" and name==message.author.name and flag==2 and xy23=="８":
            flag=3
            print("8に設置")
            if senkou==0: xy23="◯"
            if senkou==1: xy23="ｘ"
        if message.content == "8" and name==message.author.name and flag==2 and xy23!="８":
            await client.send_message(message.channel, "そこには置けません。")
            await client.delete_message(message)
        if message.content == "9" and name==message.author.name and flag==2 and xy33=="９":
            print("9に設置")
            flag=3
            if senkou==0: xy33="◯"
            if senkou==1: xy33="ｘ"
        if message.content == "9" and name==message.author.name and flag==2 and xy33!="９":
            await client.send_message(message.channel, "そこには置けません。")
            await client.delete_message(message)

        #CPU
        if flag==2:
            kr=0
        while (1):
            if flag!=3: break
            if flag==3:#◯◯やｘｘが見つかった場合となりに置く
                if xy11!="１" and xy12!="４" and xy13!="７" and xy21!="２" and xy22!="５" and xy23!="８" and xy31!="３"  and xy32!="６" and xy33!="９": break
                print("CPUのターン")
                if xy11=="◯":
                    if xy21=="◯" and xy31=="３":
                        flag=4
                        if senkou==1:
                            xy31="◯"
                            break
                        if senkou==0:
                            xy31="ｘ"
                            break
                    if xy31=="◯" and xy21=="２":
                        flag=4
                        if senkou==1:
                            xy21="◯"
                            break
                        if senkou==0:
                            xy21="ｘ"
                            break
                    if xy12=="◯" and xy13=="７":
                        flag=4
                        if senkou==1:
                            xy13="◯"
                            break
                        if senkou==0:
                            xy13="ｘ"
                            break
                    if xy13=="◯" and xy12=="４":
                        flag=4
                        if senkou==1:
                            xy12="◯"
                            break
                        if senkou==0:
                            xy12="ｘ"
                            break
                    if xy22=="◯" and xy33=="９":
                        flag=4
                        if senkou==1:
                            xy33="◯"
                            break
                        if senkou==0:
                            xy33="ｘ"
                            break
                    if xy33=="◯" and xy22=="５":
                        flag=4
                        if senkou==1:
                            xy22="◯"
                            break
                        if senkou==0:
                            xy22="ｘ"
                            break
                if xy11=="ｘ":
                    if xy21=="ｘ" and xy31=="３":
                        flag=4
                        if senkou==1:
                            xy31="◯"
                            break
                        if senkou==0:
                            xy31="ｘ"
                            break
                    if xy31=="ｘ" and xy21=="２":
                        flag=4
                        if senkou==1:
                            xy21="◯"
                            break
                        if senkou==0:
                            xy21="ｘ"
                            break
                    if xy12=="ｘ" and xy13=="７":
                        flag=4
                        if senkou==1:
                            xy13="◯"
                            break
                        if senkou==0:
                            xy13="ｘ"
                            break
                    if xy13=="ｘ" and xy12=="４":
                        flag=4
                        if senkou==1:
                            xy12="◯"
                            break
                        if senkou==0:
                            xy12="ｘ"
                            break
                    if xy22=="ｘ" and xy33=="９":
                        flag=4
                        if senkou==1:
                            xy33="◯"
                            break
                        if senkou==0:
                            xy33="ｘ"
                            break
                    if xy33=="ｘ" and xy22=="５":
                        flag=4
                        if senkou==1:
                            xy22="◯"
                            break
                        if senkou==0:
                            xy22="ｘ"
                            break

                if xy21=="◯":
                    if xy31=="◯" and xy11=="１":
                        flag=4
                        if senkou==1:
                            xy11="◯"
                            break
                        if senkou==0:
                            xy11="ｘ"
                            break
                    if xy22=="◯" and xy23=="８":
                        flag=4
                        if senkou==1:
                            xy23="◯"
                            break
                        if senkou==0:
                            xy23="ｘ"
                            break
                    if xy23=="◯" and xy22=="５":
                        flag=4
                        if senkou==1:
                            xy22="◯"
                            break
                        if senkou==0:
                            xy22="ｘ"
                            break
                if xy21=="ｘ":
                    if xy31=="ｘ" and xy11=="１":
                        flag=4
                        if senkou==1:
                            xy11="◯"
                            break
                        if senkou==0:
                            xy11="ｘ"
                            break
                    if xy22=="ｘ" and xy23=="８":
                        flag=4
                        if senkou==1:
                            xy23="◯"
                            break
                        if senkou==0:
                            xy23="ｘ"
                            break
                    if xy23=="ｘ" and xy22=="５":
                        flag=4
                        if senkou==1:
                            xy22="◯"
                            break
                        if senkou==0:
                            xy22="ｘ"
                            break

                if xy12=="◯":
                    if xy13=="◯" and xy11=="１":
                        flag=4
                        if senkou==1:
                            xy11="◯"
                            break
                        if senkou==0:
                            xy11="ｘ"
                            break
                    if xy22=="◯" and xy32=="６":
                        flag=4
                        if senkou==1:
                            xy32="◯"
                            break
                        if senkou==0:
                            xy32="ｘ"
                            break
                    if xy32=="◯" and xy22=="５":
                        flag=4
                        if senkou==1:
                            xy22="◯"
                            break
                        if senkou==0:
                            xy22="ｘ"
                            break
                if xy12=="ｘ":
                    if xy13=="ｘ" and xy11=="１":
                        flag=4
                        if senkou==1:
                            xy11="◯"
                            break
                        if senkou==0:
                            xy11="ｘ"
                            break
                    if xy22=="ｘ" and xy32=="６":
                        flag=4
                        if senkou==1:
                            xy32="◯"
                            break
                        if senkou==0:
                            xy32="ｘ"
                            break
                    if xy32=="ｘ" and xy22=="５":
                        flag=4
                        if senkou==1:
                            xy22="◯"
                            break
                        if senkou==0:
                            xy22="ｘ"
                            break

                if xy31=="◯":
                    if xy32=="◯" and xy33=="９":
                        flag=4
                        if senkou==1:
                            xy33="◯"
                            break
                        if senkou==0:
                            xy33="ｘ"
                            break
                    if xy33=="◯" and xy32=="６":
                        flag=4
                        if senkou==1:
                            xy32="◯"
                            break
                        if senkou==0:
                            xy32="ｘ"
                            break
                    if xy22=="◯" and xy13=="７":
                        flag=4
                        if senkou==1:
                            xy13="◯"
                            break
                        if senkou==0:
                            xy13="ｘ"
                            break
                    if xy13=="◯" and xy22=="５":
                        flag=4
                        if senkou==1:
                            xy22="◯"
                            break
                        if senkou==0:
                            xy22="ｘ"
                            break
                if xy31=="ｘ":
                    if xy32=="ｘ" and xy33=="９":
                        flag=4
                        if senkou==1:
                            xy33="◯"
                            break
                        if senkou==0:
                            xy33="ｘ"
                            break
                    if xy33=="ｘ" and xy32=="６":
                        flag=4
                        if senkou==1:
                            xy32="◯"
                            break
                        if senkou==0:
                            xy32="ｘ"
                            break
                    if xy22=="ｘ" and xy13=="７":
                        flag=4
                        if senkou==1:
                            xy13="◯"
                            break
                        if senkou==0:
                            xy13="ｘ"
                            break
                    if xy13=="ｘ" and xy22=="５":
                        flag=4
                        if senkou==1:
                            xy22="◯"
                            break
                        if senkou==0:
                            xy22="ｘ"
                            break

                if xy22=="◯":
                    if xy23=="◯" and xy21=="２":
                        flag=4
                        if senkou==1:
                            xy21="◯"
                            break
                        if senkou==0:
                            xy21="ｘ"
                            break
                    if xy13=="◯" and xy31=="３":
                        flag=4
                        if senkou==1:
                            xy31="◯"
                            break
                        if senkou==0:
                            xy31="ｘ"
                            break
                    if xy33=="◯" and xy11=="１":
                        flag=4
                        if senkou==1:
                            xy11="◯"
                            break
                        if senkou==0:
                            xy11="ｘ"
                            break
                    if xy32=="◯" and xy12=="４":
                        flag=4
                        if senkou==1:
                            xy12="◯"
                            break
                        if senkou==0:
                            xy12="ｘ"
                            break
                if xy22=="ｘ":
                    if xy23=="ｘ" and xy21=="２":
                        flag=4
                        if senkou==1:
                            xy21="◯"
                            break
                        if senkou==0:
                            xy21="ｘ"
                            break
                    if xy13=="ｘ" and xy31=="３":
                        flag=4
                        if senkou==1:
                            xy31="◯"
                            break
                        if senkou==0:
                            xy31="ｘ"
                            break
                    if xy33=="ｘ" and xy11=="１":
                        flag=4
                        if senkou==1:
                            xy11="◯"
                            break
                        if senkou==0:
                            xy11="ｘ"
                            break
                    if xy32=="ｘ" and xy12=="４":
                        flag=4
                        if senkou==1:
                            xy12="◯"
                            break
                        if senkou==0:
                            xy12="ｘ"
                            break

                if xy32=="◯":
                    if xy33=="◯" and xy31=="３":
                        flag=4
                        if senkou==1:
                            xy31="◯"
                            break
                        if senkou==0:
                            xy31="ｘ"
                            break
                if xy32=="ｘ":
                    if xy33=="ｘ" and xy31=="３":
                        flag=4
                        if senkou==1:
                            xy31="◯"
                            break
                        if senkou==0:
                            xy31="ｘ"
                            break

                if xy13=="◯":
                    if xy23=="◯" and xy33=="９":
                        flag=4
                        if senkou==1:
                            xy33="◯"
                            break
                        if senkou==0:
                            xy33="ｘ"
                            break
                    if xy33=="◯" and xy23=="８":
                        flag=4
                        if senkou==1:
                            xy23="◯"
                            break
                        if senkou==0:
                            xy23="ｘ"
                            break
                if xy13=="ｘ":
                    if xy23=="ｘ" and xy33=="９":
                        flag=4
                        if senkou==1:
                            xy33="◯"
                            break
                        if senkou==0:
                            xy33="ｘ"
                            break
                    if xy33=="ｘ" and xy23=="８":
                        flag=4
                        if senkou==1:
                            xy23="◯"
                            break
                        if senkou==0:
                            xy23="ｘ"
                            break

                if xy23=="◯":
                    if xy33=="◯" and xy13=="７":
                        flag=4
                        if senkou==1:
                            xy13="◯"
                            break
                        if senkou==0:
                            xy13="ｘ"
                            break
                if xy23=="ｘ":
                    if xy33=="ｘ" and xy13=="７":
                        flag=4
                        if senkou==1:
                            xy13="◯"
                            break
                        if senkou==0:
                            xy13="ｘ"
                            break

                cpu=random.randint(1,9)#連続するものが見つからなかった場合
                if cpu==1 and xy11=="１":
                    flag,cpu= 4,0
                    if senkou==1:
                        xy11="◯"
                        break
                    if senkou==0:
                        xy11="ｘ"
                        break
                if cpu==2 and xy21=="２":
                    flag,cpu= 4,0
                    if senkou==1:
                        xy21="◯"
                        break
                    if senkou==0:
                        xy21="ｘ"
                        break
                if cpu==3 and xy31=="３":
                    flag,cpu= 4,0
                    if senkou==1:
                        xy31="◯"
                        break
                    if senkou==0:
                        xy31="ｘ"
                        break
                if cpu==4 and xy21=="４":
                    flag,cpu= 4,0
                    if senkou==1:
                        xy21="◯"
                        break
                    if senkou==0:
                        xy21="ｘ"
                        break
                if cpu==5 and xy22=="５":
                    flag,cpu= 4,0
                    if senkou==1:
                        xy22="◯"
                        break
                    if senkou==0:
                        xy22="ｘ"
                        break
                if cpu==6 and xy32=="６":
                    flag,cpu= 4,0
                    if senkou==1:
                        xy32="◯"
                        break
                    if senkou==0:
                        xy32="ｘ"
                        break
                if cpu==7 and xy13=="７":
                    flag,cpu= 4,0
                    if senkou==1:
                        xy13="◯"
                        break
                    if senkou==0:
                        xy13="ｘ"
                        break
                if cpu==8 and xy23=="８":
                    flag,cpu= 4,0
                    if senkou==1:
                        xy23="◯"
                        break
                    if senkou==0:
                        xy23="ｘ"
                        break
                if cpu==9 and xy33=="９":
                    flag,cpu= 4,0
                    if senkou==1:
                        xy33="◯"
                        break
                    if senkou==0:
                        xy33="ｘ"
                        break
                kr +=1
                if kr>500:
                    await client.send_message(message.channel, "エラーが発生しました。ゲームを終了します。")
                    print("エラー")
                    start,flag,name= 0,0,""
        #勝敗判定
        if start==1 and xy11=="◯" and xy21=="◯" and xy31=="◯":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0
        if start==1 and xy11=="ｘ" and xy21=="ｘ" and xy31=="ｘ":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0
        if start==1 and xy12=="◯" and xy22=="◯" and xy32=="◯":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0
        if start==1 and xy12=="ｘ" and xy22=="ｘ" and xy32=="ｘ":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0
        if start==1 and xy13=="◯" and xy23=="◯" and xy33=="◯":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0
        if start==1 and xy13=="ｘ" and xy23=="ｘ" and xy33=="ｘ":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0
        if start==1 and xy11=="◯" and xy12=="◯" and xy13=="◯":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0
        if start==1 and xy11=="ｘ" and xy12=="ｘ" and xy13=="ｘ":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0
        if start==1 and xy21=="◯" and xy22=="◯" and xy23=="◯":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0
        if start==1 and xy21=="ｘ" and xy22=="ｘ" and xy23=="ｘ":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0
        if start==1 and xy31=="◯" and xy32=="◯" and xy33=="◯":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0
        if start==1 and xy31=="ｘ" and xy32=="ｘ" and xy33=="ｘ":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0
        if start==1 and xy11=="◯" and xy22=="◯" and xy33=="◯":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0
        if start==1 and xy11=="ｘ" and xy22=="ｘ" and xy33=="ｘ":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0
        if start==1 and xy31=="◯" and xy22=="◯" and xy13=="◯":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0
        if start==1 and xy31=="ｘ" and xy22=="ｘ" and xy13=="ｘ":
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            print("ゲーム終了")
            if senkou==1:
                await client.send_message(message.channel,message.author.mention +"さんの勝利です。")
                start= flag= 0
            if senkou==0:
                await client.send_message(message.channel,message.author.mention +"さんの負けです。")
                start= flag= 0

        if start==1 and xy11!="１" and xy12!="４" and xy13!="７" and xy21!="２" and xy22!="５" and xy23!="８" and xy31!="３"  and xy32!="６" and xy33!="９":#引き分け判定
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            await client.send_message(message.channel,"引き分けです。")
            print("ゲーム終了")
            start= flag= 0
        if flag==4 and start==1:#プレイヤーのターン
            flag=2
            await client.send_message(message.channel, xy11 + "┃" + xy21 + "┃" + xy31 + "\r\n━╋━╋━\r\n" + xy12 + "┃" + xy22 + "┃" + xy32 + "\r\n━╋━╋━\r\n" + xy13 + "┃" + xy23 + "┃" + xy33)
            await client.send_message(message.channel, message.author.mention +"さん1~9を選択してください。")
            print("＃"+ xy11+ "＃"+ xy21+ "＃"+ xy31 + "＃\r\n＃"+ xy12+ "＃"+ xy22+ "＃"+ xy32+ "＃\r\n＃"+xy13 + "＃"+ xy23+ "＃"+ xy33+ "＃")
        if message.content == "/ox" and start == 1 and message.author.name!=name: await client.send_message(message.channel, name + "さんが既にゲームを開始しています。ゲームが終了するまでお待ち下さい。")
        if message.content == "/reset" and start == 1 and message.author.name==name:#エラーした場合のリセット
            await client.send_message(message.channel, "ゲームをリセットします。")
            print("ゲームがリセットされました。")
            start,flag,name= 0,0,""

client.run("DISCORD_BOT_TOKEN")