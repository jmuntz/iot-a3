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
		if (isset($_GET['fanOn']) && (isset($_GET['fanOn']))) {
			$fp = fopen('iot_config.json', 'w');
			fwrite($fp, json_encode($_GET));
			fclose($fp);
			echo "<span style='padding: 10px 15px;
				    border: 2px solid #80b8b5;
				    background: #b9f6f3;
				    position: relative;
				    top: 10px;
				    border-radius: 6px;'>Config updated!</span>";
		} 
		echo "<br><br>
		<h1>Update config.</h1>
		<form action='https://iot.porky.dev/ass3/app/api/update/config'>
			<input type='text' name='fanOn' placeholder='fanOn value..'>
			<input type='text' name='motorPosition' placeholder='motorPosition value..'>
			<button type='submit'>Submit</button>
		</form>";
		
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
