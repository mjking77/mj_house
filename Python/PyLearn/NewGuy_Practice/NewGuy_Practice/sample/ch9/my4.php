<H1>hello PHP, powenko.com </H1><?php if( $_GET["a"] || $_GET["b"] ) {    echo shell_exec("sudo /usr/lib/cgi-bin/cgi2.py -a ".$_GET["a"]." -b".$_GET$
 }else{    echo "php?a=on&b=off"; }?>