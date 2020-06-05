<?php require_once '../config.php'; ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<link rel="stylesheet" href="../assets/stylesheet.css">
	<body>
		<?php session_start(); ?>
		
		
		<?php if (!isset($_SESSION["logged_in"]) || (!$_SESSION["logged_in"])) : ?>
		<form class="frm-login" action=<?php echo "$root_URL/api/login"; ?> method="post">
			<h1>Log in</h1>
			<input type="text" name="username" value="admin">
			<input type="text" name="password" value="password">
			<button type="submit" name="button"> Login</button>
		</form>
		<?php else : ?>
		<ul class="menu">
			<li><a class="btn" href=<?php echo '"'.$root_URL .'"'; ?>>Home</a></li>
			<li><a class="btn logout" href="logout.php">Logout</a></li>
		</ul>
		<h3>You're logged in!</h3>
		
		
		<div class="charts">
			<div class="chart">
				<h2> Latest data</h2>
				<canvas id="chart" style="max-width: 800px; max-height: 600px;"></canvas>
			</div>
			
		</div>
		<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"></script>
		<script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
		<script>
			let clients = [];
			let tempJSON;
			let humJSON;
			let temp_values = [];
			let hum_values = [];
			function getTotalHosts() {
				fetch('//iot.porky.dev/ass3/app/api/get/hosts')
				.then(response => response.json())
				.then(function(data) {
					clients = data;
				})
			}
			function generateDatasets() {
					let temp_dataset 	= [];
					let hum_dataset 	= [];
				let boss_data = {};
				var promise = new Promise(function(resolve, reject) {
					getTotalHosts();
					setTimeout(function() {
						clients.forEach((client, i) => {
							dataset = {};
							arr = [];
							tempJSON.forEach((data, i) => {
								if (data.host == client)
									arr.push(data.data);
							});
							dataset.host = client;
							dataset.data = arr;
							temp_dataset.push(dataset);
							dataset = {};
							arr = [];
							humJSON.forEach((data, i) => {
								if (data.host == client)
								arr.push(data.data);
							});
							dataset.host = client;
							dataset.data = arr;
							hum_dataset.push(dataset);
						});
						boss_data.temp = temp_dataset;
						boss_data.hum = hum_dataset;
						resolve(boss_data);
					}, 1000); // set timeout to give fetches time to finish
				});
				return promise;
			};
			function getAll() {
				return fetch('https://iot.porky.dev/ass3/app/api/get')
				.then(response => response.json())
			}
			getAll().then(function(data) {
				console.log(data);
			}).catch(function(error) {
				console.log("getAll request failed.");
			});
			let labels = [];
			for (i = 0; i < 25; i++) { labels[i] = i; }
			var ctx = document.getElementById('chart').getContext('2d');
			var chart = new Chart(ctx, {
				type: 'line',
				data: {
					labels: labels,
				},
				options: {}
			});
			updateChart();
			function updateChart() {
					temp = {};
					getAll().then(function(data) {
						console.log(data);
						console.log(data.temperature);
						console.log(data.humidity);
						dataset = [{}];
						for(index in data.temperature) {
							dataset[index] = {
								label: "Client " + index,//data.temperature[index].host,
								labels: labels,
								borderColor: "red",
								backgroundColor: 'transparent',
								data: data.temperature[index].data
							}
						}
						chart.config.data.datasets = dataset;
						chart.update();
					}).catch(function(error) {
						console.log("getAll chart request failed.");
					});
			};
		</script>
		<?php endif; ?>
	</body>
</html>