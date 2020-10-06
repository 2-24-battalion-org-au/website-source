<script>
// Based on https://www.w3schools.com/howto/howto_js_filter_table.asp


let ssh_sn='';
let ssh_n1='';
let ssh_n2='';


function SSH_ww2roll_tab(url) {
  console.log(url);
  window.open( url );
  };
function SSH_ww2roll_surname_plus() {
  if ( ssh_n1 && ssh_n2 ) {
    SSH_ww2roll_tab( 'https://nominal-rolls.dva.gov.au/search?conflict=WW2&searchType=NAME&serviceNumber=&surname='+ssh_n1+'&firstName='+ssh_n2+'&secondName=&conflict=WW2' );
    }
  };
function SSH_ww2roll_surname() {
  if ( ssh_n1 ) {
    SSH_ww2roll_tab( 'https://nominal-rolls.dva.gov.au/search?conflict=WW2&searchType=NAME&serviceNumber=&surname='+ssh_n1+'&firstName=&secondName=&conflict=WW2' );
    }
  };
function SSH_ww2roll_sn() {
  if ( ssh_sn ) {
    SSH_ww2roll_tab(  "https://nominal-rolls.dva.gov.au/searchAdvanced?surname=&firstName=&secondName=&serviceName=ALL&serviceNumber="+ssh_sn+"&rank=&honours=&deathRadio=3&deathYear=&deathDate=&pow=All&birthDate=&nokLastName=&nokFirstName=&conflict=WW2&searchType=ADVANCED" );
    }
  };

function SSH(n1,n2,sn) {
  ssh_sn=sn;
  ssh_n1=n1;
  ssh_n2=n2.split(" ")[0];
  if ( n2[1]=='.' ) { ssh_n2=n2[0]; }
  SSH_info_update();
  };

function SSH_button_set(display) {
  let b;
  b=document.getElementsByClassName("ssh_button");
  for(let i=0; i<b.length; i++ ) {
    if ( display ) { b[i].disabled=false; }
    else { b[i].disabled=true; }
    }
  }
function SSH_info_clear() {
  ssh_sn='';
  ssh_n1='';
  ssh_n2='';
  document.getElementById("ssh_sn").value="";
  document.getElementById("ssh_n1").value="";
  document.getElementById("ssh_n2").value="";
  SSH_button_set(false);
  };
function SSH_info_update() {
  console.log([ssh_sn,ssh_n1,ssh_n2]);
  document.getElementById("ssh_sn").value=ssh_sn;
  document.getElementById("ssh_n1").value=ssh_n1;
  document.getElementById("ssh_n2").value=ssh_n2;
  SSH_button_set(true);
  };


window.onload=function() {
  document.getElementById("ssInput").focus();
  if ( window.location.search.startsWith('?q=') ) {
    document.getElementById("ssInput").value = window.location.search.slice(3);
    SimpleSearch();
    }
  };


function SimpleSearchReset() {
  // Declare variables 
  var input, filter, table, tr, td0,td1, i;
  input = document.getElementById("ssInput");
  input.value="";
  //table = document.getElementById("myTable");
  table = document.getElementsByTagName("table")[0];
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    tr[i].style.display = "";
  }
  SSH_info_clear();
}

function SimpleSearch() {
  // Declare variables 
  var input, filter, table, tr, td0,td1, i;
  input = document.getElementById("ssInput");
  filter = input.value.toUpperCase();
  //table = document.getElementById("myTable");
  table = document.getElementsByTagName("table")[0];
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 1; i < tr.length; i++) {
    sname = tr[i].getElementsByTagName("td")[0];
    snum  = tr[i].getElementsByTagName("td")[2];
    if ( (sname && sname.innerHTML.toUpperCase().indexOf(filter) > -1 ) || (snum && snum.innerHTML.toUpperCase().indexOf(filter) > -1 ) ) {
      tr[i].style.display = "";
    } else {
      tr[i].style.display = "none";
    }
  }
}
</script>

