#!C:\xampp\perl\bin\perl.exe -w
# The above line is perl execution path in xampp
# The below line tells the browser, that this script will send html content.
# If you miss this line then it will show "malformed header from script" error.
use CGI;
use DBI;
use DBD::mysql;
use HTML::TEMPLATE;

local ($buffer, @pairs, $pair, $name, $value, %FORM);
# Read in text
$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;
if ($ENV{'REQUEST_METHOD'} eq "POST") {
   read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
} else {
   $buffer = $ENV{'QUERY_STRING'};
}
# Split information into name/value pairs
@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
   ($name, $value) = split(/=/, $pair);
   $value =~ tr/+/ /;
   $value =~ s/%(..)/pack("C", hex($1))/eg;
   $FORM{$name} = $value;
}
$first_name = $FORM{first_name};
$last_name  = $FORM{last_name};
$home  = $FORM{home};

# Config DB variables
our $platform = "mysql";
our $database = "test";
our $host = "localhost";
our $port = "3306";
our $tablename = "addressbook";
our $user = "root";
our $pw = "password";
our $q = new CGI;

# DATA SOURCE NAME
$dsn = "DBI:mysql:database=$database;host=$host"; 
# PERL DBI CONNECT
$connect_me = DBI->connect($dsn, $user, $pw);

#Get the parameter from your html form.
$first_name=$q->param('first_name');
$last_name=$q->param('last_name');
$home=$q->param('home');


print $q->header; 

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

$sql=$connect_me->prepare("INSERT INTO addressbook(first_name,last_name, home) VALUES($first_name,$last_name, $home)");

$run_query = $connect_me->prepare($sql)
or die "Can't prepare $sql: $DBI->errstrn";
#pass sql query to database handle..

$rv = $run_query->execute
or die "can't execute the query: $DBI->errstrn";
#execute your query

if ($rv==1){
print "Record has been successfully updated !!!n";
}else{
print "Error!!while inserting recordn";
exit;
}

