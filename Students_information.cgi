#!"C:\xampp\perl\bin\perl.exe"
# The above line is perl execution path in xampp
# The below line tells the browser, that this script will send html content.
# If you miss this line then it will show "malformed header from script" error.

use CGI;
use DBI;
use DBD::mysql;
use warnings;

use CGI ':standard';

print header();
print "<h3>Student Information form</h3>", br();

print start_form;

print "First_Name:  ", textfield('first_name'), br();  
print "Last_Name:  ", textfield('last_name'), br();  
print "Home:  ", textfield('home'), br();  
print p, submit();
print end_form;

if (param()) 
{
    print "The Student name you entered was:\n ",em(param('first_name'),param('last_name'),param('home')),br(),br(),br();
      
}

$cgiobject = new CGI;

print $cgiobject->header,

$cgiobject->start_html (

        -title=>'Student details'
),
        $cgiobject->start_table ({-border=>'1'}), "\n",

        $cgiobject->start_Tr,
                $cgiobject->start_td,
                "First_Name",
                $cgiobject->end_td,
                $cgiobject->start_td,
                "Last_Name",
                $cgiobject->end_td,
				$cgiobject->start_td,
                "Home",
                $cgiobject->end_td,
        $cgiobject->end_Tr,
        $cgiobject->start_Tr,
                $cgiobject->start_td,
                "Rose",
                $cgiobject->end_td,
                $cgiobject->start_td,
                "Tyler",
                $cgiobject->end_td,
				$cgiobject->start_td,
                "Earth",
                $cgiobject->end_td,
        $cgiobject->end_Tr,
		$cgiobject->start_Tr,
                $cgiobject->start_td,
                "Zoe",
                $cgiobject->end_td,
                $cgiobject->start_td,
                "Heriot",
                $cgiobject->end_td,
				$cgiobject->start_td,
                "Space Station W3",
                $cgiobject->end_td,
        $cgiobject->end_Tr,
		
        $cgiobject->start_Tr,
                $cgiobject->start_td,
                "Jo",
                $cgiobject->end_td,
                $cgiobject->start_td,
                "Grant",
                $cgiobject->end_td,
				$cgiobject->start_td,
                "Earth",
                $cgiobject->end_td,
        $cgiobject->end_Tr,
		
		$cgiobject->start_Tr,
                $cgiobject->start_td,
                "Leela",
                $cgiobject->end_td,
                $cgiobject->start_td,
                "Grany",
                $cgiobject->end_td,
				$cgiobject->start_td,
                "Moon",
                $cgiobject->end_td,
        $cgiobject->end_Tr,
		
		$cgiobject->start_Tr,
                $cgiobject->start_td,
                "Romana",
                $cgiobject->end_td,
                $cgiobject->start_td,
                "nully",
                $cgiobject->end_td,
				$cgiobject->start_td,
                "Gallifrey",
                $cgiobject->end_td,
        $cgiobject->end_Tr,
		
			$cgiobject->start_Tr,
                $cgiobject->start_td,
                "Clara",
                $cgiobject->end_td,
                $cgiobject->start_td,
                "Oswald",
                $cgiobject->end_td,
				$cgiobject->start_td,
                "Gallifrey",
                $cgiobject->end_td,
        $cgiobject->end_Tr,
        $cgiobject->end_table, "\n",

$cgiobject->end_html;


# MYSQL CONFIG VARIABLES
$host = "localhost";
$database = "test";
$tablename = "inform";
$user = "user@localhost";
$pw = "";

# PERL DBI CONNECT()
$driver = "DBI:mysql:database=$database;host=$host"; 
$connect_me = DBI->connect($driver, $user, $pw);

# Create contacts table
my $sql = "CREATE TABLE IF NOT EXISTS inform (
id INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY(id),
first_name VARCHAR(64),
last_name VARCHAR(64),
home VARCHAR(255))";

my $run_query = $connect_me->prepare($sql);
$run_query->execute() or die "SQL Error: $DBI::errstr\n";

# Insert data into the table
$run_query = $connect_me->prepare("INSERT INTO inform(id,first_name, last_name, home) VALUES(?,?,?,?)");
$run_query->execute("1","Rose", "Tyler", "Earth");
$run_query->execute("2","Zoe", "Heriot", "Space Station W3");
$run_query->execute("3","Jo", "Grant", "Earth");
$run_query->execute("4","Leela", "Grany", "Moon");
$run_query->execute("5","Romana", "nully", "Gallifrey");
$run_query->execute("6","Clara", "Oswald", "Gallifrey");


# SELECT DB
$run_query = $connect_me->prepare("SELECT * FROM $tablename");
$run_query->execute();

print "<hr />";
print <<HTML_PAGE;
<html>
<head>
<title>Students Table</title>
</head>
<body>
<h3>Printing list of Students information from database</h3>
<table style={"-border":'1'," -align":'center'}>
<tr>
<th>Id</th>
<th>First Name</th>
<th>Last Name</th>
<th>Home</th>
</tr>
HTML_PAGE


#looping and displaying the result
while($result=$run_query->fetchrow_hashref()) {
  #print "<b>Value returned:</b> $result->{time}\n";
 
} 


$run_query->execute();
print "<table/>";
while(@result = $run_query->fetchrow_array()){
print "<tr/>";
print "<td>";
print " $result[0]\n";
print " $result[1]\n";
print " $result[2]\n";
print "$result[3]\n";
}


exit; #The script will exit now

   


# Create contacts table
my $sql = "CREATE TABLE IF NOT EXISTS addressbook (
lname VARCHAR(64),
fname VARCHAR(64),
phone VARCHAR(64),
email VARCHAR(64),
address VARCHAR(255),
zip VARCHAR(64))";

my $run_query = $connect_me->prepare($sql);
$run_query->execute() or die "SQL Error: $DBI::errstr\n";

# Insert data into the table
$run_query = $connect_me->prepare("INSERT INTO addressbook(lname,fname, phone, email,address,zip) VALUES($lname,$fname, $phone, $email,$address,$zip)");
#$run_query->execute("1","Nick", "Jones", "earth","aaaa","ssss");
#$run_query->execute("2","Matt", "Smith", "Space Station","aaaa","ssss");
#$run_query->execute("3","Matt", "Brown", "Unspecified","aaaa","ssss");


# SELECT DB
$run_query = $connect_me->prepare("SELECT * FROM $tablename");
$run_query->execute();


#pass sql query to database handle..

$rv = $run_query->execute
or die "can't execute the query: $sth->errstrn";
#execute your query


