# -*- encoding: utf-8 -*-
"""
@Time    :   2022/01/01 00:24:32
@Author  :   辛酉
@Desc    :   None
"""
# here put the import lib
import re

from bs4 import BeautifulSoup

html = """<!DOCTYPE html_test PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html_test xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Type" content="text/html_test; charset=utf-8"/>
    <title>bobby基本信息</title>
    <meta name="keywords" content="求福利帶帶我"/>
    <meta name="description" content="求福利帶帶我 ,老司機論壇"/>

    <base href="https://www.seejav.bid/forum/"/>
    <link rel="stylesheet" type="text/css" href="data/cache/style_2_common.css?j69"/>
    <link rel="stylesheet" type="text/css" href="data/cache/style_2_forum_forumdisplay.css?j69"/>
    <script src="template/javbus/images/js/jquery-4.4.1.min.js" type="text/javascript"></script>
    <script src="template/javbus/images/js/common.min.js" type="text/javascript"></script>
    <script language="javascript" type="text/javascript">
        function killErrors() {
            return true;
        }

        window.onerror = killErrors;
    </script>

    <link rel="stylesheet" href="template/javbus/images/iconfont/iconfont.css">
    <script type="text/javascript">var STYLEID = '2', STATICURL = 'static/', IMGDIR = 'template/javbus/images/common',
        VERHASH = 'j69', charset = 'utf-8', discuz_uid = '279148', cookiepre = '4fJN_2132_', cookiedomain = '',
        cookiepath = '/', showusercard = '1', attackevasive = '0', disallowfloat = 'newthread|reply',
        creditnotice = '1|里程|,2|金錢|', defaultstyle = '',
        REPORTURL = 'aHR0cHM6Ly93d3cuc2VlamF2LmJpZC9mb3J1bS9mb3J1bS5waHA/bW9kPWZvcnVtZGlzcGxheSZmaWQ9MzY=',
        SITEURL = 'https://www.seejav.bid/forum/', JSPATH = 'static/js/', CSSPATH = 'data/cache/style_',
        DYNAMICURL = '';</script>
    <script src="static/js/common.js?j69" type="text/javascript"></script>
    <meta name="renderer" content="webkit">
    <meta name="application-name" content="老司機論壇"/>
    <meta name="msapplication-tooltip" content="老司機論壇"/>
    <meta name="msapplication-task"
          content="name=老司機論壇;action-uri=https://www.seejav.bid/forum/forum.php;icon-uri=https://www.seejav.bid/forum/template/javbus/images/common/bbs.ico"/>
    <link rel="preconnect" href="https://poweredby.jads.co" crossorigin>
    <link rel="dns-prefetch" href="https://poweredby.jads.co">
    <script src="static/js/forum.js?j69" type="text/javascript"></script>
    <link rel="stylesheet" type="text/css" href="template/javbus/common/custom.css?v=6.1.5"/>

</head>

<body id="nv_forum" class="pg_forumdisplay" onkeydown="if(event.keyCode==27) return false;">
<div id="append_parent"></div>
<div id="info-0662"></div>
<ul id="myprompt_menu" class="p_pop" style="display: none;">
    <li><a href="home.php?mod=space&amp;do=pm" id="pm_ntc"
           style="background-repeat: no-repeat; background-position: 0 50%;"><em class="prompt_news_0"></em>消息</a></li>
    <li><a href="home.php?mod=follow&amp;do=follower"><em class="prompt_follower_0"></em>新聽眾</a></li>
    <li class="ignore_noticeli"><a href="javascript:;" onClick="setcookie('ignore_notice', 1);hideMenu('myprompt_menu')"
                                   title="暫不提醒"><em class="ignore_notice"></em></a></li>
</ul>
<ul id="myitem_menu" class="p_pop" style="display: none;">
    <li><a href="forum.php?mod=guide&amp;view=my">帖子</a></li>
    <li><a href="home.php?mod=space&amp;do=favorite&amp;view=me">收藏</a></li>
    <li><a href="home.php?mod=space&amp;do=friend">好友</a></li>
</ul>
<div id="qmenu_menu" class="p_pop " style="display: none;">
    <ul class="cl nav">
        <li><a href="forum.php?mod=guide&view=my"
               style="background-image:url(/forum/static/image/feed/thread_b.png) !important">帖子</a></li>
        <li><a href="home.php?mod=space&do=favorite&view=me"
               style="background-image:url(/forum/static/image/feed/favorite_b.png) !important">收藏</a></li>
        <li><a href="home.php?mod=magic" style="background-image:url(/forum/static/image/feed/magic_b.png) !important">道具</a>
        </li>
        <li><a href="home.php?mod=medal" style="background-image:url(/forum/static/image/feed/medal_b.png) !important">勳章</a>
        </li>
        <li><a href="home.php?mod=task"
               style="background-image:url(/forum/static/image/feed/task_b.png) !important">任務</a></li>
    </ul>
    <div id="fjump_menu" class="btda"></div>
</div>
<div class="wp cl">
</div>

<script type="text/javascript">
    function searchs(obj) {
        var searchval = document.getElementById(obj).value;
        if (searchval == '') {
            return false;
        } else {
            window.open("../search/" + encodeURIComponent(searchval.replace(/(^\s*)|(\s*$)/g, '')) + "&parent=ce");
        }
    }

    document.onkeydown = function (event) {
        var e = event || window.event;
        if (e && e.keyCode == 13) {
            searchs('search-input');
        }
    }
</script>

<div id="toptb" class="cl jav-nav">
    <div class="wp">
        <div class="z">
            <ul>
                <li><a class="jav-logo" href="/"><img src="static/image/common/logo_javbus.png"></a></li>
                <div class="jav-form-group">
                    <input id="search-input" class="jav-form" placeholder="搜尋 識別碼, 影片, 演員">
                    <button class="jav-button" type="submit" onClick="searchs('search-input')">搜尋</button>
                </div>
                <li class="nav-title nav-inactive"><a href="/">有碼</a></li>
                <li class="nav-title nav-inactive"><a href="/uncensored">無碼</a></li>
                <li class="nav-title nav-inactive"><a href="https://www.javbus.red">歐美</a></li>
                <li class="nav-title nav-active"><a href="/forum/"
                                                    style="color:#555; background-color:#DBDBDB; height:20px; width:28px; margin:0; padding:15px;">論壇</a>
                </li>
                <li class="nav-title nav-inactive"><a href="/genre">類別</a></li>
                <li class="nav-title nav-inactive"><a href="/actresses">女優</a></li>
            </ul>
        </div>
    </div>
    <div class="login-wrap y">
        <div class="menu-heading">
   <span class="avatar-pic"><a href="home.php?mod=space&amp;uid=279148"><img
           src="https://uc.javbus22.com/uc/data/avatar/000/27/91/48_avatar_small.jpg"
           onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_small.gif'"/></a>
      </span>
            <span class="member-name"><a href="home.php?mod=space&amp;uid=279148" target="_blank" title="訪問我的空間">pxy785378521</a> </span>
            <span class="angle"></span>
        </div>

        <div class="menu-body">
            <div class="menu-body-panel login-detail-wrap">
                <i class="icon icon-arrow-t"></i>
                <div class="item">
                    <a href="javascript:;" id="qmenu"
                       onmouseover="delayShow(this, function () {showMenu({'ctrlid':'qmenu','pos':'34!','ctrlclass':'a','duration':2});showForummenu(36);})">快捷導航</a>
                </div>


                <div class="item">
                    <a id="nte_menu" href="home.php?mod=space&amp;do=notice" class="notification">提醒</a></li>
                </div>

                <div class="item">
                    <a id="msg_menu" href="home.php?mod=space&amp;do=pm" class="msg">消息</a>
                </div>

                <div class="item">
                    <a id="msg_menu" href="search.php?mod=forum" class="msg">搜索</a>
                </div>


                <div class="item">
                    <a href="home.php?mod=spacecp">設置</a>
                </div>

                <div class="item">
                    <a href="member.php?mod=logging&amp;action=logout&amp;formhash=a5beaa79">退出</a>
                </div>

            </div>
        </div>

    </div>


</div>
<div class="bcpic">
    <ul>
        <li><a href="https://www.hqabtjf.com:7700/?agent_code=22124" target="_blank" rel="nofollow"><img
                src="/ads/forum_bob_56x56_4.jpg">多特蒙德伙伴</a></li>
        <li><a href="https://www.udlutm.com:8888/?agent_code=2943" target="_blank" rel="nofollow"><img
                src="/ads/forum_ltt_56x56_3.jpg">MG新年大放彩</a></li>
        <li><a href="https://www.udlutm.com:8888/?agent_code=2943" target="_blank" rel="nofollow"><img
                src="/ads/forum_ltt_56x56_6.jpg">AG至尊堂送红利</a></li>
        <li><a href="https://www.hqabtjf.com:7700/?agent_code=22124" target="_blank" rel="nofollow"><img
                src="/ads/forum_bob_56x56_7.jpg">签到领彩金</a></li>
        <li><a href="https://www.0lhx7.com:7443/?i_code=9410072" target="_blank" rel="nofollow"><img
                src="/ads/forum_yb_56x56_9.jpg">双赢彩票</a></li>
        <li><a href="https://www.0lhx7.com:7443/?i_code=9410072" target="_blank" rel="nofollow"><img
                src="/ads/forum_yb_56x56_2.jpg">Yabo亚博体育</a></li>
        <li><a href="https://www.0lhx7.com:7443/?i_code=9410072" target="_blank" rel="nofollow"><img
                src="/ads/forum_yb_56x56_10.jpg">王者荣耀3888彩金</a></li>
        <li><a href="https://www.hqabtjf.com:7700/?agent_code=22124" target="_blank" rel="nofollow"><img
                src="/ads/forum_bob_56x56_5.jpg">电竞竞猜投注</a></li>
        <li><a href="https://www.udlutm.com:8888/?agent_code=2943" target="_blank" rel="nofollow"><img
                src="/ads/forum_tb_56x56_2.jpg">天博迎新钜惠</a></li>
        <li><a href="https://www.0lhx7.com:7443/?i_code=9410072" target="_blank" rel="nofollow"><img
                src="/ads/forum_yb_56x56_8.jpg">亚博棋牌赢得精彩</a></li>
        <li><a href="https://www.hqabtjf.com:7700/?agent_code=22124" target="_blank" rel="nofollow"><img
                src="/ads/forum_bob_56x56_9.jpg">天美棋牌回馈赛</a></li>
        <li><a href="https://www.udlutm.com:8888/?agent_code=2943" target="_blank" rel="nofollow"><img
                src="/ads/forum_tb_56x56_1.jpg">克罗地亚国家队</a></li>

    </ul>
</div>


</div>
<div id="wp" class="wp">
    <style id="diy_style" type="text/css"></style>
    <!--[diy=diynavtop]-->
    <div id="diynavtop" class="area"></div><!--[/diy]-->
    <div id="pt" class="bm cl">
        <div class="z">
            <a href="./" class="nvhm" title="首頁">老司機論壇</a><em>&raquo;</em><a href="forum.php">老司機論壇</a>
            <em>&rsaquo;</em> <a href="forum.php?gid=1">綜合交流區</a><em>&rsaquo;</em> <a
                href="forum.php?mod=forumdisplay&fid=36">求福利帶帶我</a>
            <div class="y">
                <a href="search.php?mod=forum" title="搜索" class="xi2"><img src="static/image/common/icon_search.png"
                                                                           style=" position:relative; top:2px;"> 搜索</a>
                <span class="pipe">|</span>
                <a href="home.php?mod=space&amp;do=favorite&amp;view=me" title="我的收藏" class="xi2"><img
                        src="static/image/feed/favorite.gif" style=" position:relative; top:2px;"> 我的收藏</a>
                <span class="pipe">|</span>
                <a href="forum.php?mod=guide&amp;view=my" title="我的帖子" class="xi2"><img
                        src="static/image/feed/article.gif" style=" position:relative; top:3px;"> 我的帖子</a><span
                    class="pipe">|</span><a href="forum.php?mod=guide&amp;view=sofa" title="搶沙發" class="xi2"><img
                    src="static/image/feed/comment.gif" style=" position:relative; top:4px;"> 搶沙發</a></div>
        </div>
    </div>
    <div class="wp">
        <!--[diy=diy1]-->
        <div id="diy1" class="area"></div><!--[/diy]-->
    </div>
    <div class="boardnav">

        <div class="biaoqi_bk_sj biaoqi_ase-gbox cl">

            <div class="forumicn"><img src="data/attachment/common/19/common_36_icon.png" alt="求福利帶帶我"></div>

            <div class="forumbky">
                <div class="forum_top_name">
                    <h1>
                        <a href="forum.php?mod=forumdisplay&amp;fid=36">求福利帶帶我</a>
                        <span>&nbsp;&nbsp;</span>
                    </h1>

                </div>

                <div class="banzhuji">

                    <div class="forum_top_info">

                    <span class="z">
                    	今日: 614<span class="pipe">|</span>主題: 58035</span>

                        <span class="y">
<a href="home.php?mod=spacecp&amp;ac=favorite&amp;type=forum&amp;id=36&amp;handlekey=favoriteforum&amp;formhash=a5beaa79"
   id="a_favorite" class="fa_fav" onclick="showWindow(this.id, this.href, 'get', 0);">收藏本版 <strong class="xi1"
                                                                                                   id="number_favorite">(<span
        id="number_favorite_num">3022</span>)</strong></a>

</span>
                    </div>
                </div>

                <div id="forum_rules_36" style="; float: left; padding-top: 8px;">
                    <div class="ptn" style="font-size:14px;overflow:hidden;">
                        暫無版塊規則說明...
                    </div>
                </div>

            </div>

        </div>


        <div id="ct" class="wp cl ct2">

            <div class="mn">


                <div class="drag">
                    <!--[diy=diy4]-->
                    <div id="diy4" class="area"></div><!--[/diy]-->
                </div>


                <div id="pgt">
                </div>
                <ul id="thread_types" class="ttp bm cl">
                    <li id="ttp_all" class="xw1 a"><a href="forum.php?mod=forumdisplay&amp;fid=36">全部</a></li>
                    <li><a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font><span class="xg1 num">36715</span></a></li>
                    <li><a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=typeid&amp;typeid=5"><font
                            color="#F26C4F">已上车</font><span class="xg1 num">19445</span></a></li>
                    <li><a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=typeid&amp;typeid=6"><font
                            color="Dodgerblue">上车中</font><span class="xg1 num">1820</span></a></li>
                    <li><span class="pipe">|</span></li>
                    <li><a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=sortid&amp;sortid=1">求福利帶帶我<span
                            class="xg1 num">51776</span></a></li>
                </ul>
                <script type="text/javascript">showTypes('thread_types');</script>
                <div id="threadlist" class="tl bm bmw" style="position: relative;">
                    <div class="th">
                        <table cellspacing="0" cellpadding="0">
                            <tr style="background: #fff;">
                                <th colspan="2">
                                    <div class="tf">
                                        <div class="y">
                                            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=lastpost&amp;orderby=lastpost">最新</a>&nbsp;
                                            <span class="pipe">|</span>
                                            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=heat&amp;orderby=heats">熱門</a>&nbsp;
                                            <span class="pipe">|</span>
                                            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=hot">熱帖</a>&nbsp;
                                            <span class="pipe">|</span>
                                            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=digest&amp;digest=1">精華</a>&nbsp;
                                            <span class="pipe">|</span>
                                            <a id="atarget" onclick="setatarget(1)" title="在新窗口中打開帖子"
                                               style="margin-right: 0;">新窗</a>

                                        </div>
                                    </div>


                                    <a id="filter_special" href="javascript:;" class="showmenu xi2"
                                       onclick="showMenu(this.id)">全部主題</a>&nbsp;
                                    <a id="filter_time" href="javascript:;" class="showmenu xi2"
                                       onclick="showMenu(this.id)">全部時間</a>&nbsp;
                                    <a id="filter_orderby" href="javascript:;" class="showmenu xi2"
                                       onclick="showMenu(this.id)">默認排序</a>&nbsp;
                                    <span id="clearstickthread" style="display: none;">
<span class="pipe">|</span>
<a href="javascript:;" onclick="clearStickThread()" class="xi2" title="顯示置頂">顯示置頂</a>
</span>
                    </div>
                    </th>

                    </tr>
                    </table>
                </div>
                <div class="bm_c cl">
                    <script type="text/javascript">var lasttime = 1655634117;
                    var listcolspan = '5';</script>
                    <div id="forumnew" style="display:none"></div>
                    <form method="post" autocomplete="off" name="moderate" id="moderate"
                          action="forum.php?mod=topicadmin&amp;action=moderate&amp;fid=36&amp;infloat=yes&amp;nopost=yes">
                        <input type="hidden" name="formhash" value="a5beaa79"/>
                        <input type="hidden" name="listextra" value="page%3D1"/>
                        <table summary="forum_36" cellspacing="0" cellpadding="0" id="threadlisttableid">
                            <tbody>
                            <tr>
                                <th>
                                    <div class="post_avatar"><a href="home.php?mod=space&amp;uid=1" target="_blank"><img
                                            src="https://uc.javbus22.com/uc/data/avatar/000/00/00/01_avatar_small.jpg"
                                            onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_small.gif'"/></a>
                                    </div>
                                    <div class=" post_infolist">
                                        <div class="post_infolist_tit">[公告] <a
                                                href="forum.php?mod=announcement&amp;id=6#6" target="_blank">請勿無中生友，幫別人求福利</a></strong>
                                        </div>
                                        <div class="post_infolist_other">
                                            <div class="author" style="float: left;margin-right: 15px;">
                                                <a href="home.php?mod=space&amp;uid=1" c="1">管理員</a></div>
                                            <span class="time">發佈於&nbsp;&nbsp;&nbsp;2020-7-27</span>
                                        </div>
                                    </div>
                                </th>
                            </tr>
                            </tbody>
                            <tbody id="stickthread_15172">
                            <tr>
                                <th style="">
                                    <div class="post_avatar_pin">
                                        <em class="avatar_pin_ico"><img src="template/javbus/images/pin_a3.png"
                                                                        alt="全局置頂" align="absmiddle" width="40"
                                                                        height="39"/></em>

                                        <div class="post_avatar">
                                            <a href="home.php?mod=space&amp;uid=1" target="_blank"><img
                                                    src="https://uc.javbus22.com/uc/data/avatar/000/00/00/01_avatar_middle.jpg"
                                                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
                                        </div>

                                    </div>
                                    <div class="post_inforight">
                                        <div class="post_infolist" style="width: 745px;">
                                            <div class="post_infolist_tit">

                                                <a href="javascript:;" id="content_15172" class="showcontent y"
                                                   title="更多操作"
                                                   onclick="CONTENT_TID='15172';CONTENT_ID='stickthread_15172';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>
                                                <a href="javascript:void(0);" onclick="hideStickThread('15172')"
                                                   class="showhide y" title="隱藏置頂帖">隱藏置頂帖</a></em>

                                                <a href="forum.php?mod=viewthread&amp;tid=15172&amp;extra=page%3D1"
                                                   style="font-weight: bold;color: #2B65B7;" onclick="atarget(this)"
                                                   class="s">新註冊會員無法回貼或發帖 + 司機等級說明</a>
                                                <a href="forum.php?mod=viewthread&amp;tid=15172&amp;extra=page%3D1"
                                                   title="全局置頂主題 - 新窗口打開" target="_blank" class="displayorder_3">
                                                </a>
                                                <span class="tps">&nbsp;...<a
                                                        href="forum.php?mod=viewthread&tid=15172&amp;extra=page%3D1&amp;page=2">2</a><a
                                                        href="forum.php?mod=viewthread&tid=15172&amp;extra=page%3D1&amp;page=3">3</a><a
                                                        href="forum.php?mod=viewthread&tid=15172&amp;extra=page%3D1&amp;page=4">4</a><a
                                                        href="forum.php?mod=viewthread&tid=15172&amp;extra=page%3D1&amp;page=5">5</a><a
                                                        href="forum.php?mod=viewthread&tid=15172&amp;extra=page%3D1&amp;page=6">6</a>..<a
                                                        href="forum.php?mod=viewthread&tid=15172&amp;extra=page%3D1&amp;page=126">126</a></span>
                                            </div>
                                        </div>

                                        <div class="post_infolist_other">
                                            <div class="z">
                                                <span class="author">         <a href="home.php?mod=space&amp;uid=1"
                                                                                 c="1">管理員</a>              </span>@
                                                <span class="dateline">2017-9-9</span>
                                            </div>

                                            <div class="z nums" style="padding-left: 25px;">
                                                <span class="views">472264</span>
                                                <span class="reply">1882</span>
                                            </div>

                                            <span class="time y"><a href="home.php?mod=space&username=qwerasd123" c="1">qwerasd123</a>			<span>@</span><span><span
                                                    title="2022-6-19 04:30">13&nbsp;小時前</span></span></span>

                                        </div>
                                    </div>
                </div>
                </th>
                </tr>
                </tbody>
                <tbody id="stickthread_462">
                <tr>
                    <th style="">
                        <div class="post_avatar_pin">
                            <em class="avatar_pin_ico"><img src="template/javbus/images/pin_a3.png" alt="全局置頂"
                                                            align="absmiddle" width="40" height="39"/></em>

                            <div class="post_avatar">
                                <a href="home.php?mod=space&amp;uid=1" target="_blank"><img
                                        src="https://uc.javbus22.com/uc/data/avatar/000/00/00/01_avatar_middle.jpg"
                                        onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
                            </div>

                        </div>
                        <div class="post_inforight">
                            <div class="post_infolist" style="width: 745px;">
                                <div class="post_infolist_tit">

                                    <a href="javascript:;" id="content_462" class="showcontent y" title="更多操作"
                                       onclick="CONTENT_TID='462';CONTENT_ID='stickthread_462';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>
                                    <a href="javascript:void(0);" onclick="hideStickThread('462')" class="showhide y"
                                       title="隱藏置頂帖">隱藏置頂帖</a></em>

                                    <a href="forum.php?mod=viewthread&amp;tid=462&amp;extra=page%3D1"
                                       onclick="atarget(this)" class="s">網站訪問加載速度調查</a>
                                    <a href="forum.php?mod=viewthread&amp;tid=462&amp;extra=page%3D1"
                                       title="全局置頂主題 - 新窗口打開" target="_blank" class="displayorder_3">
                                    </a>
                                    <span class="tps">&nbsp;...<a
                                            href="forum.php?mod=viewthread&tid=462&amp;extra=page%3D1&amp;page=2">2</a><a
                                            href="forum.php?mod=viewthread&tid=462&amp;extra=page%3D1&amp;page=3">3</a><a
                                            href="forum.php?mod=viewthread&tid=462&amp;extra=page%3D1&amp;page=4">4</a><a
                                            href="forum.php?mod=viewthread&tid=462&amp;extra=page%3D1&amp;page=5">5</a><a
                                            href="forum.php?mod=viewthread&tid=462&amp;extra=page%3D1&amp;page=6">6</a>..<a
                                            href="forum.php?mod=viewthread&tid=462&amp;extra=page%3D1&amp;page=66">66</a></span>
                                </div>
                            </div>

                            <div class="post_infolist_other">
                                <div class="z">
                                    <span class="author">         <a href="home.php?mod=space&amp;uid=1" c="1">管理員</a>              </span>@
                                    <span class="dateline">2015-12-27</span>
                                </div>

                                <div class="z nums" style="padding-left: 25px;">
                                    <span class="views">148034</span>
                                    <span class="reply">984</span>
                                </div>

                                <span class="time y"><a href="home.php?mod=space&username=abc375223506" c="1">abc375223506</a>			<span>@</span><span><span
                                        title="2022-6-17 22:09">前天&nbsp;22:09</span></span></span>

                            </div>
                        </div>
            </div>
            </th>
            </tr>
            </tbody>
            <tbody id="separatorline">
            <tr class="ts" style="background: #f5f5f5;height: 40px;line-height: 40px;">
                <th>
                    <div style="text-align: center;"><a href="javascript:;" onclick="checkForumnew_btn('36')"
                                                        title="查看更新" class="forumrefresh"
                                                        style="font-size: 16px">版塊主題</a></div>
                </th>
            </tr>
            </tbody>
            <script type="text/javascript">hideStickThread();</script>
            <tbody id="normalthread_100861">
            <tr>
                <th style="">
                    <div class="post_avatar">
                        <a href="home.php?mod=space&amp;uid=332575" target="_blank"><img
                                src="https://uc.javbus22.com/uc/data/avatar/000/33/25/75_avatar_middle.jpg"
                                onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
                    </div>
                    <div class="post_inforight">
                        <div class="post_infolist" style="width: 745px;">
                            <div class="post_infolist_tit">

                                <a href="javascript:;" id="content_100861" class="showcontent y" title="更多操作"
                                   onclick="CONTENT_TID='100861';CONTENT_ID='normalthread_100861';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                                <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                                        color="Forestgreen">带带我</font></a>]</em> <a
                                    href="forum.php?mod=viewthread&amp;tid=100861&amp;extra=page%3D1"
                                    onclick="atarget(this)" class="s">有没有老司机帮帮我</a>
                                <a href="forum.php?mod=viewthread&amp;tid=100861&amp;extra=page%3D1"
                                   title="有新回復 - 新窗口打開" target="_blank" class="">
                                </a>
                                - <span class="xi1">[回帖獎勵 <strong> 1</strong> ]</span>
                                <a href="forum.php?mod=redirect&amp;tid=100861&amp;goto=lastpost#lastpost" class="xi1">New</a>
                            </div>
                        </div>

                        <div class="post_infolist_other">
                            <div class="z">
                                <span class="author">         <a href="home.php?mod=space&amp;uid=332575" c="1">sd21080503</a>              </span>@
                                <span class="dateline"><span title="2022-6-19">1&nbsp;小時前</span></span>
                            </div>

                            <div class="z nums" style="padding-left: 25px;">
                                <span class="views">316</span>
                                <span class="reply">10</span>
                            </div>

                            <span class="time y"><a href="home.php?mod=space&username=sd21080503" c="1">sd21080503</a>			<span>@</span><span><span
                                    title="2022-6-19 18:21">9&nbsp;秒前</span></span></span>

                        </div>
                    </div>
        </div>
        </th>
        </tr>
        </tbody>
        <tbody id="normalthread_100265">
        <tr>
            <th style="">
                <div class="post_avatar">
                    <a href="home.php?mod=space&amp;uid=94496" target="_blank"><img
                            src="https://uc.javbus22.com/uc/data/avatar/000/09/44/96_avatar_middle.jpg"
                            onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
                </div>
                <div class="post_inforight">
                    <div class="post_infolist" style="width: 745px;">
                        <div class="post_infolist_tit">

                            <a href="javascript:;" id="content_100265" class="showcontent y" title="更多操作"
                               onclick="CONTENT_TID='100265';CONTENT_ID='normalthread_100265';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                            <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                                    color="Forestgreen">带带我</font></a>]</em> <a
                                href="forum.php?mod=viewthread&amp;tid=100265&amp;extra=page%3D1"
                                onclick="atarget(this)" class="s">在推上看到的妹子，有没有老司机有全套</a>
                            <a href="forum.php?mod=viewthread&amp;tid=100265&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                               target="_blank" class="">
                            </a>
                            <span class="tps">&nbsp;...<a
                                    href="forum.php?mod=viewthread&tid=100265&amp;extra=page%3D1&amp;page=2">2</a><a
                                    href="forum.php?mod=viewthread&tid=100265&amp;extra=page%3D1&amp;page=3">3</a></span>
                            <br><a href=forum.php?mod=viewthread&tid=100265><img
                                src='data/attachment/forum/thumbs/202206/stiGQQO.png'
                                style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                                href=forum.php?mod=viewthread&tid=100265><img
                                src='data/attachment/forum/thumbs/202206/2L9TRTL.png'
                                style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                                href=forum.php?mod=viewthread&tid=100265><img
                                src='data/attachment/forum/thumbs/202206/aRJZufs.jpg'
                                style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a>
                        </div>
                    </div>

                    <div class="post_infolist_other">
                        <div class="z">
                            <span class="author">         <a href="home.php?mod=space&amp;uid=94496" c="1">cs6031667</a>              </span>@
                            <span class="dateline">2022-6-5</span>
                        </div>

                        <div class="z nums" style="padding-left: 25px;">
                            <span class="views">26650</span>
                            <span class="reply">36</span>
                        </div>

                        <span class="time y"><a href="home.php?mod=space&username=qsqsqs"
                                                c="1">qsqsqs</a>			<span>@</span><span><span
                                title="2022-6-19 18:19">2&nbsp;分鐘前</span></span></span>

                    </div>
                </div>
    </div>
    </th>
    </tr>
    </tbody>
    <tbody id="normalthread_100023">
    <tr>
        <th style="">
            <div class="post_avatar">
                <a href="home.php?mod=space&amp;uid=381283" target="_blank"><img
                        src="https://uc.javbus22.com/uc/data/avatar/000/38/12/83_avatar_middle.jpg"
                        onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
            </div>
            <div class="post_inforight">
                <div class="post_infolist" style="width: 745px;">
                    <div class="post_infolist_tit">

                        <a href="javascript:;" id="content_100023" class="showcontent y" title="更多操作"
                           onclick="CONTENT_TID='100023';CONTENT_ID='normalthread_100023';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                        <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=5"><font
                                color="#F26C4F">已上车</font></a>]</em> <a
                            href="forum.php?mod=viewthread&amp;tid=100023&amp;extra=page%3D1" onclick="atarget(this)"
                            class="s">求一个影片的番号</a>
                        <a href="forum.php?mod=viewthread&amp;tid=100023&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                           target="_blank" class="">
                        </a>
                        <img src="static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle"/>
                        <span class="tps">&nbsp;...<a
                                href="forum.php?mod=viewthread&tid=100023&amp;extra=page%3D1&amp;page=2">2</a><a
                                href="forum.php?mod=viewthread&tid=100023&amp;extra=page%3D1&amp;page=3">3</a><a
                                href="forum.php?mod=viewthread&tid=100023&amp;extra=page%3D1&amp;page=4">4</a><a
                                href="forum.php?mod=viewthread&tid=100023&amp;extra=page%3D1&amp;page=5">5</a><a
                                href="forum.php?mod=viewthread&tid=100023&amp;extra=page%3D1&amp;page=6">6</a>..<a
                                href="forum.php?mod=viewthread&tid=100023&amp;extra=page%3D1&amp;page=7">7</a></span>
                        <br><a href=forum.php?mod=viewthread&tid=100023><img
                            src='data/attachment/forum/thumbs/202205/OmfLxe0.jpg'
                            style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a>
                    </div>
                </div>

                <div class="post_infolist_other">
                    <div class="z">
                        <span class="author">         <a href="home.php?mod=space&amp;uid=381283" c="1">zik-peach</a>              </span>@
                        <span class="dateline">2022-5-31</span>
                    </div>

                    <div class="z nums" style="padding-left: 25px;">
                        <span class="views">57958</span>
                        <span class="reply">92</span>
                    </div>

                    <span class="time y"><a href="home.php?mod=space&username=qsqsqs" c="1">qsqsqs</a>			<span>@</span><span><span
                            title="2022-6-19 18:16">5&nbsp;分鐘前</span></span></span>

                </div>
            </div>
</div>
</th>
</tr>
</tbody>
<tbody id="normalthread_100857">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=295468" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/29/54/68_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100857" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100857';CONTENT_ID='normalthread_100857';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100857&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">求个国产视频的磁力，视频大概一两分钟</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100857&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100857&amp;extra=page%3D1&amp;page=2">2</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100857&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100857><img
                        src='data/attachment/forum/thumbs/202206/i4yGKwh.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=295468" c="1">咸鱼楠</a>              </span>@
                    <span class="dateline"><span title="2022-6-19">3&nbsp;小時前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">8851</span>
                    <span class="reply">16</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=dnwyl2021"
                                        c="1">dnwyl2021</a>			<span>@</span><span><span
                        title="2022-6-19 18:15">6&nbsp;分鐘前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100843">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=149951" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/14/99/51_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100843" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100843';CONTENT_ID='normalthread_100843';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100843&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">这是田中瞳哪部作品啊</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100843&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <a href="forum.php?mod=redirect&amp;tid=100843&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100843><img
                        src='data/attachment/forum/thumbs/202206/AtZtnFT.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=149951" c="1">vvb148</a>              </span>@
                    <span class="dateline"><span title="2022-6-19">2&nbsp;小時前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">2877</span>
                    <span class="reply">7</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=timzhao1983" c="1">timzhao1983</a>			<span>@</span><span><span
                        title="2022-6-19 18:14">7&nbsp;分鐘前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100794">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=295058" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/29/50/58_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100794" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100794';CONTENT_ID='normalthread_100794';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100794&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">求p站NicoLove妮可一个正片</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100794&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <a href="forum.php?mod=redirect&amp;tid=100794&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100794><img
                        src='data/attachment/forum/thumbs/202206/D6VUoFi.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=295058" c="1">shuaizi98</a>              </span>@
                    <span class="dateline"><span title="2022-6-18">昨天&nbsp;16:45</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">9836</span>
                    <span class="reply">8</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=%E7%96%AF%E7%8B%82%E7%9A%84%E4%BB%93%E9%BC%A0"
                                        c="1">疯狂的仓鼠</a>			<span>@</span><span><span title="2022-6-19 18:13">8&nbsp;分鐘前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100365">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=308996" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/30/89/96_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100365" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100365';CONTENT_ID='normalthread_100365';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=5"><font
                            color="#F26C4F">已上车</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100365&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">电报群看到的图片，眼神勾魂，太顶</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100365&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <img src="template/javbus/images/hot.jpg" align="absmiddle" alt="heatlevel" title="熱度: 641"/>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100365&amp;extra=page%3D1&amp;page=2">2</a><a
                            href="forum.php?mod=viewthread&tid=100365&amp;extra=page%3D1&amp;page=3">3</a><a
                            href="forum.php?mod=viewthread&tid=100365&amp;extra=page%3D1&amp;page=4">4</a><a
                            href="forum.php?mod=viewthread&tid=100365&amp;extra=page%3D1&amp;page=5">5</a><a
                            href="forum.php?mod=viewthread&tid=100365&amp;extra=page%3D1&amp;page=6">6</a>..<a
                            href="forum.php?mod=viewthread&tid=100365&amp;extra=page%3D1&amp;page=9">9</a></span>
                    <br><a href=forum.php?mod=viewthread&tid=100365><img
                        src='data/attachment/forum/thumbs/202206/w03Czbx.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100365><img
                        src='data/attachment/forum/thumbs/202206/Vk2D2PU.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100365><img
                        src='data/attachment/forum/thumbs/202206/5FqjKhM.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=308996" c="1">Aigonl</a>              </span>@
                    <span class="dateline">2022-6-8</span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">117955</span>
                    <span class="reply">127</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=qsqsqs"
                                        c="1">qsqsqs</a>			<span>@</span><span><span title="2022-6-19 18:10">11&nbsp;分鐘前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100858">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=333051" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/33/30/51_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100858" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100858';CONTENT_ID='normalthread_100858';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100858&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">这个姿势好神奇！就十分好奇是Julia哪一部啊！</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100858&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100858&amp;extra=page%3D1&amp;page=2">2</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100858&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100858><img
                        src='data/attachment/forum/thumbs/202206/IDCY6vd.png'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=333051" c="1">cced0952</a>              </span>@
                    <span class="dateline"><span title="2022-6-19">3&nbsp;小時前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">9467</span>
                    <span class="reply">23</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=Liverbird"
                                        c="1">Liverbird</a>			<span>@</span><span><span
                        title="2022-6-19 18:09">12&nbsp;分鐘前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100711">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=452916" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/45/29/16_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100711" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100711';CONTENT_ID='normalthread_100711';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100711&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">求FC2这个卖家的母乳系列</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100711&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <img src="static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle"/>
                    <img src="template/javbus/images/hot.jpg" align="absmiddle" alt="heatlevel" title="熱度: 551"/>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100711&amp;extra=page%3D1&amp;page=2">2</a><a
                            href="forum.php?mod=viewthread&tid=100711&amp;extra=page%3D1&amp;page=3">3</a><a
                            href="forum.php?mod=viewthread&tid=100711&amp;extra=page%3D1&amp;page=4">4</a><a
                            href="forum.php?mod=viewthread&tid=100711&amp;extra=page%3D1&amp;page=5">5</a><a
                            href="forum.php?mod=viewthread&tid=100711&amp;extra=page%3D1&amp;page=6">6</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100711&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100711><img
                        src='data/attachment/forum/thumbs/202206/PsaEX7m.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100711><img
                        src='data/attachment/forum/thumbs/202206/hni53R6.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100711><img
                        src='data/attachment/forum/thumbs/202206/sFZZl5m.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=452916" c="1"><span
                            class="__cf_email__" data-cfemail="de92adb4b2aa9eeceeecef">[email&#160;protected]</span></a>              </span>@
                    <span class="dateline"><span title="2022-6-16">3&nbsp;天前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">66193</span>
                    <span class="reply">87</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=Lsjlt%402021" c="1"><span class="__cf_email__"
                                                                                                    data-cfemail="3f734c55534b7f0d0f0d0e">[email&#160;protected]</span></a>			<span>@</span><span><span
                        title="2022-6-19 18:05">16&nbsp;分鐘前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100842">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=145217" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/14/52/17_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100842" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100842';CONTENT_ID='normalthread_100842';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100842&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">求张贺玉(HeyuZhang)旁边这位网红的信息</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100842&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100842&amp;extra=page%3D1&amp;page=2">2</a><a
                            href="forum.php?mod=viewthread&tid=100842&amp;extra=page%3D1&amp;page=3">3</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100842&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100842><img
                        src='data/attachment/forum/thumbs/202206/0lK3eGX.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100842><img
                        src='data/attachment/forum/thumbs/202206/VpEAINZ.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100842><img
                        src='data/attachment/forum/thumbs/202206/4BMTvZM.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=145217" c="1">Watanabe17</a>              </span>@
                    <span class="dateline"><span title="2022-6-19">8&nbsp;小時前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">15127</span>
                    <span class="reply">31</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=549343852ye" c="1">549343852ye</a>			<span>@</span><span><span
                        title="2022-6-19 18:02">19&nbsp;分鐘前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100853">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=329560" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/32/95/60_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100853" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100853';CONTENT_ID='normalthread_100853';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100853&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">看到个动图心痒痒求资源</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100853&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <img src="static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle"/>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100853&amp;extra=page%3D1&amp;page=2">2</a><a
                            href="forum.php?mod=viewthread&tid=100853&amp;extra=page%3D1&amp;page=3">3</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100853&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100853><img
                        src='data/attachment/forum/thumbs/202206/CyqMPYB.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=329560" c="1">sd4563077</a>              </span>@
                    <span class="dateline"><span title="2022-6-19">4&nbsp;小時前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">14054</span>
                    <span class="reply">32</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=549343852ye" c="1">549343852ye</a>			<span>@</span><span><span
                        title="2022-6-19 17:43">半小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100827">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=298406" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/29/84/06_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100827" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100827';CONTENT_ID='normalthread_100827';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100827&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">求图片茶馆上看到的眼睛巨乳小姐姐</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100827&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <a href="forum.php?mod=redirect&amp;tid=100827&amp;goto=lastpost#lastpost" class="xi1">New</a>
                </div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=298406" c="1">tankyousb</a>              </span>@
                    <span class="dateline"><span title="2022-6-19">17&nbsp;小時前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">2364</span>
                    <span class="reply">7</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=135351"
                                        c="1">135351</a>			<span>@</span><span><span title="2022-6-19 17:40">半小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100863">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=229509" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/22/95/09_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100863" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100863';CONTENT_ID='normalthread_100863';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100863&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">求森山杏菜这部的资源</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100863&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <a href="forum.php?mod=redirect&amp;tid=100863&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100863><img
                        src='data/attachment/forum/thumbs/202206/aumbk8W.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=229509" c="1">qswl1234</a>              </span>@
                    <span class="dateline"><span title="2022-6-19">半小時前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">797</span>
                    <span class="reply">1</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=qswl1234" c="1">qswl1234</a>			<span>@</span><span><span
                        title="2022-6-19 17:31">半小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100801">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=353182" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/35/31/82_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100801" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100801';CONTENT_ID='normalthread_100801';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100801&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">救救孩子吧，她真的好好看</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100801&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <img src="template/javbus/images/hot.jpg" align="absmiddle" alt="heatlevel" title="熱度: 249"/>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100801&amp;extra=page%3D1&amp;page=2">2</a><a
                            href="forum.php?mod=viewthread&tid=100801&amp;extra=page%3D1&amp;page=3">3</a><a
                            href="forum.php?mod=viewthread&tid=100801&amp;extra=page%3D1&amp;page=4">4</a><a
                            href="forum.php?mod=viewthread&tid=100801&amp;extra=page%3D1&amp;page=5">5</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100801&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100801><img
                        src='data/attachment/forum/thumbs/202206/5tTUTEp.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100801><img
                        src='data/attachment/forum/thumbs/202206/B320EOp.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100801><img
                        src='data/attachment/forum/thumbs/202206/IJQbLZ0.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=353182" c="1">deepdarkfantacy</a>              </span>@
                    <span class="dateline"><span title="2022-6-18">昨天&nbsp;16:48</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">71767</span>
                    <span class="reply">61</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=%E7%A1%AC%E5%BE%97%E4%B8%80%E6%B7%AB%E9%80%BC"
                                        c="1">硬得一淫逼</a>			<span>@</span><span><span title="2022-6-19 17:30">半小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100862">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=36896" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/03/68/96_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100862" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100862';CONTENT_ID='normalthread_100862';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100862&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">老司机能不能帮我找到这部風間ゆみ片子 谢谢</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100862&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <a href="forum.php?mod=redirect&amp;tid=100862&amp;goto=lastpost#lastpost" class="xi1">New</a>
                </div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=36896" c="1">thmxh</a>              </span>@
                    <span class="dateline"><span title="2022-6-19">半小時前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">281</span>
                    <span class="reply">1</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=thmxh"
                                        c="1">thmxh</a>			<span>@</span><span><span title="2022-6-19 17:30">半小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100816">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=372934" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/37/29/34_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100816" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100816';CONTENT_ID='normalthread_100816';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100816&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">求艺术小雅的视频</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100816&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100816&amp;extra=page%3D1&amp;page=2">2</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100816&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100816><img
                        src='data/attachment/forum/thumbs/202206/844N3Ff.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=372934" c="1">2786636170</a>              </span>@
                    <span class="dateline"><span title="2022-6-19">17&nbsp;小時前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">12555</span>
                    <span class="reply">22</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=2633470135"
                                        c="1">2633470135</a>			<span>@</span><span><span
                        title="2022-6-19 17:28">半小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100547">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=360508" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/36/05/08_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100547" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100547';CONTENT_ID='normalthread_100547';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=5"><font
                            color="#F26C4F">已上车</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100547&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">求此探花、看起来很合口味</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100547&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <img src="template/javbus/images/hot.jpg" align="absmiddle" alt="heatlevel" title="熱度: 342"/>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100547&amp;extra=page%3D1&amp;page=2">2</a><a
                            href="forum.php?mod=viewthread&tid=100547&amp;extra=page%3D1&amp;page=3">3</a><a
                            href="forum.php?mod=viewthread&tid=100547&amp;extra=page%3D1&amp;page=4">4</a><a
                            href="forum.php?mod=viewthread&tid=100547&amp;extra=page%3D1&amp;page=5">5</a><a
                            href="forum.php?mod=viewthread&tid=100547&amp;extra=page%3D1&amp;page=6">6</a>..<a
                            href="forum.php?mod=viewthread&tid=100547&amp;extra=page%3D1&amp;page=7">7</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100547&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100547><img
                        src='data/attachment/forum/thumbs/202206/eWQfcXK.png'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100547><img
                        src='data/attachment/forum/thumbs/202206/8d52Ens.png'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=360508" c="1">88093767</a>              </span>@
                    <span class="dateline"><span title="2022-6-12">7&nbsp;天前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">80992</span>
                    <span class="reply">95</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=hao5989589"
                                        c="1">hao5989589</a>			<span>@</span><span><span
                        title="2022-6-19 17:04">1&nbsp;小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100736">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=384615" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/38/46/15_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100736" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100736';CONTENT_ID='normalthread_100736';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100736&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">115转存失败。版本目前是3.5版本，求最新版</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100736&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <img src="static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle"/>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100736&amp;extra=page%3D1&amp;page=2">2</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100736&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100736><img
                        src='data/attachment/forum/thumbs/202206/rtbNp5R.png'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=384615" c="1">416019273</a>              </span>@
                    <span class="dateline"><span title="2022-6-17">前天&nbsp;07:05</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">2703</span>
                    <span class="reply">25</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=formum"
                                        c="1">formum</a>			<span>@</span><span><span title="2022-6-19 16:47">1&nbsp;小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100472">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=338031" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/33/80/31_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100472" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100472';CONTENT_ID='normalthread_100472';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=6"><font
                            color="Dodgerblue">上车中</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100472&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">社保漫画，可惜不知道出处和作者，希望大伙集思广益</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100472&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <img src="template/javbus/images/hot.jpg" align="absmiddle" alt="heatlevel" title="熱度: 395"/>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100472&amp;extra=page%3D1&amp;page=2">2</a><a
                            href="forum.php?mod=viewthread&tid=100472&amp;extra=page%3D1&amp;page=3">3</a><a
                            href="forum.php?mod=viewthread&tid=100472&amp;extra=page%3D1&amp;page=4">4</a><a
                            href="forum.php?mod=viewthread&tid=100472&amp;extra=page%3D1&amp;page=5">5</a><a
                            href="forum.php?mod=viewthread&tid=100472&amp;extra=page%3D1&amp;page=6">6</a>..<a
                            href="forum.php?mod=viewthread&tid=100472&amp;extra=page%3D1&amp;page=7">7</a></span>
                    <br><a href=forum.php?mod=viewthread&tid=100472><img
                        src='data/attachment/forum/thumbs/202206/CHrgqbC.png'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100472><img
                        src='data/attachment/forum/thumbs/202206/FBYZ0mp.png'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100472><img
                        src='data/attachment/forum/thumbs/202206/MLxHPeC.png'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=338031" c="1">2310780838</a>              </span>@
                    <span class="dateline">2022-6-11</span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">96709</span>
                    <span class="reply">104</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=slience2019" c="1">slience2019</a>			<span>@</span><span><span
                        title="2022-6-19 16:35">1&nbsp;小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100850">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=152532" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/15/25/32_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100850" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100850';CONTENT_ID='normalthread_100850';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100850&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">老司机们有没有自己撸了会腰疼，跟老婆做就不会？</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100850&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100850&amp;extra=page%3D1&amp;page=2">2</a><a
                            href="forum.php?mod=viewthread&tid=100850&amp;extra=page%3D1&amp;page=3">3</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100850&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100850><img
                        src='data/attachment/forum/thumbs/202206/aRFjDRQ.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=152532" c="1">aklimingyang</a>              </span>@
                    <span class="dateline"><span title="2022-6-19">5&nbsp;小時前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">12486</span>
                    <span class="reply">30</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=zpspx"
                                        c="1">zpspx</a>			<span>@</span><span><span title="2022-6-19 16:32">1&nbsp;小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100838">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=136291" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/13/62/91_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100838" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100838';CONTENT_ID='normalthread_100838';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100838&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">求一个欧美女主播的视频</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100838&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100838&amp;extra=page%3D1&amp;page=2">2</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100838&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100838><img
                        src='data/attachment/forum/thumbs/202206/6AxWdnI.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=136291" c="1">瑞1949</a>              </span>@
                    <span class="dateline"><span title="2022-6-19">14&nbsp;小時前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">11716</span>
                    <span class="reply">27</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=721252750"
                                        c="1">721252750</a>			<span>@</span><span><span
                        title="2022-6-19 16:22">1&nbsp;小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100804">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=200279" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/20/02/79_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100804" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100804';CONTENT_ID='normalthread_100804';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100804&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">可爱知性的韩国小姐姐裸舞</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100804&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100804&amp;extra=page%3D1&amp;page=2">2</a><a
                            href="forum.php?mod=viewthread&tid=100804&amp;extra=page%3D1&amp;page=3">3</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100804&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100804><img
                        src='data/attachment/forum/thumbs/202206/aJS1OHK.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100804><img
                        src='data/attachment/forum/thumbs/202206/ZRFqysB.png'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100804><img
                        src='data/attachment/forum/thumbs/202206/6boErKg.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=200279" c="1">MrRoughJhon</a>              </span>@
                    <span class="dateline"><span title="2022-6-18">昨天&nbsp;17:21</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">18075</span>
                    <span class="reply">38</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=MrRoughJhon" c="1">MrRoughJhon</a>			<span>@</span><span><span
                        title="2022-6-19 16:18">2&nbsp;小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100379">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=204118" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/20/41/18_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100379" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100379';CONTENT_ID='normalthread_100379';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100379&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">大佬们 求助telegram电脑端登不上去</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100379&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100379&amp;extra=page%3D1&amp;page=2">2</a><a
                            href="forum.php?mod=viewthread&tid=100379&amp;extra=page%3D1&amp;page=3">3</a><a
                            href="forum.php?mod=viewthread&tid=100379&amp;extra=page%3D1&amp;page=4">4</a></span>
                    <br><a href=forum.php?mod=viewthread&tid=100379><img
                        src='data/attachment/forum/thumbs/202206/teIaNDY.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100379><img
                        src='data/attachment/forum/thumbs/202206/EqLjptz.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100379><img
                        src='data/attachment/forum/thumbs/202206/I8kn4B4.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=204118" c="1">yyt321</a>              </span>@
                    <span class="dateline">2022-6-8</span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">7686</span>
                    <span class="reply">49</span>
                </div>

                <span class="time y"><a
                        href="home.php?mod=space&username=%E5%90%83%E4%B8%8D%E8%83%96%E7%9A%84%E6%87%92%E7%BE%8A%E7%BE%8A"
                        c="1">吃不胖的懒羊羊</a>			<span>@</span><span><span title="2022-6-19 16:12">2&nbsp;小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100752">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=310721" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/31/07/21_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100752" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100752';CONTENT_ID='normalthread_100752';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100752&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">求部比较特别的步肛交片</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100752&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100752&amp;extra=page%3D1&amp;page=2">2</a><a
                            href="forum.php?mod=viewthread&tid=100752&amp;extra=page%3D1&amp;page=3">3</a><a
                            href="forum.php?mod=viewthread&tid=100752&amp;extra=page%3D1&amp;page=4">4</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100752&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100752><img
                        src='data/attachment/forum/thumbs/202206/xKRiVF6.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100752><img
                        src='data/attachment/forum/thumbs/202206/x6wHwTU.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=310721" c="1">steamboy</a>              </span>@
                    <span class="dateline"><span title="2022-6-17">前天&nbsp;12:40</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">13711</span>
                    <span class="reply">51</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=slience2019" c="1">slience2019</a>			<span>@</span><span><span
                        title="2022-6-19 16:12">2&nbsp;小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100828">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=130165" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/13/01/65_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100828" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100828';CONTENT_ID='normalthread_100828';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=5"><font
                            color="#F26C4F">已上车</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100828&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">求爸爸猜女儿 RCT-236 D位置女优信息</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100828&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100828&amp;extra=page%3D1&amp;page=2">2</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100828&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100828><img
                        src='data/attachment/forum/thumbs/202206/XT1CkC5.png'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100828><img
                        src='data/attachment/forum/thumbs/202206/wpjCaTG.png'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=130165" c="1">PeterZzz</a>              </span>@
                    <span class="dateline"><span title="2022-6-19">17&nbsp;小時前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">10451</span>
                    <span class="reply">18</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=joey067"
                                        c="1">joey067</a>			<span>@</span><span><span title="2022-6-19 16:09">2&nbsp;小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100765">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=13048" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/01/30/48_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100765" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100765';CONTENT_ID='normalthread_100765';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100765&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">求助车神这部片子的番号，谢谢了！</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100765&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100765&amp;extra=page%3D1&amp;page=2">2</a><a
                            href="forum.php?mod=viewthread&tid=100765&amp;extra=page%3D1&amp;page=3">3</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100765&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100765><img
                        src='data/attachment/forum/thumbs/202206/hECOXfz.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100765><img
                        src='data/attachment/forum/thumbs/202206/QZOWEVK.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100765><img
                        src='data/attachment/forum/thumbs/202206/CQ6EfaA.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=13048" c="1">zw798108</a>              </span>@
                    <span class="dateline"><span title="2022-6-17">前天&nbsp;18:26</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">23957</span>
                    <span class="reply">33</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=Mark123321"
                                        c="1">Mark123321</a>			<span>@</span><span><span
                        title="2022-6-19 16:08">2&nbsp;小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100452">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=301795" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/30/17/95_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100452" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100452';CONTENT_ID='normalthread_100452';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=5"><font
                            color="#F26C4F">已上车</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100452&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">求大神@aww0517带带我</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100452&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <img src="template/javbus/images/hot.jpg" align="absmiddle" alt="heatlevel" title="熱度: 216"/>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100452&amp;extra=page%3D1&amp;page=2">2</a></span>
                    <br><a href=forum.php?mod=viewthread&tid=100452><img
                        src='data/attachment/forum/thumbs/202206/ey2dpGV.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=301795" c="1">良人归来</a>              </span>@
                    <span class="dateline">2022-6-10</span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">35740</span>
                    <span class="reply">28</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=slience2019" c="1">slience2019</a>			<span>@</span><span><span
                        title="2022-6-19 16:07">2&nbsp;小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100837">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=382754" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/38/27/54_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100837" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100837';CONTENT_ID='normalthread_100837';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100837&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">豊彦修复版本有人保存过吗？</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100837&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <img src="static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle"/>
                    <a href="forum.php?mod=redirect&amp;tid=100837&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100837><img
                        src='data/attachment/forum/thumbs/202206/updmKD9.png'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=382754" c="1">dafgaq123123</a>              </span>@
                    <span class="dateline"><span title="2022-6-19">15&nbsp;小時前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">6021</span>
                    <span class="reply">7</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=shakelove"
                                        c="1">shakelove</a>			<span>@</span><span><span
                        title="2022-6-19 16:00">2&nbsp;小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100661">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=360539" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/36/05/39_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100661" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100661';CONTENT_ID='normalthread_100661';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100661&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">太刺激了！！！跪求资源</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100661&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <img src="static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle"/>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100661&amp;extra=page%3D1&amp;page=2">2</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100661&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100661><img
                        src='data/attachment/forum/thumbs/202206/AjxtQHa.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100661><img
                        src='data/attachment/forum/thumbs/202206/OdReG49.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100661><img
                        src='data/attachment/forum/thumbs/202206/A3NrLjN.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=360539" c="1">zl469</a>              </span>@
                    <span class="dateline"><span title="2022-6-16">3&nbsp;天前</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">21915</span>
                    <span class="reply">26</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=slience2019" c="1">slience2019</a>			<span>@</span><span><span
                        title="2022-6-19 15:59">2&nbsp;小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
<tbody id="normalthread_100730">
<tr>
    <th style="">
        <div class="post_avatar">
            <a href="home.php?mod=space&amp;uid=111169" target="_blank"><img
                    src="https://uc.javbus22.com/uc/data/avatar/000/11/11/69_avatar_middle.jpg"
                    onerror="this.onerror=null;this.src='https://uc.javbus22.com/uc/images/noavatar_middle.gif'"/></a>
        </div>
        <div class="post_inforight">
            <div class="post_infolist" style="width: 745px;">
                <div class="post_infolist_tit">

                    <a href="javascript:;" id="content_100730" class="showcontent y" title="更多操作"
                       onclick="CONTENT_TID='100730';CONTENT_ID='normalthread_100730';showMenu({'ctrlid':this.id,'menuid':'content_menu'})"></a>

                    <em>[<a href="forum.php?mod=forumdisplay&fid=36&amp;filter=typeid&amp;typeid=4"><font
                            color="Forestgreen">带带我</font></a>]</em> <a
                        href="forum.php?mod=viewthread&amp;tid=100730&amp;extra=page%3D1" onclick="atarget(this)"
                        class="s">此女真是极品，有没有完整版的或者其他系列？</a>
                    <a href="forum.php?mod=viewthread&amp;tid=100730&amp;extra=page%3D1" title="有新回復 - 新窗口打開"
                       target="_blank" class="">
                    </a>
                    <span class="tps">&nbsp;...<a
                            href="forum.php?mod=viewthread&tid=100730&amp;extra=page%3D1&amp;page=2">2</a><a
                            href="forum.php?mod=viewthread&tid=100730&amp;extra=page%3D1&amp;page=3">3</a></span>
                    <a href="forum.php?mod=redirect&amp;tid=100730&amp;goto=lastpost#lastpost" class="xi1">New</a>
                    <br><a href=forum.php?mod=viewthread&tid=100730><img
                        src='data/attachment/forum/thumbs/202206/yUzpADT.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100730><img
                        src='data/attachment/forum/thumbs/202206/GYNWGkG.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a><a
                        href=forum.php?mod=viewthread&tid=100730><img
                        src='data/attachment/forum/thumbs/202206/3x66sQ1.jpg'
                        style='max-width:150px;height:100px;padding:3px;border-radius:8px;margin:5px 5px 0 0'></a></div>
            </div>

            <div class="post_infolist_other">
                <div class="z">
                    <span class="author">         <a href="home.php?mod=space&amp;uid=111169" c="1">baobi008</a>              </span>@
                    <span class="dateline"><span title="2022-6-17">前天&nbsp;00:24</span></span>
                </div>

                <div class="z nums" style="padding-left: 25px;">
                    <span class="views">23009</span>
                    <span class="reply">32</span>
                </div>

                <span class="time y"><a href="home.php?mod=space&username=slience2019" c="1">slience2019</a>			<span>@</span><span><span
                        title="2022-6-19 15:55">2&nbsp;小時前</span></span></span>

            </div>
        </div>
        </div>
    </th>
</tr>
</tbody>
</table><!-- end of table "forum_G[fid]" branch 1/3 -->
</form>
<a class="bm_h" href="javascript:;" rel="forum.php?mod=forumdisplay&fid=36&page=2" curpage="1" id="autopbn"
   totalpage="1000" picstyle="0" forumdefstyle="">下一頁 &raquo;</a>
<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script>
<script src="static/js/autoloadpage.js?j69" type="text/javascript"></script>
</div>
</div>
<div class="banner728">


    <ins id="820087" data-width="728" data-height="90"></ins>
    <script type="text/javascript" data-cfasync="false"
            async>(adsbyjuicy = window.adsbyjuicy || []).push({'adzone': 820087});</script>
    <script type="text/javascript" data-cfasync="false" async src="https://poweredby.jads.co/js/jads.js"></script>


</div>
<div class="bm bw0 pgs cl mt10">
    <span id="fd_page_bottom"><div class="pg"><strong>1</strong><a
            href="forum.php?mod=forumdisplay&fid=36&amp;page=2">2</a><a
            href="forum.php?mod=forumdisplay&fid=36&amp;page=3">3</a><a
            href="forum.php?mod=forumdisplay&fid=36&amp;page=4">4</a><a
            href="forum.php?mod=forumdisplay&fid=36&amp;page=5">5</a><a
            href="forum.php?mod=forumdisplay&fid=36&amp;page=6">6</a><a
            href="forum.php?mod=forumdisplay&fid=36&amp;page=7">7</a><a
            href="forum.php?mod=forumdisplay&fid=36&amp;page=8">8</a><a
            href="forum.php?mod=forumdisplay&fid=36&amp;page=9">9</a><a
            href="forum.php?mod=forumdisplay&fid=36&amp;page=10">10</a><a
            href="forum.php?mod=forumdisplay&fid=36&amp;page=1000" class="last">... 1000</a><label><input type="text"
                                                                                                          name="custompage"
                                                                                                          class="px"
                                                                                                          size="2"
                                                                                                          title="輸入頁碼，按回車快速跳轉"
                                                                                                          value="1"
                                                                                                          onkeydown="if(event.keyCode==13) {window.location='forum.php?mod=forumdisplay&fid=36&amp;page='+this.value;; doane(event);}"/><span
            title="共 1000 頁"> / 1000 頁</span></label><a href="forum.php?mod=forumdisplay&fid=36&amp;page=2" class="nxt">下一頁</a></div></span>
</div>

<div id="filter_special_menu" class="p_pop" style="display:none"
     change="location.href='forum.php?mod=forumdisplay&fid=36&filter='+$('filter_special').value">
    <ul>
        <li><a href="forum.php?mod=forumdisplay&amp;fid=36">全部主題</a></li>
    </ul>
</div>
<div id="filter_reward_menu" class="p_pop" style="display:none"
     change="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=specialtype&amp;specialtype=reward&amp;rewardtype='+$('filter_reward').value">
    <ul>
        <li><a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=specialtype&amp;specialtype=reward">全部懸賞</a></li>
    </ul>
</div>
<div id="filter_dateline_menu" class="p_pop" style="display:none">
    <ul class="pop_moremenu">
        <li>排序:
            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=author&amp;orderby=dateline">發帖時間</a><span
                    class="pipe">|</span>
            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=reply&amp;orderby=replies">回復/查看</a><span
                    class="pipe">|</span>
            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=reply&amp;orderby=views">查看</a>
        </li>
        <li>時間:
            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;orderby=lastpost&amp;filter=dateline"
               class="xw1">全部時間</a><span class="pipe">|</span>
            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;orderby=lastpost&amp;filter=dateline&amp;dateline=86400">一天</a><span
                    class="pipe">|</span>
            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;orderby=lastpost&amp;filter=dateline&amp;dateline=172800">兩天</a><span
                    class="pipe">|</span>
            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;orderby=lastpost&amp;filter=dateline&amp;dateline=604800">一周</a><span
                    class="pipe">|</span>
            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;orderby=lastpost&amp;filter=dateline&amp;dateline=2592000">一個月</a><span
                    class="pipe">|</span>
            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;orderby=lastpost&amp;filter=dateline&amp;dateline=7948800">三個月</a>
        </li>
    </ul>
</div>
<div id="filter_orderby_menu" class="p_pop" style="display:none">
    <ul>
        <li><a href="forum.php?mod=forumdisplay&amp;fid=36">默認排序</a></li>
        <li><a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=author&amp;orderby=dateline">發帖時間</a></li>
        <li><a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=reply&amp;orderby=replies">回復/查看</a></li>
        <li><a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=reply&amp;orderby=views">查看</a></li>
        <li><a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=lastpost&amp;orderby=lastpost">最後發表</a></li>
        <li><a href="forum.php?mod=forumdisplay&amp;fid=36&amp;filter=heat&amp;orderby=heats">熱門</a></li>
    </ul>
</div>
<div id="filter_time_menu" class="p_pop" style="display:none">
    <ul>
        <li><a href="forum.php?mod=forumdisplay&amp;fid=36&amp;orderby=lastpost&amp;filter=dateline"
               class="xw1">全部時間</a></li>
        <li><a href="forum.php?mod=forumdisplay&amp;fid=36&amp;orderby=lastpost&amp;filter=dateline&amp;dateline=86400">一天</a>
        </li>
        <li>
            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;orderby=lastpost&amp;filter=dateline&amp;dateline=172800">兩天</a>
        </li>
        <li>
            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;orderby=lastpost&amp;filter=dateline&amp;dateline=604800">一周</a>
        </li>
        <li>
            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;orderby=lastpost&amp;filter=dateline&amp;dateline=2592000">一個月</a>
        </li>
        <li>
            <a href="forum.php?mod=forumdisplay&amp;fid=36&amp;orderby=lastpost&amp;filter=dateline&amp;dateline=7948800">三個月</a>
        </li>
    </ul>
</div>

<!--[diy=diyfastposttop]-->
<div id="diyfastposttop" class="area"></div><!--[/diy]-->
<!--[diy=diyforumdisplaybottom]-->
<div id="diyforumdisplaybottom" class="area"></div><!--[/diy]-->
</div>

<div class="sd sd_allbox">


    <div class="biaoqi_forum_ps cl">
        <a href="javascript:;" id="newspecial"
           onmouseover="$('newspecial').id = 'newspecialtmp';this.id = 'newspecial';showMenu({'ctrlid':this.id})"
           onclick="location.href='forum.php?mod=post&action=newthread&fid=36';return false;" title="發新帖"
           class="post-button">發表主題</a>
        <a href="#" target="_blank" class="sign-button">簽到Sign</a>
    </div>
    <div class="main-right-box cl">
        <!--[diy=biaoqicn_b_diy6]-->
        <div id="biaoqicn_b_diy6" class="area">
            <div id="framef96G32" class="cl_frame_bm frame move-span cl frame-1">
                <div id="framef96G32_left" class="column frame-1-c">
                    <div id="framef96G32_left_temp" class="move-span temp"></div>
                    <div id="portal_block_9" class="cl_block_bm block move-span">
                        <div id="portal_block_9_content" class="dxb_bc">
                            <div class="main-right-p15">
                                <h2 class="main-right-tit"><span>最新主題</span></h2>

                                <ul class="biaoqicn_bjctj cl">
                                    <li>
                                        <span class="rank1">1</span>
                                        <a href="forum.php?mod=viewthread&tid=100864" title="【每期十部国产作品】第二十期！（丝袜控福利）">【每期十部国产作品】第二十期！（丝袜控福</a>
                                    </li>
                                    <li>
                                        <span class="rank2">2</span>
                                        <a href="forum.php?mod=viewthread&tid=100863" title="求森山杏菜这部的资源">求森山杏菜这部的资源</a>
                                    </li>
                                    <li>
                                        <span class="rank3">3</span>
                                        <a href="forum.php?mod=viewthread&tid=100862" title="老司机能不能帮我找到这部風間ゆみ片子 谢谢">老司机能不能帮我找到这部風間ゆみ片子
                                            谢</a>
                                    </li>
                                    <li>
                                        <span class="rank4">4</span>
                                        <a href="forum.php?mod=viewthread&tid=100861" title="有没有老司机帮帮我">有没有老司机帮帮我</a>
                                    </li>
                                    <li>
                                        <span class="rank5">5</span>
                                        <a href="forum.php?mod=viewthread&tid=100855" title="ASMR剧情福利">ASMR剧情福利</a>
                                    </li>
                                    <li>
                                        <span class="rank6">6</span>
                                        <a href="forum.php?mod=viewthread&tid=100854" title="分享3个极品妹子">分享3个极品妹子</a>
                                    </li>
                                    <li>
                                        <span class="rank7">7</span>
                                        <a href="forum.php?mod=viewthread&tid=100847" title="找对象的SOP小教程pdf">找对象的SOP小教程pdf</a>
                                    </li>
                                    <li>
                                        <span class="rank8">8</span>
                                        <a href="forum.php?mod=viewthread&tid=100843" title="这是田中瞳哪部作品啊">这是田中瞳哪部作品啊</a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!--[/diy]-->
    </div>

    <div class="main-right-box cl">
        <!--[diy=biaoqicn_b_diy8]-->
        <div id="biaoqicn_b_diy8" class="area">
            <div id="frames7McmM" class="cl_frame_bm frame move-span cl frame-1">
                <div id="frames7McmM_left" class="column frame-1-c">
                    <div id="frames7McmM_left_temp" class="move-span temp"></div>
                    <div id="portal_block_10" class="cl_block_bm block move-span">
                        <div id="portal_block_10_content" class="dxb_bc">
                            <div class="main-right-p15">
                                <h2 class="main-right-tit"><span>精選內容</span></h2>
                                <ul class="main-right-kuaixu cl">
                                    <li>
                                        <div class="main-right-kuaixu-pic z">
                                            <a href="forum.php?mod=viewthread&tid=100808" target="_blank">
                                                <img src="data/attachment/block/9d/9dca16a42c5ba4fe065384d378d49cf8.jpg"
                                                     width="95" height="75"/>
                                            </a>
                                        </div>
                                        <div class="main-right-kuaixu-txt y">
                                            <a href="forum.php?mod=viewthread&tid=100808" target="_blank">【好玩的PMV合集
                                                视频52部 全长10小时】色</a>
                                            <p>2022-06-18</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="main-right-kuaixu-pic z">
                                            <a href="forum.php?mod=viewthread&tid=100809" target="_blank">
                                                <img src="data/attachment/block/aa/aa93272e5b666ac171082208f46329b0.jpg"
                                                     width="95" height="75"/>
                                            </a>
                                        </div>
                                        <div class="main-right-kuaixu-txt y">
                                            <a href="forum.php?mod=viewthread&tid=100809" target="_blank">~~~【NTRMAN】新作，今天凌晨刚发售，热乎</a>
                                            <p>2022-06-18</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="main-right-kuaixu-pic z">
                                            <a href="forum.php?mod=viewthread&tid=100815" target="_blank">
                                                <img src="data/attachment/block/7c/7cc1532625cd3d7e27854861827bd853.jpg"
                                                     width="95" height="75"/>
                                            </a>
                                        </div>
                                        <div class="main-right-kuaixu-txt y">
                                            <a href="forum.php?mod=viewthread&tid=100815" target="_blank">第一次发帖，闲聊一下</a>
                                            <p>2022-06-18</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="main-right-kuaixu-pic z">
                                            <a href="forum.php?mod=viewthread&tid=100851" target="_blank">
                                                <img src="data/attachment/block/f5/f577f2d500f03effbc603b816b75adeb.jpg"
                                                     width="95" height="75"/>
                                            </a>
                                        </div>
                                        <div class="main-right-kuaixu-txt y">
                                            <a href="forum.php?mod=viewthread&tid=100851" target="_blank">【永久收藏】盘点“十部”必看双飞片</a>
                                            <p>2022-06-19</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="main-right-kuaixu-pic z">
                                            <a href="forum.php?mod=viewthread&tid=100849" target="_blank">
                                                <img src="data/attachment/block/27/27d90042b7e641a7d51e4cece917d10e.jpg"
                                                     width="95" height="75"/>
                                            </a>
                                        </div>
                                        <div class="main-right-kuaixu-txt y">
                                            <a href="forum.php?mod=viewthread&tid=100849" target="_blank">左公子微密圈视频+图片
                                                4.87G</a>
                                            <p>2022-06-19</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="main-right-kuaixu-pic z">
                                            <a href="forum.php?mod=viewthread&tid=100825" target="_blank">
                                                <img src="data/attachment/block/97/9766c2af9b8ed3766b9560111206ed6b.jpg"
                                                     width="95" height="75"/>
                                            </a>
                                        </div>
                                        <div class="main-right-kuaixu-txt y">
                                            <a href="forum.php?mod=viewthread&tid=100825" target="_blank">我现在只对这种真高潮的女孩子感兴趣</a>
                                            <p>2022-06-19</p>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!--[/diy]-->
    </div>

    <div class="main-right-box cl">
        <!--[diy=biaoqicn_b_diy9]-->
        <div id="biaoqicn_b_diy9" class="area">
            <div id="frameyRZVvd" class="cl_frame_bm frame move-span cl frame-1">
                <div id="frameyRZVvd_left" class="column frame-1-c">
                    <div id="frameyRZVvd_left_temp" class="move-span temp"></div>
                    <div id="portal_block_11" class="cl_block_bm block move-span">
                        <div id="portal_block_11_content" class="dxb_bc">
                            <div class="main-right-p15">
                                <h2 class="main-right-tit"><span>精選主題</span></h2>
                                <div class="main-right-zuixin">
                                    <li class="bt1">
                                        <div class="comment-info">
                                            <table width="264" border="0">
                                                <tr>
                                                    <td>
                                                        <div class="comment-info"><a
                                                                href="home.php?mod=space&uid=404334" target="_blank">
                                                            <img src="https://uc.javbus22.com/uc/data/avatar/000/40/43/34_avatar_middle.jpg"
                                                                 alt="blank_flag"> </a> <a
                                                                href="home.php?mod=space&uid=404334" target="_blank"
                                                                class="comment-author">blank_flag</a></div>
                                                    </td>
                                                    <td rowspan="2" align="right">
                                                        <div class="diy-image-outer">
                                                            <a href="forum.php?mod=viewthread&tid=100594"
                                                               target="_blank"><img
                                                                    src="data/attachment/block/d6/d6f2ecf158274bd8bbb3d39c5cc5a0a3.jpg"
                                                                    width="120" height="95"/></a>
                                                        </div>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        <div class="comment-info">2022-06-14</div>
                                                    </td>
                                                </tr>
                                            </table>
                                        </div>
                                        <p class="comment-post"><a href="forum.php?mod=viewthread&tid=100594"
                                                                   target="_blank" title="【永久收藏】盘点“九部”必看FC2">【永久收藏】盘点“九部”必看FC2</a>
                                        </p>
                                        <div class="comment-excerpt">
                                            <p><a href="forum.php?mod=viewthread&tid=100594" target="_blank"
                                                  title="【永久收藏】盘点“九部”必看FC2">
                                                9.FC2-PPV-2643836

                                                点评：鲍鱼太嫩了！,而且属于耐看型,而且很有韵味。


                                                拉丝！
                                            </a></p>
                                        </div>
                                    </li>
                                    <li class="bt2">
                                        <div class="comment-info">
                                            <table width="264" border="0">
                                                <tr>
                                                    <td>
                                                        <div class="comment-info"><a
                                                                href="home.php?mod=space&uid=442389" target="_blank">
                                                            <img src="https://uc.javbus22.com/uc/data/avatar/000/44/23/89_avatar_middle.jpg"
                                                                 alt="mrwoof"> </a> <a
                                                                href="home.php?mod=space&uid=442389" target="_blank"
                                                                class="comment-author">mrwoof</a></div>
                                                    </td>
                                                    <td rowspan="2" align="right">
                                                        <div class="diy-image-outer">
                                                            <a href="forum.php?mod=viewthread&tid=100651"
                                                               target="_blank"><img
                                                                    src="data/attachment/block/3e/3e6662c017a4c95ad5fa57bd61c3b2ab.jpg"
                                                                    width="120" height="95"/></a>
                                                        </div>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        <div class="comment-info">2022-06-15</div>
                                                    </td>
                                                </tr>
                                            </table>
                                        </div>
                                        <p class="comment-post"><a href="forum.php?mod=viewthread&tid=100651"
                                                                   target="_blank" title="分享一个约炮“偷拍”系列">分享一个约炮“偷拍”系列</a>
                                        </p>
                                        <div class="comment-excerpt">
                                            <p><a href="forum.php?mod=viewthread&tid=100651" target="_blank"
                                                  title="分享一个约炮“偷拍”系列">
                                                早些年看过的一个系列了，今天突然想起来，就跟大家分享一下。片商是綜実社妄想族，
                                            </a></p>
                                        </div>
                                    </li>
                                    <li class="bt3">
                                        <div class="comment-info">
                                            <table width="264" border="0">
                                                <tr>
                                                    <td>
                                                        <div class="comment-info"><a
                                                                href="home.php?mod=space&uid=346776" target="_blank">
                                                            <img src="https://uc.javbus22.com/uc/data/avatar/000/34/67/76_avatar_middle.jpg"
                                                                 alt="zcm1308"> </a> <a
                                                                href="home.php?mod=space&uid=346776" target="_blank"
                                                                class="comment-author">zcm1308</a></div>
                                                    </td>
                                                    <td rowspan="2" align="right">
                                                        <div class="diy-image-outer">
                                                            <a href="forum.php?mod=viewthread&tid=100598"
                                                               target="_blank"><img
                                                                    src="data/attachment/block/d5/d506b98c0658f9186028c46e22a5a74f.jpg"
                                                                    width="120" height="95"/></a>
                                                        </div>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        <div class="comment-info">2022-06-14</div>
                                                    </td>
                                                </tr>
                                            </table>
                                        </div>
                                        <p class="comment-post"><a href="forum.php?mod=viewthread&tid=100598"
                                                                   target="_blank"
                                                                   title="【欧美传媒】茶艺之王 Belle Delphine 8.24G大合集--已更新16G磁力">【欧美传媒】茶艺之王
                                            Belle Delphine 8.24</a></p>
                                        <div class="comment-excerpt">
                                            <p><a href="forum.php?mod=viewthread&tid=100598" target="_blank"
                                                  title="【欧美传媒】茶艺之王 Belle Delphine 8.24G大合集--已更新16G磁力">
                                                【欧美传媒】茶艺之王--Belle Delphine

                                                擦边球大师她回来了！
                                                神秘退网1年多
                                                在推特
                                            </a></p>
                                        </div>
                                    </li>
                                    <li class="bt4">
                                        <div class="comment-info">
                                            <table width="264" border="0">
                                                <tr>
                                                    <td>
                                                        <div class="comment-info"><a
                                                                href="home.php?mod=space&uid=304023" target="_blank">
                                                            <img src="https://uc.javbus22.com/uc/data/avatar/000/30/40/23_avatar_middle.jpg"
                                                                 alt="Z师傅"> </a> <a href="home.php?mod=space&uid=304023"
                                                                                    target="_blank"
                                                                                    class="comment-author">Z师傅</a></div>
                                                    </td>
                                                    <td rowspan="2" align="right">
                                                        <div class="diy-image-outer">
                                                            <a href="forum.php?mod=viewthread&tid=100589"
                                                               target="_blank"><img
                                                                    src="data/attachment/block/f2/f242dc6ac01ca27ff9417a913f2ebb1f.jpg"
                                                                    width="120" height="95"/></a>
                                                        </div>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        <div class="comment-info">2022-06-13</div>
                                                    </td>
                                                </tr>
                                            </table>
                                        </div>
                                        <p class="comment-post"><a href="forum.php?mod=viewthread&tid=100589"
                                                                   target="_blank" title="【Z】吻戏鉴赏指北（上） ——舌尖上的AV(2)">【Z】吻戏鉴赏指北（上）
                                            ——舌尖上的AV(2</a></p>
                                        <div class="comment-excerpt">
                                            <p><a href="forum.php?mod=viewthread&tid=100589" target="_blank"
                                                  title="【Z】吻戏鉴赏指北（上） ——舌尖上的AV(2)">
                                                转载请注明作者及出处 盗帖贼司马！

                                                老哥萌好，天王盖地虎，我是Z师傅。
                                                闲话不说，
                                            </a></p>
                                        </div>
                                    </li>
                                    <li class="bt5">
                                        <div class="comment-info">
                                            <table width="264" border="0">
                                                <tr>
                                                    <td>
                                                        <div class="comment-info"><a
                                                                href="home.php?mod=space&uid=440145" target="_blank">
                                                            <img src="https://uc.javbus22.com/uc/data/avatar/000/44/01/45_avatar_middle.jpg"
                                                                 alt="aww0517"> </a> <a
                                                                href="home.php?mod=space&uid=440145" target="_blank"
                                                                class="comment-author">aww0517</a></div>
                                                    </td>
                                                    <td rowspan="2" align="right">
                                                        <div class="diy-image-outer">
                                                            <a href="forum.php?mod=viewthread&tid=100766"
                                                               target="_blank"><img
                                                                    src="data/attachment/block/5f/5f87d4fe178c590eda233cfbda9c50f0.jpg"
                                                                    width="120" height="95"/></a>
                                                        </div>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        <div class="comment-info">2022-06-17</div>
                                                    </td>
                                                </tr>
                                            </table>
                                        </div>
                                        <p class="comment-post"><a href="forum.php?mod=viewthread&tid=100766"
                                                                   target="_blank"
                                                                   title="极限公众场所露出. 三位不同女主合集 视频203V 图片398P 真勇!">极限公众场所露出.
                                            三位不同女主合集 视频2</a></p>
                                        <div class="comment-excerpt">
                                            <p><a href="forum.php?mod=viewthread&tid=100766" target="_blank"
                                                  title="极限公众场所露出. 三位不同女主合集 视频203V 图片398P 真勇!">
                                                镇楼图出处; 今天的资源里.
                                                这就真的极限露出.送餐小哥,开门就接受了如此暴击,
                                                可能
                                            </a></p>
                                        </div>
                                    </li>
                                    <li class="bt6">
                                        <div class="comment-info">
                                            <table width="264" border="0">
                                                <tr>
                                                    <td>
                                                        <div class="comment-info"><a
                                                                href="home.php?mod=space&uid=330382" target="_blank">
                                                            <img src="https://uc.javbus22.com/uc/data/avatar/000/33/03/82_avatar_middle.jpg"
                                                                 alt="Yes，枫"> </a> <a
                                                                href="home.php?mod=space&uid=330382" target="_blank"
                                                                class="comment-author">Yes，枫</a></div>
                                                    </td>
                                                    <td rowspan="2" align="right">
                                                        <div class="diy-image-outer">
                                                            <a href="forum.php?mod=viewthread&tid=100628"
                                                               target="_blank"><img
                                                                    src="data/attachment/block/c3/c3bd02ead9bdbae6f800d318e71be09a.jpg"
                                                                    width="120" height="95"/></a>
                                                        </div>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        <div class="comment-info">2022-06-14</div>
                                                    </td>
                                                </tr>
                                            </table>
                                        </div>
                                        <p class="comment-post"><a href="forum.php?mod=viewthread&tid=100628"
                                                                   target="_blank" title="韩漫大合集570部补链125G">韩漫大合集570部补链125G</a>
                                        </p>
                                        <div class="comment-excerpt">
                                            <p><a href="forum.php?mod=viewthread&tid=100628" target="_blank"
                                                  title="韩漫大合集570部补链125G">
                                                韩国彩漫大合集,之前发过一次很快就被和谐了
                                                后来一直没时间再发
                                                也有好多同好们发私
                                            </a></p>
                                        </div>
                                    </li>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!--[/diy]-->
    </div>
    <div class="frame move-span cl frame-1">
        <div class="banner300">
            <script type="text/javascript" data-cfasync="false" async
                    src="https://poweredby.jads.co/js/jads.js"></script>
            <ins id="820405" data-width="300" data-height="250"></ins>
            <script type="text/javascript" data-cfasync="false"
                    async>(adsbyjuicy = window.adsbyjuicy || []).push({"adzone": 820405});</script>
        </div>
    </div>
</div>


<div id="visitedforums_menu" class="p_pop blk cl" style="display: none;">
    <table cellspacing="0" cellpadding="0">
        <tr>
            <td id="v_forums">
                <h3 class="mbn pbn bbda xg1">瀏覽過的版塊</h3>
                <ul class="xl xl1">
                    <li><a href="forum.php?mod=forumdisplay&fid=2">老司機福利討論區</a></li>
                </ul>
            </td>
        </tr>
    </table>
</div>
<script type="text/javascript">document.onkeyup = function (e) {
    keyPageScroll(e, 0, 1, 'forum.php?mod=forumdisplay&fid=36&filter=&orderby=lastpost&', 1);
}</script>
<script type="text/javascript">checkForumnew_handle = setTimeout(function () {
    checkForumnew(36, lasttime);
}, checkForumtimeout);</script>
<div class="wp mtn">
    <!--[diy=diy3]-->
    <div id="diy3" class="area"></div><!--[/diy]-->
</div>
</div>
</div>

<div style="display: none;">
</div>

</div>


<div class="jav-footer">
    <p>
        <a href="/doc/terms" target="_blank" title="">Terms</a> /
        <a href="/doc/privacy" target="_blank" title="">Privacy</a> /
        <a href="/doc/usc" target="_blank" title="">2257</a> /
        <a href="http://www.rtalabel.org/" target="_blank" title="">RTA</a> /
        <a href="/?cshow=1" target="_blank" title="">廣告投放</a> /
        <a href="/?cshow=2" target="_blank" title="">聯絡我們</a>
        <br>
        Copyright © 2013 JavBus. All Rights Reserved. All other trademarks and copyrights are the property of their
        respective holders. The reviews and comments expressed at or through this website are the opinions of the
        individual author and do not reflect the opinions or views of JavBus. JavBus is not responsible for the accuracy
        of any of the information supplied here.
    </p>
</div>

<div class="focus plugin" id="ip_notice"></div>
<script type="text/javascript">ipNotice();</script>

<div class="biaoqi-fix-area">
    <a id="moquu_top" href="javascript:void(0)" style="display: none;"></a>
</div>

</body>
</html_test>
"""
bs = BeautifulSoup(html, "html.parser")
# title_tag = bs.title
# print(title_tag.string)
# div_tag = bs.div
# print(div_tag.string)
bs.find('div')
div_tags = bs.find_all('div')
# print(div_tags)
# div_tag = bs.find(id='info')
# div_tag = bs.find('div', id='info')
# div_tag = bs.find('div', id=re.compile('info-\d+'))
# div_tag = bs.find(string='分享一个约炮“偷拍”系列')
div_tag = bs.find(string=re.compile('偷拍'))
pass
# for tag in div_tags:
#     print(tag.string)
print(div_tag.string)