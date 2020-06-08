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
		<ul class="nav menu">
			<li><a class="btn" href=<?php echo '"'.$root_URL .'"'; ?>>Home</a></li>
			<li><a class="btn logout" href="logout.php">Logout</a></li>
		</ul>
		<ul class="nav chart">
			<li><strong>Charts</strong></li>
			<li><a href=<?php echo '"'.$root_URL .'/charts/latest.php"'; ?>>Latest</a></li>
			<li><a href=<?php echo '"'.$root_URL .'/charts/mean.php"'; ?>>Mean</a></li>
			<li><a href=<?php echo '"'.$root_URL .'/charts/median.php"'; ?>>Median</a></li>
		</ul>
		<ul class="nav todo">
			<li><strong>todo's</strong>
				<li>Build out median chart</li>
				<li>Build out mean chart</li>
				<li style="text-decoration: line-through;">Add humidity to <em>latest</em> chart chart</li>
				<li>Add feature to allow actuator to act based on temperature</li>
				<li> - needs to be editable via website</li>
				<li> Report</li>
			</ul>
			<h3>You're logged in!</h3>
			
			
			<div class="charts">
				<div class="chart">
					<h2> Latest data</h2>
					<p> Gets the last 25 results for each client device.</p>
					<canvas id="chart" style="max-width: 800px; max-height: 600px;"></canvas>
				</div>
				
				<button onclick=rechartTemperature();>Temperature</button>
				<button onclick=rechartHumidity();>Humidity</button>
			</div>
			<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
			<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"></script>
			<script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
			<script>

				const TOTAL_SIZE = 25;



				let clients = [];
				function getTotalHosts() {
					fetch('//iot.porky.dev/ass3/app/api/get/hosts')
					.then(response => response.json())
					.then(function(data) {
						clients = data;
					})
				}
				
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
				for (i = 0; i < TOTAL_SIZE; i++) { labels[i] = i; }
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
					getAll().then(function(data) {
						dataset = [{}];
						
						for (index in data.temperature) {
							dataset[index] = {
								// label: "Client " + index,//data.temperature[index].host,
								label: data.temperature[index].client_addr,//data.temperature[index].host,
								labels: labels,
								borderColor: "red",
								backgroundColor: 'transparent',
								data: data.temperature[0].data.splice(0, TOTAL_SIZE).reverse()
							}
						}

						chart.config.data.datasets = dataset;
						chart.update();
					}).catch(function(error) {
						console.log("getAll chart request failed.");
					});
				};
				function rechartTemperature() {
					getAll().then(function(data) {
						dataset = [{}];
						
						for (index in data.temperature) {
							dataset[index] = {
								// label: "Client " + index,//data.temperature[index].host,
								label: data.temperature[index].client_addr,//data.temperature[index].host,
								labels: labels,
								borderColor: "red",
								backgroundColor: 'transparent',
								data: data.temperature[0].data.splice(0, TOTAL_SIZE).reverse()
							}
						}
						chart.config.data.datasets = dataset;
						chart.update();
					}).catch(function(error) {
						console.log("getAll chart request failed.");
					});
				};
				function rechartHumidity() {
					getAll().then(function(data) {
						dataset = [{}];
						
						for (index in data.humidity) {
							dataset[index] = {
								// label: "Client " + index,//data.humidity[index].host,
								label: data.humidity[index].client_addr,//data.temperature[index].host,
								labels: labels,
								borderColor: "purple",
								backgroundColor: 'transparent',
								data: data.humidity[0].data.splice(0, TOTAL_SIZE).reverse()
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