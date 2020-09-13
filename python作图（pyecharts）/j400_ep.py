import pyecharts.options as opts
from pyecharts.charts import Line
import os
import xlrd
import sys

# 读取xlxs数据
# 数据处理整理
# 测试
# 可以部署到服务器上面！彻底解放人力！

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://www.echartsjs.com/examples/editor.html?c=line-log

目前无法实现的功能:

1、暂无
"""






def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

       # # if 去掉表头
       # if rowNum > 0:


    return dataFile


def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")



# 时间日期的转换

from xlrd import xldate_as_tuple
import datetime


#float--->日期字符串？
def handle_date(dates):
    f_ =[]

    for item in dates:

        tuple = xldate_as_tuple(item, 0)
        excel_datetime=datetime.datetime(*tuple)
        f_.append(str(excel_datetime))

    return f_

# 需要修改纵坐标刻度 # 默认是从
def get_v(l):
    f =[]

    for num in range(0,len(l)-1):
        f_da = "%.4f" % (l[num]/l[0]-1)

        f.append(f_da)



    return f


#J2127	J3141	J3148	J3254	J3288	J3549	J3769	J4091	J4568	J4684	J4768	J5929	J6877	J7309	J7532	J7649	J7974	J8111	J8424	J9065	J9697	J_index400

# 识别曲线
#
if __name__ =="__main__":

    y_data_1 = []
    y_data_2 = []
    y_data_3 = []
    y_data_4 = []
    y_data_5 = []
    y_data_6 = []
    y_data_7 = []
    y_data_8 = []
    y_data_9 = []
    y_data_10 = []
    y_data_11 = []
    y_data_12 = []
    y_data_13 = []
    y_data_14 = []
    y_data_15 = []
    y_data_16 = []
    y_data_17 = []
    y_data_18 = []
    y_data_19 = []
    y_data_20 = []
    y_data_21 = []
    y_data_22 = []




    date_= []
    excelFile = 'JS_Mons400.xlsx'
    full_items = read_xlrd(excelFile=excelFile)
    for item in full_items:

        if type(item[2]) ==float:
            y_data_1.append(item[2]) #J2127
        if type(item[3]) == float:
            y_data_2.append(item[3]) #J3141
        if type(item[4]) == float:
            y_data_3.append(item[4]) #J3148
        if type(item[5]) == float:
            y_data_4.append(item[5])#J3254
        if type(item[6]) == float:
            y_data_5.append(item[6])#J3288
        if type(item[7]) == float:
            y_data_6.append(item[7])#J3549
        if type(item[8]) == float:
            y_data_7.append(item[8])#J3769
        if type(item[9]) == float:
            y_data_8.append(item[9])#J4091
        if type(item[10]) == float:
            y_data_9.append(item[10])#J4568
        if type(item[11]) == float:
            y_data_10.append(item[11])#J4684
        if type(item[12]) == float:
            y_data_11.append(item[12])#J4768
        if type(item[13]) == float:
            y_data_12.append(item[13])#J5929
        if type(item[14]) == float:
            y_data_13.append(item[14])#J6877
        if type(item[15]) == float:
            y_data_14.append(item[15])#J7309
        if type(item[16]) == float:
            y_data_15.append(item[16])#J7532
        if type(item[17]) == float:
            y_data_16.append(item[17])#J7649
        if type(item[18]) == float:
            y_data_17.append(item[18])#J7974
        if type(item[19]) == float:
            y_data_18.append(item[19])#J8111
        if type(item[20]) == float:
            y_data_19.append(item[20])#J8424
        if type(item[21]) == float:
            y_data_20.append(item[21])#J9065
        if type(item[22]) == float:
            y_data_21.append(item[22])#J9697
        if type(item[23]) == float:
            y_data_22.append(item[23])#J_index400









        if item[len(item)-1] != "LastTime":
             date_.append(item[len(item)-1])
    # 日期搞定
    x_data = handle_date(date_)

    f_y_data_1 = get_v(y_data_1)
    f_y_data_2 = get_v(y_data_2)
    f_y_data_3 = get_v(y_data_3)
    f_y_data_4 = get_v(y_data_4)
    f_y_data_5 = get_v(y_data_5)
    f_y_data_6 = get_v(y_data_6)
    f_y_data_7 = get_v(y_data_7)
    f_y_data_8 = get_v(y_data_8)
    f_y_data_9 = get_v(y_data_9)
    f_y_data_10 = get_v(y_data_10)
    f_y_data_11 = get_v(y_data_11)
    f_y_data_12 = get_v(y_data_12)
    f_y_data_13 = get_v(y_data_13)
    f_y_data_14 = get_v(y_data_14)
    f_y_data_15 = get_v(y_data_15)
    f_y_data_16 = get_v(y_data_16)
    f_y_data_17 = get_v(y_data_17)
    f_y_data_18 = get_v(y_data_18)
    f_y_data_19 = get_v(y_data_19)
    f_y_data_20 = get_v(y_data_20)
    f_y_data_21 = get_v(y_data_21)
    f_y_data_22 = get_v(y_data_22)
    print(x_data)


    c = (
        Line()
            .add_xaxis(xaxis_data=x_data)

            .add_yaxis(
            "J2127",
            y_axis=f_y_data_1,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J3141",
            y_axis=f_y_data_2,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J3148",
            y_axis=f_y_data_3,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J3254",
            y_axis=f_y_data_4,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J3288",
            y_axis=f_y_data_5,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J3549",
            y_axis=f_y_data_6,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J3769",
            y_axis=f_y_data_7,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J4091",
            y_axis=f_y_data_8,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J4568",
            y_axis=f_y_data_9,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J4684",
            y_axis=f_y_data_10,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J4768",
            y_axis=f_y_data_11,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J5929",
            y_axis=f_y_data_12,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J6877",
            y_axis=f_y_data_13,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J7309",
            y_axis=f_y_data_14,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J7532",
            y_axis=f_y_data_15,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J7649",
            y_axis=f_y_data_16,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J7974",
            y_axis=f_y_data_17,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J8111",
            y_axis=f_y_data_18,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J8424",
            y_axis=f_y_data_19,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J9065",
            y_axis=f_y_data_20,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )            .add_yaxis(
            "J9697",
            y_axis=f_y_data_21,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )            .add_yaxis(
            "J_index400",
            y_axis=f_y_data_22,
            linestyle_opts=opts.LineStyleOpts(width=3,color="blue"),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )



            .set_global_opts(
            title_opts=opts.TitleOpts(title="J400POOL", pos_bottom="bottom",pos_right="middle"),
            # xaxis_opts=opts.AxisOpts(name="x"),
            yaxis_opts=opts.AxisOpts(
                        # name="y",
                splitline_opts=opts.SplitLineOpts(is_show=True),
                is_scale=True,



            ),

        )

            .render("JS_Mons400.html")
    )











