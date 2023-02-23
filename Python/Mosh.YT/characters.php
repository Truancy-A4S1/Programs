<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Characters</title>
	<div><h1></ha></div>
	<style>
		body
		{
			background-image: url('css/bg.jpg') ;
			background-repeat: no-repeat;
			background-attachment: fixed;
			background-size: cover;
			overflow: hidden;
			height: 100%;
			margin: 0;

		}
		table
		{
			background-color: #ebebeb;
			background: rgba(255,255,255,0.5);
			border-block-color: ;
			border-style: groove;
			border-collapse: collapse;


		}

		.table1
		{
			width: 1000px;
			height: 600px;
			overflow-y: auto;
		}
	

		table, th, td
		{
			border: 1px solid black;
			// border-radius: 5px;
			text-align: left;
			color: #010101;
			padding: 0px;

		}
		
		table
		{
			margin-right: auto;
			margin-left: auto;
		}

		th, td
		{
			width: 100px;
			height: 50px;
			padding-left: 10px;
		}

		tr:hover
		{
			background-color: silver;
		}

		header
		{
			background-color: #0a0a0a;
			opacity: 94%;
			text-align: center;
			box-shadow: #050505;
			padding: 15px;
		}

		header li
		{
			display: inline;
			padding-left: 45px;
			transition: .3s ease;
		}

		header li a
		{
			color: white;
			text-decoration: none;
			padding: 9px;

		}

		header li a:hover
		{
			color: #f5f5dc;
		}

		.h2
		{
			text-align: center;
		}
	</style>


</head>
<body>
	<header>
		<ul>
			<li><a class="taggs" href="wot_index.html">Home</a></li>
			<li><a class="taggs" href="map.html">Map</a></li>
			<li><a class="taggs" href="characters.php">Characters</a></li>
			<li><a class="taggs" href="chapters.html">Chapters</a></li>
			<li><a class="taggs" href="#">Terms</a></li>
		</ul>
	</header>
	<br><br><br>

	<br><br><br>
	<div class="table1" id="container" style="overflow-x: auto;">
	<table>
		<tr>
			<th colspan="4" style="text-align: center;">CHARACTER LIST</th>
		</tr>
		<tr>
			<th>First name</th>
			<th>Last name</th>
			<th>Gender</th>
			<th>Nationality</th>
		</tr>
		<?php
		$conn = mysqli_connect("localhost", "root", "", "rand");
		
		// Check connection
		if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
		}

		$sql = "SELECT charname, charsurname, gender, nationality FROM wot";
		$result = $conn->query($sql);
		if ($result->num_rows > 0) {
		// output data of each row
		while($row = $result->fetch_assoc()) {
			echo "<tr><td>" . $row["charname"]. "</td><td>" . $row["charsurname"] . "</td><td>" 
			. $row["gender"] . "</td><td>" . $row["nationality"]. "</td></tr>";
		}
		echo "</table>";
		} else { echo "0 results"; }
		$conn->close();
		?>
	</table>
</div>
</body>
</html>