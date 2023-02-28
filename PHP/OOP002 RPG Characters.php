<?php
class Character{
	protected $name;
	protected $race;
	protected $magic;

	public function __construct($name, $race, $magic){
		$this->name = $name;
		$this->race = $race;
		$this->magic = $magic;
	}
	public function get_name(){
		return $this->name;
	}
	public function get_race(){
		return $this->race;
	}
	public function get_magic(){
		return $this->magic;
	}
}

class Player extends Character{
	private $class;
	private $health;
	private $dexterity;

	public function __construct($name, $race, $class, $mgc, $hp, $dex){
		$this->name = $name;
		$this->race = $race;
		$this->class = $class;
		$this->magic = $mgc;
		$this->health = $hp;
		$this->dexterity = $dex;
	}
	public function display_stats(){
		echo "Name: {$this->name}<br>Race: {$this->race}<br>Class: {$this->class}<br>Magic: {$this->magic}<br>Health: {$this->health}<br>Dexterity: {$this->dexterity}<br><br>";
	}
	public function get_hp(){
		return $this->health;
	}
	public function get_dex(){
		return $this->dex;
	}
	public function __destruct(){
		echo "-{$this->name} joined the game-<br>";
	}
}

class NPC extends Character{
	private $job;

	public function __construct($name, $race, $magic, $job){
		$this->name = $name;
		$this->race = $race;
		$this->magic = $magic;
		$this->job = $job;
	}
	public function display_stats(){
		echo "Name: {$this->name}<br>Job: {$this->job}<br>Magic: {$this->magic}<br><br>";

	}
	public function get_job(){
		return $this->job;
	}
	public function __destruct(){
		echo "-{$this->name}, a new NPC was created-<br>";
	}
}

echo "<b>Using 'Character' (master class)<br></b>";
$char01 = new Character("Trodius","Human","Fire");
echo "{$char01->get_name()} {$char01->get_race()} {$char01->get_magic()} <br>";

$char02 = new Character("Frey","Human","Lightning");
echo "{$char02->get_name()} {$char02->get_race()} {$char02->get_magic()} <br><br>";

echo "<b>Using 'Player extends Character' (sub class)</b><br>";
$char03 = new Player("Safa", "elf", "druid", "healing", 194, 6);
echo "{$char03->display_stats()}";

$char04 = new Player("Jaden", "leonin", "rogue", "illusion", 172, 7);
echo "{$char04->display_stats()}";

$char05 = new Player("Maitland", "dragonbord", "sorcerer", "astral", 235, 5);
echo "{$char05->display_stats()}";

echo "<b>Using 'NPC extends Character' (sub class)</b><br>";
$char06 = new NPC("Yu","human","charm","trader");
echo "{$char06->display_stats()}";

$char07 = new NPC("Arya","half elf","evocation","adventurer");
echo "{$char07->display_stats()}";


?>