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



# J1925	J2801	J4568	J4578	J6361	J6841	J7004	J7912	J8331	J8804	J8830	J9433	J9983	J_index225
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



    date_= []
    excelFile = 'JS_Mons225.xlsx'
    full_items = read_xlrd(excelFile=excelFile)
    for item in full_items:

        if type(item[2]) ==float:
            y_data_1.append(item[2]) #J1925
        if type(item[3]) == float:
            y_data_2.append(item[3]) #J2801
        if type(item[4]) == float:
            y_data_3.append(item[4]) #J4568
        if type(item[5]) == float:
            y_data_4.append(item[5])#J4578
        if type(item[6]) == float:
            y_data_5.append(item[6])#J6361
        if type(item[7]) == float:
            y_data_6.append(item[7])#J6841
        if type(item[8]) == float:
            y_data_7.append(item[8])# J7004
        if type(item[9]) == float:
            y_data_8.append(item[9])# J7912
        if type(item[10]) == float:
            y_data_9.append(item[10])# J8331
        if type(item[11]) == float:
            y_data_10.append(item[11])#J8804
        if type(item[12]) == float:
            y_data_11.append(item[12])#J8830
        if type(item[13]) == float:
            y_data_12.append(item[13])#J9433
        if type(item[14]) == float:
            y_data_13.append(item[14])#J9983
        if type(item[15]) == float:
            y_data_14.append(item[15])# J_index225






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
    print(x_data)


    c = (
        Line()
            .add_xaxis(xaxis_data=x_data)

            .add_yaxis(
            "J1925",
            y_axis=f_y_data_1,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )

            .add_yaxis(
            "J2801",
            y_axis=f_y_data_2,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J4568",
            y_axis=f_y_data_3,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J4578",
            y_axis=f_y_data_4,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J6361",
            y_axis=f_y_data_5,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J6841",
            y_axis=f_y_data_6,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J7004",
            y_axis=f_y_data_7,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J7912",
            y_axis=f_y_data_8,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J8331",
            y_axis=f_y_data_9,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )

            .add_yaxis(
            "J8804",
            y_axis=f_y_data_10,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J8830",
            y_axis=f_y_data_11,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J9433",
            y_axis=f_y_data_12,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )            .add_yaxis(
            "J9983",
            y_axis=f_y_data_13,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "J_index225",
            y_axis=f_y_data_14,
            linestyle_opts=opts.LineStyleOpts(width=3,color="blue"),
            label_opts=opts.LabelOpts(is_show=False),symbol_size=1

        )

            .set_global_opts(
            title_opts=opts.TitleOpts(title="J225POOL", pos_bottom="bottom",pos_right="middle"),
            # xaxis_opts=opts.AxisOpts(name="x"),
            yaxis_opts=opts.AxisOpts(
                        # name="y",
                splitline_opts=opts.SplitLineOpts(is_show=True),
                is_scale=True,



            ),

        )

            .render("j225.html")
    )











