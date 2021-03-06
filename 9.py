#! /usr/bin/env python
# encoding:UTF-8
from bs4 import BeautifulSoup
from prettytable import PrettyTable

def get_classtb():
    txt = """E:\Python3.5\python.exe C:/Users/Administrator/Documents/pycharm/test/a.py
    识别验证码为： 257420
    <html>
    <head>
        <title>本学期课程安排</title>
        <Meta http-equiv="Content-Type" Content="text/html; Charset=gbk">
        <Meta http-equiv="Content-Language" Content="zh-CN">
        <Meta http-equiv="MSThemeCompatible" Content="No">
        <Meta name="Author" Content="Educational Technology Institute, Tsinghua University">
        <Meta name="Copyright" Content="Copyright(c)2005 Educational Technology Institute, Tsinghua University">
        <link href="../../styles/css/content.css" rel="stylesheet" type="text/css">
        <script language="javascript" src="../../styles/js/common.js"></script>
        <script language="javascript" src="../../styles/js/general.js"></script>
        <script language="javascript" src="../../styles/js/jquery.js"></script>
        <style type="text/css">
            #bookInfo {
                position: absolute;
                z-index: 9999;
                border: 1px solid #49b6e6;
                width: 400px;
                background: #fff;
                margin: 0;
                padding: 10px;
                display: none;
                text-align: left;
            }
        </style>
        <script type="text/javascript">
            $(window).load(function () {
                $('.showBook').each(function () {
                    $(this).mouseover(function () {
    //                      $('#bookInfo').remove();
                        if ($('#bookInfo').length == 0) {
                            $(document.body).append('<p id="bookInfo"></p>');
                        }
                        var _top = $(this).offset().top;
                        var _left = $(this).offset().left;
                        var info = $(this).attr('rel');

                        $('#bookInfo').html(info).css({
                            top:_top - 10,
                            left:_left - 400
                        }).fadeIn(500);

                    });
                    $(document).click(function (e) {
                        if (!$(e.target).is('#bookInfo')) {
                            $('#bookInfo').fadeOut(500, function () {
                                $('#bookInfo').remove();
                            });
                        }
                    });

                });
            });

            function weekSchoolTimeTable(){
                var year=$("select[name=year]").find(":selected");
                var term=$("select[name=term]").find(":selected");
                if(year.val()=="-2" || term.val()=="-2"){
                    alert("不能查询所有学年学期");
                }else{
                    window.open("../../manager/coursearrange/studentWeeklyTimetable.do?yearid="+year.val()+"&termid="+term.val());
                }
            }
        </script>

    </head>

    <body>
    <table cellspacing="0" cellpadding="0" id="title">
        <tr>
            <td nowrap="nowrap">
                <div>
                    2017春 课程安排
                </div>
            </td>
        </tr>
    </table>

    <p>
        <input type="button"
               onClick="openwindow('../../manager/coursearrange/showTimetable.do?id=451585&yearid=37&termid=1&timetableType=STUDENT&sectionType=BASE','')"
               class="button" value="个人课表">
        <input type="button" onclick="weekSchoolTimeTable()" class="button" value="周次课表"/>


        <input type="button"
               onClick="window.open('../../manager/electcourse/studentSelectCrgroupList.do?yearId=37&termId=1')"
               class="button" value="选择课节分组">



    </p>
    <table cellpadding="0" cellspacing="0" class="subtitle">
        <tr>
            <td class="subtitle">学年学期</td>
        </tr>
    </table>
    <table cellpadding="0" cellspacing="0" class="broken_tab">
        <form action="">
            <tr>
                <td>学年</td>
                <td>

                    <select name="year">

                        <option value=37 >
                            2017
                        </option>

                        <option value=30 >
                            2010
                        </option>

                        <option value=31 >
                            2011
                        </option>

                        <option value=32 >
                            2012
                        </option>

                        <option value=33 >
                            2013
                        </option>

                        <option value=34 >
                            2014
                        </option>

                        <option value=35 >
                            2015
                        </option>

                        <option value=36 >
                            2016
                        </option>

                        <option value=38 >
                            2018
                        </option>

                        <option value=39 >
                            2019
                        </option>

                        <option value=40 >
                            2020
                        </option>

                        <option value=41 >
                            2021
                        </option>

                        <option value=42 >
                            2022
                        </option>

                        <option value=43 >
                            2023
                        </option>

                        <option value=44 >
                            2024
                        </option>

                    </select>
                </td>
                <td>学期</td>
                <td>

                    <select name="term">

                        <option value=1 >
                            春
                        </option>

                        <option value=2 >
                            夏
                        </option>

                        <option value=3 >
                            秋
                        </option>

                    </select>
                </td>
                <td>
                    <input type="submit" value="查 询" class="button">
                </td>
            </tr>
        </form>
    </table>


    <!--调课信息-->

    <eduaffair:CTRT studentid="451585" year="37"
                    term="1"
                    windowStyle="main"></eduaffair:CTRT>


    <br>
    <table cellpadding="0" cellspacing="0" class="infolist_tab">
        <tr>
            <th>课程号</th>
            <th>课程<br>
                序号
            </th>
            <th>课程名称</th>
            <th>任课教师</th>
            <th>学 分</th>
            <th>选课属性</th>
            <th>考核方式</th>
            <th>考试<br>
                性质
            </th>
            <th>是否<br>
                缓考
            </th>
            <th>上课时间、地点</th>
            <th>教材</th>
            <th>教学记录</th>
        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td>020214106
            </td>
            <td>1
            </td>
            <td>
                <a href="../../manager/querycourse/course_detail.jsdo?cid=20184"
                   target="_blank" class="infolist">编译原理
                </a></td>
            <td class="center">
                <a href='/academic/manager/teacherinfo/showTeacherInfoItem.do?userid=27204'  class="infolist" target='_blank'>刘冬梅</a><br>

            </td>
            <td class="center">3
            </td>
            <td class="center">
                必修
            </td>
            <td class="center">考试
            </td>
            <td class="center">正常考试
            </td>
            <td class="center">非缓考
            </td>
            <td>


                <table width="100%" border="0" cellspacing="0" cellpadding="0" class="none">

                    <tr>
                        <td width="20%" nowrap>3-15周
                        </td>
                        <td width="20%" nowrap>星期一
                        </td>
                        <td width="20%" nowrap>3--4
                        </td>
                        <td width="40%" nowrap>教C203
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>3-15周
                        </td>
                        <td width="20%" nowrap>星期四
                        </td>
                        <td width="20%" nowrap>3--4
                        </td>
                        <td width="40%" nowrap>教C203
                        </td>
                    </tr>


                </table>

            </td>

            <td class="center">
                &nbsp;
            </td>
            <td class="center">


                <a href="../../teacher/teachingtask/recordStudentIndex.do?epid=112806805"
                   target="_blank"><img src="../../styles/images/see.gif" alt="查看"/></a>

            </td>
        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td>020215022
            </td>
            <td>1
            </td>
            <td>
                <a href="../../manager/querycourse/course_detail.jsdo?cid=2665"
                   target="_blank" class="infolist">单片机技术
                </a></td>
            <td class="center">
                <a href='/academic/manager/teacherinfo/showTeacherInfoItem.do?userid=35900'  class="infolist" target='_blank'>武文红</a><br>

            </td>
            <td class="center">2
            </td>
            <td class="center">
                必修
            </td>
            <td class="center">考查
            </td>
            <td class="center">正常考试
            </td>
            <td class="center">非缓考
            </td>
            <td>


                <table width="100%" border="0" cellspacing="0" cellpadding="0" class="none">

                    <tr>
                        <td width="20%" nowrap>6-14周
                        </td>
                        <td width="20%" nowrap>星期五
                        </td>
                        <td width="20%" nowrap>1--2
                        </td>
                        <td width="40%" nowrap>教C204
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>6-14周
                        </td>
                        <td width="20%" nowrap>星期三
                        </td>
                        <td width="20%" nowrap>7--8
                        </td>
                        <td width="40%" nowrap>教C204
                        </td>
                    </tr>


                </table>

            </td>

            <td class="center">
                &nbsp;
            </td>
            <td class="center">


                <a href="../../teacher/teachingtask/recordStudentIndex.do?epid=112802402"
                   target="_blank"><img src="../../styles/images/see.gif" alt="查看"/></a>

            </td>
        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td>020215024
            </td>
            <td>1
            </td>
            <td>
                <a href="../../manager/querycourse/course_detail.jsdo?cid=10023"
                   target="_blank" class="infolist">网络工程实践
                </a></td>
            <td class="center">
                <a href='/academic/manager/teacherinfo/showTeacherInfoItem.do?userid=21306'  class="infolist" target='_blank'>王海凤</a><br>

            </td>
            <td class="center">2
            </td>
            <td class="center">
                限选
            </td>
            <td class="center">考查
            </td>
            <td class="center">正常考试
            </td>
            <td class="center">非缓考
            </td>
            <td>


                <table width="100%" border="0" cellspacing="0" cellpadding="0" class="none">

                    <tr>
                        <td width="20%" nowrap>3-13周
                        </td>
                        <td width="20%" nowrap>星期三
                        </td>
                        <td width="20%" nowrap>1--4
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>3-13周
                        </td>
                        <td width="20%" nowrap>&nbsp;
                        </td>
                        <td width="20%" nowrap>&nbsp;
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>14周
                        </td>
                        <td width="20%" nowrap>星期三
                        </td>
                        <td width="20%" nowrap>1--4
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>


                </table>

            </td>

            <td class="center">
                &nbsp;
            </td>
            <td class="center">


                <a href="../../teacher/teachingtask/recordStudentIndex.do?epid=112807475"
                   target="_blank"><img src="../../styles/images/see.gif" alt="查看"/></a>

            </td>
        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td>020215069
            </td>
            <td>1
            </td>
            <td>
                <a href="../../manager/querycourse/course_detail.jsdo?cid=10037"
                   target="_blank" class="infolist">嵌入式操作系统
                </a></td>
            <td class="center">
                <a href='/academic/manager/teacherinfo/showTeacherInfoItem.do?userid=10047'  class="infolist" target='_blank'>庄旭菲</a><br>

            </td>
            <td class="center">3
            </td>
            <td class="center">
                必修
            </td>
            <td class="center">考查
            </td>
            <td class="center">正常考试
            </td>
            <td class="center">非缓考
            </td>
            <td>


                <table width="100%" border="0" cellspacing="0" cellpadding="0" class="none">

                    <tr>
                        <td width="20%" nowrap>6-18周
                        </td>
                        <td width="20%" nowrap>星期一
                        </td>
                        <td width="20%" nowrap>1--2
                        </td>
                        <td width="40%" nowrap>教C305
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>6-18周
                        </td>
                        <td width="20%" nowrap>星期四
                        </td>
                        <td width="20%" nowrap>1--2
                        </td>
                        <td width="40%" nowrap>教C305
                        </td>
                    </tr>


                </table>

            </td>

            <td class="center">
                &nbsp;
            </td>
            <td class="center">


                <a href="../../teacher/teachingtask/recordStudentIndex.do?epid=112802015"
                   target="_blank"><img src="../../styles/images/see.gif" alt="查看"/></a>

            </td>
        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td>020215070
            </td>
            <td>1
            </td>
            <td>
                <a href="../../manager/querycourse/course_detail.jsdo?cid=10038"
                   target="_blank" class="infolist">嵌入式设计与开发
                </a></td>
            <td class="center">
                <a href='/academic/manager/teacherinfo/showTeacherInfoItem.do?userid=1878'  class="infolist" target='_blank'>王晓强</a><br>

            </td>
            <td class="center">3
            </td>
            <td class="center">
                必修
            </td>
            <td class="center">考查
            </td>
            <td class="center">正常考试
            </td>
            <td class="center">非缓考
            </td>
            <td>


                <table width="100%" border="0" cellspacing="0" cellpadding="0" class="none">

                    <tr>
                        <td width="20%" nowrap>3-15周
                        </td>
                        <td width="20%" nowrap>星期五
                        </td>
                        <td width="20%" nowrap>3--4
                        </td>
                        <td width="40%" nowrap>教C207
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>3-15周
                        </td>
                        <td width="20%" nowrap>星期二
                        </td>
                        <td width="20%" nowrap>3--4
                        </td>
                        <td width="40%" nowrap>教C204
                        </td>
                    </tr>


                </table>

            </td>

            <td class="center">
                &nbsp;
            </td>
            <td class="center">


                <a href="../../teacher/teachingtask/recordStudentIndex.do?epid=112803554"
                   target="_blank"><img src="../../styles/images/see.gif" alt="查看"/></a>

            </td>
        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td>020217087
            </td>
            <td>1
            </td>
            <td>
                <a href="../../manager/querycourse/course_detail.jsdo?cid=20188"
                   target="_blank" class="infolist">软件项目综合实训
                </a></td>
            <td class="center">
                <a href='/academic/manager/teacherinfo/showTeacherInfoItem.do?userid=505606'  class="infolist" target='_blank'>石宝</a><br>

            </td>
            <td class="center">2
            </td>
            <td class="center">
                必修
            </td>
            <td class="center">考查
            </td>
            <td class="center">正常考试
            </td>
            <td class="center">非缓考
            </td>
            <td>


                <table width="100%" border="0" cellspacing="0" cellpadding="0" class="none">

                    <tr>
                        <td width="20%" nowrap>1-2周
                        </td>
                        <td width="20%" nowrap>星期四
                        </td>
                        <td width="20%" nowrap>1--8
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>1-2周
                        </td>
                        <td width="20%" nowrap>星期五
                        </td>
                        <td width="20%" nowrap>1--8
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>1-2周
                        </td>
                        <td width="20%" nowrap>星期一
                        </td>
                        <td width="20%" nowrap>1--8
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>1-2周
                        </td>
                        <td width="20%" nowrap>星期三
                        </td>
                        <td width="20%" nowrap>1--8
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>1-2周
                        </td>
                        <td width="20%" nowrap>星期二
                        </td>
                        <td width="20%" nowrap>1--8
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>


                </table>

            </td>

            <td class="center">
                &nbsp;
            </td>
            <td class="center">


                <a href="../../teacher/teachingtask/recordStudentIndex.do?epid=112804774"
                   target="_blank"><img src="../../styles/images/see.gif" alt="查看"/></a>

            </td>
        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td>020217242
            </td>
            <td>1
            </td>
            <td>
                <a href="../../manager/querycourse/course_detail.jsdo?cid=20186"
                   target="_blank" class="infolist">嵌入式项目综合实训
                </a></td>
            <td class="center">
                <a href='/academic/manager/teacherinfo/showTeacherInfoItem.do?userid=1878'  class="infolist" target='_blank'>王晓强</a><br>

            </td>
            <td class="center">2
            </td>
            <td class="center">
                必修
            </td>
            <td class="center">考查
            </td>
            <td class="center">正常考试
            </td>
            <td class="center">非缓考
            </td>
            <td>


                <table width="100%" border="0" cellspacing="0" cellpadding="0" class="none">

                    <tr>
                        <td width="20%" nowrap>19-20周
                        </td>
                        <td width="20%" nowrap>星期四
                        </td>
                        <td width="20%" nowrap>1--8
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>19-20周
                        </td>
                        <td width="20%" nowrap>星期五
                        </td>
                        <td width="20%" nowrap>1--8
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>19-20周
                        </td>
                        <td width="20%" nowrap>星期三
                        </td>
                        <td width="20%" nowrap>1--8
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>19-20周
                        </td>
                        <td width="20%" nowrap>星期二
                        </td>
                        <td width="20%" nowrap>1--8
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>19-20周
                        </td>
                        <td width="20%" nowrap>星期一
                        </td>
                        <td width="20%" nowrap>1--8
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>


                </table>

            </td>

            <td class="center">
                &nbsp;
            </td>
            <td class="center">


                <a href="../../teacher/teachingtask/recordStudentIndex.do?epid=112802343"
                   target="_blank"><img src="../../styles/images/see.gif" alt="查看"/></a>

            </td>
        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td>020218049
            </td>
            <td>1
            </td>
            <td>
                <a href="../../manager/querycourse/course_detail.jsdo?cid=2683"
                   target="_blank" class="infolist">科研训练
                </a></td>
            <td class="center">
                <a href='/academic/manager/teacherinfo/showTeacherInfoItem.do?userid=37304'  class="infolist" target='_blank'>苏依拉</a><br>

            </td>
            <td class="center">1
            </td>
            <td class="center">
                必修
            </td>
            <td class="center">考查
            </td>
            <td class="center">正常考试
            </td>
            <td class="center">非缓考
            </td>
            <td>


                <table width="100%" border="0" cellspacing="0" cellpadding="0" class="none">

                    <tr>
                        <td width="20%" nowrap>1周
                        </td>
                        <td width="20%" nowrap>星期三
                        </td>
                        <td width="20%" nowrap>1--8
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>1周
                        </td>
                        <td width="20%" nowrap>星期四
                        </td>
                        <td width="20%" nowrap>1--8
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>1周
                        </td>
                        <td width="20%" nowrap>星期二
                        </td>
                        <td width="20%" nowrap>1--8
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>1周
                        </td>
                        <td width="20%" nowrap>星期一
                        </td>
                        <td width="20%" nowrap>1--8
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>

                    <tr>
                        <td width="20%" nowrap>1周
                        </td>
                        <td width="20%" nowrap>星期五
                        </td>
                        <td width="20%" nowrap>1--8
                        </td>
                        <td width="40%" nowrap>&nbsp;
                        </td>
                    </tr>


                </table>

            </td>

            <td class="center">
                &nbsp;
            </td>
            <td class="center">


                <a href="../../teacher/teachingtask/recordStudentIndex.do?epid=112806245"
                   target="_blank"><img src="../../styles/images/see.gif" alt="查看"/></a>

            </td>
        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td>12000001x
            </td>
            <td>1
            </td>
            <td>
                <a href="../../manager/querycourse/course_detail.jsdo?cid=5345"
                   target="_blank" class="infolist">人力资源开发与管理
                </a></td>
            <td class="center">
                <a href='/academic/manager/teacherinfo/showTeacherInfoItem.do?userid=39840'  class="infolist" target='_blank'>李昶林</a><br>

            </td>
            <td class="center">2
            </td>
            <td class="center">
                任选
            </td>
            <td class="center">考查
            </td>
            <td class="center">正常考试
            </td>
            <td class="center">非缓考
            </td>
            <td>


                <table width="100%" border="0" cellspacing="0" cellpadding="0" class="none">

                    <tr>
                        <td width="20%" nowrap>7-18周
                        </td>
                        <td width="20%" nowrap>星期二
                        </td>
                        <td width="20%" nowrap>5--7
                        </td>
                        <td width="40%" nowrap>教D204
                        </td>
                    </tr>


                </table>

            </td>

            <td class="center">
                &nbsp;
            </td>
            <td class="center">


                <a href="../../teacher/teachingtask/recordStudentIndex.do?epid=112808549"
                   target="_blank"><img src="../../styles/images/see.gif" alt="查看"/></a>

            </td>
        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td>ZC04x
            </td>
            <td>1
            </td>
            <td>
                <a href="../../manager/querycourse/course_detail.jsdo?cid=23084"
                   target="_blank" class="infolist">东方文学史
                </a></td>
            <td class="center">


            </td>
            <td class="center">3
            </td>
            <td class="center">
                任选
            </td>
            <td class="center">考查
            </td>
            <td class="center">正常考试
            </td>
            <td class="center">非缓考
            </td>
            <td>


                <table width="100%" border="0" cellspacing="0" cellpadding="0" class="none">


                </table>

            </td>

            <td class="center">
                &nbsp;
            </td>
            <td class="center">


                <a href="../../teacher/teachingtask/recordStudentIndex.do?epid=118644391"
                   target="_blank"><img src="../../styles/images/see.gif" alt="查看"/></a>

            </td>
        </tr>

    </table>
    <br>
    <table width="92%" cellpadding="0" cellspacing="0" class="subtitle">
        <tr>
            <td>上课大节</td>

            <td id="rightbg">&nbsp;</td>
        </tr>
    </table>
    <table cellpadding="0" cellspacing="0" class="infolist_tab">
        <tr>
            <th>序号</th>
            <th>名称</th>
            <th>包含小节</th>

            <th>时间</th>


        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td class="center">1
            </td>
            <td class="center">1--2
            </td>
            <td class="center">
                第1节 第2节

            </td>

            <td class="center">
                2000-12-31 08:00:00.0
                --
                2000-12-31 09:50:00.0
            </td>


        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td class="center">2
            </td>
            <td class="center">1--3
            </td>
            <td class="center">
                第1节 第2节 第3节

            </td>

            <td class="center">
                2000-12-31 08:00:00.0
                --
                2000-12-31 11:00:00.0
            </td>


        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td class="center">3
            </td>
            <td class="center">1--4
            </td>
            <td class="center">
                第1节 第2节 第3节 第4节

            </td>

            <td class="center">
                2000-12-31 08:00:00.0
                --
                2000-12-31 12:00:00.0
            </td>


        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td class="center">4
            </td>
            <td class="center">1--8
            </td>
            <td class="center">
                第1节 第2节 第3节 第4节 第5节 第6节 第7节 第8节

            </td>

            <td class="center">
                2000-12-31 08:00:00.0
                --
                2000-12-31 18:00:00.0
            </td>


        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td class="center">5
            </td>
            <td class="center">3--4
            </td>
            <td class="center">
                第3节 第4节

            </td>

            <td class="center">
                2000-12-31 10:10:00.0
                --
                2000-12-31 12:00:00.0
            </td>


        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td class="center">6
            </td>
            <td class="center">5--6
            </td>
            <td class="center">
                第5节 第6节

            </td>

            <td class="center">
                2000-12-31 14:00:00.0
                --
                2000-12-31 15:50:00.0
            </td>


        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td class="center">7
            </td>
            <td class="center">5--7
            </td>
            <td class="center">
                第5节 第6节 第7节

            </td>

            <td class="center">
                2000-12-31 14:00:00.0
                --
                2000-12-31 17:00:00.0
            </td>


        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td class="center">8
            </td>
            <td class="center">5--8
            </td>
            <td class="center">
                第5节 第6节 第7节 第8节

            </td>

            <td class="center">
                2000-12-31 14:00:00.0
                --
                2000-12-31 18:00:00.0
            </td>


        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td class="center">9
            </td>
            <td class="center">7--8
            </td>
            <td class="center">
                第7节 第8节

            </td>

            <td class="center">
                2000-12-31 16:10:00.0
                --
                2000-12-31 18:00:00.0
            </td>


        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td class="center">10
            </td>
            <td class="center">9--11
            </td>
            <td class="center">
                第9节 第10节 第11节

            </td>

            <td class="center">
                2000-12-31 19:30:00.0
                --
                2000-12-31 21:20:00.0
            </td>


        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td class="center">11
            </td>
            <td class="center">9--10
            </td>
            <td class="center">
                第9节 第10节

            </td>

            <td class="center">
                2000-12-31 19:30:00.0
                --
                2000-12-31 21:20:00.0
            </td>


        </tr>

        <tr class="infolist_common" onMouseOver="javascript:this.className='infolist_current'"
            onMouseOut="javascript:this.className='infolist_common'">
            <td class="center">12
            </td>
            <td class="center">9--12
            </td>
            <td class="center">
                第9节 第10节 第11节 第12节

            </td>

            <td class="center">
                2000-12-31 19:30:00.0
                --
                2000-12-31 22:31:00.0
            </td>


        </tr>

    </table>
    </body>
    </html>


    Process finished with exit code 0
    """
    soup = BeautifulSoup(txt, "html.parser")
    a = soup.find_all(class_="infolist_common")
    tb = PrettyTable(["课程号", "课程序号", "课程名称", "任课教师", "学分", "选课属性", "考核方式", "考试性质", "是否缓考", "上课时间、地点"])
    tb.padding_width = 1
    # tb.align["课程名称"] = "l" #对齐方式
    for x in range(0, len(a) - 12):
        b = a[x].get_text()  # 处理课表信息
        c = b.split()
        q = c[9: len(c)]
        last_td = ''.join(q)
        td_row = c[0: 9]
        td_row.append(last_td)
        if x == 9:
            td_row[-1] = ' '
            td_row.insert(3, '')
        # print(td_row)
        tb.add_row(td_row)
    return tb
print(get_classtb())
url_dict = {
    'schoolroll': 'http://202.207.16.237/academic/accessModule.do?moduleId=2060&groupId=',  # 学籍信息
    'grade': 'http://202.207.16.237/academic/accessModule.do?moduleId=2020&groupId=',  # 查询成绩
    'classtb': 'http://202.207.16.237/academic/student/currcourse/currcourse.jsdo'  # 本学期课表
}
print(url_dict['classtb'])