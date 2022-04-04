<?php

include('../simple_html_dom.php');



$m16 = $_GET['name'];
$url2 = 'https://twitter-trends.iamrohit.in/'.$m16;
$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, $url2);
curl_setopt($curl, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
$result = curl_exec($curl);
curl_close($curl);
//echo $result;

$domResult = new simple_html_dom();
$domResult->load($result);
$noarray=array();
$noarray2=array();
$noarray3=array();

foreach($domResult->find('a.tweet') as $ul) {
    $noarray[]= $ul->plaintext;
    
}



foreach($domResult->find('th.sml') as $ul) {
   $noarray2[]= $ul->plaintext;
    
}


foreach($domResult->find('a.tweet') as $ul) {
   $noarray3[]= $ul->href;
    
}
unset($noarray2[0]);
$array = array_values($noarray2);


$x= 1;
foreach ($noarray as $key => $val) {
    $combined[] = ["rank"=>$x,"name"=>$val, "volume"=>$array[$key], "url"=>$noarray3[$key]];
    $x++;
}
echo json_encode(array("trends"=>$combined));
?>



<?
$x= 1;

foreach (array_combine($noarray, $array) as $code => $name) {
  
    $url2 = $noarray3[$x-1];
    $mc = str_replace("-", "%20", $m16);
 $books =array("rank"=>$x,"trends"=>    array(
       
        "author" =>$code,
        "hashtag" => $name
    ));
    
  //echo $x.'-'.$m16.'-'.$code.'-'.$name.'<br>';
  ?>
  <?php
//$myObj->rank = $x;
//$myObj->rank->hashtag = $code;
//$myObj->rank->volume = $name;

//$myJSON = json_encode($myObj);

//echo $myJSON;
?>

 

</script><?php
    $x++;
}

?>



  

  






