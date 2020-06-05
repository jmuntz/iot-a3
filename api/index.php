<?php
session_start();

require __DIR__ . '/../source/RestServer/RestServer.php';
// require 'config.php';
require 'Controller.php';
require 'SaveController.php';
require 'GetController.php';

$server = new \RestServer\RestServer('debug');
$server->useCors = true;
$server->allowedOrigin = '*';

$server->addClass('Controller');
$server->addClass('SaveController', '/save');
$server->addClass('GetController', '/get');
$server->handle();
