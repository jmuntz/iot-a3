<?php require_once 'config.php'; ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<link rel="stylesheet" href="./assets/stylesheet.css">
	<body>
		<h1>IoT Dashboard.</h1>
		<?php session_start(); ?>
		
		<?php if (!isset($_SESSION["logged_in"]) || (!$_SESSION["logged_in"])) : 
			require_once 'view/login.html'; ?>
		
		<?php else : 
			require_once 'view/menu.html'; ?>
		
		<h3>You're logged in!</h3>
		<div class="hero">
			<h1>Most recent data received</h1>
			<div id="temp"><span class="value"></span><small>temperature</small></div>
			<div id="humidity"><span class="value"></span><small>humidity</small></div>
			<p id="client"></p>
			<p id="timestamp"></p>
			<br><br>
			<p>Please view our data by selecting a chart on the right.</p>
		</div>

		<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"></script>
		<script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
	
		<?php endif; ?>

		<script>	
			
			function getTemp() {
				return fetch('https://iot.porky.dev/ass3/app/api/get/temperature/1')
				.then(response => response.json())
			}
			function getHum() {
				return fetch('https://iot.porky.dev/ass3/app/api/get/humidity/1')
				.then(response => response.json())
			}

			getTemp().then(function(data) {
				$("#temp .value").html(data[0].value + "c");
				$("#client").html("Received from client: " + data[0].client_addr);
				time = new Date(parseInt(data[0].timestamp + "000"));
				$("#timestamp").html(time.getDay() + " / " + time.getMonth() + " / " + time.getFullYear() + " " + time.getHours() + ":" + time.getMinutes());
			}).catch(function(error) {
				console.log("getAll chart request failed.");
			});

			getHum().then(function(data) {
				$("#humidity .value").html(data[0].value);
			}).catch(function(error) {
				console.log("getAll chart request failed.");
			});

		</script>
	</body>
</html>