<?php

use \RestServer\RestException;
require_once './Database.php';

class GetController {
	private $db;

	function __construct() {
		$this->db = new Database();
	}

    /**
     * Returns a JSON string object to the browser when hitting the root of the domain
     *
     * @url GET /
     */
	public function getData($limit = 25) {
 		try {
 		   $pdo = $this->db->generatePDO();

 		   $t_sql = "SELECT * FROM temperature ORDER BY id DESC LIMIT $limit";
 		   $h_sql = "SELECT * FROM humidity ORDER BY id DESC LIMIT $limit";

 		   $getTemp = $pdo->prepare($t_sql);
 		   $getTemp->execute();
 		   $getHum = $pdo->prepare($h_sql);
 		   $getHum->execute();

 		   $temp =  $getTemp->fetchAll(PDO::FETCH_ASSOC);
 		   $hum = $getHum->fetchAll(PDO::FETCH_ASSOC);


 		   if (!empty($temp)) {
 			   $host = '';
 			   $arr_t = array();
 			   $dataset = [];
 			   $dataset_t = [];
 			   $dataset_h = [];
 			   $data_obj = [];
 			   $host_list = $this->getHosts();


 			   foreach ($host_list as $key => $host) {
 				   $data_obj['host'] = $host;
 				   $sql = "SELECT * FROM temperature WHERE host = '$host' ORDER BY id DESC LIMIT $limit";
 				   $q = $pdo->prepare($sql);
 				   $q->execute();
 				   $data = $q->fetchAll(PDO::FETCH_ASSOC);
 				   $data_obj['data'] = [];

 				   foreach($data as $key => $value) {
 					   array_push($data_obj['data'], $value['data']);
 				   }
 				   array_push($dataset_t, $data_obj);

 			   }
 			   foreach ($host_list as $key => $host) {
 				   $data_obj['host'] = $host;
 				   $sql = "SELECT * FROM humidity WHERE host = '$host' ORDER BY id DESC LIMIT $limit";
 				   $q = $pdo->prepare($sql);
 				   $q->execute();
 				   $data = $q->fetchAll(PDO::FETCH_ASSOC);
 				   $data_obj['data'] = [];

 				   foreach($data as $key => $value) {
 					   array_push($data_obj['data'], $value['data']);
 				   }
 				   array_push($dataset_h, $data_obj);

 			   }

 			   $dataset['temperature'] = $dataset_t;
 			   $dataset['humidity'] = $dataset_h;

 			   return $dataset;
 		   }

 	   } catch (PDOException $e) {
 		   $this->throwError($e->getMessage());
 	   }
    }

	/**
	 * Returns a JSON string object to the browser when hitting the root of the domain
	 *
	 * @url GET /temperature
	 * @url GET /temperature
	 * @url GET /temperature/$limit
	 * @url GET /temperature/$limit/$host
	 */
	public function getTemp($host = null, $limit = 25) {
		try {
			$pdo = $this->db->generatePDO();

			$sql = $host ? "SELECT * FROM temperature WHERE host = '$host' ORDER BY id DESC LIMIT $limit" : "SELECT * FROM temperature ORDER BY id DESC LIMIT $limit";

			$getTemp = $pdo->prepare($sql);
			$getTemp->execute();
			$data =  $getTemp->fetchAll(PDO::FETCH_ASSOC);
			return $data;

		} catch (PDOException $e) {
			$this->throwError($e->getMessage());
		}

	}

	/**
	 * Returns a JSON string object to the browser when hitting the root of the domain
	 *
	 * @url GET /humidity
	 * @url GET /humidity/$limit
	 * @url GET /humidity/$limit/$host
	 */
	 public function getHum($host = null, $limit = 10) {
		try {
			$pdo = $this->db->generatePDO();

			$sql = $host ? "SELECT * FROM humidity WHERE host = '$host' ORDER BY id DESC LIMIT $limit" : "SELECT * FROM humidity ORDER BY id DESC LIMIT $limit";

			$getTemp = $pdo->prepare($sql);
			$getTemp->execute();
			$data =  $getTemp->fetchAll(PDO::FETCH_ASSOC);
			return $data;

		} catch (PDOException $e) {
			$this->throwError($e->getMessage());
		}
	}


	/**
	 * Returns a JSON string object to the browser when hitting the root of the domain
	 *
	 *
	 * @url GET /all
	 */





		/**
		 * Returns a JSON string object to the browser when hitting the root of the domain
		 * Gets the unique number of hosts that have submitted data to server.
		 * Only uses temp data for now.
		 *
		 * @url GET /hosts
		 */
		 public function getHosts() {
	 		try {
	 			$pdo = $this->db->generatePDO();

	 			$sql = "SELECT DISTINCT(host) FROM temperature";

				$hosts = array();

	 			$getTemp = $pdo->prepare($sql);
	 			$getTemp->execute();
				$data = $getTemp->fetchAll(PDO::FETCH_ASSOC);

				foreach($data as $key => $value)
					array_push($hosts, $value['host']);
	 			return $hosts;

	 		} catch (PDOException $e) {
	 			$this->throwError($e->getMessage());
	 		}
	 	}

    /**
     * Get Charts
     *
     * @url GET /charts
     * @url GET /charts/$id
     * @url GET /charts/$id/$date
     * @url GET /charts/$id/$date/$interval/
     * @url GET /charts/$id/$date/$interval/$interval_months
     */
    public function getCharts($id=null, $date=null, $interval = 30, $interval_months = 12) {
        echo "$id, $date, $interval, $interval_months";
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
