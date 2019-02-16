#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

path = '/script/output/'
now_path = os.getcwd()

port_txt_list = ['portresult']
weak_txt_list = ['mysqlresult','ftpresult']
file_txt_list = ['fileresult','wallresult']
sysconfig_txt_list = ['Klog']
memory_txt_list = ['osresult']
sysdetect_txt_list = ['serresult','proresult','logresult','logstaresult','sshresult','deresult']

port_sug_txt = '/script/suggestion/portsuggestion'
weak_sug_txt = ['/script/suggestion/ftpsuggestion','/script/suggestion/mysqlsuggestion']
file_sug_txt = '/script/suggestion/filesuggestion'
sysconfig_sug_txt = '/script/suggestion/out.txt'
memory_sug_txt = ''
sysdetect_sug_txt = '/script/suggestion/suggestion'

port_none_demo = ("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title>Visual Admin Dashboard - Manage Users</title>
    <meta name="description" content="">
    <meta name="author" content="templatemo">
    <!-- 
    Visual Admin Template
    #/preview/templatemo_455_visual_admin
    -->
    <link href='http://fonts.useso.com/css?family=Open+Sans:400,300,400italic,700' rel='stylesheet' type='text/css'>
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/templatemo-style.css" rel="stylesheet">
    
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

  </head>
  <body>  
    <!-- Left column -->
    <div class="templatemo-flex-row">
      <div class="templatemo-sidebar">
        <header class="templatemo-site-header">
          <div class="square"></div>
          <h1>Turkey</h1>
        </header>
        <div class="profile-photo-container">
          <img src="images/turkey2.jpg"  class="img-responsive">  
          
        </div>      
        <!-- Search box -->
        <div class="mobile-menu-icon">
            <i class="fa fa-bars"></i>
          </div>
        <nav class="templatemo-left-nav">          
          <ul>
            <li><a href="#" class="active"><i class="fa fa-home fa-fw"></i>端口扫描</a></li>
            <li><a href="weak_check.html"><i class="fa fa-bar-chart fa-fw"></i>弱口令检测</a></li>
            <li><a href="file_check.html"><i class="fa fa-users fa-fw"></i>文件权限及防火墙扫描</a></li>
            <li><a href="sys_config.html"><i class="fa fa-database fa-fw"></i>系统配置检查</a></li>
            <li><a href="system_check.html"><i class="fa fa-sliders fa-fw"></i>系统信息检测</a></li>
            <li><a href="system_detect.html"><i class="fa fa-sliders fa-fw"></i>系统检测</a></li>
            <li><a href="index.html"><i class="fa fa-eject fa-fw"></i>安全建议</a></li>
          </ul>  
        </nav>
      </div>
      <!-- Main content --> 
      <div class="templatemo-content col-1 light-gray-bg">
        <div class="templatemo-top-nav-container">
          <div class="row">
            <nav class="templatemo-top-nav col-lg-12 col-md-12">  
            </nav> 
          </div>
        </div>
        <div class="templatemo-content-container">
          
          <div class="templatemo-flex-row flex-content-row">


            <div class="templatemo-content-widget white-bg col-1 text-center">
              <i class="fa fa-times"></i>
              <h2 class="text-uppercase">Scenery</h2>
              <h3 class="text-uppercase margin-bottom-10">Have a rest</h3>
              <img src="images/bicycle.jpg" alt="Bicycle" class="img-circle img-thumbnail">
            </div>

          </div>
                    
          <footer class="text-right">
            <p>Copyright &copy; 2084 Company Name 
            | Designed by <a href="#" target="_parent">templatemo</a></p>
          </footer>         
        </div>
      </div>
    </div>
    
    <!-- JS -->
    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/1.11.1/jquery.min.js"></script>      <!-- jQuery -->
    <script type="text/javascript" src="js/templatemo-script.js"></script>      <!-- Templatemo Script -->
    <script>
      $(document).ready(function(){
        // Content widget with background image
        var imageUrl = $('img.content-bg-img').attr('src');
        $('.templatemo-content-img-bg').css('background-image', 'url(' + imageUrl + ')');
        $('img.content-bg-img').hide();        
      });
    </script>
  </body>
</html>""")
weak_none_demo = ("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title>Visual Admin Dashboard - Manage Users</title>
    <meta name="description" content="">
    <meta name="author" content="templatemo">
    <!-- 
    Visual Admin Template
    #/preview/templatemo_455_visual_admin
    -->
    <link href='http://fonts.useso.com/css?family=Open+Sans:400,300,400italic,700' rel='stylesheet' type='text/css'>
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/templatemo-style.css" rel="stylesheet">
    
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

  </head>
  <body>  
    <!-- Left column -->
    <div class="templatemo-flex-row">
      <div class="templatemo-sidebar">
        <header class="templatemo-site-header">
          <div class="square"></div>
          <h1>Turkey</h1>
        </header>
        <div class="profile-photo-container">
          <img src="images/turkey2.jpg"  class="img-responsive">  
          
        </div>      
        <!-- Search box -->
        <div class="mobile-menu-icon">
            <i class="fa fa-bars"></i>
          </div>
        <nav class="templatemo-left-nav">          
          <ul>
            <li><a href="port_scanner.html"><i class="fa fa-home fa-fw"></i>端口扫描</a></li>
            <li><a href="#" class="active"><i class="fa fa-bar-chart fa-fw"></i>弱口令检测</a></li>
            <li><a href="file_check.html"><i class="fa fa-users fa-fw"></i>文件权限及防火墙扫描</a></li>
            <li><a href="sys_config.html"><i class="fa fa-database fa-fw"></i>系统配置检查</a></li>
            <li><a href="system_check.html"><i class="fa fa-sliders fa-fw"></i>系统信息检测</a></li>
            <li><a href="system_detect.html"><i class="fa fa-sliders fa-fw"></i>系统检测</a></li>
            <li><a href="index.html"><i class="fa fa-eject fa-fw"></i>安全建议</a></li>
          </ul>  
        </nav>
      </div>
      <!-- Main content --> 
      <div class="templatemo-content col-1 light-gray-bg">
        <div class="templatemo-top-nav-container">
          <div class="row">
            <nav class="templatemo-top-nav col-lg-12 col-md-12">  
            </nav> 
          </div>
        </div>
        <div class="templatemo-content-container">
          
          <div class="templatemo-flex-row flex-content-row">


            <div class="templatemo-content-widget white-bg col-1 text-center">
              <i class="fa fa-times"></i>
              <h2 class="text-uppercase">Scenery</h2>
              <h3 class="text-uppercase margin-bottom-10">Have a rest</h3>
              <img src="images/bicycle.jpg" alt="Bicycle" class="img-circle img-thumbnail">
            </div>

          </div>
                    
          <footer class="text-right">
            <p>Copyright &copy; 2084 Company Name 
            | Designed by <a href="#" target="_parent">templatemo</a></p>
          </footer>         
        </div>
      </div>
    </div>
    
    <!-- JS -->
    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/1.11.1/jquery.min.js"></script>      <!-- jQuery -->
    <script type="text/javascript" src="js/templatemo-script.js"></script>      <!-- Templatemo Script -->
    <script>
      $(document).ready(function(){
        // Content widget with background image
        var imageUrl = $('img.content-bg-img').attr('src');
        $('.templatemo-content-img-bg').css('background-image', 'url(' + imageUrl + ')');
        $('img.content-bg-img').hide();        
      });
    </script>
  </body>
</html>""")
file_none_demo = ("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title>Visual Admin Dashboard - Manage Users</title>
    <meta name="description" content="">
    <meta name="author" content="templatemo">
    <!-- 
    Visual Admin Template
    #/preview/templatemo_455_visual_admin
    -->
    <link href='http://fonts.useso.com/css?family=Open+Sans:400,300,400italic,700' rel='stylesheet' type='text/css'>
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/templatemo-style.css" rel="stylesheet">
    
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

  </head>
  <body>  
    <!-- Left column -->
    <div class="templatemo-flex-row">
      <div class="templatemo-sidebar">
        <header class="templatemo-site-header">
          <div class="square"></div>
          <h1>Turkey</h1>
        </header>
        <div class="profile-photo-container">
          <img src="images/turkey2.jpg"  class="img-responsive">  
          
        </div>      
        <!-- Search box -->
        <div class="mobile-menu-icon">
            <i class="fa fa-bars"></i>
          </div>
        <nav class="templatemo-left-nav">          
          <ul>
            <li><a href="port_scanner.html"><i class="fa fa-home fa-fw"></i>端口扫描</a></li>
            <li><a href="weak_check.html"><i class="fa fa-bar-chart fa-fw"></i>弱口令检测</a></li>
            <li><a href="#" class="active"><i class="fa fa-users fa-fw"></i>文件权限及防火墙扫描</a></li>
            <li><a href="sys_config.html"><i class="fa fa-database fa-fw"></i>系统配置检查</a></li>
            <li><a href="system_check.html"><i class="fa fa-sliders fa-fw"></i>系统信息检测</a></li>
            <li><a href="system_detect.html"><i class="fa fa-sliders fa-fw"></i>系统检测</a></li>
            <li><a href="index.html"><i class="fa fa-eject fa-fw"></i>安全建议</a></li>
          </ul>  
        </nav>
      </div>
      <!-- Main content --> 
      <div class="templatemo-content col-1 light-gray-bg">
        <div class="templatemo-top-nav-container">
          <div class="row">
            <nav class="templatemo-top-nav col-lg-12 col-md-12">  
            </nav> 
          </div>
        </div>
        <div class="templatemo-content-container">
          
          <div class="templatemo-flex-row flex-content-row">


            <div class="templatemo-content-widget white-bg col-1 text-center">
              <i class="fa fa-times"></i>
              <h2 class="text-uppercase">Scenery</h2>
              <h3 class="text-uppercase margin-bottom-10">Have a rest</h3>
              <img src="images/bicycle.jpg" alt="Bicycle" class="img-circle img-thumbnail">
            </div>

          </div>
                    
          <footer class="text-right">
            <p>Copyright &copy; 2084 Company Name 
            | Designed by <a href="#" target="_parent">templatemo</a></p>
          </footer>         
        </div>
      </div>
    </div>
    
    <!-- JS -->
    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/1.11.1/jquery.min.js"></script>      <!-- jQuery -->
    <script type="text/javascript" src="js/templatemo-script.js"></script>      <!-- Templatemo Script -->
    <script>
      $(document).ready(function(){
        // Content widget with background image
        var imageUrl = $('img.content-bg-img').attr('src');
        $('.templatemo-content-img-bg').css('background-image', 'url(' + imageUrl + ')');
        $('img.content-bg-img').hide();        
      });
    </script>
  </body>
</html>""")
sysconfig_none_demo = ("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title>Visual Admin Dashboard - Manage Users</title>
    <meta name="description" content="">
    <meta name="author" content="templatemo">
    <!-- 
    Visual Admin Template
    #/preview/templatemo_455_visual_admin
    -->
    <link href='http://fonts.useso.com/css?family=Open+Sans:400,300,400italic,700' rel='stylesheet' type='text/css'>
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/templatemo-style.css" rel="stylesheet">
    
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

  </head>
  <body>  
    <!-- Left column -->
    <div class="templatemo-flex-row">
      <div class="templatemo-sidebar">
        <header class="templatemo-site-header">
          <div class="square"></div>
          <h1>Turkey</h1>
        </header>
        <div class="profile-photo-container">
          <img src="images/turkey2.jpg"  class="img-responsive">  
          
        </div>      
        <!-- Search box -->
        <div class="mobile-menu-icon">
            <i class="fa fa-bars"></i>
          </div>
        <nav class="templatemo-left-nav">          
          <ul>
            <li><a href="port_scanner.html"><i class="fa fa-home fa-fw"></i>端口扫描</a></li>
            <li><a href="weak_check.html" ><i class="fa fa-bar-chart fa-fw"></i>弱口令检测</a></li>
            <li><a href="file_check.html"><i class="fa fa-users fa-fw"></i>文件权限及防火墙扫描</a></li>
            <li><a href="#" class="active"><i class="fa fa-database fa-fw"></i>系统配置检查</a></li>
            <li><a href="system_check.html"><i class="fa fa-sliders fa-fw"></i>系统信息检测</a></li>
            <li><a href="system_detect.html"><i class="fa fa-sliders fa-fw"></i>系统检测</a></li>
            <li><a href="index.html"><i class="fa fa-eject fa-fw"></i>安全建议</a></li>
          </ul>  
        </nav>
      </div>
      <!-- Main content --> 
      <div class="templatemo-content col-1 light-gray-bg">
        <div class="templatemo-top-nav-container">
          <div class="row">
            <nav class="templatemo-top-nav col-lg-12 col-md-12">  
            </nav> 
          </div>
        </div>
        <div class="templatemo-content-container">
          
          <div class="templatemo-flex-row flex-content-row">


            <div class="templatemo-content-widget white-bg col-1 text-center">
              <i class="fa fa-times"></i>
              <h2 class="text-uppercase">Scenery</h2>
              <h3 class="text-uppercase margin-bottom-10">Have a rest</h3>
              <img src="images/bicycle.jpg" alt="Bicycle" class="img-circle img-thumbnail">
            </div>

          </div>
                    
          <footer class="text-right">
            <p>Copyright &copy; 2084 Company Name 
            | Designed by <a href="#" target="_parent">templatemo</a></p>
          </footer>         
        </div>
      </div>
    </div>
    
    <!-- JS -->
    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/1.11.1/jquery.min.js"></script>      <!-- jQuery -->
    <script type="text/javascript" src="js/templatemo-script.js"></script>      <!-- Templatemo Script -->
    <script>
      $(document).ready(function(){
        // Content widget with background image
        var imageUrl = $('img.content-bg-img').attr('src');
        $('.templatemo-content-img-bg').css('background-image', 'url(' + imageUrl + ')');
        $('img.content-bg-img').hide();        
      });
    </script>
  </body>
</html>""")
syscheck_none_demo = ("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title>Visual Admin Dashboard - Manage Users</title>
    <meta name="description" content="">
    <meta name="author" content="templatemo">
    <!-- 
    Visual Admin Template
    #/preview/templatemo_455_visual_admin
    -->
    <link href='http://fonts.useso.com/css?family=Open+Sans:400,300,400italic,700' rel='stylesheet' type='text/css'>
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/templatemo-style.css" rel="stylesheet">
    
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

  </head>
  <body>  
    <!-- Left column -->
    <div class="templatemo-flex-row">
      <div class="templatemo-sidebar">
        <header class="templatemo-site-header">
          <div class="square"></div>
          <h1>Turkey</h1>
        </header>
        <div class="profile-photo-container">
          <img src="images/turkey2.jpg"  class="img-responsive">  
          
        </div>      
        <!-- Search box -->
        <div class="mobile-menu-icon">
            <i class="fa fa-bars"></i>
          </div>
        <nav class="templatemo-left-nav">          
          <ul>
            <li><a href="port_scanner.html"><i class="fa fa-home fa-fw"></i>端口扫描</a></li>
            <li><a href="weak_check.html"><i class="fa fa-bar-chart fa-fw"></i>弱口令检测</a></li>
            <li><a href="file_check.html"><i class="fa fa-users fa-fw"></i>文件权限及防火墙扫描</a></li>
            <li><a href="sys_config.html"><i class="fa fa-database fa-fw"></i>系统配置检查</a></li>
            <li><a href="#" class="active"><i class="fa fa-sliders fa-fw"></i>系统信息检测</a></li>
            <li><a href="system_detect.html"><i class="fa fa-sliders fa-fw"></i>系统检测</a></li>
            <li><a href="index.html"><i class="fa fa-eject fa-fw"></i>安全建议</a></li>
          </ul>  
        </nav>
      </div>
      <!-- Main content --> 
      <div class="templatemo-content col-1 light-gray-bg">
        <div class="templatemo-top-nav-container">
          <div class="row">
            <nav class="templatemo-top-nav col-lg-12 col-md-12">  
            </nav> 
          </div>
        </div>
        <div class="templatemo-content-container">
          
          <div class="templatemo-flex-row flex-content-row">


            <div class="templatemo-content-widget white-bg col-1 text-center">
              <i class="fa fa-times"></i>
              <h2 class="text-uppercase">Scenery</h2>
              <h3 class="text-uppercase margin-bottom-10">Have a rest</h3>
              <img src="images/bicycle.jpg" alt="Bicycle" class="img-circle img-thumbnail">
            </div>

          </div>
                    
          <footer class="text-right">
            <p>Copyright &copy; 2084 Company Name 
            | Designed by <a href="#" target="_parent">templatemo</a></p>
          </footer>         
        </div>
      </div>
    </div>
    
    <!-- JS -->
    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/1.11.1/jquery.min.js"></script>      <!-- jQuery -->
    <script type="text/javascript" src="js/templatemo-script.js"></script>      <!-- Templatemo Script -->
    <script>
      $(document).ready(function(){
        // Content widget with background image
        var imageUrl = $('img.content-bg-img').attr('src');
        $('.templatemo-content-img-bg').css('background-image', 'url(' + imageUrl + ')');
        $('img.content-bg-img').hide();        
      });
    </script>
  </body>
</html>""")
sysdetect_none_demo = ("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title>Visual Admin Dashboard - Manage Users</title>
    <meta name="description" content="">
    <meta name="author" content="templatemo">
    <!-- 
    Visual Admin Template
    #/preview/templatemo_455_visual_admin
    -->
    <link href='http://fonts.useso.com/css?family=Open+Sans:400,300,400italic,700' rel='stylesheet' type='text/css'>
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/templatemo-style.css" rel="stylesheet">
    
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

  </head>
  <body>  
    <!-- Left column -->
    <div class="templatemo-flex-row">
      <div class="templatemo-sidebar">
        <header class="templatemo-site-header">
          <div class="square"></div>
          <h1>Turkey</h1>
        </header>
        <div class="profile-photo-container">
          <img src="images/turkey2.jpg"  class="img-responsive">  
          
        </div>      
        <!-- Search box -->
        <div class="mobile-menu-icon">
            <i class="fa fa-bars"></i>
          </div>
        <nav class="templatemo-left-nav">          
          <ul>
            <li><a href="port_scanner.html"><i class="fa fa-home fa-fw"></i>端口扫描</a></li>
            <li><a href="weak_check.html"><i class="fa fa-bar-chart fa-fw"></i>弱口令检测</a></li>
            <li><a href="file_check.html"><i class="fa fa-users fa-fw"></i>文件权限及防火墙扫描</a></li>
            <li><a href="sys_config.html"><i class="fa fa-database fa-fw"></i>系统配置检查</a></li>
            <li><a href="system_check.html"><i class="fa fa-sliders fa-fw"></i>系统信息检测</a></li>
            <li><a href="#" class="active"><i class="fa fa-sliders fa-fw"></i>系统检测</a></li>
            <li><a href="index.html"><i class="fa fa-eject fa-fw"></i>安全建议</a></li>
          </ul>  
        </nav>
      </div>
      <!-- Main content --> 
      <div class="templatemo-content col-1 light-gray-bg">
        <div class="templatemo-top-nav-container">
          <div class="row">
            <nav class="templatemo-top-nav col-lg-12 col-md-12">  
            </nav> 
          </div>
        </div>
        <div class="templatemo-content-container">
          
          <div class="templatemo-flex-row flex-content-row">


            <div class="templatemo-content-widget white-bg col-1 text-center">
              <i class="fa fa-times"></i>
              <h2 class="text-uppercase">Scenery</h2>
              <h3 class="text-uppercase margin-bottom-10">Have a rest</h3>
              <img src="images/bicycle.jpg" alt="Bicycle" class="img-circle img-thumbnail">
            </div>

          </div>
                    
          <footer class="text-right">
            <p>Copyright &copy; 2084 Company Name 
            | Designed by <a href="#" target="_parent">templatemo</a></p>
          </footer>         
        </div>
      </div>
    </div>
    
    <!-- JS -->
    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/1.11.1/jquery.min.js"></script>      <!-- jQuery -->
    <script type="text/javascript" src="js/templatemo-script.js"></script>      <!-- Templatemo Script -->
    <script>
      $(document).ready(function(){
        // Content widget with background image
        var imageUrl = $('img.content-bg-img').attr('src');
        $('.templatemo-content-img-bg').css('background-image', 'url(' + imageUrl + ')');
        $('img.content-bg-img').hide();        
      });
    </script>
  </body>
</html>""")


