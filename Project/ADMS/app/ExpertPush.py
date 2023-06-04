#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
import xlrd
from xlrd import xldate_as_tuple
import os
import pymysql
import pandas as pd
from flask import Flask, url_for, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/adms?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
# 设置session密钥
app.config['SECRET_KEY'] = 'secret_key'
# # 设置连接的redis数据库 默认连接到本地6379
app.config['SESSION_TYPE'] = 'redis'
# app.config['SESSION_PERMANENT'] = True
# # 设置远程
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)

db = SQLAlchemy(app)
"""
从excel表格导入专家用户数据
"""
def get_expertexcel(filename):
    rbook = xlrd.open_workbook(filename)
    sheet = rbook.sheet_by_name('Sheet1')
    rows = sheet.nrows
    cols = sheet.ncols

    all_content = []
    row_flag = 0
    for i in range(rows):
        row_content = []
        row_flag += 1
        for j in range(cols):
            ctype = sheet.cell(i, j).ctype#表格数据类型
            cell = sheet.cell_value(i, j)
            if ctype == 2 and cell % 1 == 0:#如果是整型
                cell = int(cell)
            elif ctype == 3:
                #转换成datetime对象
                date = datetime(*xldate_as_tuple(cell, 0))
                cell = date.strftime('%Y/%d/%m %H:%M:%S')
            elif ctype == 4:
                cell = True if cell == 1 else False
            if row_flag != 1:
                row_content.append(cell)
        if row_content:
            all_content.append(row_content)
    print(all_content)
    return all_content



def get_expertdata(filename):
    index = 0
    data = xlrd.open_workbook(filename)
    table = data.sheets()[index]
    rows = table.nrows
    result = []
    row_flag = 0
    for i in range(rows):
        row_flag += 1
        col = table.row_values(i)  ##获取每一列数据
        # print(col)
        # print(row_flag)
        if row_flag != 1:
            print(int(col[5]))
            result.append(col)
    # print(result)
    return result

class excel_read():
    def __init__(self, excel_path=r'Experts.xls',encoding='utf-8',index=0):

      self.data=xlrd.open_workbook(excel_path)  ##获取文本对象
      self.table=self.data.sheets()[index]     ###根据index获取某个sheet
      self.rows=self.table.nrows   ##3获取当前sheet页面的总行数,把每一行数据作为list放到 list

    def get_data(self):
        result=[]
        row = 0
        for i in range(self.rows):
            row += 1
            col=self.table.row_values(i)  ##获取每一列数据
            print(col)
            print(row)
            if row != 1:
                print(int(col[5]))
                result.append(col)
        print(result)
        return result


def importexpert():

    # 配置 MySQL 数据库连接
    db = pymysql.connect(host='localhost', port=3306, user='root', password='pjc20020204', db='adms')

    # 读取 Excel 文件
    df = pd.read_excel('../Experts.xls')

    # 将数据写入 MySQL 数据库中的表
    with db.cursor() as cursor:
        # 创建表
        #cursor.execute(
        #    'CREATE TABLE IF NOT EXISTS example (id INT, pwd VARCHAR(255), name VARCHAR(255), sex VARCHAR(10), birth DATE, phone VARCHAR(20))')
        #db.commit()

        # 写入数据
        for i, row in df.iterrows():
            cursor.execute('INSERT INTO example (id, pwd, name, sex, birth, phone) VALUES (%s, %s, %s, %s, %s, %s)',
                           (row['e_id'], row['e_pwd'], row['e_name'], row['e_sex'], row['e_birth'], row['e_phone']))
        db.commit()

    db.close()

    # 关闭数据库
    #cur.close()  # 关闭游标
    db.close()  # 关闭数据库连接
if __name__ == '__main__':
    # get_expertexcel('../Experts.xls')
    # importexpert()
     get_expertexcel('../Experts.xls')



        ##获取的结果样式[[],[],[],[]]
