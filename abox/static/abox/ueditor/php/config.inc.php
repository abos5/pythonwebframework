<?php
    /**
     * Created by JetBrains PhpStorm.
     * User: 魏应彬
     * Date: 13-12-28
     * Time: 下午10:44
     * To change this template use File | Settings | File Templates.
     */
	$_baseDir = '/www/img2.37wanimg.com';
	$_uploadDir = $_baseDir.'/'.date("Y/md");	
	$_baseUrl = 'http://img2.37wanimg.com/'.date("Y/md/");///data/upload/
	if(!is_dir($_uploadDir)){
		mkdir($_uploadDir,0775,true);
	}
	