def read_file(file_path):
    line_list = []
    f = open(file_path)  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        line_list.append(line)
        line = f.readline()
    f.close()
    return line_list


#--------------------------------系统信息检测网页模版--------------------------------------------
memory_info_list = read_file(now_path+path+memory_txt_list[0])
sys_check_demo = ("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title>Visual Admin Dashboard - Manage Users</title>
    <meta name="description" content="">
    <meta name="author" content="templatemo">
    <!-- 
    Visual Admin Template
    #/preview/templatemo_455_visual_admin
    -->
    <link href='http://fonts.useso.com/css?family=Open+Sans:400,300,400italic,700' rel='stylesheet' type='text/css'>
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/templatemo-style.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

  </head>
  <body>  
    <!-- Left column -->
    <div class="templatemo-flex-row">
      <div class="templatemo-sidebar">
        <header class="templatemo-site-header">
          <div class="square"></div>
          <h1>Turkey</h1>
        </header>
        <div class="profile-photo-container">
          <img src="images/turkey2.jpg"  class="img-responsive">  

        </div>      
        <!-- Search box -->
        <div class="mobile-menu-icon">
            <i class="fa fa-bars"></i>
          </div>
        <nav class="templatemo-left-nav">          
          <ul>
            <li><a href="port_scanner.html"><i class="fa fa-home fa-fw"></i>端口扫描</a></li>
            <li><a href="weak_check.html"><i class="fa fa-bar-chart fa-fw"></i>弱口令检测</a></li>

            <li><a href="file_check.html"><i class="fa fa-users fa-fw"></i>文件权限及防火墙扫描</a></li>
            <li><a href="sys_config.html"><i class="fa fa-database fa-fw"></i>系统配置检查</a></li>
            <li><a href="#" class="active"><i class="fa fa-sliders fa-fw"></i>系统信息检测</a></li>
            <li><a href="system_detect.html"><i class="fa fa-sliders fa-fw"></i>系统检测</a></li>
            <li><a href="index.html"><i class="fa fa-eject fa-fw"></i>安全建议</a></li>
          </ul>  
        </nav>
      </div>
      <!-- Main content --> 
      <div class="templatemo-content col-1 light-gray-bg">
        <div class="templatemo-top-nav-container">
          <div class="row">
            <nav class="templatemo-top-nav col-lg-12 col-md-12">  
            </nav> 
          </div>
        </div>
        <div class="templatemo-content-container">
          <div class="templatemo-flex-row flex-content-row">
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">Server info</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>info_name</strong></td>
                        <td><strong>specific_info</strong></td>                        
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>HostName</td>
                        <td>"""+memory_info_list[0].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>CPU info</td>
                        <td>"""+memory_info_list[1].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>HW Machine</td>
                        <td>"""+memory_info_list[2].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>CPU info</td>
                        <td>"""+memory_info_list[3].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>Network info</td>
                        <td>"""+memory_info_list[4].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>External Ip</td>
                        <td>"""+memory_info_list[5].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>Username</td>
                        <td>"""+memory_info_list[6].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>UserHomeDir</td>
                        <td>"""+memory_info_list[7].strip()+"""</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">Disk info</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>info_name</strong></td>
                        <td><strong>specific_data</strong>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>Disk Total</td>
                        <td>"""+memory_info_list[11].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>Disk Free</td>
                        <td>"""+memory_info_list[12].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>Disk Used Percent</td>
                        <td>"""+memory_info_list[13].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>Inode Total</td>
                        <td>"""+memory_info_list[14].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>Inode Free</td>
                        <td>"""+memory_info_list[15].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>Inode Used Percent</td>
                        <td>"""+memory_info_list[16].strip()+"""</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>

          </div> <!-- Second row ends -->
          <div class="templatemo-flex-row flex-content-row">
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">Memory info</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>info_name</strong></td>
                        <td><strong>specific_data</strong></td>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>Memory Total</td>
                        <td>"""+memory_info_list[8].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>Memory Total</td>
                        <td>"""+memory_info_list[9].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>Memory Total</td>
                        <td>"""+memory_info_list[10].strip()+"""</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>

          </div> <!-- Second row ends -->

          <div class="templatemo-flex-row flex-content-row">


            <div class="templatemo-content-widget white-bg col-1 text-center">
              <i class="fa fa-times"></i>
              <h2 class="text-uppercase">Scenery</h2>
              <h3 class="text-uppercase margin-bottom-10">Have a rest</h3>
              <img src="images/bicycle.jpg" alt="Bicycle" class="img-circle img-thumbnail">
            </div>
          </div>

          <footer class="text-right">
            <p>Copyright &copy; 2084 Company Name
            | Designed by <a href="#" target="_parent">templatemo</a></p>
          </footer>
        </div>
      </div>
    </div>

    <!-- JS -->
    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/1.11.1/jquery.min.js"></script>      <!-- jQuery -->
    <script type="text/javascript" src="js/templatemo-script.js"></script>      <!-- Templatemo Script -->
    <script>
      $(document).ready(function(){
        // Content widget with background image
        var imageUrl = $('img.content-bg-img').attr('src');
        $('.templatemo-content-img-bg').css('background-image', 'url(' + imageUrl + ')');
        $('img.content-bg-img').hide();
      });
    </script>
  </body>
</html>""")

#----------------------------------系统检测--------------------------------------------------------
sys_info_list = []

for txt in sysdetect_txt_list:
    list_result = read_file(now_path+path+txt)
    for line in list_result:
        sys_info_list.append(line)

sysdetect_sug_list = ''
list_result = read_file(now_path+sysdetect_sug_txt)
for line in list_result:
    message = "<p>"+line+"</p>"
    sysdetect_sug_list+=message

sys_detect_demo = ("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title>Visual Admin Dashboard - Manage Users</title>
    <meta name="description" content="">
    <meta name="author" content="templatemo">
    <!-- 
    Visual Admin Template
    #/preview/templatemo_455_visual_admin
    -->
    <link href='http://fonts.useso.com/css?family=Open+Sans:400,300,400italic,700' rel='stylesheet' type='text/css'>
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/templatemo-style.css" rel="stylesheet">
    
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

  </head>
  <body>  
    <!-- Left column -->
    <div class="templatemo-flex-row">
      <div class="templatemo-sidebar">
        <header class="templatemo-site-header">
          <div class="square"></div>
          <h1>Turkey</h1>
        </header>
        <div class="profile-photo-container">
          <img src="images/turkey2.jpg"  class="img-responsive">  
          
        </div>      
        <!-- Search box -->
        <div class="mobile-menu-icon">
            <i class="fa fa-bars"></i>
          </div>
        <nav class="templatemo-left-nav">          
          <ul>
            <li><a href="port_scanner.html"><i class="fa fa-home fa-fw"></i>端口扫描</a></li>
            <li><a href="weak_check.html"><i class="fa fa-bar-chart fa-fw"></i>弱口令检测</a></li>

            <li><a href="file_check.html"><i class="fa fa-users fa-fw"></i>文件权限及防火墙扫描</a></li>
            <li><a href="sys_config.html"><i class="fa fa-database fa-fw"></i>系统配置检查</a></li>
            <li><a href="system_check.html"><i class="fa fa-sliders fa-fw"></i>系统信息检测</a></li>
            <li><a href="#" class="active"><i class="fa fa-sliders fa-fw"></i>系统检测</a></li>
            <li><a href="index.html"><i class="fa fa-eject fa-fw"></i>安全建议</a></li>
          </ul>  
        </nav>
      </div>
      <!-- Main content --> 
      <div class="templatemo-content col-1 light-gray-bg">
        <div class="templatemo-top-nav-container">
          <div class="row">
            <nav class="templatemo-top-nav col-lg-12 col-md-12"> 
            </nav> 
          </div>
        </div>
        <div class="templatemo-content-container">
          <div class="templatemo-flex-row flex-content-row">
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">service scan</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>scan_name</strong></td>
                        <td><strong>result</strong></td>
                        <td><strong>statuxs</strong></td>                        
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>Service Config Scan</td>
                        <td>the result is in the ./service</td>  
                        <td>"""+sys_info_list[0]+"""</td>                     
                      </tr>
                   
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div>
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">Process detection</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>process_name</strong></td>
                        <td><strong>result</strong></td>
                        <td><strong>status</strong></td>                        
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>The access of Process on root</td>
                        <td>the result is in the ./process</td>  
                        <td>"""+sys_info_list[1]+"""</td>                     
                      </tr>
                      <tr>
                      	<td>Defunct Process</td>
                      	<td></td>
                      	<td>"""+sys_info_list[2]+"""</td>
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div> 
           

          </div> <!-- Second row ends -->  
          <div class="templatemo-flex-row flex-content-row"> 
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">Log Sensitive Detection</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>Detection_name</strong></td>
                        <td><strong>result</strong></td>
                        <td><strong>status</strong></td>                        
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>Sensitive information in Logs</td>
                        <td>the result is in the ./certlog</td>  
                        <td>"""+sys_info_list[3]+"""</td>                     
                      </tr>
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div> 
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">login status</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>project_name</strong></td>
                        <td><strong>result</strong></td>
                        <td><strong>status</strong></td>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>Login status</td>
                        <td>The result is in the ./loginf</td>
                        <td>"""+sys_info_list[4]+"""</td>
                      </tr>
       
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div>
            
            

          </div> <!-- Second row ends -->  
            <div class="templatemo-flex-row flex-content-row"> 
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">SSH DETECTIONS</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>SSH_project</strong></td>
                        <td><strong>status</strong></td>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>SSH server</td>
                        <td>"""+sys_info_list[5]+"""</td>
                      </tr>
                      <tr>
                        <td>SSH Configurtation</td>
                        <td>"""+sys_info_list[6]+"""</td>
                      </tr>
                      <tr>
                        <td>SSH Port is 22</td>
                        <td>"""+sys_info_list[7]+"""</td>
                      </tr>
                      <tr>
                        <td>SSH Protocol is 2</td>
                        <td>"""+sys_info_list[8]+"""</td>
                      </tr> 
                      <tr>
                        <td>SSH Permit Root Login</td>
                        <td>"""+sys_info_list[9]+"""</td>
                      </tr> 
                      <tr>
                        <td>SSH Banner not find</td>
                        <td>"""+sys_info_list[10]+"""</td>
                      </tr> 
                      <tr>
                        <td>SSH RSAAuthentication is closed</td>
                        <td>"""+sys_info_list[11]+"""</td>
                      </tr>
                                            <tr>
                        <td>SSH TCP wrappers is closed</td>
                        <td>"""+sys_info_list[12]+"""</td>
                      </tr>           
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div>
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">Bash or Shell Debug Module</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>project_name</strong></td>
                        <td><strong>result</strong></td>
                        <td><strong>status</strong></td>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>Contain Open Shell Debug Files</td>
                        <td>the result is in the ./debugmodel</td>
                        <td>"""+sys_info_list[13]+"""</td>
                      </tr>
                      <tr>
                        <td>Contain Open Bash Debug Files</td>
                        <td>the result is in the ./debugmodel</td>
                        <td>"""+sys_info_list[14]+"""</td>
                      </tr>         
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div>
            
            

          </div> <!-- Second row ends -->  
          <div class="templatemo-flex-row flex-content-row">


            <div class="templatemo-content-widget white-bg col-1 text-center">
              <i class="fa fa-times"></i>
              <h2 class="text-uppercase">Scenery</h2>
              <h3 class="text-uppercase margin-bottom-10">Have a rest</h3>
              <img src="images/bicycle.jpg" alt="Bicycle" class="img-circle img-thumbnail">
            </div>

            <div class="templatemo-content-widget white-bg col-2">
              <i class="fa fa-times"></i>
              <div class="square"></div>
              <h2 class="templatemo-inline-block">Suggestion</h2><hr>
              """+sysdetect_sug_list+"""            
            </div>
          </div>     

          <footer class="text-right">
            <p>Copyright &copy; 2084 Company Name 
            | Designed by <a href="#" target="_parent">templatemo</a></p>
          </footer>         
        </div>
      </div>
    </div>
    
    <!-- JS -->
    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/1.11.1/jquery.min.js"></script>      <!-- jQuery -->
    <script type="text/javascript" src="js/templatemo-script.js"></script>      <!-- Templatemo Script -->
    <script>
      $(document).ready(function(){
        // Content widget with background image
        var imageUrl = $('img.content-bg-img').attr('src');
        $('.templatemo-content-img-bg').css('background-image', 'url(' + imageUrl + ')');
        $('img.content-bg-img').hide();        
      });
    </script>
  </body>
</html>""")


