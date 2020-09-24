## 项目代码
* [qmks](https://github.com/L-Tony-info/python2020/tree/master/qmks)
## pythonanywhere
* 链接：[http://ltonyinfo.pythonanywhere.com/](http://ltonyinfo.pythonanywhere.com/)
## 技术文档
### HTML
* 在选择感兴趣的图表处，用了轮播图跳转，点击轮播图就能跳转到相应的交互数据页面。代码如下：
```
<div id="wrapper">
  <div id="slider-wrap">
             <ul id="slider">
               <li >
                 <a href="/total_people" type='submit'><img class="i" src="static/entry/img/全国男女人口数对比.png" /></a>
               </li>
               <li>
                  <a href="/GDP" type="submit"><img class="i" src="static/entry/img/中国各省2016-2018年GDP情况.png" /></a>
               </li>
               <li >
               <a href="/unmarried_people" type="submit"><img class="i" src="static/entry/img/中国各省单身人口情况.png" /></a>
               </li>
               <li>
               <a href="/junior_college_people" type="submit"><img class="i" src="static/entry/img/2018年各省6岁及以上大专学历以上总人数.jpg" /></a>
               </li>
               <li>
               <a href="provice_people" type="submit"><img class="i" src="static/entry/img/各省总人口数男女人口数对比.png" /></a>
               </li>
            </ul>`
             <!--控制按钮-->
            <div class="btns" id="next"><i class="fa fa-arrow-right"><img src="static/entry/img/right.png" /></i></div>
            <div class="btns" id="previous"><img src="static/entry/img/left.png" /><i class="fa fa-arrow-left"></i></div>
            <div id="counter"></div>
            <div id="pagination-wrap">
              <ul>
              </ul>
            </div>
            <!--控制按钮-->
  			</div>
```

* 在每个交互数据页面的右底部，添加了返回首页的按钮，代码如下：
```
<div align="right">
    <a href="/"><input class="anniu" name="" type="button" value="返回首页" /></a>
</div>
```

* 在首页的选择想了解的数据的选择框里加入选择框跳转，代码如下：
```
<div align="center">
<select name="" onchange="javascript:window.open(this.options[this.selectedindex].value)" style="width:250px;height:30px;text-align:center;text-align-last:center">
<option value='total_people' selected>全国总男女人口数对比</option>
<option value='provice_people' selected>各省总人口和男女人口数对比</option>
<option value='GDP' selected>中国各省2016-2018年GDP情况</option>
<option value='unmarried_people' selected>2016-2018年各省总单身人口数和男女单身人口数对比</option>
<option value='junior_college_people' selected>大专学历以上总人数和男女人数</option>
<option value="#" selected>--请选择--</option>
</SELECT>
    <SCRIPT language=JavaScript>
var select = document.querySelector('select');select.onchange = function(){	window.location=this.value;}
    </SCRIPT>
    </div>
```
### py
* 运用了Flask,render_template,request三个模块；
* 加入if、else的条件语句以实现筛选不同省份的GDP，代码如下：
```
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
```

