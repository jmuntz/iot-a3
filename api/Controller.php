<?php

use \RestServer\RestException;

class Controller {
    /**
     * Returns a JSON string object to the browser when hitting the root of the domain
     *
     * @url GET /
     */
    public function donkey() {
        return "Hello World";
    }

	/**
     * Returns a JSON string object to the browser when hitting the root of the domain
     *
     * @url GET /temp
     */
	public function getTemp() {
		$data = array();
		array_push($data, array(
			array("192.168.1.11", "17", 1590766410),
			array("192.168.1.11", "17", 1590766410),
			array("192.168.1.11", "18", 1590766410),
		));

		array_push($data, array(
			array("192.168.1.14", "13", 1590766410),
			array("192.168.1.14", "13", 1590766410),
		));

		array_push($data, array(
			array("192.168.1.66", "11", 1590766410),
			array("192.168.1.66", "11", 1590766410),
			array("192.168.1.66", "11", 1590766410),
			array("192.168.1.66", "11", 1590766410)
		));

		return $data; // serializes object into JSON
	}

	/**
	 * Returns a JSON string object to the browser when hitting the root of the domain
	 *
	 * @url GET /hum
	 */
	public function getHum() {
		$data = array();
		array_push($data, array(
			array("192.168.1.11", "17", 1590766410),
			array("192.168.1.11", "17", 1590766410),
			array("192.168.1.11", "18", 1590766410),
		));

		array_push($data, array(
			array("192.168.1.14", "13", 1590766410),
			array("192.168.1.14", "13", 1590766410),
		));

		array_push($data, array(
			array("192.168.1.66", "11", 1590766410),
			array("192.168.1.66", "11", 1590766410),
			array("192.168.1.66", "11", 1590766410),
			array("192.168.1.66", "11", 1590766410)
		));

		return $data; // serializes object into JSON
	}

    /**
     * Logs in a user with the given username and password POSTed. Though true
     * REST doesn't believe in sessions, it is often desirable for an AJAX server.
     *
     * @url POST /login
     */
    public function login() {
		print_r($_POST);
		if (isset($_POST['username']) && isset($_POST['password'])) {
			$username = filter_var($_POST["username"], FILTER_SANITIZE_STRING);
			$password = filter_var($_POST["password"], FILTER_SANITIZE_STRING);

			if (($username == "admin") && ($password == "password")) {
				$_SESSION["logged_in"] = true;

				header("Location: ../index.php");
				exit();
			} else {
				return array("error" => "Account details incorrect you numpty");
			}
		} else {
			return array("error" => "something bad happened");
		}





    }

    /**
     * Gets the user by id or current user
     *
     * @url GET /users/$id
     * @url GET /users/current
     */
    public function getUser($id = null) {
        // if ($id) {
        //     $user = User::load($id); // possible user loading method
        // } else {
        //     $user = $_SESSION['user'];
        // }

        return array("id" => $id, "name" => null); // serializes object into JSON
    }

    /**
     * Saves a user to the database
     *
     * @url POST /users
     * @url PUT /users/$id
     */
    public function saveUser($id = null, $data) {
        // ... validate $data properties such as $data->username, $data->firstName, etc.
        // $data->id = $id;
        // $user = User::saveUser($data); // saving the user to the database
        $user = array("id" => $id, "name" => null);
        return $user; // returning the updated or newly created user object
    }

    /**
     * Gets user list
     *
     * @url GET /users
     */
    public function listUsers($query) {
        $users = array('Andra Combes', 'Valerie Shirkey', 'Manda Douse', 'Nobuko Fisch', 'Roger Hevey');
        if (isset($query['search'])) {
          $users = preg_grep("/{$query[search]}/i", $users);
        }
        return $users; // serializes object into JSON
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
    public function throwError() {
        throw new RestException(401, "Empty password not allowed");
    }
}
