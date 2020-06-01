<?php

use \RestServer\RestException;

class SaveController {
	/**
     * Returns a JSON string object to the browser when hitting the root of the domain
     *
     * @url GET /
     */
    public function donkey() {
        return "ur a turd";
    }

	/**
     * Returns a JSON string object to the browser when hitting the root of the domain
     *
     * @url GET /temperature
     */
	public function saveTemp() {

		require_once './Database.php';
		$db = new Database();
		$pdo = $db->generatePDO();
		//
		// if (isset($_POST['data'])) {
		// 	if ($this->validData($_POST['data'])) {
		// 		return $this->saveData($_POST['data'], 'temperature');
		// 	} $this->throwError('Data not valid.');
		// } $this->throwError('Data not set.');
	}

	/**
     * Returns a JSON string object to the browser when hitting the root of the domain
     *
     * @url GET /humidity
     */
	public function saveHumidity() {
		if (isset($_POST['data'])) {
			if ($this->validData($_POST['data'])) {
				return $this->saveData($_POST['data'], 'humidity');
			} $this->throwError('Data not valid.');
		} $this->throwError('Data not set.');
	}

	private function validData($data) {
		return ((filter_var($data[0], FILTER_VALIDATE_IP)) && ($this->isValidTimeStamp($data[1]) && is_int($data[2])));
	}

	private function isValidTimeStamp($timestamp) {
	    return ((string) (int) $timestamp === $timestamp)
	        && ($timestamp <= PHP_INT_MAX)
	        && ($timestamp >= ~PHP_INT_MAX);
	}

	private function saveData($tmp_data, $type) {
		require_once './Database.php';
		$db = new Database();
		$pdo = $db->generatePDO();

		if (($type == "temperature") || ($type == "humidity")) {
			$data = [
				'host' => $tmp_data[0],
				'timestamp' => $tmp_data[1],
				'data' => $tmp_data[2],
			];
			echo "saving data:";
			print_r($tmp_data);
			$sql = "INSERT INTO " . $type . " (host, timestamp, data) VALUES (:host, :timestamp, :data)";

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

    /**
     * Throws an error
     *
     * @url GET /error
     */
    public function throwError($msg) {
        throw new RestException(666, "Saving data failed. $msg");
    }
}
