<?php
require_once('TwitterAPIExchange.php');
 
/** Set access tokens here - see: https://dev.twitter.com/apps/ **/
$settings = array(
   'oauth_access_token' => "af",
    'oauth_access_token_secret' => "asf",
    'consumer_key' => "asf",
    'consumer_secret' => "asf"
);

 $url = "https://api.twitter.com/1.1/search/tweets.json";
 
$requestMethod = "GET";
 
 

   
   $getfield = '?q=%23CampingWorldinAmerica&count=100';
 
$twitter = new TwitterAPIExchange($settings);


$twitter = new TwitterAPIExchange($settings);
    $myfile = fopen("peri.json", "w") or die("Unable to open file!");
    $txt = $twitter->setGetfield($getfield)
             ->buildOauth($url, $requestMethod)
                 ->performRequest();
    fwrite($myfile, $txt);
