<?php
$age = $_GET["age"];
$sex = $_GET["sex"];
$cp = $_GET["cp"];
$trestbps = $_GET["trestbps"];
$chol = $_GET["chol"];
$fbs = $_GET["fbs"];
$restecg = $_GET["restecg"];
$thalach = $_GET["thalach]";
$exang = $_GET["exang"];
$oldpeak = $_GET["oldpeak"];
$slope = $_GET["slope"];
$ca = $_GET["ca"];
$thal = $_GET["thal"];

system("/usr/anaconda/bin/python3 HEART.py ".$age." ".$sex." ".$cp." ".$trestbps." ".$chol." ".$fbs." ".$restecg." ".$thalach." ".$exang." ".$oldpeak." ".$slope." ".$ca." ".$thal." 2>&1");
?>