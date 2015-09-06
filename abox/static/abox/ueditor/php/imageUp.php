<?php
	

    /**
     * Created by JetBrains PhpStorm.
     * User: taoqili
     * Date: 12-7-18
     * Time: 上午10:42
     */
    header("Content-Type: text/html; charset=utf-8");
	session_start();
    error_reporting(E_ERROR | E_WARNING);
    date_default_timezone_set("Asia/chongqing");
    include "Uploader.class.php";
	include 'config.inc.php';
    //上传图片框中的描述表单名称，
    $title = htmlspecialchars($_POST['pictitle'], ENT_QUOTES);
    $path = htmlspecialchars($_POST['dir'], ENT_QUOTES);
    $not_cut_img = htmlspecialchars($_POST['not_cut_img'], ENT_QUOTES);
    //上传配置
    $config = array(
        "savePath" => $_uploadDir."/",
        "maxSize" => 2000, //单位KB
        "allowFiles" => array(".gif", ".png", ".jpg", ".jpeg", ".bmp")
    );

    //生成上传实例对象并完成上传
    $up = new Uploader("upfile", $config);

    /**
     * 得到上传文件所对应的各个参数,数组结构
     * array(
     *     "originalName" => "",   //原始文件名
     *     "name" => "",           //新文件名
     *     "url" => "",            //返回的地址
     *     "size" => "",           //文件大小
     *     "type" => "" ,          //文件类型
     *     "state" => ""           //上传状态，上传成功时必须返回"SUCCESS"
     * )
     */
    $info = $up->getFileInfo();
	if(!$not_cut_img){
		$img_info = getimagesize($info['path']);
		if($img_info!==FALSE && $img_info[0]>500){
			include dirname(__FILE__).'/../../../lib/ResizeImage.php';
			$img = $info['path'];
			$exName = strtolower(substr($img,(strrpos($img,'.')+1)));
			$imgSmall = str_replace($exName, "small.", $img).$exName;
			new ResizeImage($img, 500, 100000, 0, $imgSmall);
			$imgSmall = str_replace($exName, "small.", $info['url']).$exName;		
			$info['url'] = $imgSmall;
			@unlink($img);
		}
	}


   // $file = str_replace("http://", '', $info["url"]);
	exec("/usr/local/webserver/php/bin/php /www/admin2013.37wan.com/daemon/file_sync.php \"items:queue|type:dir|file:img2.37wanimg.com|admin:{$_SESSION['admin']['USER_NAME']}\">/dev/null &");
    /**
     * 向浏览器返回数据json数据
     * {
     *   'url'      :'a.jpg',   //保存后的文件路径
     *   'title'    :'hello',   //文件描述，对图片来说在前端会添加到title属性上
     *   'original' :'b.jpg',   //原始文件名
     *   'state'    :'SUCCESS'  //上传状态，成功时返回SUCCESS,其他任何值将原样返回至图片上传框中
     * }
     */
	$title = '';
    echo "{'url':'" . $info["url"] . "','title':'" . $title . "','original':'" . $info["originalName"] . "','state':'" . $info["state"] . "'}";

