<?php

use \RestServer\RestException;
require_once './Database.php';

class UpdateController {
	private $db;

	function __construct() {
		$this->db = new Database();
	}

	/**
     * Returns a JSON string object to the browser when hitting the root of the domain
     *
     * @url GET /
     */
	public function donkey() {
		return "Update endpoint.";
	}

	/**
     * Returns a JSON string object to the browser when hitting the root of the domain
     *
     * @url GET /config
     */
	public function processConfigOptions() {
		if (isset($_GET['fanSpeed']) && (isset($_GET['motorPosition'])) && (isset($_GET['status']))) {
			$fp = fopen('iot_config.json', 'w');
			fwrite($fp, json_encode($_GET));
			fclose($fp);
			echo "<style>* { font-family: sans-serif; }</style>
			<span style='padding: 10px 15px;
				    border: 2px solid #80b8b5;
				    background: #b9f6f3;
				    position: relative;
				    top: 10px;
				    border-radius: 6px;'>Config updated!</span>";
		} 
		echo "<style>* { font-family: sans-serif; }</style>
		<br><br>
		<h1>Update config.</h1>
		<style>
		input, select {
			display: block;
			padding: 10px 15px;
			border-radius: 4px;
			margin-bottom: 5px;
			border: 1px solid #d1d1d1;
		}
		</style>
		<form action='https://iot.porky.dev/ass3/app/api/update/config'>
			<input type='text' name='fanSpeed' placeholder='Maximum fan speed'>
			<input type='text' name='motorPosition' placeholder='motorPosition value'>
			<label for='status'>Device mode:</label>
			<select id='status' name='status'>
				<option value='OFF' selected>OFF</option>
				<option value='ON'>ON</option>
				<option value='TEST'>TEST</option>
				<option value='SWEEP'>SWEEP</option>
			</select>
			<button type='submit'>Submit</button>
		</form>";

		$json = file_get_contents('https://iot.porky.dev/ass3/app/api/get/config');
		$obj = json_decode($json);
		echo "<br>Fan speed: " . $obj->fanSpeed;
		echo "<br>Motor position: " . $obj->motorPosition;
		echo "<br>Status: " . $obj->status;
		
	}

    /**
     * Throws an error
     *
     * @url GET /error
     */
    public function throwError($msg) {
        throw new RestException(401, "$msg");
    }


	private function dump($data) {
		echo "<pre>";
		print_r($data);
		echo "</pre>";
	}
}
