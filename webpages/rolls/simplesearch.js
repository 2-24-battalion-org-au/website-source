<script>
// Based on https://www.w3schools.com/howto/howto_js_filter_table.asp

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

