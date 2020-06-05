<?php

use \RestServer\RestException;

class SaveController {
	// $_POST = json_decode(file_get_contents("php://input"), true);

	/**
     * Returns a JSON string object to the browser when hitting the root of the domain
     *
     * @url GET /
     */
    public function donkey() {
        return "ur a turddd";
    }


	/**
     * Returns a JSON string object to the browser when hitting the root of the domain
     *
	 * @url POST /dump
     */
    public function testy() {
		$json = json_decode(file_get_contents('php://input'), true);
		return $json;
	}




	/**
     * Returns a JSON string object to the browser when hitting the root of the domain
     *
     * @url POST /temperature
     */
	public function saveTemp() {
		$json = json_decode(file_get_contents('php://input'), true);

		if (isset($json)) {
			if ($this->validData($json)) {
				return $this->saveData($this->formatTemperature($json), 'temperature');
			} $this->throwError('Data not valid.');
		} $this->throwError('Data not set.');
	}

	/**
     * Returns a JSON string object to the browser when hitting the root of the domain
     *
     * @url POST /humidity
     */
	public function saveHumidity() {
		$json = json_decode(file_get_contents('php://input'), true);

		if (isset($json)) {
			if ($this->validData($json)) {
				return $this->saveData($this->formatHumidity($json), 'humidity');
			} $this->throwError('Data not valid.');
		} $this->throwError('Data not set.');
	}

	private function validData($data) {
		return true;
		//return ((filter_var($data[0], FILTER_VALIDATE_IP)) && ($this->isValidTimeStamp($data[1]) && is_int($data[2])));
	}

	private function isValidTimeStamp($timestamp) {
	    return ((string) (int) $timestamp === $timestamp)
	        && ($timestamp <= PHP_INT_MAX)
	        && ($timestamp >= ~PHP_INT_MAX);
	}

	private function saveData($data, $type) {
		require_once './Database.php';
		$db = new Database();
		$pdo = $db->generatePDO();

		if (($type == "temperature") || ($type == "humidity")) {
			$sql = "INSERT INTO " . $type . " (client_addr, timestamp, value) VALUES (:client_addr, :timestamp, :value)";
			$stmt = $pdo->prepare($sql);

			if (!$stmt->execute($data)) {
				$this->throwError($pdo->errorInfo());
			} else {
				return "Success";
			}
		} else {
			$this->throwError("Data type not set.");
		}

	}


	private function formatTemperature($json) {
		// return $json;
		$data["client_addr"] = $_SERVER['REMOTE_ADDR'];
		$data["timestamp"] = time();
		$data["value"] = $json["temp"];

		return $data;
	}

	private function formatHumidity($json) {
		// return $json;
		$data["client_addr"] = $_SERVER['REMOTE_ADDR'];
		$data["timestamp"] = time();
		$data["value"] = $json["humidity"];

		return $data;
	}

    /**
     * Throws an error
     *
     * @url GET /error
     */
    public function throwError($msg) {
        throw new RestException(666, "Saving data failed. $msg");
    }
}
