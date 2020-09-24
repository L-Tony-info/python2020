from flask import Flask,render_template,request
import csv
app = Flask(__name__)

contents = []

@app.route('/')
def base() -> 'html':
    return render_template('entry.html')

#2016年-2018年全国男女人口占比
@app.route('/total_people')
def total_people() -> 'html':
    title = "2016年-2018年全国男女人口占比"
    titles = ("年份","总人数","男性人数","女性人数","男性人数占比","女性人数占比"
)
    contents = []
    with open('data/China_total_people.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('China_total_people.html',
                           the_title = title,
                           the_row_titles = titles,
                           the_data = contents)

#2016-2018年各省总人口数和男女人口数对比
@app.route('/provice_people')
def provice_people() -> 'html':
    title = "2016-2018年各省总人口数和男女人口数对比"
    return render_template('provice-people.html',
                           the_title = title,
                          )
@app.route('/provice_people/2016')
def provice_people_2016() -> 'html':
    title = "2016年各省总人口数和男女人口数对比"
    titles = ("省份","总人口数","男性人口数","女性人口数"
)
    contents = []
    with open('data/2016_province_people.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('provice-people.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )

@app.route('/provice_people/2017')
def provice_people_2017() -> 'html':
    title = "2017年各省总人口数和男女人口数对比"
    titles = ("省份","总人口数","男性人口数","女性人口数"
)
    contents = []
    with open('data/2017_province_people.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('provice-people.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )
@app.route('/provice_people/2018')
def provice_people_2018() -> 'html':
    title = "2018年各省总人口数和男女人口数对比"
    titles = ("省份","总人口数","男性人口数","女性人口数"
)
    contents = []
    with open('data/2018_province_people.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('provice-people.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )

#GDP
@app.route('/GDP')
def GDP() -> 'html':
    title = "中国各省2016-2018年GDP情况"
    shengfen = ["全部", "北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江", "上海", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南",
                "湖北", "湖南", "广东", "广西", "海南", "重庆", "四川", "贵州", "云南", "西藏", "陕西", "甘肃", "青海", "宁夏", "新疆"]
    titles = ("省份","2018年","2017年","2016年")
    with open('data/China_GDP.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('GDP.html',
                           the_title = title,
                           the_row_titles = titles,
                           the_data = contents,
                           the_data1 = shengfen)

contents1=[]
@app.route('/GDP/result',methods=['POST'])
def GDP_result() -> 'html':
    shengfen = ["全部", "北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江", "上海", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "广西", "海南", "重庆", "四川", "贵州", "云南", "西藏", "陕西", "甘肃", "青海", "宁夏", "新疆"]
    provice = request.form['provice']
    title = "中国各省2016-2018年GDP情况"
    titles = ("省份", "2018年", "2017年", "2016年")
    with open('data/China_GDP.csv') as csv2:
        for line in csv2:
            contents1.append([])
            for item in line.split(','):
                contents1[-1].append(item)
    if provice == "全部":
        return render_template('GDP.html',
                               the_data1=shengfen,
                               the_title = title,
                               the_row_titles = titles,
                               the_data = contents1)
    else:
        return render_template('result.html',
                               the_data2= contents1[shengfen.index(provice)],
                               the_title = title)



#中国各省单身人口情况
@app.route('/unmarried_people')
def provice_unmarried_people() -> 'html':
    title = "2016-2018年中国各省单身人口情况"
    return render_template('provice-unmarried.html',
                           the_title = title,
                          )
@app.route('/unmarried_people/2016')
def provice_unmarried_people_16() -> 'html':
    title = "2016年中国各省单身人口情况"
    titles = ("省份","总单身数","男性单身数","女性单身数"
)
    contents = []
    with open('data/16_unmarried.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('provice-unmarried.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )

@app.route('/unmarried_people/2017')
def provice_unmarried_people_17() -> 'html':
    title = "2017年中国各省单身人口情况"
    titles = ("省份", "总单身数", "男性单身数", "女性单身数")
    contents = []
    with open('data/17_unmarried.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('provice-unmarried.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )
@app.route('/unmarried_people/2018')
def provice_unmarried_people_18() -> 'html':
    title = "2018年中国各省单身人口情况"
    titles = ("省份", "总单身数", "男性单身数", "女性单身数")
    contents = []
    with open('data/18_unmarried.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('provice-unmarried.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )


#大专学历以上总人数和男女人数
@app.route('/junior_college_people')
def junior_college_people() -> 'html':
    title = "2016-2018年中国各省大专学历以上总人数和男女人数"
    return render_template('junior_college.html',
                           the_title = title,
                          )
@app.route('/junior_college_people/2016')
def junior_college_people_2016() -> 'html':
    title = "2016年中国各省大专学历以上总人数和男女人数"
    titles = ("省份","总人数","男性人数","女性人数")
    contents = []
    with open('data/16_junior_college.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('junior_college.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )

@app.route('/junior_college_people/2017')
def junior_college_people_2017() -> 'html':
    title = "2017年中国各省大专学历以上总人数和男女人数"
    titles = ("省份", "总人数", "男性人数", "女性人数")
    contents = []
    with open('data/17_junior_college.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('junior_college.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )
@app.route('/junior_college_people/2018')
def junior_college_people_2018() -> 'html':
    title = "2018年中国各省大专学历以上总人数和男女人数"
    titles = ("省份", "总人数", "男性人数", "女性人数")
    contents = []
    with open('data/18_junior_college.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('junior_college.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )

if __name__ == '__main__':
    app.run()