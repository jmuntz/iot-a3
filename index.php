<?php require_once 'config.php'; echo $root_URL; ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
	<head>
		<meta charset="utf-8">
		<title>IoT Sensor Project</title>
	</head>
	<link rel="stylesheet" href="./assets/stylesheet.css">
	<body>
		<h1>IoT Dashboard.</h1>
		<?php session_start(); ?>
		
		<?php if (!isset($_SESSION["logged_in"]) || (!$_SESSION["logged_in"])) : ?>
		<form class="frm-login" action=<?php echo "$root_URL/api/login"; ?> method="post">
			<h1>Log in</h1>
			<input type="text" name="username" value="admin">
			<input type="text" name="password" value="password">
			<button type="submit" name="button"> Login</button>
		</form>
		<?php else : ?>
		<ul class="nav menu">
			<li><a class="btn" href=<?php echo '"'.$root_URL .'"'; ?>>Home</a></li>
			<li><a class="btn logout" href="logout.php">Logout</a></li>
		</ul>
		<ul class="nav chart">
			<li><strong>Charts</strong></li>
			<li><a href=<?php echo '"'.$root_URL .'/charts/latest.php"'; ?>>Latest</a></li>
			<li><a href=<?php echo '"'.$root_URL .'/charts/mean.php"'; ?>>Mean</a></li>
			<li><a href=<?php echo '"'.$root_URL .'/charts/median.php"'; ?>>Median</a></li>
			<li><a href=<?php echo '"'.$root_URL .'/api/update/config.php"'; ?>>Config</a></li>
		</ul>
		<ul class="nav todo">
			<li><strong>todo's</strong>
			<li style="text-decoration: line-through;">Build out median chart</li>
			<li style="text-decoration: line-through;">Build out mean chart</li>
			<li style="text-decoration: line-through;">Add humidity to <em>latest</em> chart chart</li>
			<li style="text-decoration: line-through;">Add feature to allow actuator to act based on temperature</li>
			<li style="text-decoration: line-through;"> - needs to be editable via website</li>
			<li> Report</li>
		</ul>
		<h3>You're logged in!</h3>
		<div class="hero">
			<h1>Some c00l statz</h1>
			<div id="temp"><span class="value"></span><small>temperature</small></div>
			<div id="humidity"><span class="value"></span><small>humidity</small></div>
			<p>Here we can showcase some hero stats such as median, mean, highest temp etc</p>
			<br><br>
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