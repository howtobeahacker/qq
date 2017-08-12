import re
html='''C:\python3\python.exe C:/Users/lenovo/Desktop/ /qq/download_b_music.py
<html lang="en"><head><script type="text/javascript" async="" charset="utf-8" src="https://c.cnzz.com/core.php?web_id=2724999&amp;t=z"></script><script type="text/javascript" async="" charset="utf-8" src="https://s11.cnzz.com/stat.php?id=2724999&amp;web_id=2724999&amp;async=1"></script>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>三次元音乐 - 哔哩哔哩 (゜-゜)つロ 干杯~-bilibili</title>
            <meta name="description" content="bilibili是国内知名的视频弹幕网站，这里有最及时的动漫新番，最棒的ACG氛围，最有创意的Up主。大家可以在这里找到许多欢乐。">
                <meta name="keywords" content="B站,弹幕,字幕,AMV,MAD,MTV,ANIME,动漫,动漫音乐,游戏,游戏解说,ACG,galgame,动画,番组,新番,初音,洛天依,vocaloid">
                    <meta name="renderer" content="webkit">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <link rel="shortcut icon" href="//static.hdslb.com/images/favicon.ico">
                                <link rel="search" type="application/opensearchdescription+xml" href="//static.hdslb.com/opensearch.xml" title="哔哩哔哩">

                                <link rel="stylesheet" href="//static.hdslb.com/images/jquery-ui/custom/jquery-ui.css" type="text/css">
                                    <link rel="stylesheet" href="//static.hdslb.com/css/core-v5/page-core.css" type="text/css">

                                    <script type="text/javascript" src="//static.hdslb.com/js/jquery.min.js"></script>
                                    <script type="text/javascript" src="//static.hdslb.com/js/jquery-ui.min.js"></script>
                                    <script type="text/javascript" src="//static.hdslb.com/js/core-v5/base.core.js"></script>
                                    <script type="text/javascript" src="//s3.hdslb.com/bfs/cm/st/seed.js"></script><script type="text/javascript" src="//s3.hdslb.com/bfs/cm/st/20170720174732/bundle.js"></script>

<link type="text/css" href="//static.hdslb.com/css/core-v5/page-tag.css" rel="stylesheet">
<meta name="spm_prefix" content="333.339">
<script type="text/javascript" charset="utf-8" async="" src="//s1.hdslb.com/bfs/static/log/report/3.cd856.function.chunk.js"></script></head>
<body data-cover-preview="true">
   <!-- 2017-08-11 10:30:19 -->    <script type="text/javascript">biliAdjust();
            $(function () {
                biliAdjust(true);
                $(window).resize(biliAdjust);
            });</script>

    <div class="float_window"><div class="close"></div><div id="float_window"></div></div>

    <div class="z_top_container">
        <div class="z_top b-header-blur b-header-blur-black">
            <div class="b-header-mask-wrp"><div class="b-header-mask-bg" style="background-image: url(&quot;//i0.hdslb.com/bfs/archive/17759bd2d61eb97e992642f79a15ddabd015d0dc.png&quot;);"></div><div class="b-header-mask"></div></div>
            <div class="z_header">
                <div class="z_top_nav">
                    <!--<div id="httpsNotWorkTips">
    <text style="font-family: 'PingFang SC'; font-size: 16px; font-variant-ligatures: normal; orphans: 2; widows: 2; color: red;">访问异常？</text><span style="font-family: 'PingFang SC'; font-size: medium; font-variant-ligatures: normal; orphans: 2; widows: 2;">&nbsp;</span><a style="font-family: 'PingFang SC'; font-size: medium; font-variant-ligatures: normal; orphans: 2; widows: 2; color: blue;" target="_blank" href="http://www.bilibili.com/html/diagnostics.html">【点击这里】</a><span style="font-family: 'PingFang SC'; font-size: medium; font-variant-ligatures: normal; orphans: 2; widows: 2;">&nbsp;</span><text style="font-family: 'PingFang SC'; font-size: 16px; font-variant-ligatures: normal; orphans: 2; widows: 2; color: red;">请将的诊断结果与系统环境、正在使用的浏览器信息发送给我们，邮箱：bug@bilibili.com，或进入</text><span style="font-family: 'PingFang SC'; font-size: medium; font-variant-ligatures: normal; orphans: 2; widows: 2;">&nbsp;</span><a style="font-family: 'PingFang SC'; font-size: medium; font-variant-ligatures: normal; orphans: 2; widows: 2; color: blue;" target="_blank" href="http://link.acg.tv">【用户反馈论坛】</a><span style="font-family: 'PingFang SC'; font-size: medium; font-variant-ligatures: normal; orphans: 2; widows: 2;">&nbsp;</span><text style="font-family: 'PingFang SC'; font-size: 16px; font-variant-ligatures: normal; orphans: 2; widows: 2; color: red;">反映。</text><span style=" font-size:12pt;font-family:DengXian ;;;"><br></span>
</div>-->
<ul>
	<li class="home">
		<a class="i-link" href="//www.bilibili.com/index.html"><span>主站</span></a>
	</li>
		<li class="hbili"><a class="i-link" href="http://h.bilibili.com/" title="画友">画友</a></li>
	<li class="b-gc" hasframe="true">
		<a class="i-link" href="//game.bilibili.com/" title="游戏中心">游戏中心</a>
		<div class="i_div game" data-frame="game"></div>
	</li>
		<li class="live" hasframe="true">
		<a class="i-link" target="_blank" href="//live.bilibili.com" title="直播">直播</a>
		<div class="i_div stream" data-frame="stream"></div>
	</li>
  <li class="b-ml"><a class="i-link" target="_blank" href="//show.bilibili.com/platform/home.html" title="会员购">会员购</a></li>
	<li class="b-zb"><a class="i-link" target="_blank" href="//bmall.bilibili.com/#!/" title="周边">周边</a></li>
	<li class="shouji">
		<a class="i-link" target="_blank" href="//app.bilibili.com" title="移动端">移动端</a>
		<div class="mobile-p-box"><div class="mobile-p-qrcode"></div></div>
	</li>
	<li class="b-mz" hasframe="true">
	  <a class="i-link" target="_blank" href="//bangumi.bilibili.com/moe/2017/index" title="萌战">萌战</a>
			<i class="new" style="display: inline;"></i>
			<i class="dot"></i>
			<div class="i_div mz" data-frame="mz"></div>
		
	</li>
</ul>
                </div>
                <div class="uns_box">
	<ul class="menu">
		<li id="i_menu_profile_btn" guest="no" class="u-i i_user" i_menu="#i_menu_profile" style="display: none;">
			<a class="i-link" href="//space.bilibili.com/" target="_blank">
				<img class="i_face">
			</a>
			<div id="i_menu_profile" class="i_menu">
				<div class="i_menu_bg_t"></div>
				<div class="info clearfix"><div class="uname"></div><div class="coin"></div></div>
				<div class="member-menu-wrp">
					<ul class="member-menu">
						<li><a href="https://account.bilibili.com/site/home" target="_blank" class="account"><i class="b-icon b-icon-p-account"></i>个人中心</a></li>
						<li><a href="//member.bilibili.com/v/#/article" target="_blank" class="member"><i class="b-icon b-icon-p-member"></i>投稿管理</a></li>
						<li><a href="https://pay.bilibili.com/" target="_blank" class="wallet"><i class="b-icon b-icon-p-wallet"></i>B币钱包</a></li>
						<li><a href="//link.bilibili.com/p/center/index" target="_blank" class="live"><i class="b-icon b-icon-p-live"></i>直播中心</a></li>
						<li><a href="http://show.bilibili.com/orderlist" target="_blank" class="ticket"><i class="b-icon b-icon-p-ticket"></i>会员购订单</a></li>
					</ul>
				</div>
				<div class="member-bottom">
					<a class="logout" href="https://account.bilibili.com/login?act=exit">退出</a>
				</div>
			</div>
		</li>
		<li id="i_menu_become_vip" guest="no" i_menu="become_vip" class="u-i" style="display: none;">
			<a class="i-link" href="//big.bilibili.com/site/big.html" target="_blank">成为大会员</a>
		</li>
		<li id="i_menu_community_msg_btn" guest="no" i_menu="community_msg" class="u-i" style="display: none;">
            <a class="i-link" href="//message.bilibili.com" target="_blank">消息</a>
        </li>
		<li id="i_menu_msg_btn" guest="no" i_menu="#dyn_wnd" class="u-i" style="display: none;">
			<div class="num" id="dynamic_num_total"></div>
			<a class="i-link" href="//www.bilibili.com/account/dynamic" target="_blank">动态</a>
		</li>
    <li id="i_menu_watchLater_btn" guest="no" class="u-i" style="display: none;">
      <a class="i-link" href="//www.bilibili.com/watchlater/#/list" target="_blank">稍后再看</a>
    </li>
		<li id="i_menu_fav_btn" guest="no" i_menu="#i_menu_fav" class="u-i" style="display: none;">
			<a class="i-link" href="//space.bilibili.com/#!/favlist" target="_blank">收藏夹</a>
		</li>
		<li id="i_menu_login_reg" guest="yes" class="u-i" style="display: list-item;">
			<a id="i_menu_login_btn" class="i-link login" href="https://account.bilibili.com/login"><span>登录</span></a><i class="s-line"></i><a id="i_menu_register_btn" class="i-link reg" href="https://www.bilibili.com/register"><span>注册</span></a>
		</li>
		<li id="i_menu_history_btn" class="u-i">
			<a class="i-link" href="//www.bilibili.com/account/history">历史</a>
		<div class="mini-wnd hsmini" style="left: -138.2px; top: 42px;"><div class="top-login"><p class="txt">登录后有更多功能哦～</p><a class="loginbtn" href="https://passport.bilibili.com/login">登录</a></div><ul class="list history"></ul><a class="read-more" href="//www.bilibili.com/account/history">查看更多<i class="b-icon b-icon-arrow-r"></i></a></div></li>
		<li class="u-i b-post">
			<a class="i-link" href="//member.bilibili.com/v/video/submit.html" target="_blank">投 稿</a>
			<ul class="s-menu">
        <li class="article"><a href="//member.bilibili.com/v/#/text-apply" target="_blank"><i class="b-icon b-icon-art"></i><em>专栏投稿</em><i class="new"></i></a></li>
        <li class="music-up"><a href="//www.bilibili.com/audio/submit/" target="_blank"><i class="b-icon b-icon-music"></i><em>音频投稿</em></a></li>
				<li><a href="//member.bilibili.com/v/video/submit.html" target="_blank"><i class="b-icon b-icon-vp"></i><em>视频投稿</em></a></li>
				<li><a href="//member.bilibili.com/v/#/article" target="_blank"><i class="b-icon b-icon-vm"></i><em>投稿管理</em></a></li>
				<li><a href="//member.bilibili.com/v/" target="_blank"><i class="b-icon b-icon-vc"></i><em>创作中心</em></a></li>
			</ul>
		<i class="up-new"></i></li>
	</ul>
</div>
            </div>
        </div>
    </div>
    <div class="header" style="background-image: url(&quot;//i0.hdslb.com/bfs/archive/17759bd2d61eb97e992642f79a15ddabd015d0dc.png&quot;);"><div class="header-layer" style="height: 170px;"></div><a class="header-link" target="_blank" href="javascript:;" data-loc-id="1580" style="height: 170px;"></a>
        <div class="h-center">
            <a href="//www.bilibili.com/index.html" class="logo" style="background-image: url(&quot;//i0.hdslb.com/bfs/archive/58d322146cb4b1685a5775478b9753f96a0c2ff6.png&quot;);"></a>
            <a href="//www.bilibili.com/random" target="_blank" title="随便找个视频看看?" class="lsb"></a>
        </div>
        <div class="num">
            <div class="menu-wrapper">			
                <ul class="nav-menu">
	<li class="m-i home"><a class="i-link" href="//www.bilibili.com/index.html"><em>首页</em></a></li>
	<!-- 动画 -->
	<li class="m-i" data-tid="1">
		<a class="i-link" href="//www.bilibili.com/video/douga.html"><em>动画</em><div class="v-num"><span class="addnew_1">762</span></div></a>
		<ul class="i_num">
			<li><a href="//www.bilibili.com/video/douga-mad-1.html"><b>MAD·AMV<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/douga-mmd-1.html"><b>MMD·3D<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/douga-voice-1.html"><b>短片·手书·配音<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/douga-else-1.html"><b>综合<em></em></b></a></li>
		</ul>
	</li>
	<!-- 番剧 -->
	<li class="m-i" data-tid="13">
		<a class="i-link" href="//bangumi.bilibili.com/22/"><em>番剧</em><div class="v-num"><span class="addnew_13">81</span></div></a>
		<ul class="i_num">
			<li><a href="//www.bilibili.com/video/bangumi-two-1.html"><b>连载动画<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/part-twoelement-1.html"><b>完结动画<em></em></b></a></li>
            <li><a href="//www.bilibili.com/video/douga-else-information-1.html"><b>资讯<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/bagumi_offical_1.html"><b>官方延伸<em></em></b></a></li>
            <li><a href="//bangumi.bilibili.com/anime/timeline"><b>新番时间表<em></em></b></a></li>
            <li><a href="//bangumi.bilibili.com/anime/index"><b>番剧索引<em></em></b></a></li>
		</ul>
	</li>
	<!-- 国创 -->
	<li class="m-i" data-tid="167">
		<a class="i-link" href="//bangumi.bilibili.com/guochuang/"><em>国创</em><div class="v-num"><span class="addnew_167">75</span></div></a>
		<ul class="i_num">
			<li><a href="//www.bilibili.com/video/bangumi_chinese_1.html"><b>国产动画<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/guochuang-fanvid-1.html"><b>国产原创相关<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/glove-puppetry-1.html"><b>布袋戏<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/guochuang-offical-1.html"><b>资讯<em></em></b></a></li>
			<li><a href="//bangumi.bilibili.com/guochuang/timeline"><b>新番时间表<em></em></b></a></li>
			<li><a href="//bangumi.bilibili.com/guochuang/index"><b>国产动画索引<em></em></b></a></li>
		</ul>
	</li>
	<!-- 音乐 -->
	<li class="m-i on" data-tid="3">
		<a class="i-link" href="//www.bilibili.com/video/music.html"><em>音乐</em><div class="v-num"><span class="addnew_3">999+</span></div></a>
		<ul class="i_num">
			<li><a href="//www.bilibili.com/video/music-original-1.html"><b>原创音乐<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/music-Cover-1.html"><b>翻唱<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/music-vocaloid-1.html"><b>VOCALOID·UTAU<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/music-perform-1.html"><b>演奏<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/music-coordinate-1.html"><b>三次元音乐<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/music-oped-1.html"><b>OP/ED/OST<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/music-collection-1.html"><b>音乐选集<em></em></b></a></li>
		</ul>
	</li>
	<!-- 舞蹈 -->
	<li class="m-i" data-tid="129">
		<a class="i-link" href="//www.bilibili.com/video/dance.html"><em>舞蹈</em><div class="v-num"><span class="addnew_129">121</span></div></a>
		<ul class="i_num">
			<li><a href="//www.bilibili.com/video/dance-1.html"><b>宅舞<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/three-dimension-dance-1.html"><b>三次元舞蹈<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/dance-demo-1.html"><b>舞蹈教程<em></em></b></a></li>
		</ul>
	</li>
	<!-- 游戏 -->
	<li class="m-i" data-tid="4">
		<a class="i-link" href="//www.bilibili.com/video/game.html"><em>游戏</em><div class="v-num"><span class="addnew_4">999+</span></div></a>
		<ul class="i_num">
			<li><a href="//www.bilibili.com/video/videogame-1.html"><b>单机游戏<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/esports-1.html"><b>电子竞技<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/mobilegame-1.html"><b>手机游戏<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/onlinegame-1.html"><b>网络游戏<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/boardgame-1.html"><b>桌游棋牌<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/gmv-1.html"><b>GMV<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/music-game-1.html"><b>音游<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/game-mugen-1.html"><b>Mugen<em></em></b></a></li>
		</ul>
	</li>
	<!-- 科技 -->
	<li class="m-i" data-tid="36">
		<a class="i-link" href="//www.bilibili.com/video/technology.html"><em>科技</em><div class="v-num"><span class="addnew_36">641</span></div></a>
		<ul class="i_num">
			<li><a href="//www.bilibili.com/video/tech-popular-science-1.html"><b>纪录片<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/tech-fun-1.html"><b>趣味科普人文<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/tech-wild-1.html"><b>野生技术协会<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/speech-course-1.html"><b>演讲·公开课<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/tech-future-military-1.html"><b>星海<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/tech-future-digital-1.html"><b>数码<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/tech-future-other-1.html"><b>机械<em></em></b></a></li>
		</ul>
	</li>
	<!-- 生活 -->
	<li class="m-i" data-tid="160">
		<a class="i-link" href="//www.bilibili.com/video/life.html"><em>生活</em><div class="v-num"><span class="addnew_160">999+</span></div></a>
		<ul class="i_num">
			<li><a href="//www.bilibili.com/video/ent_funny_1.html"><b>搞笑<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/ent-life-1.html"><b>日常<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/ent-food-1.html"><b>美食圈<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/ent-animal-1.html"><b>动物圈<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/ent-handmake-1.html"><b>手工<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/ent-painting-1.html"><b>绘画<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/ent-sports-1.html"><b>运动<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/others-1.html"><b>其他<em></em></b></a></li>
		</ul>
	</li>
	<!-- 鬼畜 -->
	<li class="m-i" data-tid="119">
		<a class="i-link" href="//www.bilibili.com/video/kichiku.html"><em>鬼畜</em><div class="v-num"><span class="addnew_119">106</span></div></a>
		<ul class="i_num">
			<li><a href="//www.bilibili.com/video/ent-Kichiku-1.html"><b>鬼畜调教<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/douga-kichiku-1.html"><b>音MAD<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/kichiku-manual_vocaloid-1.html"><b>人力VOCALOID<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/kichiku-course-1.html"><b>教程演示<em></em></b></a></li>
		</ul>
	</li>
	<!-- 时尚 -->
	<li class="m-i" data-tid="155">
		<a class="i-link" href="//www.bilibili.com/video/fashion.html"><em>时尚</em><div class="v-num"><span class="addnew_155">256</span></div></a>
		<ul class="i_num">
			<li><a href="//www.bilibili.com/video/fashion-makeup-fitness-1.html"><b>美妆<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/fashion-clothing-1.html"><b>服饰<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/fashion-body-1.html"><b>健身<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/fashion-info-1.html"><b>资讯<em></em></b></a></li>
		</ul>
	</li>
	<!-- 广告 -->
	<li class="m-i" data-tid="165">
		<a class="i-link" href="//www.bilibili.com/video/ad-ad-1.html"><em>广告</em><div class="v-num"><span class="addnew_165">55</span></div></a>
	</li>
	<!-- 娱乐 -->
	<li class="m-i" data-tid="5">
		<a class="i-link" href="//www.bilibili.com/video/ent.html"><em>娱乐</em><div class="v-num"><span class="addnew_5">999+</span></div></a>
		<ul class="i_num">
			<li><a href="//www.bilibili.com/video/ent-variety-1.html"><b>综艺<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/ent-circle-1.html"><b>明星<em></em></b></a></li>
			<li><a href="//www.bilibili.com/video/ent-korea-1.html"><b>Korea相关<em></em></b></a></li>
		</ul>
	</li>
	<!-- 影视 -->
	<li class="m-i" data-tid="23">
		<a class="i-link" href="//bangumi.bilibili.com/33/"><em>影视</em><div class="v-num"><span class="addnew_23_11">999+</span></div></a>
		<ul class="i_num">
			<li><a href="//bangumi.bilibili.com/movie/"><b>电影<em></em></b></a></li>
			<li><a href="//bangumi.bilibili.com/tv/"><b>电视剧<em></em></b></a></li>
		</ul>
	</li>
	<li class="m-i m-i-square">
		<a class="i-link" href="//www.bilibili.com/square"><em>广场</em></a>
		<div class="i_num">
			<ul>
        <li><a href="//show.bilibili.com/platform/home.html"><i class="vip-buy"></i><b>会员购</b></a></li>
				<li><a href="//activity.bilibili.com"><i class="b-icon b-icon-n-activity"></i><b>活动中心</b></a></li>
				<li><a href="//game.bilibili.com"><i class="b-icon b-icon-n-gc"></i><b>游戏中心</b></a></li>
				<li><a href="//news.bilibili.com"><i class="b-icon b-icon-n-new"></i><b>新闻中心</b></a></li>
				<li><a href="//h.bilibili.com/"><i class="b-icon b-icon-n-h"></i><b>画友</b></a></li>
				<li><a href="//www.bilibili.com/mango"><i class="b-icon b-icon-n-mango"></i><b>芒果TV</b></a></li>
			</ul>
		</div>
	</li>
  <li class="m-i m-i-live m-i-last">
		<a class="i-link" href="//live.bilibili.com"><em>直播</em></a>
    <div class="nav-live i_num">
      <ul>
  			<li><a href="//live.bilibili.com/subject"><b>推荐主播<em></em></b></a></li>
  			<li><a href="//live.bilibili.com/pages/area/ent"><b>生活娱乐<em></em></b></a></li>
  			<li><a href="//live.bilibili.com/draw"><b>绘画专区<em></em></b></a></li>
  			<li><a href="//live.bilibili.com/pages/area/ent"><b>唱见舞见<em></em></b></a></li>
  			<li><a href="//live.bilibili.com/pages/area/ent"><b>御宅文化<em></em></b></a></li>
  			<li><a href="//live.bilibili.com/single"><b>单机联机<em></em></b></a></li>
  			<li><a href="//live.bilibili.com/online"><b>网络游戏<em></em></b></a></li>
  			<li><a href="//live.bilibili.com/e-sports"><b>电子竞技<em></em></b></a></li>
  			<li><a href="//live.bilibili.com/mobile-game"><b>手游直播<em></em></b></a></li>
  		</ul>
      <div class="live-field">
        <a class="pic" target="_blank" href="//h.bilibili.com/ywh/"><img src="//static.hdslb.com/images/base/live/wh2.png" alt="有文画"></a>
        <a class="pic" target="_blank" href="//vc.bilibili.com"><img src="//static.hdslb.com/images/base/live/sp2.png" alt="小视频"></a>
      </div>
    </div>
	</li>
	<li class="m-i m-i-blackroom"><a class="i-link" href="//www.bilibili.com/blackroom/"><em>小黑屋</em></a></li>
</ul>
                <div class="menu-r">
                    <a id="random_p" class="random-p" target="_blank" href="//search.bilibili.com/all?keyword=%E7%88%86%E7%AC%91%E6%98%9F%E9%99%852&amp;from_source=gif_recommend" title="爆笑星际2"><div class="random-p-movie"><img src="//i0.hdslb.com/bfs/active/d2f969750728b47ee83bd8a37687a582652b060d.gif" alt="爆笑星际2"></div></a>
                </div>
                <div class="search">
                    <form action="//search.bilibili.com/all" id="searchform" target="_blank">
                        <input name="keyword" class="search-keyword" id="search-keyword" autocomplete="off" accesskey="s" x-webkit-speech="" x-webkit-grammar="builtin:translate" placeholder="揭秘《星际穿越》里隐藏的宇宙真相 " data-recommend="av13033064" type="text">
                        <button type="submit" class="search-submit"></button>
                    </form>
                    <a class="link-ranking" href="//www.bilibili.com/ranking" target="_blank"><span>排行榜</span></a>
                </div>
            </div>
        </div>
    </div>
    <div class="b-page-body">
                                <script>$('.header .num .m-i[data-tid=3]').addClass('on');</script>
        <div class="main-inner">
                <div class="fcname">
                <ul class="n_num">
                    <!-- Layer 1 -->
                                                <li desc="" tid="3"><a href="/video/music.html">全部</a></li>
                                                    <li desc="个人或团队制作以音乐为主要原创因素的歌曲或纯音乐" tid="28"><a href="/video/music-original-1.html">原创音乐</a></li>
                                                    <li desc="一切非官方的人声再演绎歌曲作品" tid="31"><a href="/video/music-Cover-1.html">翻唱</a></li>
                                                    <li desc="以雅马哈Vocaloid和UTAU引擎为基础，包含其他调教引擎，运用各类音源进行的歌曲创作内容" tid="30"><a href="/video/music-vocaloid-1.html">VOCALOID·UTAU</a></li>
                                                    <li desc="传统或非传统乐器及器材的演奏作品" tid="59"><a href="/video/music-perform-1.html">演奏</a></li>
                                                    <li desc="三次元艺人的音乐作品和相关" tid="29" class="on"><a href="/video/music-coordinate-1.html">三次元音乐</a></li>
                                                    <li desc="包括但不限于OP、ED、OST、角色歌等，由官方发售或公布的实体或非实体专辑和曲目内容" tid="54"><a href="/video/music-oped-1.html">OP/ED/OST</a></li>
                                                    <li desc="任何形式的图包、曲包、作品推荐、作品精选、XX向(包括但不限于AB向、PK向、循环向、睡眠向、排行向)视频" tid="130"><a href="/video/music-collection-1.html">音乐选集</a></li>
                        
                                                            <!-- Layer 1 end -->
                </ul>
            </div>
        <div class="container-body">
        <div class="list-custom-wrp ">
                                     <div class="tag-list-wrp">
                        <div class="b-head"><span class="b-head-i"></span><span class="b-head-t">热门标签</span><span class="b-head-s">点击即可查看本区标签的相关内容</span>
                        </div>
                        <div class="tag-list-cnt" id="tag_list" style="height: auto;">
                            <ul class="tag-list"><li class="tag-item" title="全部标签" tag-id="" style="padding-left: 10px; padding-right: 10px;" row="1"><span>全部标签</span></li><li class="tag-item on" title="电音" tag-id="14426" tag="电音" style="padding-left: 10px; padding-right: 10px;" row="1"><span>电音</span><div class="hot"></div></li><li class="tag-item" title="欧美音乐" tag-id="17034" tag="欧美音乐" style="padding-left: 10px; padding-right: 10px;" row="1"><span>欧美音乐</span></li><li class="tag-item" title="MV" tag-id="1817" tag="MV" style="padding-left: 10px; padding-right: 10px;" row="1"><span>MV</span><div class="hot"></div></li><li class="tag-item" title="日本音乐" tag-id="105946" tag="日本音乐" style="padding-left: 10px; padding-right: 10px;" row="1"><span>日本音乐</span><div class="hot"></div></li><li class="tag-item" title="现场" tag-id="7992" tag="现场" style="padding-left: 10px; padding-right: 10px;" row="1"><span>现场</span></li><li class="tag-item" title="BILLBOARD" tag-id="31781" tag="BILLBOARD" style="padding-left: 10px; padding-right: 10px;" row="1"><span>BILLBOARD</span></li><li class="tag-item" title="演唱会" tag-id="1794" tag="演唱会" style="padding-left: 10px; padding-right: 10px;" row="1"><span>演唱会</span></li><li class="tag-item" title="单曲" tag-id="2360" tag="单曲" style="padding-left: 10px; padding-right: 10px;" row="1"><span>单曲</span></li><li class="tag-item" title="AKB48" tag-id="2592" tag="AKB48" style="padding-left: 10px; padding-right: 10px;" row="1"><span>AKB48</span></li><li class="tag-item" title="翻唱" tag-id="386" tag="翻唱" style="padding-left: 10px; padding-right: 10px;" row="1"><span>翻唱</span></li><li class="tag-item" title="欧美" tag-id="13619" tag="欧美" style="padding-left: 10px; padding-right: 10px;" row="1"><span>欧美</span></li><li class="tag-item" title="RAP" tag-id="246" tag="RAP" style="padding-left: 10px; padding-right: 10px;" row="1"><span>RAP</span></li><li class="tag-item" title="摇滚" tag-id="7993" tag="摇滚" style="padding-left: 10px; padding-right: 10px;" row="1"><span>摇滚</span></li><li class="tag-item" title="开口跪" tag-id="12784" tag="开口跪" style="padding-left: 14px; padding-right: 15px;" row="1"><span>开口跪</span></li><li class="tag-item" title="岚" tag-id="37800" tag="岚" style="padding-left: 10px; padding-right: 10px;" row="2"><span>岚</span></li><li class="tag-item" title="原创" tag-id="536" tag="原创" style="padding-left: 10px; padding-right: 10px;" row="2"><span>原创</span></li><li class="tag-item" title="音乐剧" tag-id="11559" tag="音乐剧" style="padding-left: 10px; padding-right: 10px;" row="2"><span>音乐剧</span></li><li class="tag-item" title="SNH48" tag-id="171662" tag="SNH48" style="padding-left: 10px; padding-right: 10px;" row="2"><span>SNH48</span></li><li class="tag-item" title="大野智" tag-id="53445" tag="大野智" style="padding-left: 10px; padding-right: 10px;" row="2"><span>大野智</span></li><li class="tag-item" title="Taylor Swift" tag-id="2514240" tag="Taylor Swift" style="padding-left: 10px; padding-right: 10px;" row="2"><span>Taylor Swift</span></li><li class="tag-item" title="二宫和也" tag-id="48326" tag="二宫和也" style="padding-left: 10px; padding-right: 10px;" row="2"><span>二宫和也</span></li><li class="tag-item" title="听歌" tag-id="10666" tag="听歌" style="padding-left: 10px; padding-right: 10px;" row="2"><span>听歌</span></li><li class="tag-item" title="live" tag-id="2508482" tag="live" style="padding-left: 10px; padding-right: 10px;" row="2"><span>live</span></li><li class="tag-item" title="内地音乐" tag-id="1257849" tag="内地音乐" style="padding-left: 10px; padding-right: 10px;" row="2"><span>内地音乐</span></li></ul>
                        </div><div class="b-toggle-block tag-more" style="display: none;"><div class="b-toggle-btn" id="btn_tag_more" b-stat="tag_toggle" b-stat-v="29"><span>展开</span><i class="b-icon b-icon-toggle-down"></i></div></div>
                    </div>
                        <!--左-->
            <div class="b-page-large b-f-left">
                                                                        <div class="vl-dyn-wrp">
                                    <div class="b-head" id="vl_dyn_hd"><span class="b-head-i"></span><span class="b-head-t">动态</span>
                                    <div class="read-push" b-stat="tag_dyn" b-stat-v="29"><span class="icon-refresh"></span><span class="info">换一换</span></div></div>
                                    <div class="vl-dyn-cnt">
                                        <ul class="v-list" id="vl_dyn_list"><li><div class="v" gk="undefined" sc="undefined" pl="undefined" dm="undefined" up="undefined" subtitle="undefined" lm="undefined" tg="undefined" yb="undefined"><a class="preview cover-preview" href="/video/av13051736/" target="_blank"><div class="medal"></div><div class="original"></div><div class="border"></div><img data-img="" src="//i2.hdslb.com/bfs/archive/048d777dbc4059ee5f387c9989d559dfc58e7321.jpg" loaded="loaded" style="opacity: 1;"><div class="back"><div></div></div><div class="fore"><span></span><div class="bar"><div></div></div></div><div class="x"><b class="x2">4:33</b></div></a><a href="/video/av13051736/" target="_blank" title="中英字幕 好看好听好有韵味的一首MV Avicii - Wake Me Up"><div class="t">中英字幕 好看好听好有韵味的一首MV Avicii - Wake Me Up</div><div class="i"><span><i class="b-icon b-icon-v-play"></i><em number="56">56</em></span><span><i class="b-icon b-icon-v-dm"></i><em number="2">2</em></span></div></a></div><i class="watch-later" aid="13051736"></i></li><li><div class="v" gk="undefined" sc="undefined" pl="undefined" dm="undefined" up="undefined" subtitle="undefined" lm="undefined" tg="undefined" yb="undefined"><a class="preview cover-preview" href="/video/av12933751/" target="_blank"><div class="medal"></div><div class="original"></div><div class="border"></div><img data-img="" src="//i2.hdslb.com/bfs/archive/59f3eb6740e0e34d8f963f45e4bc49a2580f9663.jpg" loaded="loaded" style="opacity: 1;"><div class="back"><div></div></div><div class="fore"><span></span><div class="bar"><div></div></div></div><div class="x"><b class="x2">1:35</b></div></a><a href="/video/av12933751/" target="_blank" title="A神Avicii正式回归！"><div class="t">A神Avicii正式回归！</div><div class="i"><span><i class="b-icon b-icon-v-play"></i><em number="219">219</em></span><span><i class="b-icon b-icon-v-dm"></i><em number="8">8</em></span></div></a></div><i class="watch-later" aid="12933751"></i></li><li><div class="v" gk="undefined" sc="undefined" pl="undefined" dm="undefined" up="undefined" subtitle="undefined" lm="undefined" tg="undefined" yb="undefined"><a class="preview cover-preview" href="/video/av12985525/" target="_blank"><div class="medal"></div><div class="original"></div><div class="border"></div><img data-img="" src="//i1.hdslb.com/bfs/archive/e4e157cbb14d2bce32ecd6aabb3329d58f2aa71c.jpg" loaded="loaded" style="opacity: 1;"><div class="back"><div></div></div><div class="fore"><span></span><div class="bar"><div></div></div></div><div class="x"><b class="x2">24:56</b></div></a><a href="/video/av12985525/" target="_blank" title="Cheat Codes - Lollapalooza Chicago 2017"><div class="t">Cheat Codes - Lollapalooza Chicago 2017</div><div class="i"><span><i class="b-icon b-icon-v-play"></i><em number="28">28</em></span><span><i class="b-icon b-icon-v-dm"></i><em number="0">0</em></span></div></a></div><i class="watch-later" aid="12985525"></i></li><li><div class="v" gk="undefined" sc="undefined" pl="undefined" dm="undefined" up="undefined" subtitle="undefined" lm="undefined" tg="undefined" yb="undefined"><a class="preview cover-preview" href="/video/av9497992/" target="_blank"><div class="medal"></div><div class="original"></div><div class="border"></div><img data-img="" src="//i2.hdslb.com/bfs/archive/7c7f744bcdc379afe2a8993d899a01312df9808c.jpg" loaded="loaded" style="opacity: 1;"><div class="back"><div></div></div><div class="fore"><span></span><div class="bar"><div></div></div></div><div class="x"><b class="x2">52:57</b></div></a><a href="/video/av9497992/" target="_blank" title="Trap Music 2017  Bass Boosted Best Trap Mix"><div class="t">Trap Music 2017  Bass Boosted Best Trap Mix</div><div class="i"><span><i class="b-icon b-icon-v-play"></i><em number="87">87</em></span><span><i class="b-icon b-icon-v-dm"></i><em number="0">0</em></span></div></a></div><i class="watch-later" aid="9497992"></i></li><li><div class="v" gk="undefined" sc="undefined" pl="undefined" dm="undefined" up="undefined" subtitle="undefined" lm="undefined" tg="undefined" yb="undefined"><a class="preview cover-preview" href="/video/av13220018/" target="_blank"><div class="medal"></div><div class="original"></div><div class="border"></div><img data-img="" src="//i2.hdslb.com/bfs/archive/70ac13664a57a7ead940b721ce0109923b3d1e9b.jpg" loaded="loaded" style="opacity: 1;"><div class="back"><div></div></div><div class="fore"><span></span><div class="bar"><div></div></div></div><div class="x"><b class="x2">62:10</b></div></a><a href="/video/av13220018/" target="_blank" title="怪猫播客:野性呼唤 第164期  Kayzo Gammer KUURO  More [COTW164]"><div class="t">怪猫播客:野性呼唤 第164期  Kayzo Gammer KUURO  More [COTW164]</div><div class="i"><span><i class="b-icon b-icon-v-play"></i><em number="10">10</em></span><span><i class="b-icon b-icon-v-dm"></i><em number="1">1</em></span></div></a></div><i class="watch-later" aid="13220018"></i></li></ul>
                                    </div>
                                </div>
                                                <div class="video-list list-c">
                    <div class="vl-hd clearfix">
                        <div class="left">
                            <ul class="vl-tab" id="tab_list_order">
                                <li class="tab-i" id="list_order_default" order="default">投稿时间排序</li>
                                <li class="tab-i on" id="list_order_hot" order="hot">视频热度排序</li>
                            </ul>
                        </div>
                        <div class="right">
                            <ul class="b-slt-tab s-origin" id="tab_list_type">
                                <li class="tab-i on" id="all" type="all">全部</li>
                                <li class="tab-i" id="origin" type="origin">原创</li>
                            </ul>
                            <span class="s-line"></span>
                            <ul class="b-slt-tab" id="tab_list_mode">
                                <li class="tab-i" id="mode_1" mode="1"></li>
                                <li class="tab-i on" id="mode_2" mode="2"></li>
                                <li class="tab-i" id="mode_3" mode="3"></li>
                            </ul>
                        </div>
                        <div class="vl-hd-sub" style="display: block;">
                            <div class="selector-block">
                                <div id="select_list_order" class="b-slt" style="display: block;"><span class="txt">播放数</span>
                                    <div class="b-slt-arrow"></div>
                                    <ul class="list">
                                        <li val="hot" selected="selected" class="b-state-selected">播放数</li>
                                        <li val="review">评论数</li>
                                        <li val="stow">收藏数</li>
                                        <li val="promote">硬币数</li>
                                        <li val="damku">弹幕数</li>
                                    </ul>
                                </div>
                            </div>
                                                                <div class="selector-block">
                                        <div id="list_tag_days" class="b-slt" style="display: none;"><span class="txt">一个月</span>
                                            <div class="b-slt-arrow"></div>
                                            <ul class="list">
                                                <li val="7" class="">一周</li>
                                                <li val="30" selected="selected" class="b-state-selected">一个月</li>
                                                <li val="90">三个月</li>
                                            </ul>
                                        </div>
                                    </div>
                                                        <div class="selector-block">
                                <div id="date_select" class="date-select"> <span>2017-08-04 ~ 2017-08-11</span></div>
                                <div id="selet_datebox_none" style="display:none;">
                                    <div class="selet-datebox">
                                        <h3>日期选择</h3>
                                        <div class="inpt">
                                            <input value="2017-08-04" class="range_start" id="range_start" type="text"> - <input value="2017-08-11" class="range_end" id="range_end" type="text">
                                            <a class="b-btn" id="range_select">确定</a>
                                        </div>
                                        <h4>按月份快速选择</h4>
                                        <div class="sse clearfix"></div>
                                    </div>
                                </div>
                            </div>
                            <span class="s-line"></span>
                        </div>
                    </div>
                    <div class="vd-list-cnt loaded"><ul class="vd-list l2"><li><div class="l-item"><div class="l-l"><a href="//www.bilibili.com/video/av9401651" target="_blank" class="preview cover-preview"><img data-img="" src="//i0.hdslb.com/bfs/archive/423071e6652c44582f52b12d8f985405e39d1979.jpg_160x100.jpg" loaded="loaded" alt="【耳机福利】【House】Felix Cartal - Get What You Give" style="opacity: 1;"><div class="back"><div></div></div><div class="fore"><span></span><div class="bar"><div></div></div></div><div class="x"><b class="x2">3:39</b></div></a><i class="watch-later" aid="9401651"></i><a href="//www.bilibili.com/video/av9401651" target="_blank" class="title" title="【耳机福利】【House】Felix Cartal - Get What You Give">【耳机福利】【House】Felix Cartal - Get What You Give</a></div><div class="l-r"><div class="v-desc">关注Felix Cartal声云:soundcloud.com/felixcartal
关注Felix Cartal脸书:facebook.com/felixcartal
关注Felix Cartal推特:twitter.com/felixcartal
关注背景画师Guweiz:deviantart.com/art/One-Eye-669137725
关注画师INS@guweiz
注明:音乐作品及画作授权or转载请联系制作人@Felix Cartal或画师@guweiz</div><div class="v-info"><span class="v-info-i gk"><i class="b-icon b-icon-v-play" title="观看"></i><span number="72813">7.3万</span></span><span class="v-info-i dm"><i class="b-icon b-icon-v-dm" title="弹幕"></i><span number="267">267</span></span><span class="v-info-i sc"><i class="b-icon b-icon-v-fav" title="收藏"></i><span number="2883">2883</span></span></div><div class="up-info"><a class="v-author" href="//space.bilibili.com/2949989" target="_blank" title="电喵大战皮卡丘">电喵大战皮卡丘</a><span class="v-date" title="日期">2017-03-26 11:44:44</span></div></div></div></li><li><div class="l-item"><div class="l-l"><a href="//www.bilibili.com/video/av11189480" target="_blank" class="preview cover-preview"><img data-img="" src="//i0.hdslb.com/bfs/archive/a13f6a5ae72a9e0f444c0e93aa0de08d01164a75.jpg_160x100.jpg" loaded="loaded" alt="【斩杀神曲】Epic Sax Guy VS Ultra Sax Guy" style="opacity: 1;"><div class="back"><div></div></div><div class="fore"><span></span><div class="bar"><div></div></div></div><div class="x"><b class="x2">1:29</b></div></a><i class="watch-later" aid="11189480"></i><a href="//www.bilibili.com/video/av11189480" target="_blank" class="title" title="【斩杀神曲】Epic Sax Guy VS Ultra Sax Guy">【斩杀神曲】Epic Sax Guy VS Ultra Sax Guy</a></div><div class="l-r"><div class="v-desc">https://www.youtube.com/results?search_query=Ultra+Sax+Guy
转载自youtube
原标题：Epic Sax Guy VS Ultra Sax Guy
作者：-N- Tertain</div><div class="v-info"><span class="v-info-i gk"><i class="b-icon b-icon-v-play" title="观看"></i><span number="71377">7.1万</span></span><span class="v-info-i dm"><i class="b-icon b-icon-v-dm" title="弹幕"></i><span number="279">279</span></span><span class="v-info-i sc"><i class="b-icon b-icon-v-fav" title="收藏"></i><span number="1654">1654</span></span></div><div class="up-info"><a class="v-author" href="//space.bilibili.com/6977332" target="_blank" title="Patrickikiki">Patrickikiki</a><span class="v-date" title="日期">2017-06-09 16:32:31</span></div></div></div></li><li><div class="l-item"><div class="l-l"><a href="//www.bilibili.com/video/av12560868" target="_blank" class="preview cover-preview"><div class="img-loading" style="background: rgb(245, 245, 245) url(&quot;//static.hdslb.com/images/v3images/img_loading.png&quot;) no-repeat scroll center center; height: 100%;"><img data-img="//i0.hdslb.com/bfs/archive/9e26cfca674a1153d718781116c943270325d946.jpg_160x100.jpg" alt="【致敬缅怀】Linkin Park - Numb ( Areon Remix )" src="//static.hdslb.com/images/transparent.gif"></div><div class="back"><div></div></div><div class="fore"><span></span><div class="bar"><div></div></div></div><div class="x"><b class="x2">2:56</b></div></a><i class="watch-later" aid="12560868"></i><a href="//www.bilibili.com/video/av12560868" target="_blank" class="title" title="【致敬缅怀】Linkin Park - Numb ( Areon Remix )">【致敬缅怀】Linkin Park - Numb ( Areon Remix )</a></div><div class="l-r"><div class="v-desc">关注Areon声云:soundcloud.com/areonmusic
关注Areon推特:twitter.com/andrevalentimyt
关注AreonINS:instagram.com/andre_valentim97
背景画师Rida-Farooq:rida-farooq.deviantart.com/art/Chester-Tribute-694079838
关注画师:rida-farooq.deviantart.com</div><div class="v-info"><span class="v-info-i gk"><i class="b-icon b-icon-v-play" title="观看"></i><span number="70850">7.1万</span></span><span class="v-info-i dm"><i class="b-icon b-icon-v-dm" title="弹幕"></i><span number="1089">1089</span></span><span class="v-info-i sc"><i class="b-icon b-icon-v-fav" title="收藏"></i><span number="3468">3468</span></span></div><div class="up-info"><a class="v-author" href="//space.bilibili.com/2949989" target="_blank" title="电喵大战皮卡丘">电喵大战皮卡丘</a><span class="v-date" title="日期">2017-07-25 13:21:34</span></div></div></div></li><li><div class="l-item"><div class="l-l"><a href="//www.bilibili.com/video/av10596556" target="_blank" class="preview cover-preview"><div class="img-loading" style="background: rgb(245, 245, 245) url(&quot;//static.hdslb.com/images/v3images/img_loading.png&quot;) no-repeat scroll center center; height: 100%;"><img data-img="//i0.hdslb.com/bfs/archive/814f69c6f357b985054ac29ceece617768403e7e.jpg_160x100.jpg" alt="【耳机福利】【Future Bass】Krewella - Be There" src="//static.hdslb.com/images/transparent.gif"></div><div class="back"><div></div></div><div class="fore"><span></span><div class="bar"><div></div></div></div><div class="x"><b class="x2">3:20</b></div></a><i class="watch-later" aid="10596556"></i><a href="//www.bilibili.com/video/av10596556" target="_blank" class="title" title="【耳机福利】【Future Bass】Krewella - Be There">【耳机福利】【Future Bass】Krewella - Be There</a></div><div class="l-r"><div class="v-desc">关注Krewella声云:soundcloud.com/krewella
关注Krewella脸书:facebook.com/krewella
关注Krewella推特:twitter.com/krewella
关注Krewellains:instagram.com/krewella
关注画师WLOP微博:weibo.com/wlop
画师(INS)@GUWEIZ</div><div class="v-info"><span class="v-info-i gk"><i class="b-icon b-icon-v-play" title="观看"></i><span number="57893">5.8万</span></span><span class="v-info-i dm"><i class="b-icon b-icon-v-dm" title="弹幕"></i><span number="185">185</span></span><span class="v-info-i sc"><i class="b-icon b-icon-v-fav" title="收藏"></i><span number="2997">2997</span></span></div><div class="up-info"><a class="v-author" href="//space.bilibili.com/2949989" target="_blank" title="电喵大战皮卡丘">电喵大战皮卡丘</a><span class="v-date" title="日期">2017-06-11 10:50:00</span></div></div></div></li></ul></div><div class="pagelistbox"><a class="p prevPage" href="javascript:;" page="1">上一页</a><a class="p" href="javascript:;" page="1">1</a><a class="p active">2</a><a class="p" href="javascript:;" page="3">3</a><a class="p" href="javascript:;" page="4">4</a><a class="p" href="javascript:;" page="5">5</a><a class="p" href="javascript:;" page="6">6</a><a class="p" href="javascript:;" page="7">7</a><strong>...</strong><a class="p endPage" href="javascript:;" page="400">400</a><a class="p nextPage" href="javascript:;" page="3">下一页</a><div class="custom-right"><span class="result custom-right-inner">共 400 页/ 8000 个 ，跳至</span><input class="b-input custompage custom-right-inner" type="text"><span class="custom-right-inner">页</span></div></div>
                </div>
                <script type="text/javascript">var lastpinyin = '';var order = 'default';var tid = '29';</script>
            </div>
            <!--左-->

                                <!--右-->
                    <div class="b-page-small b-f-right">
                        <div class="b-head">
                            <span class="b-head-t">热门</span>
                        </div>
                        <div class="rlist-wrp">
                            <ul class="rlist loaded"><li data-gk="0" data-sc="0" data-pl="0" data-dm="97" data-up="Celina_卿叶" data-lm="" data-tg="2017-07-30 23:00:43" data-txt="网易云ID：一定要考上一本
点个关注吧。" data-yb="0" class="on"><i class="number n3">3</i><div class="preview"><a href="/video/av11421056/" title="速度与激情8 声道混音 低音" target="_blank"><img data-img="" src="//i1.hdslb.com/bfs/archive/4bdd9b8a68cfb4f6181757a96aac0ad3c4345e53.jpg_320x200.jpg" loaded="loaded" alt="速度与激情8 声道混音 低音" style="opacity: 1;"></a><i class="watch-later" aid="11421056"></i></div><a class="rl-info" href="/video/av11421056/" title="速度与激情8 声道混音 低音" target="_blank"><div class="title t">速度与激情8 声道混音 低音</div><div class="i"><b class="pts" title="综合评分：9044">综合评分：<em number="9044">9044</em></b></div></a></li><li data-gk="0" data-sc="0" data-pl="0" data-dm="2267" data-up="韩国东东" data-lm="" data-tg="2017-07-05 19:12:29" data-txt="东东给韩国超棒的电音乐队&amp;#39;Luna Pirates&amp;#39;介绍了中国民谣，然后他们演奏了Tropical House风格的混音版《董小姐》！！音乐真是无国境啊啊" data-yb="0"><i class="number">4</i><div class="preview"><a href="/video/av11913646/" title="初次接触中国民谣的韩国乐队，玩出了电音版的《董小姐》！" target="_blank"><img data-img="" src="//i2.hdslb.com/bfs/archive/071d30f1efa1a066bfdbd33823a0e7de2402e120.png_320x200.png" style="opacity: 1;" loaded="loaded" alt="初次接触中国民谣的韩国乐队，玩出了电音版的《董小姐》！"></a><i class="watch-later" aid="11913646"></i></div><a class="rl-info" href="/video/av11913646/" title="初次接触中国民谣的韩国乐队，玩出了电音版的《董小姐》！" target="_blank"><div class="title t">初次接触中国民谣的韩国乐队，玩出了电音版的《董小姐》！</div><div class="i"><b class="pts" title="综合评分：7456">综合评分：<em number="7456">7456</em></b></div></a></li><li data-gk="0" data-sc="0" data-pl="1" data-dm="1089" data-up="电喵大战皮卡丘" data-lm="" data-tg="2017-07-25 13:21:34" data-txt="关注Areon声云:soundcloud.com/areonmusic
关注Areon推特:twitter.com/andrevalentimyt
关注AreonINS:instagram.com/andre_valentim97
背景画师Rida-Farooq:rida-farooq.deviantart.com/art/Chester-Tribute-694079838
关注画师:rida-farooq.deviantart.com" data-yb="0"><i class="number">5</i><div class="preview"><a href="/video/av12560868/" title="【致敬缅怀】Linkin Park - Numb ( Areon Remix )" target="_blank"><img data-img="" src="//i2.hdslb.com/bfs/archive/9e26cfca674a1153d718781116c943270325d946.jpg_320x200.jpg" style="opacity: 1;" loaded="loaded" alt="【致敬缅怀】Linkin Park - Numb ( Areon Remix )"></a><i class="watch-later" aid="12560868"></i></div><a class="rl-info" href="/video/av12560868/" title="【致敬缅怀】Linkin Park - Numb ( Areon Remix )" target="_blank"><div class="title t">【致敬缅怀】Linkin Park - Numb ( Areon Remix )</div><div class="i"><b class="pts" title="综合评分：6658">综合评分：<em number="6658">6658</em></b></div></a></li><li data-gk="0" data-sc="0" data-pl="0" data-dm="363" data-up="电喵大战皮卡丘" data-lm="" data-tg="2017-07-20 11:08:50" data-txt="关注Syzz声云:soundcloud.com/syzzmusic
关注Syzz脸书:facebook.com/SYZZmusic
关注 Rave Republic声云:soundcloud.com/theraverepublic
关注关注 Rave Republic脸书:facebook.com/raverepublicofficial
关注背景画师yuumei:deviantart.com/art/A-Moment-Alone-688641079
关注画师ins@yuumeiart" data-yb="0"><i class="number">6</i><div class="preview"><a href="/video/av12382373/" title="【耳机福利】【震荡旋律】Viva La Vida (Syzz X Rave Republic Remix)" target="_blank"><img data-img="" src="//i2.hdslb.com/bfs/archive/76681305d23bf1b38a4b3a7a4a89eca68fce4035.jpg_320x200.jpg" style="opacity: 1;" loaded="loaded" alt="【耳机福利】【震荡旋律】Viva La Vida (Syzz X Rave Republic Remix)"></a><i class="watch-later" aid="12382373"></i></div><a class="rl-info" href="/video/av12382373/" title="【耳机福利】【震荡旋律】Viva La Vida (Syzz X Rave Republic Remix)" target="_blank"><div class="title t">【耳机福利】【震荡旋律】Viva La Vida (Syzz X Rave Republic Remix)</div><div class="i"><b class="pts" title="综合评分：5673">综合评分：<em number="5673">5673</em></b></div></a></li><li data-gk="0" data-sc="0" data-pl="0" data-dm="455" data-up="迪乐儿EM" data-lm="" data-tg="2017-07-24 05:52:47" data-txt="这是第一周的由于有些视频有违禁内容无法通过审核，请不要再提没有谁谁谁了，第二周敏感旗挥舞太多主舞台视频无法上传故只传云村了。" data-yb="0"><i class="number">7</i><div class="preview"><a href="/video/av12517007/" title="【2017 Tomorrowland电音节超清全场比利时站第一周】EDM百大DJ火爆高清现场演出" target="_blank"><img data-img="" src="//i0.hdslb.com/bfs/archive/3bc135af87a33384eadcce09b95de4f188e68fde.jpg_320x200.jpg" style="opacity: 1;" loaded="loaded" alt="【2017 Tomorrowland电音节超清全场比利时站第一周】EDM百大DJ火爆高清现场演出"></a><i class="watch-later" aid="12517007"></i></div><a class="rl-info" href="/video/av12517007/" title="【2017 Tomorrowland电音节超清全场比利时站第一周】EDM百大DJ火爆高清现场演出" target="_blank"><div class="title t">【2017 Tomorrowland电音节超清全场比利时站第一周】EDM百大DJ火爆高清现场演出</div><div class="i"><b class="pts" title="综合评分：5230">综合评分：<em number="5230">5230</em></b></div></a></li><li data-gk="0" data-sc="0" data-pl="0" data-dm="355" data-up="克里斯属实嚣张" data-lm="" data-tg="2017-06-15 09:55:30" data-txt="喜欢电音的小伙伴可以多多关注，往后会有精彩电音视频等你们来看还有现场版的哦！" data-yb="0"><i class="number">8</i><div class="preview"><a href="/video/av11337042/" title="Marshmello - Alone-无可取代的电音小王子" target="_blank"><img data-img="" src="//i1.hdslb.com/bfs/archive/f2d1c3b82c762939a6a05682ee7bcada48bc3f21.jpg_320x200.jpg" style="opacity: 1;" loaded="loaded" alt="Marshmello - Alone-无可取代的电音小王子"></a><i class="watch-later" aid="11337042"></i></div><a class="rl-info" href="/video/av11337042/" title="Marshmello - Alone-无可取代的电音小王子" target="_blank"><div class="title t">Marshmello - Alone-无可取代的电音小王子</div><div class="i"><b class="pts" title="综合评分：4939">综合评分：<em number="4939">4939</em></b></div></a></li></ul>
                        </div>
                        <div class="mobile-link-l"><a href="//app.bilibili.com/" target="_blank"></a></div>
                    </div>
                    <!--右-->
                    </div>
    </div>
</div>

<script src="//static.hdslb.com/js/core-v5/page.list_tag.js" type="text/javascript"></script>
<script type="text/javascript" src="//static.hdslb.com/images/js/jquery.ui.datepicker-zh-CN.js"></script>
    </div>
    <div class="footer">
    <div class="footer-wrp">
        <div class="footer-cnt clearfix">
            <ul class="boston-postcards">
                <li>
                  <div class="tips">bilibili</div>
                  <div class="cards"><a target="_blank" href="//www.bilibili.com/blackboard/aboutUs.html">关于我们</a></div>
                  <div class="cards"><a target="_blank" href="//www.bilibili.com/blackboard/friends-links.html">友情链接</a></div>
                  <div class="cards"><a target="_blank" href="//bmall.bilibili.com/#!/">哔哩哔哩周边</a></div>
                  <div class="cards"><a target="_blank" href="//www.bilibili.com/blackboard/contact.html">联系我们</a></div>
                  <div class="cards"><a target="_blank" href="//www.bilibili.com/blackboard/join.html">加入我们</a></div>
                  <div class="cards"><a target="_blank" href="https://account.bilibili.com/site/ident.html">官方认证</a></div>
                </li>
                <li>
                  <div class="tips">传送门</div>
                  <div class="cards"><a target="_blank" href="//www.bilibili.com/blackboard/help.html">帮助中心</a></div>
                  <div class="cards"><a target="_blank" href="//www.bilibili.com/video/av120040/">高级弹幕</a></div>
                  <div class="cards"><a target="_blank" href="//www.bilibili.com/event">活动专题页</a></div>
                  <div class="cards"><a target="_blank" href="//www.bilibili.com/blackboard/copyright.html">侵权申诉</a></div>
                  <div class="cards"><a target="_blank" href="https://account.bilibili.com/answer/addq">分院帽计划</a></div>
                  <div class="cards"><a target="_blank" href="//activity.bilibili.com/">活动中心</a></div>
                  <div class="cards"><a target="_blank" href="http://link.acg.tv">用户反馈论坛</a></div>
                  <div class="cards"><a target="_blank" href="http://h.bilibili.com/wallpaper?action=list">壁纸站</a></div>
                  <div class="cards"><a target="_blank" href="http://www.bilibili.com/html/cele.html">名人堂</a></div>
                </li>
                <li>
                    <div class="block right">
                        <a target="_blank" href="//app.bilibili.com/">
                            <div class="phone">
                                <div class="pic"></div>
                                <em>手机端下载</em>
                                <div class="qrcode-box-wrp">
                                    <div class="qrcode-box qrcode-app">
                                        <div class="qrcode-box-arrow">
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </a>
                        <a target="_blank" href="http://weibo.com/bilibiliweb">
                            <div class="weibo">
                                <div class="pic"></div>
                                <em>新浪微博</em>
                                <div class="qrcode-box-wrp">
                                    <div class="qrcode-box qrcode-weibo">
                                        <div class="qrcode-box-arrow">
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </a>
                        <a id="weixin">
                            <div class="weixin">
                                <div class="pic"></div>
                                <em>官方微信</em>
                                <div class="qrcode-box-wrp bigvip-qrcode">
                                    <div class="qrcode-box qrcode-weixin">
                                        <div class="qrcode-box-arrow">
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </div>
                </li>
            </ul>
            <div class="partner">
                <div class="block left" style="padding-top: 0px;">
                    <div class="partner-banner"></div>
                </div>
                <div class="block left" style="margin: 0px 68px 0 115px;line-height:24px;float: none;">
                  <p>广播电视节目制作经营许可证：<span>（沪）字第1248号 </span> | 网络文化经营许可证：<span>沪网文[2013]0480-056号</span> | 信息网络传播视听节目许可证：<span>0910417</span> | 互联网ICP备案：<span>沪ICP备13002172号-3</span> 沪ICP证：<span>沪B2-20100043</span> | 违法不良信息举报邮箱：help@bilibili.com | 违法不良信息举报电话：4000233233转3</p>
                  <p><a href="http://www.shjbzx.cn" target="_blank"><i class="icons-footer icons-footer-report"></i><span> 上海互联网举报中心</span></a> | <a href="http://jb.ccm.gov.cn/" target="_blank">12318 全国文化市场举报网站</a> | <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502001911"><img src="//static.hdslb.com/images/base/beiantubiao.png" style="vertical-align: top;"> 沪公网安备 31011502001911号</a></p>
                  <p><a href="http://report.12377.cn:13225/toreportinputNormal_anis.do" target="_blank">网上有害信息举报专区：<img src="//static.hdslb.com/images/12377.png" style="vertical-align: sub;" width="16" height="16"> 中国互联网违法和不良信息举报中心</a></p>
                </div>
            </div>
        </div>
    </div>
</div>

<script type="text/javascript">loadLoginStatus();</script>
<script type="text/javascript" src="//www.bilibili.com/online.js"></script>
<div style="display:none;">
    <script type="text/javascript">
    $(function () {
        $.ajax({url: '//data.bilibili.com/rec.js', cache: true, dataType: 'script'});
        $('<scr' + 'ipt type="text/javascript" src="//static.hdslb.com/js/bfd.js" charset="UTF-8"></scri' + 'pt>').appendTo('body');
//        $('<scr' + 'ipt type="text/javascript" src="//s11.cnzz.com/stat.php?id=2724999&web_id=2724999" charset="UTF-8"></scri' + 'pt>').appendTo('body');
        $('<scr' + 'ipt type="text/javascript" src="//tajs.qq.com/stats?sId=9156259" charset="UTF-8"></scri' + 'pt>').appendTo('body');
    });
    </script>

    <script type="text/javascript">
      //日志上报
      window.spmReportData = {}
      window.reportConfig = {
        sample : 1,
        scrollTracker: true,
        msgObjects : 'spmReportData'
      }
      var reportScript = document.createElement('script')
      reportScript.src = "//s1.hdslb.com/bfs/static/log/report/log-reporter.js"
      document.getElementsByTagName('body')[0].appendChild(reportScript)
    </script>

    <script>
        var cnzz_s_tag = document.createElement('script');
        cnzz_s_tag.type = 'text/javascript';
        cnzz_s_tag.async = true;
        cnzz_s_tag.charset = "utf-8";
        cnzz_s_tag.src = "https://s11.cnzz.com/stat.php?id=2724999&web_id=2724999&async=1";
        var root_s = document.getElementsByTagName('script')[0];
        root_s.parentNode.insertBefore(cnzz_s_tag, root_s);
    </script>

</div><script src="//s1.hdslb.com/bfs/static/log/report/log-reporter.js"></script>


<div class="index-nav sub" id="index_nav" style="opacity: 0;"><div class="border"></div><div class="nav-list"><div class="pointer-block"></div></div><div class="n-i gotop sub"><div class="s-line"></div><div class="btn_gotop" title="返回顶部"></div></div></div><ul class="bilibili-suggest" style="top: 154px; left: 846px; display: none; min-width: 268px; max-width: 360px;"></ul></body></html>

Process finished with exit code 0

'''
url=re.findall('''<a href="//www.bilibili.com/video/av9401651" target="_blank" class="title" title="【耳机福利】''',html)
