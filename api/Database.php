<?php
use \RestServer\RestException;

class Database {
	private $host = "";
	private $db = "";
	private $username = "";
	private $password = "";

	function __construct() {
		require_once '../config.php';

		$this->host = $host;
		$this->db = $db;
		$this->username = $username;
		$this->password = $password;
	}

	function generatePDO() {
	    try {
			$pdo = new PDO("mysql:host=$this->host;dbname=$this->db;charset=UTF8", $this->username, $this->password);
			$pdo->setAttribute( PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION );
			return $pdo;
		} catch (PDOException $e) {
			$this->throwError($e->getMessage());
		}
	}

	public function throwError($msg) {
        throw new RestException(666, "Database connection failed. $msg");
    }
}

?>
