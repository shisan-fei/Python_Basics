# Author:Kelly

# coding=utf-8


data = {

    "北京": {

        "一号线": {"四惠": {}, "大望路": {}, "天安门": {}, "西单": {}},

        "二号线": {"北京站": {}, "朝阳门": {}, "东直门": {}, "西直门": {}},

        "三号线": {"国贸": {}, "三元桥": {}, "知春路": {}, "巴沟": {}}

    },

    "上海": {

        "四号线": {"徐家汇": {}, "人民广场": {}, "延长路": {}, "共康路": {}, "呼兰路": {}},

        "五号线": {"东昌路": {}, "静安寺": {}, "江苏路": {}, "虹桥火车站": {}},

        "六号线": {"宝山路": {}, "赤峰路": {}, "曹阳路": {}, "虹桥路": {}, "宜山路": {}}

    },

    "广州": {

        "七号线": {"东山口": {}, "农讲所": {}, "烈士陵园": {}, "公园前": {}, "体育西路": {}},

        "八号线": {"黄边": {}, "纪念堂": {}, "三元里": {}, "白云公园": {}},

        "九号线": {"沙河顶": {}, "北京路": {}, "一德路": {}, "文化公园": {}}

    },

    "深圳": {

        "一号线": {"高新园": {}, "桃园": {}, "白石洲": {}, "华侨城": {}},

        "四号线": {"白石龙": {}, "明乐": {}, "少年宫": {}, "红山": {}},

        "五号线": {"大学城": {}, "兴东": {}, "西里": {}, "深圳北站": {}}

    },

}

exit_flag = False
while not exit_flag:
    for i in data:
        print(i)
    choice = input("选择进入1>>：")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t", i2)
            choice2 = input("选择进入2>>:")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input("选择进入3>>:")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t", i4)
                        choice4 = input("最后一层，按b返回,按q退出>>:")
                        if choice4 == 'b':
                            pass
                        elif choice4 == 'q':
                            exit_flag = True
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_flag = True
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit_flag = True
