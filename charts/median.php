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
		
		<?php if (!isset($_SESSION["logged_in"]) || (!$_SESSION["logged_in"])) : 
			require_once 'view/login.html'; ?>
		
		<?php else : 
			require_once 'view/menu.html'; ?>
		<h3>You're logged in!</h3>
		
		
		<div class="charts">
			<div class="chart">
				<h2> Median data</h2>
				<p> Calculates the mean of each device for the last 25 datapoints.</p>
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

			function getTemperature() {
				return fetch('https://iot.porky.dev/ass3/app/api/get/temperature/25')
				.then(response => response.json())
			}

			function getHumidity() {
				return fetch('https://iot.porky.dev/ass3/app/api/get/humidity/25')
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
			
			dataset = [{}];
			function updateChart() {
				getAll().then(function(data) {
					dataset = [{}];
					sum = 0;
					median_data = [];

					median_data = calculateMedian(data.temperature);

					dataset[0] = {
						label: "Median",//data.temperature[index].host,
						labels: labels,
						borderColor: "orange",
						backgroundColor: 'transparent',
						data: median_data
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
					sum = 0;
					median_data = [];

					median_data = calculateMedian(data.temperature);

					dataset[0] = {
						label: "Median",//data.temperature[index].host,
						labels: labels,
						borderColor: "orange",
						backgroundColor: 'transparent',
						data: median_data
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
					sum = 0;
					median_data = [];

					median_data = calculateMedian(data.humidity);

					dataset[0] = {
						label: "Median",//data.temperature[index].host,
						labels: labels,
						borderColor: "orange",
						backgroundColor: 'transparent',
						data: median_data
					}

					chart.config.data.datasets = dataset;
					chart.update();
				}).catch(function(error) {
					console.log("getAll chart request failed.");
				});
			};


			function calculateMedian(data) {
				median_data = [];
				spliced_array = [];

				for (index in data) {
					spliced_array[index] = data[index].data.splice(0, TOTAL_SIZE).reverse()
				}
								
				
				for (var i = 0; i < spliced_array[0].length; i++) {
					median = [];
					for (var k = 0; k < spliced_array.length; k++) {
						median.push(spliced_array[k][i]);
					}	
					
					var half = Math.floor(median.length / 2);

				    if (median.length % 2) {
				        median_data.push(median[Math.floor(median.length / 2)]);
				    } else {
				        median_data.push(median[Math.floor(median.length / 2) -1]);
				    }
				}
				return median_data;
			}
 


		</script>
		<?php endif; ?>
	</body>
</html>