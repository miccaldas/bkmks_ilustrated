<!DOCTYPE html>
<html>
<head>
  <title>Ls-colors</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="author" content="Mclds">
  <meta name="description" content="modified ls that print icons">
  <meta property="og:type" content="web page">
  <meta property="og:url" content="">
  <link rel="stylesheet" type="text/css" href="http://localhost//css/tachyons.css" media="screen">
  <link rel="stylesheet" type="text/css" href="http://localhost//css/index.css" media="screen">
  <meta http-equiv="refresh" content="">
  <style>
        a, a:hover {
  text-decoration: none;
  font-weight: 600; }

  nav {
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  height: 50px;
  background: #f4f4f4;
  box-shadow: 0 0px 9px 4px rgba(0, 0, 0, 0.1), 0 -5px 2px 2px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  min-width: 580px; }
  nav .logo {
    position: relative;
    float: left;
    height: 50px;
    line-height: 50px;
    padding: 0 15px;
    font-size: 22px;
    font-weight: 900;
    color: #aa6f73;
    text-transform: uppercase; }
    nav .logo span {
      display: inline-block;
      position: relative;
      top: -8px;
      font-size: 13pt; }
    nav .logo:hover {
      color-background: #7e7e7e; }
  nav .links {
    float: right;
    margin-right: 30px;
    position: relative; }
    nav .links li {
      float: left;
      list-style: none;
      position: relative;
      margin: 10px;
      display: inline-block; }
      nav .links li > a {
        position: relative;
        display: inline-block;
        padding: 0 10px;
        line-height: 30px;
        height: 30px; }
        nav .links li > a:hover {
          color: #608d98;
          background: #7e7e7e;
          border-radius: 2px; }
        nav .links li > a[class^="trigger-"] {
          padding-right: 40px; }
        nav .links li > a .arrow {
          position: absolute;
          width: 10px;
          height: 10px;
          top: 35%;
          text-align: center;
          right: 10px;
          border-width: 5px 5px 0 5px;
          border-style: solid;
          border-color: rgba(0, 0, 0, 0.3) transparent; }
        nav .links li > a .arrow:after {
            content: "";
            border-left: 1px solid rgba(0, 0, 0, 0.15);
            top: -10px;
            left: -15px;
            position: absolute;
            height: 15px; }
      nav .links li ul {
        position: absolute;
        left: 0;
        margin: 0;
        background: #f4f4f4;
        border-radius: 2px;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.15);
        display: none; }
        nav .links li ul > li {
          clear: both;
          list-style: none;
          display: block;
          padding: 0 10px;
          margin: 0;
          width: 100%; }
          nav .links li ul > li:hover {
            background: #7e7e7e; }
            nav .links li ul > li:hover > a {
              background: #7e7e7e;
              color: ""; }
      nav .links li:hover > .drop {
        display: block;
        animation: fadeInRight .3s ease;
        -webkit-animation: fadeInRight .3s ease; }
  @keyframes fadeInRight {
  0% {
    opacity: 0;
    transform: translate3d(100%, 0, 0); }
  100% {
    opacity: 1;
    transform: none; } }
  </style>
</head>
<body>
<?php include '/usr/share/nginx/html/bkmks_ilustrated/partials/header.php'; ?>
  <div id="flex-container" class="flex mt=2 mb=2" style="padding-top:20px">
    <div id="col1" class="flex-row items-center self-center justify-center content-center w-10 order-0"></div>
    <div id="col2" class="w-80 order-1" style="display:flex;justify-content:center;align-items:center">>
      <div id='content'> 
        <img src="screenshots/Ls-colors.png" class="" alt="new_Ls-colors" style="margin:auto">
        <br>
        <br>
        <h1 class="f-6-ns lh-solid gray bold lh-title" style="margin:0 auto;position:relative;top:50px;margin-bottom:70px">Ls-colors</h1>
        <h3 class="f-5-ns bold silver f-subheadline measure lh-title" style="margin:0 auto; position:relative;left:80px;top:30px;margin-bottom:40px">modified ls that print icons</h3>
        <br>
        <a href="https://tinyurl.com/ybboeh4e" class="f2 i mid-gray black link hover-dark-red" style="position:relative;left:350px">LINK</a>
        <div id="col3" class="flex-row items-center self-center justify-center content-center w-10 order-2"></div>
    </div>
      </div>
      <?php include '/usr/share/nginx/html/support_services/partials/footer.php'; ?>
 </div>
    <script src="/new_rss/support_files/js/vendor/modernizr-3.11.2.min.js"></script> 
    <script src="/new_rss/support_files/js/plugins.js"></script> 
    <script src="/new_rss/support_files/js/main.js"></script>
 </body>
</html>