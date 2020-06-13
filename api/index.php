<?php
session_start();

require __DIR__ . '/../source/RestServer/RestServer.php';
// require 'config.php';
require 'SaveController.php';
require 'GetController.php';
require 'UpdateController.php';

$server = new \RestServer\RestServer('debug');
$server->useCors = true;
$server->allowedOrigin = '*';

$server->addClass('SaveController', '/save');
$server->addClass('GetController', '/get');
$server->addClass('UpdateController', '/update');
$server->handle();
