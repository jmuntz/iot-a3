<ul class="nav menu">
	<li><a class="btn" href=<?php echo '"'.$root_URL .'"'; ?>>Home</a></li>
	<li><a class="btn logout" href="logout.php">Logout</a></li>
</ul>
<ul class="nav chart">
	<li><strong>Charts</strong></li>
	<li><a href=<?php echo '"'.$root_URL .'/charts/latest.php"'; ?>>Latest</a></li>
	<li><a href=<?php echo '"'.$root_URL .'/charts/mean.php"'; ?>>Mean</a></li>
	<li><a href=<?php echo '"'.$root_URL .'/charts/median.php"'; ?>>Median</a></li>
	<li><a href=<?php echo '"'.$root_URL .'/api/update/config"'; ?>>Config</a></li>
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