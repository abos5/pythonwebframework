<?php
    /**
     * Created by JetBrains PhpStorm.
     * User: taoqili
     * Date: 12-1-16
     * Time: 上午11:44
     * To change this template use File | Settings | File Templates.
     */
    header("Content-Type: text/html; charset=utf-8");
	ini_set("display_errors","On");
    error_reporting( E_ERROR | E_WARNING );
    include "config.inc.php";
    //需要遍历的目录列表，最好使用缩略图地址，否则当网速慢时可能会造成严重的延时
//echo "sdfjsdkjfskld";
    $action = htmlspecialchars( $_POST[ "action" ] );
    if ( $action == "get" ) {
        $files = array();
		$tmp = getfiles( $_uploadDir );
		//echo "sdfjsdkjfskld";
		if($tmp){
			$files = array_merge($files,$tmp);
		}
        if ( !count($files) ) return;
        //rsort($files,SORT_STRING);
        $str = "";
        foreach ( $files as $file ) {
            $str .= $file . "ue_separate_ue";
        }
        echo $str;
    }

    /**
     * 遍历获取目录下的指定类型的文件
     * @param $path
     * @param array $files
     * @return array
     */
    function getfiles( $path , &$files = array() )
    {
		global $_baseUrl,$_uploadDir;
        if ( !is_dir( $path ) ) return null;
        $handle = opendir( $path );
		//echo $path;
		$sort = array();
        while ( false !== ( $file = readdir( $handle ) ) ) {
            if ( $file != '.' && $file != '..' ) {
                $path2 = $path . '/' . $file;
                if ( is_dir( $path2 ) ) {
                    //getfiles( $path2 , $files );
                } else {
                    if ( preg_match( "/\.(gif|jpeg|jpg|png|bmp)$/i" , $file ) ) {
                    	$fTime   =   filemtime($path2);
                    	$sort[] = $fTime;
                        $files[] = $_baseUrl.$file;
                    }
                }
            }
        }
        //print_r($sort);
        array_multisort($sort,SORT_DESC,$files);
        return $files;
    }