#----------------------------------文件权限和防火墙扫描-------------------------------------------------------------------
file_info_list = []
for txt in file_txt_list:
    list_result = read_file(now_path+path+txt)
    for line in list_result:
        file_info_list.append(line)

file_sug_list = ''
list_result = read_file(now_path+file_sug_txt)
for line in list_result:
    message = "<p>"+line+"</p>"
    file_sug_list += message

file_check_demo =("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title>Visual Admin Dashboard - Manage Users</title>
    <meta name="description" content="">
    <meta name="author" content="templatemo">
    <!-- 
    Visual Admin Template
    #/preview/templatemo_455_visual_admin
    -->
    <link href='http://fonts.useso.com/css?family=Open+Sans:400,300,400italic,700' rel='stylesheet' type='text/css'>
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/templatemo-style.css" rel="stylesheet">
    
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

  </head>
  <body>  
    <!-- Left column -->
    <div class="templatemo-flex-row">
      <div class="templatemo-sidebar">
        <header class="templatemo-site-header">
          <div class="square"></div>
          <h1>Turkey</h1>
        </header>
        <div class="profile-photo-container">
          <img src="images/turkey2.jpg"  class="img-responsive">  
          
        </div>      
        <!-- Search box -->
        <div class="mobile-menu-icon">
            <i class="fa fa-bars"></i>
          </div>
        <nav class="templatemo-left-nav">          
          <ul>
            <li><a href="port_scanner.html"><i class="fa fa-home fa-fw"></i>端口扫描</a></li>
            <li><a href="weak_check.html"><i class="fa fa-bar-chart fa-fw"></i>弱口令检测</a></li>
            <li><a href="#" class = active><i class="fa fa-users fa-fw"></i>文件权限及防火墙扫描</a></li>
            <li><a href="sys_config.html"><i class="fa fa-database fa-fw"></i>系统配置检查</a></li>
            <li><a href="system_check.html"><i class="fa fa-sliders fa-fw"></i>系统信息检测</a></li>
            <li><a href="system_detect.html"><i class="fa fa-sliders fa-fw"></i>系统检测</a></li>
            <li><a href="index.html"><i class="fa fa-eject fa-fw"></i>安全建议</a></li>
          </ul>  
        </nav>
      </div>
      <!-- Main content --> 
      <div class="templatemo-content col-1 light-gray-bg">
        <div class="templatemo-top-nav-container">
          <div class="row">
            <nav class="templatemo-top-nav col-lg-12 col-md-12">  
            </nav> 
          </div>
        </div>
        <div class="templatemo-content-container">
          <div class="templatemo-flex-row flex-content-row">
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">file access scan</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>File_name</strong></td>
                        <td><strong>Status</strong></td>                        
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>File Permission</td>
                        <td>"""+file_info_list[0].strip()+"""</td>                     
                      </tr>
                      <tr>
                        <td>/etc</td>
                        <td>"""+file_info_list[1].strip()+"""</td>                     
                      </tr>
                      <tr>
                        <td>/root</td>
                        <td>"""+file_info_list[2].strip()+"""</td>                     
                      </tr>
                      <tr>
                        <td>/usr</td>
                        <td>"""+file_info_list[3].strip()+"""</td>                     
                      </tr>
                      <tr>
                        <td>log | pem | crt | key | file</td>
                        <td>"""+file_info_list[4].strip()+"""</td>                     
                      </tr>                  
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div> 
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">firewall detection</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>Project_name</strong></td>
                        <td><strong>status</strong>          
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>iptables rules numbers less that 5</td>
                        <td>"""+file_info_list[5].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>defense syn flood</td>
                        <td>"""+file_info_list[6].strip()+"""</td>
                      </tr>
                      <tr>
                        <td>limit package</td>
                        <td>"""+file_info_list[7].strip()+"""</td>
                      </tr>       
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div>

          </div> <!-- Second row ends -->  
                 
          <div class="templatemo-flex-row flex-content-row">
        

            <div class="templatemo-content-widget white-bg col-1 templatemo-position-relative templatemo-content-img-bg">
              <img src="images/sunset-big.jpg" alt="Sunset" class="img-responsive content-bg-img">
              <i class="fa fa-heart"></i>
              <h2 class="templatemo-position-relative white-text">Sunset</h2>
              <div class="view-img-btn-wrap">
                <a href="" class="btn btn-default templatemo-view-img-btn">View</a>  
              </div>              
            </div>
            <div class="templatemo-content-widget white-bg col-2">
              <i class="fa fa-times"></i>
              <div class="square"></div>
              <h2 class="templatemo-inline-block">Suggestion</h2><hr>
              """+file_sug_list+"""              
            </div>
          </div>
                    
          <footer class="text-right">
            <p>Copyright &copy; 2084 Company Name 
            | Designed by <a href="#" target="_parent">templatemo</a></p>
          </footer>         
        </div>
      </div>
    </div>
    
    <!-- JS -->
    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/1.11.1/jquery.min.js"></script>      <!-- jQuery -->
    <script type="text/javascript" src="js/templatemo-script.js"></script>      <!-- Templatemo Script -->
    <script>
      $(document).ready(function(){
        // Content widget with background image
        var imageUrl = $('img.content-bg-img').attr('src');
        $('.templatemo-content-img-bg').css('background-image', 'url(' + imageUrl + ')');
        $('img.content-bg-img').hide();        
      });
    </script>
  </body>
</html>""")

