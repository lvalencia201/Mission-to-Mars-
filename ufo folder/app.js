// from data.js
const tableData = data;

// get table references
var tbody = d3.select("tbody");

function buildTable(data) {
  // First, clear out any existing data
  tbody.html("");

  // Next, loop through each object in the data
  // and append a row and cells for each value in the row
  data.forEach((dataRow) => {
    // Append a row to the table body
    let row = tbody.append("tr");

    // Loop through each field in the dataRow and add
    // each value as a table cell (td)
    Object.values(dataRow).forEach((val) => {
      let cell = row.append("td");
      cell.text(val);
    });
  });
}

// 1. Create a variable to keep track of all the filters as an object.


// 3. Use this function to update the filters. 
function updateFilters() {

    // 4a. Save the element that was changed as a variable.

    // 4b. Save the value that was changed as a variable.

    // 4c. Save the id of the filter that was changed as a variable.

  
    // 5. If a filter value was entered then add that filterId and value
    // to the filters list. Otherwise, clear that filter from the filters object.
 
  
    // 6. Call function to apply all filters and rebuild the table
    filterTable();
  
  }
  
  // 7. Use this function to filter the table when data is entered.
 
    
    function filterTable() {
      console.log("Hello");
      // 8. Set the filtered data to the tableData.
      // all data to start with
      filtered = JSON.parse(JSON.stringify(data));
      var date_selected = document.getElementById("datetime").value;
      if(date_selected){
        var filtered = filtered.filter(d => d.datetime === date_selected);
      }
      var city_selected = document.getElementById("city").value;
      if(city_selected){
        var filtered = filtered.filter(d => d.city === city_selected);
      }
      var state_selected = document.getElementById("state").value;
      if(state_selected){
        var filtered = filtered.filter(d => d.state === state_selected);
      }
      var country_selected = document.getElementById("country").value;
      if(country_selected){
        var filtered = filtered.filter(d => d.country === country_selected);
      }
      var shape_selected = document.getElementById("shape").value;
      if(shape_selected){
        var filtered = filtered.filter(d => d.shape === shape_selected);
      }
      // 9. Loop through all of the filters and keep any data that
      // matches the filter values
      // 10. Finally, rebuild the table using the filtered data
      buildTable(filtered);
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    // 9. Loop through all of the filters and keep any data that
    // matches the filter values
    
  
    // 10. Finally, rebuild the table using the filtered data
 
  
  // 2. Attach an event to listen for changes to each filter
  
  
  // Build the table when the page loads
  buildTable(tableData);


  document.getElementById("filter-btn").onclick = filterTable;