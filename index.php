<?php require_once 'config.php'; echo $root_URL; ?>

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

		<?php if (!isset($_SESSION["logged_in"]) || (!$_SESSION["logged_in"])) : ?>
			<form class="frm-login" action=<?php echo "$root_URL/api/login"; ?> method="post">
				<h1>Log in</h1>
				<input type="text" name="username" value="admin">
				<input type="text" name="password" value="password">
				<button type="submit" name="button"> Login</button>
			</form>
		<?php else : ?>
		    <h3>You're logged in!</h3>
			<a class="btn logout" href="logout.php">Logout</a>


		<div class="hero">
			<h1>Some c00l statz</h1>
			<div id="temp"><span class="value"><?php //echo round($most_recent['temp'], 2); ?>66°c</span><small>temperature</small></div>
			<div id="humidity"><span class="value"><?php //echo $most_recent['humidity']; ?>66</span><small>humidity</small></div>
			<p>Here we can showcase some hero stats such as median, mean, highest temp etc</p>
		</div>

		<div class="charts">
			<div class="chart">
				<h2> Temperature</h2>
				<canvas id="tempChart" style="max-width: 500px; max-height: 500px;"></canvas>
			</div>
			<div class="chart">
				<h2>Humidity</h2>
				<canvas id="humChart" style="max-width: 500px; max-height: 500px;"></canvas>
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
				fetch('//localhost/app/api/get/hosts')
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
				return fetch('//iot.porky.dev/ass3/app/api/get')
				.then(response => response.json())
			}

			getAll().then(function(data) {
				console.log(data);
			}).catch(function(error) {
				console.log("getAll request failed.");
			});




			let labels = [];

	  		for (i = 0; i < 25; i++) { labels[i] = i; }

			var ctx_temp = document.getElementById('tempChart').getContext('2d');
			var ctx_hum = document.getElementById('humChart').getContext('2d');
			var chart_temp = new Chart(ctx_temp, {
				type: 'line',
				data: {
					labels: labels,
				},
				options: {}
			});
			var chart_hum = new Chart(ctx_hum, {
				type: 'line',
				data: {
					labels: labels,
				},
				options: {}
			});

	  		updateChart();

	  		function updateChart() {
	  			setInterval(function () {
					temp = {};
					getAll().then(function(data) {
						console.log(data);

						console.log(data.temperature);
						console.log(data.humidity);


						dataset = [{}];
						for(index in data.temperature) {
							dataset[index] = {
								label: "Host " + index,//data.temperature[index].host,
								labels: labels,
								borderColor: "red",
								backgroundColor: 'transparent',
								data: data.temperature[index].data
							}
						}
						chart_temp.config.data.datasets = dataset;
						dataset = [{}];
						for(index in data.humidity) {

							dataset[index] = {
								label: "Host " + index,//data.humidity[index].host,
								labels: labels,
								borderColor: "purple",
								backgroundColor: 'transparent',
								data: data.humidity[index].data
							}
						}
						chart_hum.config.data.datasets = dataset;
						chart_hum.update();
						chart_temp.update();
					}).catch(function(error) {
						console.log("getAll chart request failed.");
					});





	  			}, 5000);
	  		};



		</script>



	<?php endif; ?>

	</body>
</html>