#---------------------------------系统配置检查----------------------------------------------------

config_info_list = []
for txt in sysconfig_txt_list:
    list_result = read_file(now_path+path+txt)
    for line in list_result:
        config_info_list.append(line)

configs_sug_list = ""
list_result = read_file(now_path+sysconfig_sug_txt)
for line in list_result:
    message = "<p>"+line+"</p>"
    configs_sug_list += message

sysconfig_check_demo = ("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title>Visual Admin Dashboard - Manage Users</title>
    <meta name="description" content="">
    <meta name="author" content="templatemo">
    <!-- 
    Visual Admin Template
    #/preview/templatemo_455_visual_admin
    -->
    <link href='http://fonts.useso.com/css?family=Open+Sans:400,300,400italic,700' rel='stylesheet' type='text/css'>
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/templatemo-style.css" rel="stylesheet">
    
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

  </head>
  <body>  
    <!-- Left column -->
    <div class="templatemo-flex-row">
      <div class="templatemo-sidebar">
        <header class="templatemo-site-header">
          <div class="square"></div>
          <h1>Turkey</h1>
        </header>
        <div class="profile-photo-container">
          <img src="images/turkey2.jpg"  class="img-responsive">  
          
        </div>      
        <!-- Search box -->
        <div class="mobile-menu-icon">
            <i class="fa fa-bars"></i>
          </div>
        <nav class="templatemo-left-nav">          
          <ul>
            <li><a href="port_scanner.html"><i class="fa fa-home fa-fw"></i>端口扫描</a></li>
            <li><a href="weak_check.html"><i class="fa fa-bar-chart fa-fw"></i>弱口令检测</a></li>
            <li><a href="file_check.html"><i class="fa fa-users fa-fw"></i>文件权限及防火墙扫描</a></li>
            <li><a href="#" class="active"><i class="fa fa-database fa-fw"></i>系统配置检查</a></li>
            <li><a href="system_check.html"><i class="fa fa-sliders fa-fw"></i>系统信息检测</a></li>
            <li><a href="system_detect.html"><i class="fa fa-sliders fa-fw"></i>系统检测</a></li>
            <li><a href="index.html"><i class="fa fa-eject fa-fw"></i>安全建议</a></li>
          </ul>  
        </nav>
      </div>
      <!-- Main content --> 
      <div class="templatemo-content col-1 light-gray-bg">
        <div class="templatemo-top-nav-container">
          <div class="row">
            <nav class="templatemo-top-nav col-lg-12 col-md-12">
            </nav> 
          </div>
        </div>
        <div class="templatemo-content-container">
          <div class="templatemo-flex-row flex-content-row">
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">account policy</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>project_name</strong></td>
                        <td><strong>status</strong></td>                        
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>password lifetime</td>
                        <td>"""+config_info_list[0]+"""</td>                       
                      </tr>
                      <tr>
                        <td>minimum time interval of password change</td>
                        <td>"""+config_info_list[1]+"""</td>                       
                      </tr>
                      <tr>
                        <td>minimum password length</td>
                        <td>"""+config_info_list[2]+"""</td>                       
                      </tr>
                      <tr>
                        <td>days of password expiration warning time</td>
                        <td>"""+config_info_list[3]+"""</td>                       
                      </tr>                   
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div> 
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">umask settings</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>project_name</strong></td>
                        <td><strong>status</strong>          
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>umask setting in /etc/profile file</td>
                        <td>"""+config_info_list[4]+"""</td>
                      </tr>
                      <tr>
                        <td>umask setting in /etc/csh.cshrc file</td>
                        <td>"""+config_info_list[5]+"""</td>
                      </tr>
                      <tr>
                        <td>umask setting in /etc/bashrc file</td>
                        <td>"""+config_info_list[6]+"""</td>
                      </tr>        
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div>

          </div> <!-- Second row ends -->  
          <div class="templatemo-flex-row flex-content-row"> 
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">Account cancellation</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>project_name</strong></td>
                        <td><strong>status</strong></td>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>account will be cancelled automatically</td>
                        <td>"""+config_info_list[7]+"""</td>
                      </tr>       
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div>
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">root with uid 0</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>project_name</strong></td>
                        <td><strong>status</strong></td>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>there are non root accounts with UID 0</td>
                        <td>"""+config_info_list[8]+"""</td>
                      </tr>       
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div>

          </div> <!-- Second row ends -->  
          <div class="templatemo-flex-row flex-content-row"> 
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">Cipher code</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>project_name</strong></td>
                        <td><strong>status</strong></td>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>GRUB cipher</td>
                        <td>"""+config_info_list[9]+"""</td>
                      </tr>
                      <tr>
                        <td>LILO cipher</td>
                        <td>"""+config_info_list[10]+"""</td>
                      </tr>        
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div>
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">Core dump</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>project_name</strong></td>
                        <td><strong>status</strong></td>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>system core dump meets the specifications</td>
                        <td>"""+config_info_list[11]+"""</td>
                      </tr>       
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div>

          </div> <!-- Second row ends --> 
          <div class="templatemo-flex-row flex-content-row"> 
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">Important document authority</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>project_name</strong></td>
                        <td><strong>status</strong></td>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>/etc/passwd permissions</td>
                        <td>"""+config_info_list[12]+"""</td>
                      </tr>
                      <tr>
                        <td>/etc/shadow permissions</td>
                        <td>"""+config_info_list[13]+"""</td>
                      </tr>
                      <tr>
                        <td>/etc/group permissions</td>
                        <td>"""+config_info_list[14]+"""</td>
                      </tr>
                      <tr>
                        <td>/etc/security permissions</td>
                        <td>"""+config_info_list[15]+"""</td>
                      </tr> 
                      <tr>
                        <td>/etc/services permissions</td>
                        <td>"""+config_info_list[16]+"""</td>
                      </tr> 
                      <tr>
                        <td>/etc/xinetd.conf permissions</td>
                        <td>"""+config_info_list[17]+"""</td>
                      </tr> 
                      <tr>
                        <td>/etc/grub.conf permissions</td> 
                        <td>"""+config_info_list[18]+"""</td>
                      </tr> 
                      <tr>
                        <td>/etc/lilo.conf permissions</td>
                        <td>"""+config_info_list[19]+"""</td>
                      </tr>         
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div>
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">OTHERS</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>project_name</strong></td>
                        <td><strong>status</strong></td>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>telnet service is open</td>
                        <td>"""+config_info_list[20]+"""</td>
                      </tr>
                      <tr>
                        <td>openssh security configuration</td>
                        <td>"""+config_info_list[21]+"""</td>
                      </tr> 
                      <tr>
                        <td>numbers of history command</td>
                        <td>"""+config_info_list[22]+"""</td>
                      </tr> 
                      <tr>
                        <td>SNMP default group password public</td>
                        <td>"""+config_info_list[23]+"""</td>
                      </tr> 
                      <tr>
                        <td>Disk dynamic space</td>
                        <td>"""
                        # +config_info_list[24]+
                        """</td>

                      </tr>        
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div>

          </div> <!-- Second row ends -->        

          <div class="templatemo-flex-row flex-content-row">


            <div class="templatemo-content-widget white-bg col-1 text-center">
              <i class="fa fa-times"></i>
              <h2 class="text-uppercase">Scenery</h2>
              <h3 class="text-uppercase margin-bottom-10">Have a rest</h3>
              <img src="images/bicycle.jpg" alt="Bicycle" class="img-circle img-thumbnail">
            </div>

            <div class="templatemo-content-widget white-bg col-2">
              <i class="fa fa-times"></i>
              <div class="square"></div>
              <h2 class="templatemo-inline-block">Suggestion</h2><hr>
              """+configs_sug_list+"""             
            </div>
          </div>
                    
          <footer class="text-right">
            <p>Copyright &copy; 2084 Company Name 
            | Designed by <a href="#" target="_parent">templatemo</a></p>
          </footer>         
        </div>
      </div>
    </div>
    
    <!-- JS -->
    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/1.11.1/jquery.min.js"></script>      <!-- jQuery -->
    <script type="text/javascript" src="js/templatemo-script.js"></script>      <!-- Templatemo Script -->
    <script>
      $(document).ready(function(){
        // Content widget with background image
        var imageUrl = $('img.content-bg-img').attr('src');
        $('.templatemo-content-img-bg').css('background-image', 'url(' + imageUrl + ')');
        $('img.content-bg-img').hide();        
      });
    </script>
  </body>
</html>""")

#------------------------------端口检查--------------------------------------------------------
port_info_list =[]
for txt in port_txt_list:
    list_result = read_file(now_path+path+txt)
    for line in list_result:
        port_info_list.append(line)

insert_message = ''
for i in range(9,len(port_info_list)):
    message = """<tr>
                            <td>{}</td>
                            <td>[Found]</td>
                    </tr>"""
    insert_message += message.format(port_info_list[i][20:42].strip())

port_sug_list = ''
list_result = read_file(now_path+port_sug_txt)
for line in list_result:
    message = "<p>"+line+"</p>"
    port_sug_list += message


port_scanner_demo = ("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title>Visual Admin Dashboard - Manage Users</title>
    <meta name="description" content="">
    <meta name="author" content="templatemo">
    <!-- 
    Visual Admin Template
    #/preview/templatemo_455_visual_admin
    -->
    <link href='http://fonts.useso.com/css?family=Open+Sans:400,300,400italic,700' rel='stylesheet' type='text/css'>
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/templatemo-style.css" rel="stylesheet">
    
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

  </head>
  <body>  
    <!-- Left column -->
    <div class="templatemo-flex-row">
      <div class="templatemo-sidebar">
        <header class="templatemo-site-header">
          <div class="square"></div>
          <h1>Turkey</h1>
        </header>
        <div class="profile-photo-container">
          <img src="images/turkey2.jpg"  class="img-responsive">  
          
        </div>      
        <!-- Search box -->
        <div class="mobile-menu-icon">
            <i class="fa fa-bars"></i>
          </div>
        <nav class="templatemo-left-nav">          
          <ul>
            <li><a href="#" class="active"><i class="fa fa-home fa-fw"></i>端口扫描</a></li>
            <li><a href="weak_check.html"><i class="fa fa-bar-chart fa-fw"></i>弱口令检测</a></li>
            <li><a href="file_check.html"><i class="fa fa-users fa-fw"></i>文件权限及防火墙扫描</a></li>
            <li><a href="sys_config.html"><i class="fa fa-database fa-fw"></i>系统配置检查</a></li>
            <li><a href="system_check.html"><i class="fa fa-sliders fa-fw"></i>系统信息检测</a></li>
            <li><a href="system_detect.html"><i class="fa fa-sliders fa-fw"></i>系统检测</a></li>
            <li><a href="index.html"><i class="fa fa-eject fa-fw"></i>安全建议</a></li>
          </ul>  
        </nav>
      </div>
      <!-- Main content --> 
      <div class="templatemo-content col-1 light-gray-bg">
        <div class="templatemo-top-nav-container">
          <div class="row">
            <nav class="templatemo-top-nav col-lg-12 col-md-12">
 
            </nav> 
          </div>
        </div>
        <div class="templatemo-content-container">
          <div class="templatemo-flex-row flex-content-row">
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">widely used port</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>port_name</strong></td>
                        <td><strong>status</strong></td>                        
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>Ftp data port 20</td>
                        <td>"""+port_info_list[0]+"""</td>                       
                      </tr>
                      <tr>
                        <td>Ftp port 21</td>
                        <td>"""+port_info_list[1]+"""</td>                       
                      </tr>
                      <tr>
                        <td>SSH port 22</td>
                        <td>"""+port_info_list[2]+"""</td>                       
                      </tr>
                      <tr>
                        <td>Smtp port 25</td>
                        <td>"""+port_info_list[3]+"""</td>                       
                      </tr>
                      <tr>
                        <td>Domain port 53</td>
                        <td>"""+port_info_list[4]+"""</td>                       
                      </tr> 
                      <tr>
                        <td>Http port 80</td>
                        <td>"""+port_info_list[5]+"""</td>                       
                      </tr>
                      <tr>
                        <td>Pop2 port 109</td>
                        <td>"""+port_info_list[6]+"""</td>                       
                      </tr>  
                      <tr>
                        <td>Imap port 143</td>
                        <td>"""+port_info_list[7]+"""</td>                       
                      </tr>
                      <tr>
                        <td>Snmap port 161</td>
                        <td>"""+port_info_list[8]+"""</td>                       
                      </tr>                 
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div> 
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">Port more than 1024</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>port_number</strong></td>
                        <td><strong>status</strong>          
                      </tr>
                    </thead>
                    <tbody>
                      """+insert_message+"""
                           
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div>

          </div> <!-- Second row ends -->  
        

          <div class="templatemo-flex-row flex-content-row">
            <div class="templatemo-content-widget white-bg col-1 text-center">
              <i class="fa fa-times"></i>
              <h2 class="text-uppercase">Scenery</h2>
              <h3 class="text-uppercase margin-bottom-10">Have a rest</h3>
              <img src="images/bicycle.jpg" alt="Bicycle" class="img-circle img-thumbnail">
            </div>

            <div class="templatemo-content-widget white-bg col-2">
              <i class="fa fa-times"></i>
              <div class="square"></div>
              <h2 class="templatemo-inline-block">Suggestion</h2><hr>
              """+port_sug_list+"""              
            </div>
          </div>
                    
          <footer class="text-right">
            <p>Copyright &copy; 2084 Company Name 
            | Designed by <a href="#" target="_parent">templatemo</a></p>
          </footer>         
        </div>
      </div>
    </div>
    
    <!-- JS -->
    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/1.11.1/jquery.min.js"></script>      <!-- jQuery -->
    <script type="text/javascript" src="js/templatemo-script.js"></script>      <!-- Templatemo Script -->
    <script>
      $(document).ready(function(){
        // Content widget with background image
        var imageUrl = $('img.content-bg-img').attr('src');
        $('.templatemo-content-img-bg').css('background-image', 'url(' + imageUrl + ')');
        $('img.content-bg-img').hide();        
      });
    </script>
  </body>
</html>""")

#-----------------------------弱口令检测--------------------------------------------------------

mysql_info = read_file(now_path+path+weak_txt_list[0])
ftp_info = read_file(now_path+path+weak_txt_list[1])

weak_sug_list = ''
for txt in weak_sug_txt:
    line_result = read_file(now_path+txt)
    for line in line_result:
        message = "<p>"+line+"</p>"
        weak_sug_list += message

weak_check_demo = ("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title>Visual Admin Dashboard - Manage Users</title>
    <meta name="description" content="">
    <meta name="author" content="templatemo">
    <!-- 
    Visual Admin Template
    #/preview/templatemo_455_visual_admin
    -->
    <link href='http://fonts.useso.com/css?family=Open+Sans:400,300,400italic,700' rel='stylesheet' type='text/css'>
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/templatemo-style.css" rel="stylesheet">
    
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

  </head>
  <body>  
    <!-- Left column -->
    <div class="templatemo-flex-row">
      <div class="templatemo-sidebar">
        <header class="templatemo-site-header">
          <div class="square"></div>
          <h1>Turkey</h1>
        </header>
        <div class="profile-photo-container">
          <img src="images/turkey2.jpg"  class="img-responsive">  
          
        </div>      
        <!-- Search box -->
        <div class="mobile-menu-icon">
            <i class="fa fa-bars"></i>
          </div>
        <nav class="templatemo-left-nav">          
          <ul>
            <li><a href="port_scanner.html"><i class="fa fa-home fa-fw"></i>端口扫描</a></li>
            <li><a href="#" class="active"><i class="fa fa-bar-chart fa-fw"></i>弱口令检测</a></li>
            <li><a href="file_check.html"><i class="fa fa-users fa-fw"></i>文件权限及防火墙扫描</a></li>
            <li><a href="sys_config.html"><i class="fa fa-database fa-fw"></i>系统配置检查</a></li>
            <li><a href="system_check.html"><i class="fa fa-sliders fa-fw"></i>系统信息检测</a></li>
            <li><a href="system_detect.html"><i class="fa fa-sliders fa-fw"></i>系统检测</a></li>
            <li><a href="index.html"><i class="fa fa-eject fa-fw"></i>安全建议</a></li>
          </ul>  
        </nav>
      </div>
      <!-- Main content --> 
      <div class="templatemo-content col-1 light-gray-bg">
        <div class="templatemo-top-nav-container">
          <div class="row">
            <nav class="templatemo-top-nav col-lg-12 col-md-12">  
            </nav> 
          </div>
        </div>
        <div class="templatemo-content-container">
          <div class="templatemo-flex-row flex-content-row">
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">ftp weak password detection</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>target_ip</strong></td>
                        <td><strong>weak_username</strong></td> 
                        <td><strong>weak_password</strong></td> 
                        <td><strong>Status</strong></td>                        
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>127.0.0.1</td>
                        <td>6</td>
                        <td>30</td>
                        <td>"""+ftp_info[0]+"""</td>                     
                      </tr>                 
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div> 
            <div class="col-1">
              <div class="panel panel-default templatemo-content-widget white-bg no-padding templatemo-overflow-hidden">
                <i class="fa fa-times"></i>
                <div class="panel-heading templatemo-position-relative"><h2 class="text-uppercase">mysql weak password detection</h2></div>
                <div class="table-responsive">
                  <table class="table table-striped table-bordered">
                    <thead>
                      <tr>
                        <td><strong>target_ip</strong></td>
                        <td><strong>weak_username</strong></td>
                        <td><strong>weak_password</strong></td> 
                        <td><strong>status</strong></td>          
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>127.0.0.1</td>
                        <td>6</td>
                        <td>30</td>
                        <td>"""+mysql_info[0]+"""</td>
                      </tr>      
                    </tbody>
                  </table>    
                </div>                          
              </div>
            </div>

          </div> <!-- Second row ends -->  
          <div class="templatemo-flex-row flex-content-row">


            <div class="templatemo-content-widget white-bg col-1 text-center">
              <i class="fa fa-times"></i>
              <h2 class="text-uppercase">Scenery</h2>
              <h3 class="text-uppercase margin-bottom-10">Have a rest</h3>
              <img src="images/bicycle.jpg" alt="Bicycle" class="img-circle img-thumbnail">
            </div>

            <div class="templatemo-content-widget white-bg col-2">
              <i class="fa fa-times"></i>
              <div class="square"></div>
              <h2 class="templatemo-inline-block">Suggestion</h2><hr>
              """+weak_sug_list+"""              
            </div>
          </div>
                    
          <footer class="text-right">
            <p>Copyright &copy; 2084 Company Name 
            | Designed by <a href="#" target="_parent">templatemo</a></p>
          </footer>         
        </div>
      </div>
    </div>
    
    <!-- JS -->
    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/1.11.1/jquery.min.js"></script>      <!-- jQuery -->
    <script type="text/javascript" src="js/templatemo-script.js"></script>      <!-- Templatemo Script -->
    <script>
      $(document).ready(function(){
        // Content widget with background image
        var imageUrl = $('img.content-bg-img').attr('src');
        $('.templatemo-content-img-bg').css('background-image', 'url(' + imageUrl + ')');
        $('img.content-bg-img').hide();        
      });
    </script>
  </body>
</html>""")
